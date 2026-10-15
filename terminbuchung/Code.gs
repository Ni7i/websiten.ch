/**
 * websiten.ch Terminbuchung
 * Google Apps Script als Web-App.
 *
 * GET  ?action=slots  -> freie Zeiten der nächsten Wochen
 * POST (JSON)         -> Termin in Google Kalender eintragen, E-Mail an dich und an den Kunden
 *
 * Einrichtung: siehe ANLEITUNG.txt
 */

const CONFIG = {
  // In diesen Kalender wird gebucht. 'primary' = dein Hauptkalender.
  CALENDAR_ID: 'primary',

  // Diese Kalender werden auf Belegung geprüft (z.B. auch privater Kalender oder Kalender von LoliT).
  // Der Google-Account, unter dem das Script läuft, braucht Lesezugriff auf alle.
  CHECK_CALENDARS: ['primary'],

  // An diese Adresse geht die Meldung über einen neuen Termin.
  OWNER_EMAIL: 'hallo@websiten.ch',
  SENDER_NAME: 'websiten.ch',

  TIMEZONE: 'Europe/Zurich',
  DURATION_MIN: 15,        // Länge eines Termins
  STEP_MIN: 30,            // Abstand der Startzeiten (30 = 15 Min. Gespräch + 15 Min. Luft)
  BUFFER_MIN: 10,          // Mindestabstand zu anderen Terminen im Kalender
  MIN_NOTICE_HOURS: 12,    // frühestens so viele Stunden im Voraus buchbar
  DAYS_AHEAD: 21,          // so weit im Voraus buchbar
  MAX_PER_DAY: 6,          // höchstens so viele Buchungen pro Tag

  // Sprechzeiten pro Wochentag: 1 = Montag ... 7 = Sonntag. Tage ohne Eintrag sind geschlossen.
  HOURS: {
    1: [['09:00', '12:00'], ['13:30', '17:00']],
    2: [['09:00', '12:00'], ['13:30', '17:00']],
    3: [['09:00', '12:00'], ['13:30', '17:00']],
    4: [['09:00', '12:00'], ['13:30', '17:00']],
    5: [['09:00', '12:00']]
  },

  // Tage ohne Termine (Ferien, Feiertage), Format JJJJ-MM-TT
  CLOSED_DAYS: ['2026-12-24', '2026-12-25', '2026-12-26', '2026-12-31', '2027-01-01', '2027-01-02'],

  INVITE_CUSTOMER: true,       // Kunde bekommt eine Google-Kalendereinladung
  SEND_CUSTOMER_MAIL: true,    // Kunde bekommt zusätzlich eine Bestätigung von dir
  MAX_BOOKINGS_PER_EMAIL: 2    // Schutz vor Spam: offene Buchungen pro E-Mail-Adresse
};

const TAG = 'websitenBooking';
const WD = ['Sonntag', 'Montag', 'Dienstag', 'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag'];
const MO = ['Januar', 'Februar', 'März', 'April', 'Mai', 'Juni', 'Juli', 'August', 'September', 'Oktober', 'November', 'Dezember'];

/* ---------------------------------------------------------------- Web-App */

function doGet(e) {
  try {
    if ((e.parameter.action || '') === 'slots') return json_({ ok: true, tz: CONFIG.TIMEZONE, days: getDays_() });
    return json_({ ok: true, info: 'websiten.ch Terminbuchung' });
  } catch (err) {
    console.error(err);
    return json_({ ok: false, error: 'server' });
  }
}

function doPost(e) {
  let d;
  try { d = JSON.parse(e.postData.contents); } catch (err) { return json_({ ok: false, error: 'invalid', message: 'Ungültige Anfrage.' }); }

  // Honeypot: Bots füllen das versteckte Feld aus
  if (d.website) return json_({ ok: true });

  const v = validate_(d);
  if (v) return json_({ ok: false, error: 'invalid', message: v });

  const lock = LockService.getScriptLock();
  if (!lock.tryLock(20000)) return json_({ ok: false, error: 'busy', message: 'Gerade viel los. Bitte versuchen Sie es nochmals.' });
  try {
    const day = getDays_(true).find(x => x.date === d.date);
    if (!day || day.slots.indexOf(d.time) === -1) return json_({ ok: false, error: 'taken' });
    if (countOpenForEmail_(d.email) >= CONFIG.MAX_BOOKINGS_PER_EMAIL) {
      return json_({ ok: false, error: 'limit', message: 'Mit dieser E-Mail-Adresse ist schon ein Termin gebucht. Schreiben Sie uns, wenn Sie einen weiteren brauchen.' });
    }
    const ev = createEvent_(d);
    CacheService.getScriptCache().remove('days');
    const label = label_(d.date, d.time);
    notifyOwner_(d, label, ev);
    if (CONFIG.SEND_CUSTOMER_MAIL) confirmCustomer_(d, label, ev);
    return json_({ ok: true, label: label, meet: ev.hangoutLink || '' });
  } catch (err) {
    console.error(err);
    return json_({ ok: false, error: 'server', message: 'Das hat nicht geklappt. Bitte schreiben Sie an ' + CONFIG.OWNER_EMAIL + '.' });
  } finally {
    lock.releaseLock();
  }
}

/* ---------------------------------------------------------------- Freie Zeiten */

function getDays_(fresh) {
  const cache = CacheService.getScriptCache();
  if (!fresh) { const c = cache.get('days'); if (c) return JSON.parse(c); }

  const tz = CONFIG.TIMEZONE, now = new Date();
  const earliest = new Date(now.getTime() + CONFIG.MIN_NOTICE_HOURS * 3600e3);
  const today = Utilities.formatDate(now, tz, 'yyyy-MM-dd');
  const noon = Utilities.parseDate(today + ' 12:00', tz, 'yyyy-MM-dd HH:mm');
  const until = new Date(noon.getTime() + (CONFIG.DAYS_AHEAD + 1) * 864e5);

  const busy = getBusy_(now, until);
  const perDay = countBookingsPerDay_(now, until);
  const buf = CONFIG.BUFFER_MIN * 60e3, dur = CONFIG.DURATION_MIN * 60e3;
  const days = [];

  for (let i = 0; i < CONFIG.DAYS_AHEAD; i++) {
    const ref = new Date(noon.getTime() + i * 864e5);
    const date = Utilities.formatDate(ref, tz, 'yyyy-MM-dd');
    const wd = Number(Utilities.formatDate(ref, tz, 'u'));
    const hours = CONFIG.HOURS[wd];
    if (!hours || CONFIG.CLOSED_DAYS.indexOf(date) !== -1) continue;

    const slots = [];
    let future = 0;
    if ((perDay[date] || 0) < CONFIG.MAX_PER_DAY) {
      hours.forEach(function (w) {
        for (let t = min_(w[0]); t + CONFIG.DURATION_MIN <= min_(w[1]); t += CONFIG.STEP_MIN) {
          const hm = hm_(t);
          const s = Utilities.parseDate(date + ' ' + hm, tz, 'yyyy-MM-dd HH:mm'), e = new Date(s.getTime() + dur);
          if (s < earliest) continue;
          future++;
          const clash = busy.some(b => b[0] < e.getTime() + buf && b[1] > s.getTime() - buf);
          if (!clash) slots.push(hm);
        }
      });
    }
    if (!future && (perDay[date] || 0) < CONFIG.MAX_PER_DAY) continue; // Tag schon vorbei
    days.push({ date: date, slots: slots });
  }
  cache.put('days', JSON.stringify(days), 60);
  return days;
}

function getBusy_(from, to) {
  const res = Calendar.Freebusy.query({
    timeMin: from.toISOString(), timeMax: to.toISOString(), timeZone: CONFIG.TIMEZONE,
    items: CONFIG.CHECK_CALENDARS.map(id => ({ id: id }))
  });
  const out = [];
  Object.keys(res.calendars || {}).forEach(function (k) {
    (res.calendars[k].busy || []).forEach(b => out.push([new Date(b.start).getTime(), new Date(b.end).getTime()]));
  });
  return out;
}

function listBookings_(from, to, extra) {
  const opt = Object.assign({ timeMin: from.toISOString(), timeMax: to.toISOString(), singleEvents: true, maxResults: 250, privateExtendedProperty: TAG + '=1' }, extra || {});
  return (Calendar.Events.list(CONFIG.CALENDAR_ID, opt).items || []).filter(ev => ev.status !== 'cancelled');
}

function countBookingsPerDay_(from, to) {
  const out = {};
  listBookings_(from, to).forEach(function (ev) {
    const d = Utilities.formatDate(new Date(ev.start.dateTime || ev.start.date), CONFIG.TIMEZONE, 'yyyy-MM-dd');
    out[d] = (out[d] || 0) + 1;
  });
  return out;
}

function countOpenForEmail_(email) {
  const now = new Date(), to = new Date(now.getTime() + (CONFIG.DAYS_AHEAD + 2) * 864e5);
  return listBookings_(now, to).filter(ev => (ev.extendedProperties.private.email || '').toLowerCase() === email.toLowerCase()).length;
}

/* ---------------------------------------------------------------- Termin anlegen */

function createEvent_(d) {
  const tz = CONFIG.TIMEZONE;
  const start = Utilities.parseDate(d.date + ' ' + d.time, tz, 'yyyy-MM-dd HH:mm');
  const end = new Date(start.getTime() + CONFIG.DURATION_MIN * 60e3);
  const meet = d.mode === 'meet';

  const desc = [
    'Erstgespräch über websiten.ch gebucht',
    '',
    'Name: ' + d.name,
    d.firma ? 'Firma: ' + d.firma : null,
    'E-Mail: ' + d.email,
    d.phone ? 'Telefon: ' + d.phone : null,
    'Art: ' + (meet ? 'Video (Google Meet)' : 'Telefon, wir rufen an'),
    d.message ? '\nNachricht:\n' + d.message : null
  ].filter(x => x !== null).join('\n');

  const ev = {
    summary: 'Erstgespräch: ' + d.name + (d.firma ? ' (' + d.firma + ')' : ''),
    description: desc,
    location: meet ? '' : 'Telefon ' + d.phone,
    start: { dateTime: start.toISOString(), timeZone: tz },
    end: { dateTime: end.toISOString(), timeZone: tz },
    reminders: { useDefault: false, overrides: [{ method: 'popup', minutes: 10 }] },
    extendedProperties: { private: { websitenBooking: '1', email: d.email } }
  };
  if (CONFIG.INVITE_CUSTOMER) ev.attendees = [{ email: d.email, displayName: d.name }];
  if (meet) ev.conferenceData = { createRequest: { requestId: Utilities.getUuid(), conferenceSolutionKey: { type: 'hangoutsMeet' } } };

  return Calendar.Events.insert(ev, CONFIG.CALENDAR_ID, {
    conferenceDataVersion: meet ? 1 : 0,
    sendUpdates: CONFIG.INVITE_CUSTOMER ? 'all' : 'none'
  });
}

/* ---------------------------------------------------------------- E-Mails */

function notifyOwner_(d, label, ev) {
  const rows = [
    ['Wann', label],
    ['Name', d.name],
    ['Firma', d.firma],
    ['E-Mail', d.email],
    ['Telefon', d.phone],
    ['Art', d.mode === 'meet' ? 'Google Meet' + (ev.hangoutLink ? ': ' + ev.hangoutLink : '') : 'Telefon, du rufst an']
  ].filter(r => r[1]);
  const html =
    '<div style="font-family:Arial,sans-serif;font-size:15px;color:#1b2420">' +
    '<p style="font-size:18px"><b>Neuer Termin über websiten.ch</b></p>' +
    '<table cellpadding="6" style="border-collapse:collapse">' +
    rows.map(r => '<tr><td style="color:#667;vertical-align:top">' + esc_(r[0]) + '</td><td>' + esc_(r[1]) + '</td></tr>').join('') +
    '</table>' +
    (d.message ? '<p style="margin-top:16px;color:#667">Nachricht</p><p style="white-space:pre-wrap">' + esc_(d.message) + '</p>' : '') +
    (ev.htmlLink ? '<p><a href="' + ev.htmlLink + '">Im Kalender öffnen</a></p>' : '') +
    '</div>';
  MailApp.sendEmail({
    to: CONFIG.OWNER_EMAIL,
    subject: 'Neuer Termin: ' + label + ', ' + d.name + (d.firma ? ' (' + d.firma + ')' : ''),
    htmlBody: html,
    replyTo: d.email,
    name: 'Terminbuchung websiten.ch'
  });
}

function confirmCustomer_(d, label, ev) {
  const how = d.mode === 'meet'
    ? 'Wir sprechen per Video. ' + (ev.hangoutLink ? 'Der Link: <a href="' + ev.hangoutLink + '">' + ev.hangoutLink + '</a>' : 'Den Link finden Sie in der Kalendereinladung.')
    : 'Wir rufen Sie unter ' + esc_(d.phone) + ' an.';
  const html =
    '<div style="font-family:Arial,sans-serif;font-size:15px;line-height:1.55;color:#1b2420;max-width:520px">' +
    '<p>Guten Tag ' + esc_(d.name) + '</p>' +
    '<p>Ihr Termin ist gebucht:<br><b>' + esc_(label) + '</b>, 15 Minuten.</p>' +
    '<p>' + how + '</p>' +
    '<p>Damit wir das Gespräch gut nutzen: Überlegen Sie sich kurz, was die Website können soll und bis wann Sie sie brauchen. Mehr braucht es nicht.</p>' +
    '<p>Passt die Zeit doch nicht? Antworten Sie einfach auf diese E-Mail.</p>' +
    '<p>Freundliche Grüsse<br>websiten.ch</p>' +
    '</div>';
  MailApp.sendEmail({
    to: d.email,
    subject: 'Ihr Termin mit websiten.ch: ' + label,
    htmlBody: html,
    replyTo: CONFIG.OWNER_EMAIL,
    name: CONFIG.SENDER_NAME
  });
}

/* ---------------------------------------------------------------- Hilfen */

function validate_(d) {
  const s = x => typeof x === 'string';
  if (!s(d.date) || !/^\d{4}-\d{2}-\d{2}$/.test(d.date) || !s(d.time) || !/^\d{2}:\d{2}$/.test(d.time)) return 'Bitte wählen Sie eine Zeit.';
  if (!s(d.name) || !d.name.trim() || d.name.length > 100) return 'Bitte tragen Sie Ihren Namen ein.';
  if (!s(d.email) || !/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(d.email) || d.email.length > 120) return 'Bitte prüfen Sie die E-Mail-Adresse.';
  if (d.mode !== 'phone' && d.mode !== 'meet') return 'Bitte wählen Sie Telefon oder Video.';
  if (d.mode === 'phone' && (!s(d.phone) || d.phone.replace(/\D/g, '').length < 9)) return 'Für den Anruf brauchen wir Ihre Telefonnummer.';
  ['firma', 'phone', 'message'].forEach(k => { d[k] = s(d[k]) ? d[k].trim() : ''; });
  if (d.firma.length > 120 || d.phone.length > 40 || d.message.length > 3000) return 'Ein Feld ist zu lang.';
  d.name = d.name.trim(); d.email = d.email.trim();
  return '';
}

function label_(date, time) {
  const x = new Date(date + 'T12:00:00Z');
  return WD[x.getUTCDay()] + ', ' + x.getUTCDate() + '. ' + MO[x.getUTCMonth()] + ' ' + x.getUTCFullYear() + ', ' + time + ' Uhr';
}
function min_(s) { return Number(s.slice(0, 2)) * 60 + Number(s.slice(3)); }
function hm_(n) { return ('0' + Math.floor(n / 60)).slice(-2) + ':' + ('0' + (n % 60)).slice(-2); }
function esc_(s) { return String(s || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' })[c]); }
function json_(o) { return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON); }

/* ---------------------------------------------------------------- Zum Testen im Editor */

// Zeigt die freien Zeiten im Protokoll. Beim ersten Ausführen fragt Google nach den Berechtigungen.
function testFreieZeiten() {
  getDays_(true).forEach(d => console.log(d.date + ': ' + (d.slots.join(', ') || 'keine')));
}

// Bucht einen Testtermin am ersten freien Platz und schickt beide E-Mails an dich.
function testBuchung() {
  const day = getDays_(true).find(d => d.slots.length);
  if (!day) return console.log('Keine freien Zeiten gefunden.');
  const res = doPost({ postData: { contents: JSON.stringify({
    date: day.date, time: day.slots[0], mode: 'meet', name: 'Test Kunde', firma: 'Testfirma',
    email: CONFIG.OWNER_EMAIL, phone: '079 000 00 00', message: 'Testbuchung, bitte löschen.'
  }) } });
  console.log(res.getContent());
}
