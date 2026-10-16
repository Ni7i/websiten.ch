
/* Terminbuchung
   BOOKING_API: Web-App-Adresse des Google Apps Script (siehe ANLEITUNG.md).
   Leer = Vorschau-Modus: Zeiten werden lokal berechnet, es wird nichts gebucht. */
const BOOKING_API = '';

(function(){
  const $ = id => document.getElementById(id);
  const WD = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'], WDL = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'];
  const MO = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'], MOL = ['January','February','March','April','May','June','July','August','September','October','November','December'];
  const st = {days:[], day:null, time:null, mode:'meet'};
  const dt = s => new Date(s + 'T12:00:00Z');
  const longLabel = (d, t) => { const x = dt(d); return WDL[x.getUTCDay()] + ', ' + x.getUTCDate() + '. ' + MOL[x.getUTCMonth()] + ', ' + t + ' '; };

  // Vorschau: gleiche Regeln wie im Script (Mo bis Fr, 9 bis 12 und 13.30 bis 17 Uhr, alle 30 Min., 12 Std. Vorlauf, 3 Wochen)
  function demoSlots(){
    const HOURS = {1:[['09:00','12:00'],['13:30','17:00']],2:[['09:00','12:00'],['13:30','17:00']],3:[['09:00','12:00'],['13:30','17:00']],4:[['09:00','12:00'],['13:30','17:00']],5:[['09:00','12:00']]};
    const zf = new Intl.DateTimeFormat('sv-SE', {timeZone:'Europe/Zurich', year:'numeric', month:'2-digit', day:'2-digit', hour:'2-digit', minute:'2-digit', hourCycle:'h23'});
    const earliest = zf.format(new Date(Date.now() + 12*3600e3)).replace(',', '');
    const today = zf.format(new Date()).slice(0, 10);
    const m = s => +s.slice(0, 2)*60 + +s.slice(3), hm = n => String(Math.floor(n/60)).padStart(2, '0') + ':' + String(n%60).padStart(2, '0');
    const out = [];
    for(let i = 0; i < 21; i++){
      const x = dt(today); x.setUTCDate(x.getUTCDate() + i);
      const ds = x.toISOString().slice(0, 10), wd = x.getUTCDay();
      if(!HOURS[wd]) continue;
      const slots = [];
      HOURS[wd].forEach(([a, b]) => { for(let t = m(a); t + 15 <= m(b); t += 30){ if(ds + ' ' + hm(t) >= earliest) slots.push(hm(t)); } });
      if(slots.length) out.push({date:ds, slots});
    }
    return out;
  }

  function renderDays(){
    const box = $('days'); box.innerHTML = '';
    let prevWd = null;
    st.days.forEach(d => {
      const x = dt(d.date), b = document.createElement('button');
      b.type = 'button'; b.className = 'day'; b.disabled = !d.slots.length;
      if(prevWd !== null && x.getUTCDay() < prevWd) b.classList.add('wkb');
      prevWd = x.getUTCDay();
      b.setAttribute('aria-pressed', d.date === st.day);
      b.setAttribute('aria-label', WDL[x.getUTCDay()] + ', ' + x.getUTCDate() + '. ' + MOL[x.getUTCMonth()] + (d.slots.length ? ', ' + d.slots.length + ' Zeiten frei' : ', ausgebucht'));
      b.innerHTML = `<small>${WD[x.getUTCDay()]}</small><b>${x.getUTCDate()}</b><span>${d.slots.length ? MO[x.getUTCMonth()] : 'full'}</span>`;
      b.onclick = () => { st.day = d.date; st.time = null; renderDays(); renderTimes(); renderPicked(); };
      box.appendChild(b);
    });
    if(!st.days.some(d => d.slots.length)) box.innerHTML = '<span class="times-empty">Sorry, everything is booked over the next few weeks. Write to us and we’ll find a time.</span>';
  }
  function renderTimes(){
    const box = $('times'), d = st.days.find(x => x.date === st.day);
    box.innerHTML = '';
    if(!d){ box.innerHTML = '<span class="times-empty">Pick a day first.</span>'; return; }
    d.slots.forEach(t => {
      const b = document.createElement('button'); b.type = 'button'; b.textContent = t;
      b.setAttribute('aria-pressed', t === st.time);
      b.onclick = () => { st.time = t; renderTimes(); renderPicked(); };
      box.appendChild(b);
    });
  }
  function renderPicked(){
    $('picked').innerHTML = st.time ? 'Selected: <b>' + longLabel(st.day, st.time) + '</b>' : 'No time selected yet.';
    $('sendBtn').disabled = !st.time;
  }

  async function load(){
    if(!BOOKING_API){ st.days = demoSlots(); }
    else {
      try {
        const r = await fetch(BOOKING_API + '?action=slots', {cache:'no-store'});
        const j = await r.json(); if(!j.ok) throw 0; st.days = j.days;
      } catch(e){
        $('days').innerHTML = '<span class="times-empty">The calendar can’t be reached right now. Write to hallo@websiten.ch or try again in a few minutes.</span>';
        return;
      }
    }
    const first = st.days.find(d => d.slots.length); st.day = first ? first.date : null;
    renderDays(); renderTimes(); renderPicked();
  }

  try { const v = localStorage.getItem('websiten-anfrage'); if(v && !$('msg').value) $('msg').value = v + '\n\n'; } catch(e){}

  const err = t => { $('err').textContent = t; $('err').hidden = !t; };
  $('form').addEventListener('submit', async e => {
    e.preventDefault(); err('');
    const name = $('name'), mail = $('mail');
    [name, mail].forEach(i => i.classList.remove('bad'));
    if(!st.time) return err('Please pick a time first.');
    if(!name.value.trim()){ name.classList.add('bad'); name.focus(); return err('Please enter your name.'); }
    if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(mail.value.trim())){ mail.classList.add('bad'); mail.focus(); return err('Please check the email address.'); }
    const data = {date:st.day, time:st.time, mode:st.mode, name:name.value.trim(), firma:$('firma').value.trim(), email:mail.value.trim(), phone:'', message:$('msg').value.trim(), website:$('website').value};
    const label = longLabel(st.day, st.time);
    if(!BOOKING_API){ return done(label, data, '', true); }
    const btn = $('sendBtn'); btn.disabled = true; btn.firstChild.textContent = 'Wird gebucht … ';
    try {
      const r = await fetch(BOOKING_API, {method:'POST', headers:{'Content-Type':'text/plain;charset=utf-8'}, body:JSON.stringify(data)});
      const j = await r.json();
      if(j.ok) return done(label, data, j.meet || '', false);
      if(j.error === 'taken'){ err('This time was just taken. Please pick another one.'); st.time = null; await load(); }
      else err(j.message || 'That didn’t work. Please try again or write to hallo@websiten.ch.');
    } catch(e){ err('No connection to the calendar. Please try again or write to hallo@websiten.ch.'); }
    btn.disabled = !st.time; btn.firstChild.textContent = 'Book call  ';
  });

  function done(label, d, meet, demo){
    const how = d.mode === 'meet' ? (meet ? `You’ll find the Google Meet link in the email and in the calendar invitation.` : `You’ll get the Google Meet link by email.`) : `You’ll get the Google Meet link by email.`;
    $('booker').innerHTML = `<div class="ok" role="status"><h2>Booked: ${label}</h2><p>${how} The confirmation goes to ${d.email.replace(/</g, '')}.</p><p>Something came up? Just reply to the confirmation.</p>${demo ? '<p class="demo">Note: this is a preview of the website. The calendar isn’t connected here yet, nothing was booked.</p>' : ''}</div>`;
    try { localStorage.removeItem('websiten-anfrage'); } catch(e){}
    $('booker').scrollIntoView({block:'start', behavior:'smooth'});
  }
  load();
})();
