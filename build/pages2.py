# Unterseiten im neuen Stil: dunkel, Salbei als Akzent, Linien statt Kästen, MacBook mit echtem Bildschirm
import re, home9, pages as P
from parts import ARROW, LI, GRAIN, MARK_LIGHT, MARK_DARK

UP = home9.UP
FILES = {'websites': 'websites.html', 'shops': 'online-shops.html', 'seo': 'google-seo.html',
         'hosting': 'hosting.html', 'm365': 'microsoft-365.html', 'ki': 'ki-chatbots.html'}
NAMES = {k: t for k, t, *_ in [(i, t) for i, t, d, s in home9.SV]}
SHORT = {i: d for i, t, d, s in home9.SV}
SHORT['shops'] = 'Ihr Shopify-Account auf professionellem Niveau. Mit TWINT, Karte, Rechnung und Versand in der Schweiz.'


def mac(scr, alt, eager=False):
    lz = '' if eager else ' loading="lazy"'
    return (f'<div class="mac"><div class="mac-scr"><img src="assets/img/scr-{scr}.jpg" alt="{alt}"{lz} width="1440" height="900">'
            f'<span class="mac-gl"></span></div><img class="mac-fr" src="assets/img/mac-frame.webp" alt="" aria-hidden="true"{lz}></div>')


def head(title, text, tag='h2', id_=''):
    i = f' id="{id_}"' if id_ else ''
    return f'<div class="lx-head"><{tag}{i}>{title}</{tag}><p>{text}</p></div>'


# ------------------------------------------------------------------ Inhalte der sechs Leistungen
SVC = {
 'websites': dict(
  desc='Websites für Schweizer KMU. Gestaltet für Ihren Betrieb, gebaut fürs Handy. Ab CHF 590.– mit festem Preis, Server in Genf.',
  h1='Websites, die <em class="hl">Anfragen bringen.</em>',
  intro='Wir gestalten Ihre Website für Ihren Betrieb und bauen sie fürs Handy. Mit Texten, die Ihre Kunden verstehen, und einem Formular, das Anfragen bringt. Öffnungszeiten oder Fotos ändern Sie danach selbst. Oder Sie schreiben uns, und wir machen es.',
  facts=['Ab CHF 590.–', 'In 3 bis 4 Wochen online', 'Server in Genf'],
  incl_t='Alles, was eine gute Firmenwebsite braucht. Im Preis inbegriffen, ausser es steht etwas anderes dabei.',
  incl=[('Planung', 'Wir klären mit Ihnen, welche Seiten Sie brauchen und was darauf stehen soll.'),
        ('Gestaltung', 'Für Ihren Betrieb gemacht. Mit Ihrem Logo, Ihren Farben und Ihren Fotos.'),
        ('Fürs Handy gebaut', 'Die meisten Besucher kommen übers Handy. Darauf bauen wir zuerst.'),
        ('Kontaktformular', 'Anfragen landen direkt in Ihrem Postfach, mit Schutz gegen Spam.'),
        ('Texte', 'Auf Wunsch schreiben wir die Texte. Pro Seite CHF 90.–.'),
        ('Weitere Sprachen', 'Französisch, Italienisch oder Englisch. Pro Sprache und Seite CHF 70.–.'),
        ('Google-Grundlagen', 'Schnelle Ladezeit, saubere Struktur und Titel, die Google versteht.'),
        ('Einführung', 'Wir zeigen Ihnen, wie Sie Texte und Bilder selbst ändern.')],
  steps=[('Gespräch', '15 Minuten per Video. Sie erzählen, was Sie vorhaben.', 'Tag 1'),
         ('Offerte', 'Sie bekommen einen festen Preis und einen Termin für den Start.', 'Tag 2'),
         ('Entwurf', 'Sie sehen die Startseite und sagen uns, was passt und was nicht.', 'Woche 1 bis 2'),
         ('Online', 'Wir bauen alle Seiten, testen auf Handy und Computer und schalten auf.', 'Woche 3 bis 4')],
  prices=[('Website mit 4 Seiten', 'Zum Beispiel Start, Leistungen, Über uns, Kontakt', '', '590.–', ''),
          ('Bis 6 Seiten', '', '', '890.–', ''),
          ('Bis 8 Seiten', '', '', '1’190.–', ''),
          ('Bis 10 Seiten', 'Jede weitere Seite CHF 150.–', '', '1’490.–', ''),
          ('Hosting und Domain', 'Mit Backups, Updates und E-Mail', '', '25.–', '/ Monat')],
  refs=True,
  faq=[('Wie lange dauert es?', 'Eine Website mit 4 Seiten ist meistens in drei bis vier Wochen online. Grössere Websites brauchen fünf bis acht Wochen. Das Datum steht in der Offerte.'),
       ('Kann ich selbst Änderungen machen?', 'Ja. Nach der Einführung ändern Sie Texte, Bilder und Öffnungszeiten selbst. Wenn Sie lieber nicht, schreiben Sie uns, und wir erledigen es.'),
       ('Was brauchen Sie von mir?', 'Ihr Logo, ein paar Fotos und die Angaben zu Ihren Leistungen. Die Texte schreiben wir auf Wunsch. Fehlen Fotos, besprechen wir, woher sie kommen.'),
       ('Ich habe schon eine Website.', 'Dann übernehmen wir, was gut ist, und leiten die alten Adressen weiter. So verlieren Sie Ihre Plätze bei Google nicht.'),
       ('Gehört die Website danach mir?', 'Ja. Domain, Inhalte und Zugänge laufen auf Ihren Namen. Wenn Sie einmal wechseln möchten, bekommen Sie alles.')]),
 'shops': dict(
  desc='Online-Shops für Schweizer KMU. Shopify professionell eingerichtet, mit TWINT, Karte, Rechnung und Versand in der Schweiz. Ab CHF 1’890.–.',
  h1='Online-Shops, die in der Schweiz <em class="hl">verkaufen.</em>',
  intro='Wir richten Ihren Shopify-Account auf professionellem Niveau ein. Mit TWINT, Karte, Rechnung und Versand in der Schweiz. Produkte und Bestellungen verwalten Sie danach selbst.',
  facts=['Ab CHF 1’890.–', 'TWINT, Karte und Rechnung', 'Versand in der Schweiz'],
  incl_t='Ein Shop, der vom ersten Tag an so läuft, wie Kunden in der Schweiz es erwarten.',
  incl=[('Shopify sauber eingerichtet', 'Konto, Zahlungen, Steuern, Versand und rechtliche Seiten. Vollständig und geprüft.'),
        ('TWINT, Karte und Rechnung', 'Die Zahlungsarten, die Ihre Kunden in der Schweiz erwarten.'),
        ('Versand', 'Versandregeln für die Post, Gratisversand ab einem Betrag, Abholung im Laden.'),
        ('Preise mit MwSt.', 'Preise, Rechnungen und Belege mit 8,1 % MwSt. richtig eingestellt.'),
        ('Gestaltung', 'Ihr Shop sieht aus wie Ihr Betrieb und nicht wie eine Vorlage.'),
        ('Produkte', 'Die ersten 30 Produkte erfassen wir. Grosse Sortimente importieren wir aus Excel oder dem alten Shop.'),
        ('Shop-Umzug', 'Von WooCommerce, Wix oder einem anderen System. Mit Kunden, Bestellungen und Weiterleitungen.'),
        ('Schulung', 'Sie lernen, wie Sie Produkte, Bestellungen und Rabatte selbst verwalten.')],
  steps=[('Gespräch', 'Was verkaufen Sie, an wen und wie verschicken Sie?', 'Tag 1'),
         ('Offerte', 'Fester Preis, fester Termin. Dazu der passende Shopify-Plan.', 'Tag 2'),
         ('Einrichtung', 'Zahlungen, Versand, Gestaltung und Produkte. Sie sehen den Shop vor dem Start.', 'Woche 1 bis 3'),
         ('Testkauf und Start', 'Wir kaufen selbst ein, mit TWINT und Karte. Erst wenn alles stimmt, geht der Shop online.', 'Woche 4 bis 5')],
  prices=[('Shop mit 4 Seiten und bis 30 Produkten', 'Mit TWINT, Karte, Rechnung und Versand', 'ab', '1’890.–', ''),
          ('Bis 150 Produkte', '', '+', '490.–', ''),
          ('Bis 500 Produkte', '', '+', '990.–', ''),
          ('Über 500 Produkte, mit Import', 'Das Shopify-Abo zahlen Sie direkt an Shopify', '+', '1’890.–', '')],
  faq=[('Warum Shopify?', 'Shopify läuft stabil, ist sicher und wird laufend weiterentwickelt. Um Updates müssen Sie sich nicht kümmern. Für kleine Sortimente direkt in einer WordPress-Website arbeiten wir auch mit WooCommerce.'),
       ('Was kostet Shopify im Monat?', 'Das Abo zahlen Sie direkt an Shopify. Welcher Plan passt, besprechen wir im ersten Gespräch. Dazu kommen die Gebühren der Zahlungsanbieter pro Verkauf.'),
       ('Kann ich Produkte selbst erfassen?', 'Ja. Nach der Schulung erfassen Sie Produkte, Preise und Rabatte selbst.'),
       ('Ich habe schon einen Shop.', 'Wir ziehen ihn um, mit Produkten, Kunden und Bestellungen. Alte Adressen leiten wir weiter, damit Google Sie weiterhin findet.'),
       ('Ist TWINT dabei?', 'Ja. TWINT, Karte und Kauf auf Rechnung richten wir von Anfang an ein.')]),
 'seo': dict(
  desc='Google und SEO für Schweizer KMU. Google-Unternehmensprofil, saubere Technik, Seiten für Ihre Region und Google Ads mit festem Budget.',
  h1='Gefunden werden, wo Ihre Kunden <em class="hl">suchen.</em>',
  intro='Ihre Kunden suchen nach «Gipser Buchs AG» oder «Coiffeur Baden». Dort sollten Sie auftauchen. Wir bringen die Technik in Ordnung, richten Ihr Google-Profil ein und schreiben Seiten zu dem, was Ihre Kunden suchen.',
  facts=['Google-Profil ab CHF 150.–', 'Ads mit festem Budget', 'Keine Platz-Garantien'],
  incl_t='Ehrliche Arbeit, die messbar ist. Gekaufte Links und leere Versprechen gibt es bei uns nicht.',
  incl=[('Google-Unternehmensprofil', 'Mit Öffnungszeiten, Fotos und Leistungen. Damit Sie auf Google Maps richtig erscheinen.'),
        ('Technik', 'Ladezeit, saubere Struktur und Titel, die Google versteht.'),
        ('Seiten für Ihre Region', 'Eine Seite pro Leistung und Ort. Geschrieben für Menschen, nicht für Maschinen.'),
        ('Google Ads', 'Anzeigen mit festem Monatsbudget. Sie wissen genau, was es kostet.'),
        ('Search Console', 'Wir verbinden Ihre Website mit Google und beheben, was Google bemängelt.'),
        ('Monatliche Auswertung', 'Wie viele Besucher und Anfragen kamen und woher. Kurz und verständlich.')],
  steps=[('Analyse', 'Wir schauen, wie Sie heute gefunden werden und wo Ihre Konkurrenz steht.', 'Woche 1'),
         ('Offerte', 'Sie sehen, was wir vorschlagen, was es kostet und was es bringen soll.', 'Woche 1'),
         ('Umsetzung', 'Profil, Technik und Inhalte. Jede Änderung zeigen wir Ihnen.', 'Woche 2 bis 4'),
         ('Auswertung', 'Jeden Monat sehen Sie, was es gebracht hat.', 'Danach')],
  prices=[('Google-Unternehmensprofil einrichten', 'Mit Fotos, Leistungen und Öffnungszeiten', '', '150.–', ''),
          ('Google Ads einrichten', 'Das Werbebudget zahlen Sie direkt an Google', '', '390.–', '')],
  price_note='Seiten für Ihre Region und die laufende Betreuung rechnen wir nach Umfang. Sie bekommen vorher eine Offerte mit festem Preis.',
  faq=[('Bringt ihr mich auf Platz 1?', 'Das kann niemand ehrlich versprechen. Wir schaffen die Grundlage: saubere Technik, gute Inhalte und ein vollständiges Google-Profil.'),
       ('Wann sehe ich Resultate?', 'Das Google-Profil wirkt oft nach wenigen Wochen. In der normalen Suche dauert es meistens einige Monate. Google Ads wirken ab dem ersten Tag.'),
       ('Wie viel Werbebudget brauche ich?', 'Das hängt von Ihrer Branche und Region ab. Wir schlagen ein Budget vor, Sie legen das Monatsbudget fest.'),
       ('Was ist lokale SEO?', 'Damit sind Suchen mit Ort gemeint, zum Beispiel «Maler Aarau». Dafür zählen vor allem Ihr Google-Profil, Bewertungen und Seiten, die Ihren Ort nennen.')]),
 'hosting': dict(
  desc='Domains, Hosting und E-Mail bei Infomaniak in Genf. Mit Updates, Backups und SSL für CHF 25.– im Monat. Ihre Daten bleiben in der Schweiz.',
  h1='Hosting in Genf. <em class="hl">Wir kümmern uns darum.</em>',
  intro='Domain, Website und E-Mail liegen bei Infomaniak, einem Schweizer Anbieter mit Rechenzentren in der Schweiz. Updates, Backups und Sicherheit übernehmen wir. Sie sehen jederzeit, dass alles läuft.',
  facts=['CHF 25.– im Monat', '.ch-Domain inbegriffen', 'Daten in der Schweiz'],
  incl_t='Ein fester Betrag im Monat. Dafür läuft Ihre Website, und Sie müssen nicht daran denken.',
  incl=[('.ch-Domain', 'Wir registrieren Ihre Domain oder ziehen sie um. Sie läuft auf Ihren Namen.'),
        ('Hosting bei Infomaniak', 'Server in der Schweiz, bei einem unabhängigen Anbieter aus Genf.'),
        ('E-Mail mit Ihrer Domain', 'Zum Beispiel info@ihre-firma.ch, auf Handy und Computer eingerichtet.'),
        ('Tägliche Backups', 'Geht etwas schief, holen wir den Stand vom Vortag zurück.'),
        ('Updates', 'WordPress und Plugins halten wir aktuell, geprüft und ohne Ausfall.'),
        ('SSL-Zertifikat', 'Das Schloss im Browser. Es wird automatisch erneuert.'),
        ('Kleine Änderungen', 'Neue Öffnungszeiten oder ein neues Foto? Schreiben Sie uns, wir erledigen es.'),
        ('Umzug', 'Ihre bestehende Website und Ihre E-Mails ziehen wir ohne Unterbruch um.')],
  steps=[('Bestandsaufnahme', 'Wir schauen, wo Domain, Website und E-Mails heute liegen.', 'Tag 1'),
         ('Umzug', 'Wir ziehen alles zu Infomaniak um. Ihre E-Mails gehen dabei nicht verloren.', 'Woche 1'),
         ('Einrichtung', 'E-Mail auf Handy und Computer, Backups und Updates.', 'Woche 1'),
         ('Betreuung', 'Wir halten alles aktuell. Sie schreiben uns, wenn Sie etwas brauchen.', 'Laufend')],
  prices=[('Hosting und .ch-Domain', 'Server bei Infomaniak in Genf', '', '25.–', '/ Monat'),
          ('E-Mail-Adresse mit Ihrer Domain', '', '', 'inbegriffen', ''),
          ('Backups, Updates und SSL', '', '', 'inbegriffen', '')],
  faq=[('Warum Infomaniak?', 'Infomaniak ist ein unabhängiger Schweizer Anbieter aus Genf. Ihre Daten liegen in Rechenzentren in der Schweiz und unterstehen Schweizer Recht.'),
       ('Ich habe schon eine Domain.', 'Kein Problem. Wir ziehen sie zu Infomaniak um oder lassen sie, wo sie ist, und richten sie richtig ein.'),
       ('Gehen beim Umzug E-Mails verloren?', 'Nein. Wir übertragen Ihre bisherigen E-Mails und stellen erst um, wenn alles bereit ist.'),
       ('Wie lese ich meine E-Mails?', 'Im Browser, mit der App von Infomaniak oder in Outlook, Apple Mail und Gmail. Wir richten es auf Ihren Geräten ein.'),
       ('Was, wenn die Website nicht erreichbar ist?', 'Schreiben Sie uns. Wir prüfen es rasch und sagen Ihnen, was los ist.')]),
 'm365': dict(
  desc='Microsoft 365 für Schweizer KMU. E-Mail, Kalender, Teams und OneDrive sauber eingerichtet, E-Mail-Umzug und Betreuung per Fernwartung.',
  h1='Microsoft 365, <em class="hl">sauber eingerichtet.</em>',
  intro='E-Mail, Kalender, Teams und Dateien für Ihr Team. Wir richten alles ein, ziehen Ihre alten E-Mails um und betreuen es danach. Neue Leute haben ihr Konto am ersten Tag, und wer geht, verliert den Zugriff am letzten.',
  facts=['Fester Preis nach dem Gespräch', 'Lizenzen auf Ihren Namen', 'Hilfe per Fernwartung'],
  incl_t='Ordnung im Büro. Damit jeder findet, was er sucht, und niemand Zugriff hat, der keinen haben soll.',
  incl=[('Einrichtung und Lizenzen', 'Wir wählen mit Ihnen die passenden Lizenzen und richten alles ein.'),
        ('E-Mail-Umzug', 'Vom alten Anbieter zu Microsoft 365, mit allen Ordnern und Kontakten.'),
        ('Teams und OneDrive', 'Klare Ordner und Kanäle, damit jeder findet, was er sucht.'),
        ('Sichere Anmeldung', 'Anmeldung mit zweitem Faktor. Das schützt vor den häufigsten Angriffen.'),
        ('Neue Mitarbeitende', 'Konto, E-Mail und Zugriffe sind am ersten Tag bereit.'),
        ('Austritte', 'Wer geht, verliert den Zugriff. Die Daten bleiben in der Firma.'),
        ('Geräte', 'Neue Laptops richten wir ein, damit sie sofort laufen.'),
        ('Fernwartung', 'Klemmt etwas, schalten wir uns auf Ihren Bildschirm und lösen es.')],
  steps=[('Gespräch', 'Wie viele Leute, welche Geräte, wo liegen die E-Mails heute?', 'Tag 1'),
         ('Offerte', 'Fester Preis für Einrichtung und Umzug, Lizenzen klar aufgelistet.', 'Tag 2'),
         ('Umzug', 'Wir stellen um, wenn es Ihren Betrieb am wenigsten stört.', 'Woche 1 bis 2'),
         ('Betreuung', 'Neue Leute, neue Geräte, Fragen im Alltag. Wir sind da.', 'Laufend')],
  price_note='Der Preis hängt davon ab, wie viele Personen und Geräte Sie haben. Nach dem ersten Gespräch bekommen Sie eine Offerte mit festem Preis. Die Lizenzen laufen auf Ihren Namen.',
  faq=[('Brauche ich Microsoft 365?', 'Wenn Sie mit mehreren Leuten E-Mails, Kalender und Dateien teilen, meistens ja. Arbeiten Sie allein, reicht oft eine E-Mail-Adresse bei Infomaniak. Wir sagen Ihnen ehrlich, was passt.'),
       ('Können wir unsere alten E-Mails behalten?', 'Ja. Wir übertragen alle E-Mails, Ordner und Kontakte.'),
       ('Welche Lizenz brauchen wir?', 'Für die meisten kleinen Betriebe reicht Microsoft 365 Business Basic oder Business Standard. Wir schauen es mit Ihnen an.'),
       ('Helft ihr auch bei Problemen im Alltag?', 'Ja. Per Fernwartung schalten wir uns auf Ihren Bildschirm und lösen es.')]),
 'ki': dict(
  desc='KI-Chatbots für Schweizer KMU. Beantwortet häufige Fragen direkt auf Ihrer Website, nur mit Ihren Informationen, und gibt den Rest an Sie weiter.',
  h1='Ein Chatbot, der Ihre <em class="hl">Antworten kennt.</em>',
  intro='Viele Fragen kommen immer wieder: Öffnungszeiten, Preise, Parkplätze, freie Termine. Ein Chatbot beantwortet sie direkt auf Ihrer Website, mit Ihren Informationen. Was er nicht weiss, gibt er an Sie weiter.',
  facts=['Antwortet rund um die Uhr', 'Nur mit Ihren Informationen', 'In mehreren Sprachen'],
  incl_t='Ein Helfer auf Ihrer Website, der nichts erfindet und weiss, wann er Sie fragen muss.',
  incl=[('Ihre Inhalte', 'Der Chatbot antwortet nur mit dem, was auf Ihrer Website und in Ihren Unterlagen steht.'),
        ('Mehrsprachig', 'Er antwortet in der Sprache, in der man ihn fragt.'),
        ('Übergabe an Sie', 'Bei schwierigen Fragen nimmt er Name und E-Mail auf und gibt sie an Sie weiter.'),
        ('Termine', 'Auf Wunsch schlägt er freie Termine vor oder führt zur Buchung.'),
        ('Gestaltung', 'Er passt zu Ihrer Website, mit Ihren Farben und Ihrem Ton.'),
        ('Datenschutz', 'Was gespeichert wird, ist dokumentiert und steht in Ihrer Datenschutzerklärung.')],
  steps=[('Gespräch', 'Welche Fragen bekommen Sie jeden Tag?', 'Tag 1'),
         ('Inhalte sammeln', 'Wir sammeln die Fragen und Ihre Antworten dazu.', 'Woche 1'),
         ('Test', 'Sie testen den Chatbot, bevor ihn Ihre Kunden sehen.', 'Woche 2'),
         ('Start und Pflege', 'Wir schauen, was gefragt wird, und verbessern die Antworten.', 'Laufend')],
  price_note='Der Preis hängt davon ab, wie viele Inhalte der Chatbot kennen soll und ob er Termine vorschlägt. Nach dem ersten Gespräch bekommen Sie eine Offerte mit festem Preis.',
  faq=[('Erfindet der Chatbot Antworten?', 'Er ist so eingestellt, dass er nur mit Ihren Informationen antwortet. Weiss er etwas nicht, sagt er das und gibt die Frage an Sie weiter.'),
       ('Brauche ich dafür eine neue Website?', 'Nein. Der Chatbot funktioniert auch auf Ihrer bestehenden Website.'),
       ('Wer sieht die Gespräche?', 'Sie. So merken Sie, was Ihre Kunden wirklich wissen wollen.'),
       ('Ersetzt er meine Mitarbeitenden?', 'Nein. Er nimmt Ihnen die immer gleichen Fragen ab. Für alles andere sind Sie da.')]),
}
ORDER = ['websites', 'shops', 'seo', 'hosting', 'm365', 'ki']


def incl(items):
    return '<ol class="inc">' + ''.join(f'<li><span class="n">{k + 1:02d}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for k, (t, d) in enumerate(items)) + '</ol>'


def steps(items):
    return '<ol class="stp">' + ''.join(f'<li><span class="stp-n">{k + 1:02d}</span><span class="stp-w">{w}</span><h3>{t}</h3><p>{d}</p></li>' for k, (t, d, w) in enumerate(items)) + '</ol>'


def prlist(rows):
    out = '<dl class="pr-list">'
    for t, sub, pre, val, post in rows:
        s = f'<small>{sub}</small>' if sub else ''
        if not val[0].isdigit():
            out += f'<div><dt>{t}{s}</dt><dd class="t">{val}</dd></div>'
            continue
        p = {'': 'CHF', 'ab': 'ab CHF', '+': '+ CHF'}[pre]
        po = f'<small>{post}</small>' if post else ''
        out += f'<div><dt>{t}{s}</dt><dd><small>{p}</small>{val}{po}</dd></div>'
    return out + '</dl>'


def faq(items, title='Häufige <em class="hl">Fragen</em>'):
    qs = ''.join(f'<details><summary><span>{q}</span><i class="px" aria-hidden="true"></i></summary><p>{a}</p></details>' for q, a in items)
    return (f'<section class="sp-sec sp-faq pad" aria-labelledby="fqT"><div class="sp-faq-l"><h2 id="fqT">{title}</h2>'
            f'<a class="sv-all" href="fragen.html">Alle Fragen {ARROW}</a></div><div class="dl">{qs}</div></section>')


def more(cur):
    rows = ''.join(f'<li><a href="{FILES[k]}"><span class="lx-t">{NAMES[k]}</span><span class="lx-d">{SHORT[k]}</span><span class="lx-a">{ARROW}</span></a></li>' for k in ORDER if k != cur)
    return ('<section class="sp-sec pad" aria-labelledby="mrT">' + head('Weitere <em class="hl">Leistungen</em>', 'Alles aus einer Hand. Mit einer Ansprechperson, die Ihren Betrieb kennt.', id_='mrT') +
            f'<ul class="lx-list">{rows}</ul></section>')


def crumb(here, parent=('Leistungen', 'leistungen.html')):
    p = f'<a href="{parent[1]}">{parent[0]}</a><span aria-hidden="true">/</span>' if parent else ''
    return f'<nav class="crumb" aria-label="Pfad"><a href="index.html">Start</a><span aria-hidden="true">/</span>{p}<span aria-current="page">{here}</span></nav>'


def service(k):
    s = SVC[k]
    name = NAMES[k]
    hero = f'''<section class="sp-hero pad">
    <div class="sp-tx">
      {crumb(name)}
      <h1>{s['h1']}</h1>
      <p class="sp-in">{s['intro']}</p>
      <div class="sp-act"><a class="btn btn-sage" href="kontakt.html">Termin wählen {ARROW}</a><a class="btn btn-out" href="preise.html">Preise ansehen</a></div>
      <ul class="sp-facts">{''.join(f'<li>{f}</li>' for f in s['facts'])}</ul>
    </div>
    <div class="sp-dev">{mac(k, 'Beispiel: ' + name, eager=True)}</div>
  </section>'''
    inc = '<section class="sp-sec pad" aria-labelledby="incT">' + head('Was <em class="hl">dazugehört</em>', s['incl_t'], id_='incT') + incl(s['incl']) + '</section>'
    stp = '<section class="sp-sec pad" aria-labelledby="stpT">' + head('So <em class="hl">läuft es</em>', 'Sie wissen in jedem Schritt, wo wir stehen und was als Nächstes kommt.', id_='stpT') + steps(s['steps']) + '</section>'
    refs = ''
    if s.get('refs'):
        refs = ('<section class="wks pad" aria-labelledby="wksT">' + head('Unsere <em class="hl">Arbeiten</em>', 'Zwei Websites, die wir zuletzt gebaut haben. Beide sind online, schauen Sie sie sich ruhig selbst an.', id_='wksT') +
                ''.join(home9._ref(i, r) for i, r in enumerate(home9.REFS)).replace('%%DEV_kf%%', 'assets/img/dev-kf.webp').replace('%%DEV_ka%%', 'assets/img/dev-ka.webp') + '</section>')
    note = f'<p class="pr-note">{s["price_note"]}</p>' if s.get('price_note') else ''
    if s.get('prices'):
        pr = f'''<section class="pr pad" aria-labelledby="prT">
    <div class="pr-left"><h2 id="prT">Was es <em class="hl">kostet</em></h2><p>Sie kennen den Preis, bevor wir anfangen. Alle Preise in CHF, einmalig, wenn nichts anderes steht.</p><a class="sv-all" href="preise.html">Zum Preisrechner {ARROW}</a></div>
    <div>{prlist(s['prices'])}{note}</div>
  </section>'''
    else:
        pr = f'''<section class="pr pad" aria-labelledby="prT">
    <div class="pr-left"><h2 id="prT">Was es <em class="hl">kostet</em></h2></div>
    <div class="pr-only"><p>{s['price_note']}</p><a class="btn btn-sage" href="kontakt.html">Termin wählen {ARROW}</a></div>
  </section>'''
    main = '\n  ' + '\n\n  '.join([hero, inc, stp, refs, pr, faq(s['faq']), more(k)]) + '\n'
    return (f'{name} | websiten.ch', s['desc'], main)


# ------------------------------------------------------------------ Leistungen (Übersicht)
def leistungen():
    rows = ''
    for i, k in enumerate(ORDER):
        subs = next(s for j, t, d, s in home9.SV if j == k)
        rows += (f'<li><a href="{FILES[k]}"><span class="ov-n">{i + 1:02d}</span>'
                 f'<span class="ov-tx"><span class="ov-t">{NAMES[k]}</span><span class="ov-d">{SHORT[k]}</span>'
                 f'<span class="ov-s">{"".join(f"<i>{x}</i>" for x in subs)}</span><span class="ov-m">Mehr erfahren {ARROW}</span></span>'
                 f'<span class="ov-v">{mac(k, "Beispiel: " + NAMES[k], eager=i < 2)}</span></a></li>')
    hero = f'''<section class="ph pad">
    {crumb('Leistungen', None)}
    <h1>Alles, was Ihr Betrieb <em class="hl">online braucht.</em></h1>
    <p class="sp-in">Sechs Leistungen von einer Ansprechperson. Mit festem Preis und Servern in der Schweiz. Wählen Sie, was Sie brauchen, den Rest lassen Sie weg.</p>
  </section>'''
    ov = f'<section class="ov pad" aria-label="Unsere Leistungen"><ol class="ov-list">{rows}</ol></section>'
    who = ['Handwerk und Bau', 'Gastronomie und Cafés', 'Coiffeur und Kosmetik', 'Praxen und Therapie', 'Läden und Shops', 'Treuhand und Beratung']
    why = [('Eine Ansprechperson', 'Sie erklären Ihr Anliegen einmal. Wir kennen Ihren Betrieb, Ihre Website und Ihre Zugänge.'),
           ('Fester Preis', 'Sie kennen den Betrag, bevor wir anfangen. Kommt etwas dazu, besprechen wir es vorher.'),
           ('Daten in der Schweiz', 'Domains, Hosting und E-Mail laufen bei Infomaniak in Genf.')]
    whyh = ('<section class="sp-sec pad" aria-labelledby="whyT">' + head('Warum aus <em class="hl">einer Hand</em>', 'Sie müssen nicht fünf Firmen koordinieren, die sich bei einem Problem gegenseitig die Schuld geben.', id_='whyT') +
            '<ol class="stp stp-3">' + ''.join(f'<li><span class="stp-n">{i + 1:02d}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(why)) + '</ol></section>')
    whoh = ('<section class="sp-sec pad" aria-labelledby="whoT">' + head('Für wen wir <em class="hl">arbeiten</em>', 'Für Betriebe, die gut in ihrer Arbeit sind und das auch online zeigen wollen.', id_='whoT') +
            '<ul class="who">' + ''.join(f'<li>{w}</li>' for w in who) + '</ul></section>')
    main = '\n  ' + '\n\n  '.join([hero, ov, whyh, whoh]) + '\n'
    return ('Leistungen | websiten.ch', 'Websites, Online-Shops, Google und SEO, Hosting bei Infomaniak, Microsoft 365 und KI-Chatbots für Schweizer KMU.', main)


# ------------------------------------------------------------------ Preise
def preise():
    m = P.PREISE_MAIN
    lists = m[m.index('<div class="pl-grid">'):m.index('</div>\n    </div><div class="pv" id="v2"')]
    lists = re.sub(r'<li><span>Die ersten 3 Monate, pro Monat</span><i></i><b>10\.–</b></li>', '', lists)
    assert '10.–' not in lists
    lists = lists.replace('<p>Mit TWINT, Karte und Versand. Das Shopify-Abo zahlen Sie direkt.</p>', '<p>Mit TWINT, Karte, Rechnung und Versand. Das Shopify-Abo zahlen Sie direkt an Shopify.</p>')
    hero = f'''<section class="ph pad">
    {crumb('Preise', None)}
    <h1>Feste Preise. <em class="hl">Vorher bekannt.</em></h1>
    <p class="sp-in">Sie wissen, was es kostet, bevor wir anfangen. Sie zahlen die Hälfte bei Auftrag und den Rest, wenn alles online ist.</p>
  </section>'''
    calc = f'''<section class="sp-sec calc pad" id="rechner" aria-labelledby="rcT">
    {head('Rechnen Sie <em class="hl">selbst</em>', 'Wählen Sie aus, was Sie brauchen. Der Betrag, den Sie hier sehen, steht so auch in der Offerte.', id_='rcT')}
    <div class="ps">
      <div class="ps-ctrl">
        <div class="ps-type" role="group" aria-label="Art"><button type="button" data-t="web" aria-pressed="true">Website</button><button type="button" data-t="shop" aria-pressed="false">Online-Shop</button></div>
        <label class="ps-lbl" for="psPages">Wie viele Seiten? <b id="psPagesOut">4</b></label>
        <input type="range" id="psPages" min="1" max="20" value="4">
        <div class="ps-scale" aria-hidden="true"><span>1</span><span>5</span><span>10</span><span>15</span><span>20</span></div>
        <div class="ps-prod" id="psProd" hidden><label class="ps-lbl" for="psProducts">Wie viele Produkte? <b id="psProductsOut">bis 30</b></label><input type="range" id="psProducts" min="0" max="3" value="0"><div class="ps-scale" aria-hidden="true"><span>30</span><span>150</span><span>500</span><span>mehr</span></div></div>
        <div class="ps-lang"><span class="ps-lbl" id="langLbl">Wie viele Sprachen?</span><div class="seg" role="group" aria-labelledby="langLbl"><button type="button" data-l="1" aria-pressed="true">1</button><button type="button" data-l="2" aria-pressed="false">2</button><button type="button" data-l="3" aria-pressed="false">3</button><button type="button" data-l="4" aria-pressed="false">4</button></div></div>
        <div class="ps-opts">
          <label><input type="checkbox" id="psTexts" data-p="90" data-per="1"><span>Texte schreiben wir<small>CHF 90.– pro Seite</small></span></label>
          <label><input type="checkbox" id="psBook" data-p="290"><span>Online-Terminbuchung<small>CHF 290.–</small></span></label>
          <label><input type="checkbox" id="psBlog" data-p="190"><span>News oder Blog<small>CHF 190.–</small></span></label>
          <label><input type="checkbox" id="psGmb" data-p="150"><span>Google-Profil einrichten<small>CHF 150.–</small></span></label>
          <label><input type="checkbox" id="psAds" data-p="390"><span>Google Ads einrichten<small>CHF 390.–</small></span></label>
        </div>
      </div>
      <div class="ps-out" aria-live="polite">
        <small>Einmalig</small>
        <div class="ps-total"><span>CHF</span><b id="psTotal">590</b></div>
        <div class="ps-year" id="psYear">Dazu Hosting und Domain CHF 25.– im Monat</div>
        <div class="ps-lines" id="psLines"></div>
        <a class="btn btn-sage" id="psGo" href="kontakt.html">Termin wählen {ARROW}</a>
      </div>
    </div>
  </section>'''
    lst = f'''<section class="sp-sec pad" aria-labelledby="plT">
    {head('Alle Preise <em class="hl">auf einen Blick</em>', 'In CHF, einmalig, wenn nichts anderes steht. Hosting rechnen wir monatlich ab.', id_='plT')}
    {lists}
  </section>'''
    fine = '''<section class="sp-sec fine2 pad" aria-labelledby="fnT">
    <div class="fine2-l"><h2 id="fnT">Gut zu <em class="hl">wissen</em></h2></div>
    <div class="fine2-r">
      <div><h3>Immer dabei</h3><p>Gestaltung, Handy-Version, SSL, Kontaktformular, die Einrichtung bei Infomaniak und eine Einführung.</p></div>
      <div><h3>Nicht dabei</h3><p>Fotografen, gekaufte Bilder, das Shopify-Abo und die Gebühren der Zahlungsanbieter. Kommt so etwas dazu, steht es vorher in der Offerte.</p></div>
      <div><h3>Bezahlung</h3><p>Die Hälfte bei Auftrag, der Rest, wenn alles online ist. Hosting monatlich.</p></div>
    </div>
  </section>'''
    main = '\n  ' + '\n\n  '.join([hero, calc, lst, fine]) + '\n'
    return ('Preise | websiten.ch', 'Feste Preise für Websites, Online-Shops und Hosting. Website mit 4 Seiten CHF 590.–, Hosting CHF 25.– im Monat. Mit Preisrechner.', main)


PREISE_JS = r'''
(function(){
  const $ = id => document.getElementById(id), fmt = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '’');
  let type = 'web', langs = 1;
  const PROD = [['bis 30', 0], ['bis 150', 490], ['bis 500', 990], ['über 500', 1890]];
  let last = '';
  function calc(){
    const pages = +$('psPages').value, shop = type === 'shop', L = [];
    $('psPagesOut').textContent = pages;
    L.push([shop ? 'Shop mit 4 Seiten und 30 Produkten' : 'Website mit 4 Seiten', shop ? 1890 : 590]);
    if(pages > 4) L.push([(pages - 4) + ' weitere Seite' + (pages > 5 ? 'n' : ''), (pages - 4) * 150]);
    if(shop){ const p = PROD[+$('psProducts').value]; $('psProductsOut').textContent = p[0]; if(p[1]) L.push(['Produkte ' + p[0], p[1]]); }
    if(langs > 1) L.push([(langs - 1) + ' weitere Sprache' + (langs > 2 ? 'n' : '') + ', ' + pages + ' Seiten', (langs - 1) * pages * 70]);
    document.querySelectorAll('.ps-opts input').forEach(i => { if(i.checked){ const p = +i.dataset.p; const t = i.nextElementSibling.firstChild.textContent.trim(); L.push(i.dataset.per ? [t + ', ' + pages + ' Seiten', p * pages] : [t, p]); } });
    const total = L.reduce((a, l) => a + l[1], 0);
    $('psTotal').textContent = fmt(total);
    $('psYear').textContent = shop ? 'Dazu das Shopify-Abo, direkt an Shopify' : 'Dazu Hosting und Domain CHF 25.– im Monat';
    $('psLines').innerHTML = L.map(l => `<div><span>${l[0]}</span><b>${fmt(l[1])}</b></div>`).join('');
    last = 'Preisrechner: ' + L.map(l => l[0] + ' (CHF ' + fmt(l[1]) + ')').join(', ') + '. Total CHF ' + fmt(total) + '.';
  }
  document.querySelectorAll('.ps-type button').forEach(b => b.onclick = () => { document.querySelectorAll('.ps-type button').forEach(o => o.setAttribute('aria-pressed', o === b)); type = b.dataset.t; $('psProd').hidden = type !== 'shop'; calc(); });
  document.querySelectorAll('.seg button').forEach(b => b.onclick = () => { document.querySelectorAll('.seg button').forEach(o => o.setAttribute('aria-pressed', o === b)); langs = +b.dataset.l; calc(); });
  ['psPages','psProducts'].forEach(id => $(id).addEventListener('input', calc));
  document.querySelectorAll('.ps-opts input').forEach(i => i.addEventListener('change', calc));
  $('psGo').addEventListener('click', () => { try { localStorage.setItem('websiten-anfrage', last); } catch(e){} });
  calc();
})();
'''

# ------------------------------------------------------------------ Über uns
def ueber():
    hero = f'''<section class="ph pad">
    {crumb('Über uns', None)}
    <h1>Klartext, feste Preise und <em class="hl">Termine, die halten.</em></h1>
    <p class="sp-in">websiten.ch baut Websites, Online-Shops und alles, was dazugehört, für Betriebe in der ganzen Schweiz. Für Handwerker, Praxen, Restaurants und Läden, die online gefunden werden wollen, ohne sich selbst um die Technik zu kümmern.</p>
  </section>'''
    bel = [('Ein fester Preis ist ein fester Preis.', 'Sie bekommen eine Offerte, und die gilt. Möchten Sie unterwegs etwas Neues, besprechen wir das vorher. Überraschungen auf der Rechnung gibt es bei uns nicht.'),
           ('Sie verstehen, was wir tun.', 'Wir erklären, was wir vorschlagen und warum. Ohne Abkürzungen, die niemand kennt. Ergibt etwas für Ihren Betrieb keinen Sinn, sagen wir es, auch wenn wir daran verdienen würden.'),
           ('Ihre Website gehört Ihnen.', 'Domain, Inhalte und Zugänge laufen auf Ihren Namen. Möchten Sie einmal wechseln, bekommen Sie alles, was Sie dafür brauchen.'),
           ('Ihre Daten bleiben in der Schweiz.', 'Domains, Hosting und E-Mail laufen bei Infomaniak, einem Schweizer Anbieter aus Genf mit Rechenzentren in der Schweiz.')]
    beliefs = ('<section class="sp-sec pad" aria-labelledby="blT">' + head('Woran Sie uns <em class="hl">messen können</em>', 'Vier Dinge, die bei uns immer gelten. Für die Website mit vier Seiten genauso wie für den grossen Shop.', id_='blT') +
               '<ol class="bel">' + ''.join(f'<li><span class="n">{i + 1:02d}</span><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(bel)) + '</ol></section>')
    band = f'''<section class="band2 pad" data-sage>
    {GRAIN}
    <div><h2>Eine Ansprechperson für alles, was online ist.</h2><p>Website, Shop, Google, Domains, E-Mail und Microsoft 365. Sie müssen nicht fünf Firmen koordinieren, die sich bei einem Problem gegenseitig die Schuld geben. Sie schreiben uns, und die Sache wird erledigt.</p></div>
    <svg class="band2-mark" viewBox="12 10 174 188" aria-hidden="true"><path class="lm-l" d="{MARK_LIGHT}"/><path class="lm-d" d="{MARK_DARK}"/></svg>
  </section>'''
    tools = [('Infomaniak', 'Domains, Hosting und E-Mail bei einem Schweizer Anbieter aus Genf'),
             ('WordPress', 'Für Websites, die Sie danach selbst pflegen können'),
             ('Shopify', 'Für Online-Shops, die ohne Bastelei laufen'),
             ('WooCommerce', 'Für einen Shop direkt in der bestehenden WordPress-Website'),
             ('Microsoft 365', 'E-Mail, Teams und OneDrive fürs Büro'),
             ('Google', 'Unternehmensprofil, Search Console und Google Ads')]
    tl = ('<section class="sp-sec pad" aria-labelledby="tlT">' + head('Womit wir <em class="hl">arbeiten</em>', 'Bewährte Werkzeuge, die Ihr Betrieb auch in fünf Jahren noch nutzen kann.', id_='tlT') +
          '<dl class="tools2">' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in tools) + '</dl>'
          f'<div class="li-row"><a class="sv-all" href="{LI}" target="_blank" rel="noopener">websiten.ch auf LinkedIn {UP}</a></div></section>')
    main = '\n  ' + '\n\n  '.join([hero, beliefs, band, tl]) + '\n'
    return ('Über uns | websiten.ch', 'Wie websiten.ch arbeitet: feste Preise, klare Worte, eine Ansprechperson und Daten in der Schweiz.', main)


# ------------------------------------------------------------------ Kontakt (ohne Telefon)
def kontakt():
    m = P.KONTAKT_MAIN
    m = m.replace('<div><h1>Termin wählen</h1><p>15 Minuten am Telefon oder per Video. Sie erzählen, was Sie vorhaben. Danach wissen Sie, was es kostet und wie lange es dauert. Das Gespräch ist kostenlos.</p></div>',
                  '<div>' + crumb('Kontakt', None) + '<h1>Termin <em class="hl">wählen</em></h1><p class="sp-in">15 Minuten per Video. Sie erzählen, was Sie vorhaben. Danach wissen Sie, was es kostet und wie lange es dauert. Das Gespräch ist kostenlos.</p></div>')
    m = m.replace('\n      <div><span><small>Telefon</small><b>[Telefon]</b></span></div>', '\n      <div><span><small>Antwort</small><b class="nb">Am gleichen oder nächsten Arbeitstag</b></span></div>')
    m = m.replace('<div class="f"><label for="tel">Telefon</label><input type="tel" id="tel" autocomplete="tel" maxlength="40"></div>\n', '')
    m = re.sub(r'\s*<div class="f full"><span class="lbl2" id="modeLbl">.*?</div></div>', '', m, flags=re.S)
    m = m.replace('<li>Wir rufen Sie an oder treffen uns per Video. 15 Minuten, ohne Verkaufsgespräch.</li>', '<li>Wir treffen uns per Video mit Google Meet. 15 Minuten, ohne Verkaufsgespräch.</li>')
    m = m.replace('<section class="page-hero pad k-hero">', '<section class="ph pad k-hero">')
    assert 'Telefon' not in m and 'tel"' not in m and 'modeLbl' not in m, re.findall(r'.{40}Telefon.{40}', m)
    j = P.KONTAKT_JS
    j = j.replace("b.classList.add('wk')", "b.classList.add('wkb')")
    j = j.replace("const st = {days:[], day:null, time:null, mode:'phone'};", "const st = {days:[], day:null, time:null, mode:'meet'};")
    j = j.replace("const name = $('name'), mail = $('mail'), tel = $('tel');\n    [name, mail, tel].forEach(i => i.classList.remove('bad'));", "const name = $('name'), mail = $('mail');\n    [name, mail].forEach(i => i.classList.remove('bad'));")
    j = re.sub(r"\n    if\(st\.mode === 'phone'.*?\n", '\n', j)
    j = j.replace("phone:tel.value.trim(), ", "phone:'', ")
    j = re.sub(r"  document\.querySelectorAll\('\.modes button'\).*?\}\)\);\n", '', j, flags=re.S)
    j = j.replace(" : `Wir rufen Sie unter ${d.phone.replace(/</g, '')} an.`", " : `Den Link für Google Meet bekommen Sie per E-Mail.`")
    assert "$('tel')" not in j and 'tel.value' not in j and 'Wir rufen' not in j, j
    css = P.KONTAKT_CSS.replace('.day.wk{', '.day.wkb{').replace('#34403A', '#3A3A3A').replace('rgba(131,170,140,.08)', 'rgba(143,174,150,.07)').replace('#BAC5BE', '#B5B5B5').replace('#C7D0CA', '#BDBDBD').replace('#C9D3CD', '#C9C9C9').replace('#D3DBD6', '#D3D3D3')
    return ('Termin wählen | websiten.ch', 'Buchen Sie ein kostenloses Gespräch von 15 Minuten per Video mit websiten.ch.', m, css, j)


# ------------------------------------------------------------------ Fragen
FQ = [('Wie lange geht es, bis meine Website online ist?', 'Eine Website mit 4 Seiten meistens drei bis vier Wochen, eine grössere fünf bis acht. Das Datum steht in der Offerte, und daran halten wir uns.'),
      ('Was kostet eine Website?', 'Eine Website mit 4 Seiten kostet CHF 590.–, jede weitere Seite CHF 150.–. Einen Online-Shop gibt es ab CHF 1’890.–. Im Preisrechner sehen Sie den genauen Betrag.'),
      ('Was zahle ich nach dem Start noch?', 'CHF 25.– im Monat für Hosting, .ch-Domain, E-Mail, SSL, Backups und Updates. Kleine Änderungen sind dabei.'),
      ('Gehört die Website danach mir?', 'Ja. Domain, Inhalte und Zugänge laufen auf Ihren Namen. Wenn Sie einmal wechseln wollen, bekommen Sie alles.'),
      ('Wo sind meine Daten gespeichert?', 'In der Schweiz. Server, Domains und E-Mail laufen bei Infomaniak in Genf.'),
      ('Kann ich Texte und Bilder selbst ändern?', 'Ja, Sie bekommen eine kurze Einführung. Oder Sie schicken uns eine Nachricht, und wir machen es.'),
      ('Bringt ihr mich bei Google auf Platz 1?', 'Das kann niemand ehrlich versprechen. Wir machen die Seite technisch sauber und schreiben Inhalte zu dem, was Ihre Kunden suchen. Das ist die Grundlage, damit Sie gefunden werden.'),
      ('Schreibt ihr auch die Texte?', 'Ja, auf Wunsch. Pro Seite CHF 90.–. Sie lesen alles, bevor es online geht.'),
      ('Wie läuft die Bezahlung?', 'Die Hälfte bei Auftrag, der Rest, wenn die Website online ist. Hosting rechnen wir monatlich ab.'),
      ('Arbeitet ihr nur in meiner Region?', 'Nein, wir arbeiten für Betriebe in der ganzen Schweiz. Das erste Gespräch läuft per Video, alles Weitere per E-Mail und Video.')]


def fragen():
    q = ''.join(f'<li><button type="button" class="fq" id="fq{i}" aria-controls="fa{i}" aria-expanded="{"true" if i == 0 else "false"}"><span>{a}</span></button><div class="fa-m" id="fam{i}"><p>{b}</p></div></li>' for i, (a, b) in enumerate(FQ))
    a = ''.join(f'<div class="fa{" on" if i == 0 else ""}" id="fa{i}" role="region" aria-labelledby="fq{i}"><p>{b}</p></div>' for i, (x, b) in enumerate(FQ))
    main = f'''
  <section class="ph pad">
    {crumb('Fragen', None)}
    <h1>Häufige <em class="hl">Fragen</em></h1>
    <p class="sp-in">Die Antworten auf das, was wir am häufigsten gefragt werden. Fahren Sie über eine Frage, die Antwort steht daneben.</p>
  </section>
  <section class="faq pad" id="fragen" style="padding-top:0">
    <div class="fq-grid">
      <ol class="fq-list">{q}</ol>
      <div class="fq-ans" aria-live="polite">{a}
        <a class="fq-more" href="kontakt.html">Ihre Frage ist nicht dabei? Schreiben Sie uns. {ARROW}</a>
      </div>
    </div>
  </section>
'''
    css = P.FRAGEN_CSS.replace('#7F8B84', '#7A7A7A').replace('#C9D2CD', '#CFCFCF').replace('#C7D0CA', '#BDBDBD').replace('var(--sage)', 'var(--acc-s)').replace('color:var(--sage-light);padding-bottom:6px;border-bottom:1px solid var(--sage-deep)', 'color:var(--text);padding-bottom:6px;border-bottom:1px solid var(--acc-s)')
    return ('Fragen | websiten.ch', 'Häufige Fragen zu Websites, Preisen, Hosting und Daten.', main, css, P.FRAGEN_JS)


# ------------------------------------------------------------------ Rechtliches
def legal(which):
    m = P.IMPRESSUM_MAIN if which == 'i' else P.DATENSCHUTZ_MAIN
    name = 'Impressum' if which == 'i' else 'Datenschutz'
    m = re.sub(r'<section class="page-hero pad"><h1>.*?</h1></section>', f'<section class="ph ph-s pad">{crumb(name, None)}<h1>{name}</h1></section>', m)
    m = m.replace('E-Mail: hallo@websiten.ch<br>Telefon: [Telefon]', 'E-Mail: hallo@websiten.ch')
    m = m.replace('zum Beispiel Name, Firma, E-Mail, Telefonnummer und Ihre Nachricht', 'zum Beispiel Name, Firma, E-Mail-Adresse und Ihre Nachricht')
    m = m.replace('und senden Ihnen eine Bestätigung per E-Mail.', 'und senden Ihnen eine Bestätigung per E-Mail. Das Gespräch findet über Google Meet statt.')
    assert 'Telefon' not in m
    return m


# ------------------------------------------------------------------ Gestaltung
CSS = r'''
/* Unterseiten: gleiche Sprache wie die Startseite */
.hl{font-style:normal;color:var(--acc-s)}
.btn-sage{background:var(--acc-s);color:#0C201A}
.btn-sage:hover{background:var(--acc-a1);color:#0C201A}
.btn-out{border:1px solid rgba(255,255,255,.26);color:var(--text)}
.btn-out:hover{border-color:var(--text)}
.sv-all{display:inline-flex;align-items:center;gap:12px;font-size:17px;padding-bottom:6px;border-bottom:1px solid var(--acc-s);transition:gap .3s var(--ease)}
.sv-all:hover{gap:18px}
.sv-all svg{color:var(--acc-s)}
.crumb{display:flex;flex-wrap:wrap;align-items:center;gap:10px;font-size:14px;color:var(--muted);margin-bottom:clamp(22px,2.6vw,36px)}
.crumb a{transition:color .2s}
.crumb a:hover{color:var(--text)}
.crumb span[aria-hidden]{color:#4A4A4A}
.crumb [aria-current]{color:var(--acc-s)}
.sp-in{font-size:clamp(17px,1.35vw,21px);line-height:1.6;color:#C4C4C4;max-width:52ch;margin-top:clamp(22px,2.4vw,34px)}

/* Einstieg mit MacBook */
.sp-hero{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.12fr);gap:clamp(32px,5vw,96px);align-items:center;padding-top:clamp(120px,13vw,190px);padding-bottom:clamp(70px,8vw,120px);min-height:min(100svh,980px)}
.sp-hero h1,.ph h1{font-size:clamp(42px,5vw,92px);line-height:.98;font-weight:700;letter-spacing:-.055em;max-width:14ch}
.ph h1{max-width:16ch}
.sp-act{display:flex;flex-wrap:wrap;gap:12px;margin-top:clamp(28px,3vw,44px)}
.sp-facts{list-style:none;display:flex;flex-wrap:wrap;gap:10px 26px;margin:clamp(28px,3vw,44px) 0 0;padding:22px 0 0;border-top:1px solid var(--line);font-size:15px;color:var(--muted)}
.sp-facts li::before{content:"";display:inline-block;width:5px;height:5px;border-radius:50%;background:var(--acc-s);margin-right:9px;vertical-align:middle}
.sp-dev{margin-right:calc(var(--pad) * -.6)}
.mac{position:relative;width:100%;aspect-ratio:1060/690}
.mac-scr{position:absolute;left:9.717%;top:6.522%;width:80.566%;height:77.391%;overflow:hidden;background:#0B0B0B;border-radius:.6% .6% 0 0}
.mac-scr img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top}
.mac-gl{position:absolute;inset:0;background:linear-gradient(118deg,rgba(255,255,255,.08),rgba(255,255,255,.02) 30%,rgba(255,255,255,0) 44%);pointer-events:none}
.mac-fr{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.ph{padding-top:clamp(130px,14vw,210px);padding-bottom:clamp(56px,7vw,100px)}
.ph-s h1{font-size:clamp(40px,4.4vw,72px)}
@keyframes spUp{from{opacity:0;transform:translateY(18px)}to{opacity:1;transform:none}}
.sp-tx > *,.ph > *{animation:spUp .8s var(--ease) both}
.sp-tx > *:nth-child(2),.ph > *:nth-child(2){animation-delay:.06s}
.sp-tx > *:nth-child(3),.ph > *:nth-child(3){animation-delay:.12s}
.sp-tx > *:nth-child(4){animation-delay:.18s}
.sp-tx > *:nth-child(5){animation-delay:.24s}
.sp-dev{animation:spUp 1s .15s var(--ease) both}
@media (prefers-reduced-motion: reduce){ .sp-tx > *,.ph > *,.sp-dev{animation:none} }

/* Abschnitte */
.sp-sec{padding-top:clamp(90px,10vw,150px);padding-bottom:clamp(90px,10vw,150px);border-top:1px solid var(--line)}
.lx-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);gap:clamp(24px,7vw,140px);align-items:end;margin-bottom:clamp(44px,5.5vw,84px)}
.lx-head h2{font-size:clamp(38px,4.4vw,76px);line-height:1;font-weight:700;letter-spacing:-.05em}
.lx-head p{font-size:clamp(17px,1.35vw,20px);line-height:1.6;color:#BDBDBD;max-width:42ch}

/* Was dazugehört */
.inc{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:clamp(40px,7vw,140px);border-bottom:1px solid var(--line)}
.inc li{display:grid;grid-template-columns:48px minmax(0,1fr);padding:clamp(24px,2.4vw,34px) 0;border-top:1px solid var(--line)}
.inc .n,.bel .n{font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums;padding-top:7px}
.inc h3{font-size:clamp(20px,1.6vw,25px);font-weight:600;letter-spacing:-.025em;line-height:1.2}
.inc p{font-size:16.5px;line-height:1.6;color:#B5B5B5;margin-top:8px;max-width:44ch}
.inc li:hover .n{color:var(--acc-s)}

/* Ablauf */
.stp{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:clamp(24px,3vw,48px)}
.stp-3{grid-template-columns:repeat(3,minmax(0,1fr))}
.stp li{position:relative;border-top:1px solid var(--line);padding-top:26px}
.stp li::before{content:"";position:absolute;left:0;top:-1px;width:44px;height:2px;background:var(--acc-s)}
.stp-n{font-size:13px;color:var(--acc-s);font-variant-numeric:tabular-nums}
.stp-w{float:right;font-size:13px;color:var(--muted)}
.stp h3{font-size:clamp(22px,1.8vw,28px);font-weight:700;letter-spacing:-.035em;margin-top:18px}
.stp p{font-size:16.5px;line-height:1.6;color:#B5B5B5;margin-top:10px;max-width:34ch}

/* Arbeiten (aus der Startseite) */
.wks{padding-top:clamp(90px,10vw,150px);padding-bottom:clamp(50px,6vw,90px);border-top:1px solid var(--line)}
.wks .lx-head{margin-bottom:clamp(20px,3vw,40px)}
.wk{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);gap:clamp(40px,7vw,140px);align-items:center;padding:clamp(40px,5vw,72px) 0;border-top:1px solid var(--line)}
.wk-n{font-size:14px;color:var(--acc-s);font-variant-numeric:tabular-nums}
.wk h3{font-size:clamp(26px,2.4vw,40px);line-height:1.08;font-weight:700;letter-spacing:-.04em;margin-top:14px}
.wk-p{display:block;font-size:15px;color:var(--muted);margin-top:8px}
.wk p{font-size:clamp(16px,1.2vw,18px);line-height:1.65;color:#C4C4C4;margin-top:22px;max-width:42ch}
.wk ul{list-style:none;display:flex;flex-wrap:wrap;gap:8px 18px;margin:22px 0 0;padding:0;font-size:14.5px;color:var(--muted)}
.wk li::before{content:"";display:inline-block;width:5px;height:5px;border-radius:50%;background:var(--acc-s);margin-right:8px;vertical-align:middle}
.wk-l{display:inline-flex;align-items:center;gap:10px;margin-top:30px;font-size:16.5px;padding-bottom:5px;border-bottom:1px solid var(--acc-s);transition:gap .3s var(--ease)}
.wk-l:hover{gap:14px}
.wk-l svg{color:var(--acc-s)}
.wk-v{display:block;margin:-3% -4% -4% -2%}
.wk-v img{display:block;width:100%;height:auto;transition:transform .8s var(--ease)}
.wk-v:hover img{transform:translateY(-6px) scale(1.01)}
.wk.flip{grid-template-columns:minmax(0,1.35fr) minmax(0,1fr)}
.wk.flip .wk-tx{order:2}

/* Preise */
.pr{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);gap:clamp(40px,7vw,140px);padding-top:clamp(90px,10vw,150px);padding-bottom:clamp(90px,10vw,150px);border-top:1px solid var(--line)}
.pr h2{font-size:clamp(38px,4.4vw,76px);line-height:1;font-weight:700;letter-spacing:-.05em}
.pr-left p{font-size:clamp(17px,1.35vw,20px);line-height:1.6;color:#BDBDBD;max-width:34ch;margin:24px 0 32px}
.pr-list{margin:0;border-top:1px solid var(--line)}
.pr-list > div{display:flex;justify-content:space-between;align-items:baseline;gap:24px;padding:clamp(20px,2.2vw,30px) 0;border-bottom:1px solid var(--line)}
.pr-list dt{font-size:clamp(18px,1.45vw,22px);font-weight:600;letter-spacing:-.02em}
.pr-list dt small{display:block;font-size:15px;font-weight:400;letter-spacing:0;color:var(--muted);margin-top:6px}
.pr-list dd{margin:0;white-space:nowrap;font-size:clamp(30px,3vw,50px);font-weight:700;letter-spacing:-.05em;line-height:1;font-variant-numeric:tabular-nums;transition:color .3s}
.pr-list dd small{font-size:14px;font-weight:500;letter-spacing:0;color:var(--acc-s);margin:0 8px}
.pr-list dd small:last-child{margin-right:0}
.pr-list dd.t{font-size:clamp(17px,1.4vw,21px);font-weight:500;letter-spacing:-.01em;color:var(--acc-s)}
.pr-list > div:hover dd:not(.t){color:var(--acc-s)}
.pr-note{font-size:16px;line-height:1.6;color:var(--muted);margin-top:24px;max-width:56ch}
.pr-only p{font-size:clamp(19px,1.6vw,24px);line-height:1.55;color:#D0D0D0;max-width:40ch;margin-bottom:34px}

/* Fragen pro Leistung */
.sp-faq{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);gap:clamp(40px,7vw,140px);align-items:start}
.sp-faq h2{font-size:clamp(38px,4.4vw,76px);line-height:1;font-weight:700;letter-spacing:-.05em;margin-bottom:32px}
.dl{border-bottom:1px solid var(--line)}
.dl details{border-top:1px solid var(--line)}
.dl summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:24px;padding:24px 0;font-size:clamp(18px,1.45vw,22px);font-weight:500;letter-spacing:-.01em;transition:color .2s}
.dl summary::-webkit-details-marker{display:none}
.dl summary:hover{color:#FFF}
.px{position:relative;flex:none;width:16px;height:16px}
.px::before,.px::after{content:"";position:absolute;left:0;top:7px;width:16px;height:1.6px;background:var(--acc-s);transition:transform .35s var(--ease)}
.px::after{transform:rotate(90deg)}
details[open] .px::after{transform:rotate(0)}
.dl p{font-size:17px;line-height:1.7;color:#BDBDBD;max-width:58ch;padding:0 0 28px}

/* Weitere Leistungen */
.lx-list{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.lx-list li{border-bottom:1px solid var(--line)}
.lx-list a{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);column-gap:clamp(40px,7vw,140px);align-items:center;padding:clamp(22px,2.4vw,34px) 0;position:relative}
.lx-t{font-size:clamp(26px,2.6vw,44px);line-height:1.05;font-weight:700;letter-spacing:-.045em;transition:color .3s,transform .45s var(--ease)}
.lx-d{font-size:clamp(16px,1.2vw,18px);line-height:1.55;color:var(--muted);padding-right:56px;max-width:52ch;transition:color .3s}
.lx-a{position:absolute;right:0;top:50%;transform:translateY(-50%);color:var(--acc-d1);transition:transform .35s var(--ease),color .3s}
.lx-list:hover .lx-t{color:#5E5E5E}
.lx-list a:hover .lx-t{color:var(--text);transform:translateX(10px)}
.lx-list a:hover .lx-d{color:#D0D0D0}
.lx-list a:hover .lx-a{color:var(--acc-s);transform:translate(4px,-50%)}

/* Übersicht Leistungen */
.ov{padding-bottom:clamp(60px,7vw,110px)}
.ov-list{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.ov-list li{border-bottom:1px solid var(--line)}
.ov-list a{display:grid;grid-template-columns:56px minmax(0,1fr) minmax(0,1.05fr);gap:clamp(20px,4vw,72px);align-items:center;padding:clamp(28px,3.4vw,52px) 0}
.ov-n{font-size:14px;color:var(--muted);font-variant-numeric:tabular-nums;align-self:start;padding-top:12px;transition:color .3s}
.ov-t{display:block;font-size:clamp(32px,3.6vw,62px);line-height:1;font-weight:700;letter-spacing:-.05em;transition:color .3s}
.ov-d{display:block;font-size:clamp(16px,1.25vw,19px);line-height:1.6;color:#BDBDBD;margin-top:18px;max-width:44ch}
.ov-s{display:flex;flex-wrap:wrap;gap:6px 18px;margin-top:18px;font-size:14px;color:var(--muted)}
.ov-s i{font-style:normal}
.ov-s i::before{content:"";display:inline-block;width:4px;height:4px;border-radius:50%;background:var(--acc-s);margin-right:8px;vertical-align:middle}
.ov-m{display:inline-flex;align-items:center;gap:10px;margin-top:26px;font-size:16px;padding-bottom:4px;border-bottom:1px solid var(--acc-s);transition:gap .3s var(--ease)}
.ov-m svg{color:var(--acc-s)}
.ov-v .mac{transition:transform .8s var(--ease)}
.ov-list a:hover .ov-n{color:var(--acc-s)}
.ov-list a:hover .ov-m{gap:16px}
.ov-list a:hover .ov-v .mac{transform:translateY(-6px)}
.who{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));column-gap:clamp(24px,4vw,64px);border-bottom:1px solid var(--line)}
.who li{border-top:1px solid var(--line);padding:22px 0;font-size:clamp(19px,1.6vw,24px);font-weight:600;letter-spacing:-.02em}

/* Preise */
.calc .ps{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(300px,.8fr);gap:clamp(40px,6vw,120px);align-items:start}
.ps-type{display:inline-flex;padding:4px;border-radius:999px;border:1px solid var(--line);margin-bottom:40px}
.ps-type button,.seg button{padding:9px 20px;border-radius:999px;font-size:15px;color:#C9C9C9;transition:background .2s,color .2s}
.ps-type button[aria-pressed="true"],.seg button[aria-pressed="true"]{background:var(--acc-s);color:#0C201A;font-weight:600}
.ps-lbl{display:flex;justify-content:space-between;font-size:18px;margin-bottom:14px}
.ps-lbl b{color:var(--acc-s);font-variant-numeric:tabular-nums}
.ps input[type=range]{width:100%;-webkit-appearance:none;appearance:none;height:4px;border-radius:4px;background:#333;outline:none}
.ps input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:26px;height:26px;border-radius:50%;background:var(--acc-s);border:4px solid var(--bg);box-shadow:0 0 0 1px var(--acc-s);cursor:grab}
.ps input[type=range]::-moz-range-thumb{width:20px;height:20px;border-radius:50%;background:var(--acc-s);border:4px solid var(--bg);cursor:grab}
.ps-scale{display:flex;justify-content:space-between;font-size:12px;color:var(--muted);margin-top:10px}
.ps-prod,.ps-lang{margin-top:38px}
.seg{display:inline-flex;padding:4px;border-radius:999px;border:1px solid var(--line)}
.seg button{padding:8px 18px;font-variant-numeric:tabular-nums}
.ps-opts{display:grid;grid-template-columns:minmax(0,1fr);margin-top:44px;border-top:1px solid var(--line);max-width:520px}
.ps-opts label{display:flex;align-items:center;gap:14px;font-size:17px;cursor:pointer;padding:15px 0;border-bottom:1px solid var(--line-soft)}
.ps-opts label > span{flex:1;display:flex;justify-content:space-between;gap:16px}
.ps-opts label small{font-size:15px;color:var(--muted);font-variant-numeric:tabular-nums;white-space:nowrap}
.ps-opts input{width:20px;height:20px;accent-color:var(--acc-s);flex:none}
.ps-out{position:sticky;top:110px;border-left:1px solid var(--line);padding-left:clamp(24px,3vw,48px)}
.ps-out > small{font-size:13px;color:var(--muted)}
.ps-total{display:flex;align-items:flex-start;gap:8px;font-size:clamp(64px,6vw,96px);font-weight:700;letter-spacing:-.05em;line-height:1;font-variant-numeric:tabular-nums;margin-top:6px}
.ps-total span{font-size:.22em;letter-spacing:0;font-weight:500;color:var(--acc-s);margin-top:.5em}
.ps-year{font-size:15px;color:var(--muted);margin-top:10px}
.ps-lines{margin:24px 0 28px;border-top:1px solid var(--line)}
.ps-lines div{display:flex;justify-content:space-between;gap:12px;padding:9px 0;border-bottom:1px solid var(--line-soft);font-size:14.5px;color:#BDBDBD}
.ps-lines b{font-weight:500;font-variant-numeric:tabular-nums;color:var(--text)}
.pl-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(48px,6vw,100px) clamp(40px,7vw,140px)}
.pl-blk h2{font-size:clamp(24px,2vw,32px);font-weight:700;letter-spacing:-.035em;margin-bottom:16px;padding-bottom:16px;border-bottom:1px solid var(--line)}
.pl-blk ul{list-style:none}
.pl-blk li{display:flex;align-items:baseline;gap:10px;padding:10px 0;font-size:18px}
.pl-blk li span{color:#D6D6D6}
.pl-blk li i{flex:1;border-bottom:1.5px dotted #444;transform:translateY(-4px)}
.pl-blk li b{font-weight:600;font-variant-numeric:tabular-nums;white-space:nowrap}
.pl-blk p{margin-top:14px;font-size:15px;line-height:1.55;color:var(--muted);max-width:44ch}
.fine2{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);gap:clamp(40px,7vw,140px)}
.fine2 h2{font-size:clamp(38px,4.4vw,76px);line-height:1;font-weight:700;letter-spacing:-.05em}
.fine2-r{border-top:1px solid var(--line)}
.fine2-r div{display:grid;grid-template-columns:minmax(0,.6fr) minmax(0,1.4fr);gap:24px;padding:24px 0;border-bottom:1px solid var(--line)}
.fine2-r h3{font-size:19px;font-weight:600}
.fine2-r p{font-size:17px;line-height:1.65;color:#BDBDBD;max-width:52ch}

/* Über uns */
.bel{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:clamp(40px,7vw,140px);border-bottom:1px solid var(--line)}
.bel li{display:grid;grid-template-columns:48px minmax(0,1fr);row-gap:12px;padding:clamp(28px,3vw,44px) 0;border-top:1px solid var(--line)}
.bel h3{grid-column:2;font-size:clamp(24px,2.2vw,36px);line-height:1.08;font-weight:700;letter-spacing:-.04em}
.bel p{grid-column:2;font-size:17px;line-height:1.65;color:#B5B5B5;max-width:46ch}
.bel .n{grid-row:1}
.band2{position:relative;background:var(--sage);color:var(--ink);overflow:hidden;padding-top:clamp(80px,10vw,150px);padding-bottom:clamp(80px,10vw,150px);display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,.6fr);gap:clamp(32px,5vw,96px);align-items:center}
.band2 > *:not(.grain){position:relative}
.band2 h2{font-size:clamp(36px,4.4vw,78px);line-height:.98;font-weight:700;letter-spacing:-.05em;max-width:16ch}
.band2 p{font-size:clamp(18px,1.4vw,21px);line-height:1.65;color:#17241F;max-width:50ch;margin-top:28px}
.band2-mark{width:min(100%,300px);justify-self:end}
.band2-mark .lm-l{fill:#B7CDBC}.band2-mark .lm-d{fill:var(--ink)}
.tools2{margin:0;border-top:1px solid var(--line)}
.tools2 div{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);gap:clamp(24px,7vw,140px);padding:22px 0;border-bottom:1px solid var(--line);align-items:baseline}
.tools2 dt{font-size:clamp(22px,2vw,32px);font-weight:700;letter-spacing:-.035em}
.tools2 dd{margin:0;font-size:17px;color:#BDBDBD}
.li-row{margin-top:clamp(36px,4vw,56px)}

/* Kontakt */
.k-hero h1{max-width:12ch}
.direct .nb{user-select:auto;font-size:clamp(17px,1.4vw,21px)}
.day[aria-pressed="true"],.times button[aria-pressed="true"]{background:var(--acc-s);border-color:var(--acc-s);color:#0C201A}

/* Handy */
@media (max-width: 1000px){
  .stp{grid-template-columns:repeat(2,minmax(0,1fr));row-gap:44px}
  .stp-3{grid-template-columns:1fr}
  .who{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (max-width: 960px){
  .calc .ps{grid-template-columns:minmax(0,1fr)}
  .ps-out{position:static;border-left:0;padding-left:0;border-top:1px solid var(--line);padding-top:28px}
}
@media (max-width: 860px){
  .sp-hero{grid-template-columns:minmax(0,1fr);min-height:0;padding-top:120px;gap:44px}
  .sp-dev{margin:0 -6px}
  .lx-head,.lx-list a,.inc,.bel,.pr,.sp-faq,.fine2,.tools2 div,.pl-grid,.band2{grid-template-columns:minmax(0,1fr)}
  .lx-head{gap:16px}
  .lx-d{margin-top:8px;padding-right:40px}
  .lx-list:hover .lx-t{color:var(--text)}
  .ov-list a{grid-template-columns:minmax(0,1fr);gap:20px}
  .ov-n{display:none}
  .ov-v{order:-1;width:min(100%,520px)}
  .wk,.wk.flip{grid-template-columns:minmax(0,1fr);gap:28px}
  .wk.flip .wk-tx{order:0}
  .wk-v{order:-1}
  .pr-list dd{font-size:28px}
  .tools2 div{gap:6px}
  .fine2-r div{grid-template-columns:minmax(0,1fr);gap:6px}
  .band2-mark{justify-self:start;width:120px}
}
@media (max-width: 560px){
  .stp,.who,.ps-opts{grid-template-columns:minmax(0,1fr)}
  .sp-act .btn{flex:1 1 100%;justify-content:center}
  .pr-list > div{flex-direction:column;gap:10px}
  .pl-blk li{font-size:16px}
}
'''

SERVICE_PAGES = {FILES[k]: service(k) for k in ORDER}
