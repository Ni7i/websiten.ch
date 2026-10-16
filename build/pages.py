from parts import ARROW, GRAIN, MARK_LIGHT, MARK_DARK
from home import M1, M2, M3, strip_t

# ---------------------------------------------------------------- Leistungen
LEISTUNGEN_CSS = r'''
.svc{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(32px,6vw,120px);padding-top:clamp(64px,8vw,120px);padding-bottom:clamp(64px,8vw,120px);border-top:1px solid var(--line);scroll-margin-top:60px}
.svc-head{align-self:start;min-width:0}
.svc-head h2{font-size:clamp(40px,4.6vw,84px);line-height:.98;font-weight:700;letter-spacing:-.05em}
.svc-head p{color:var(--muted);font-size:17px;margin-top:18px;max-width:30ch}
.svc-body{min-width:0}
.svc-body > p{font-size:clamp(19px,1.5vw,23px);line-height:1.62;color:#D3DBD6;max-width:50ch}
.svc-body h3{font-size:15px;font-weight:500;color:var(--muted);margin-top:44px;margin-bottom:6px}
.svc-body .more{margin-top:40px}
.incl{list-style:none;columns:2;column-gap:40px;max-width:720px}
.incl li{break-inside:avoid;padding:10px 0 10px 18px;position:relative;border-bottom:1px solid var(--line-soft);font-size:16.5px;line-height:1.45;color:#C7D0CA}
.incl li::before{content:"";position:absolute;left:0;top:19px;width:7px;height:1.5px;background:var(--sage)}
.vg{margin-top:40px;width:min(100%,480px);border-radius:16px;overflow:hidden;box-shadow:0 30px 70px -20px rgba(0,0,0,.55)}
.vg-web{background:#F4F6F5;color:#13201E}
.vg-web .frame-b{border:0;border-radius:0;box-shadow:none}
.vg-shop{display:grid;grid-template-columns:1fr 1fr;background:#EEF1F0;color:#13201E;height:260px}
.vg-shop .img{position:relative;isolation:isolate;background:linear-gradient(160deg,#C9DDCF,#86A98F)}
.vg-shop .img::before{content:"";position:absolute;left:50%;top:16%;width:58%;aspect-ratio:1;transform:translateX(-50%);border-radius:50%;background:radial-gradient(circle,#8A9896 1.2px,transparent 1.6px) 0 0/9px 9px,radial-gradient(circle at 35% 30%,#FFFFFF,#DCE3E2 60%,#B4C1BF);box-shadow:0 10px 24px rgba(20,33,31,.25),inset 0 0 0 5px #F3F6F5}
.vg-shop .img::after{content:"";position:absolute;left:calc(50% - 4px);top:45%;width:8px;height:44%;border-radius:4px;background:linear-gradient(90deg,#9FAEAC,#F4F7F6 45%,#A9B7B5);z-index:-1}
.vg-shop .info{padding:24px 20px;display:flex;flex-direction:column;gap:6px}
.vg-shop small{font-size:11px;color:#6B7674}
.vg-shop h4{font-size:18px;font-weight:600;line-height:1.15}
.vg-shop .pr{font-size:22px;font-weight:600;margin-top:4px}
.vg-shop .pay{font-size:11px;color:#55605E}
.vg-shop .cart{margin-top:auto;background:#13201E;color:#fff;font-size:12px;text-align:center;border-radius:99px;padding:10px}
.vg-seo{background:#FAFAF9;color:#202124;padding:22px}
.vg-seo .q{display:flex;align-items:center;gap:8px;border:1px solid #DFE1E5;border-radius:99px;padding:9px 16px;font-size:13px}
.vg-seo .q i{width:11px;height:11px;border:1.6px solid #70757A;border-radius:50%}
.vg-seo .r{margin-top:18px;padding:14px;border-radius:12px;background:#EFF5F0;border:1px solid #CFE0D3}
.vg-seo .r small{display:flex;gap:6px;align-items:center;font-size:11.5px;color:#4D5156}
.vg-seo .r small b{width:18px;height:18px;border-radius:50%;background:#2E4A3B;color:#fff;font-size:10px;display:grid;place-items:center}
.vg-seo .r h4{font-size:17px;font-weight:500;color:#1A3A8A;margin-top:5px}
.vg-seo .r p{font-size:12px;color:#4D5156;line-height:1.45;margin-top:3px}
.vg-seo .r2{margin-top:12px;opacity:.45;padding:0 14px}
.vg-seo .r2 i{display:block;height:8px;border-radius:2px;background:#D5D9DD;margin-top:7px}
.vg-seo .r2 i:nth-child(2){width:70%}
.vg-host{background:#151B18;color:#E8ECEA;padding:22px;border:1px solid #2C3631}
.vg-host .t{display:flex;justify-content:space-between;align-items:center;font-size:14px}
.vg-host .t span{display:flex;gap:7px;align-items:center;color:#9FD3B8;font-size:13px}
.vg-host .t span i{width:8px;height:8px;border-radius:50%;background:#6FC79C}
.vg-host .graph{height:80px;margin:18px 0 12px;background:linear-gradient(180deg,rgba(131,170,140,.4),transparent);clip-path:polygon(0 70%,8% 62%,16% 66%,24% 50%,32% 56%,40% 40%,48% 46%,56% 30%,64% 38%,72% 24%,80% 32%,88% 18%,100% 22%,100% 100%,0 100%)}
.vg-host .row{display:flex;justify-content:space-between;font-size:13px;padding:8px 0;border-top:1px solid #26302B;color:#BAC5BE}
.vg-host .row b{font-weight:500;color:#E8ECEA}
.vg-it{background:#F3F5F4;color:#13201E;padding:20px 22px}
.vg-it .t{display:flex;justify-content:space-between;font-size:13px;font-weight:600}
.vg-it .t span{font-weight:400;color:#6B7674}
.vg-it .m{display:grid;grid-template-columns:30px 1fr auto;gap:12px;align-items:center;padding:11px 0;border-top:1px solid #DDE3E1;margin-top:8px}
.vg-it .m i{width:30px;height:30px;border-radius:50%;background:#C9DDCF;font-style:normal;font-size:11px;display:grid;place-items:center;font-weight:600}
.vg-it .m b{display:block;font-size:13px}
.vg-it .m span{display:block;font-size:12px;color:#6B7674}
.vg-it .m em{font-style:normal;font-size:11px;color:#6B7674}
.vg-ki{background:#151B18;border:1px solid #2C3631;padding:22px;display:flex;flex-direction:column;gap:10px}
.vg-ki .b{max-width:82%;font-size:14.5px;line-height:1.45;padding:12px 16px;border-radius:14px}
.vg-ki .in{align-self:flex-start;background:#212A25;color:#E8ECEA;border-bottom-left-radius:4px}
.vg-ki .out{align-self:flex-end;background:var(--sage);color:var(--ink);border-bottom-right-radius:4px}
.vg-ki small{display:block;font-size:11.5px;opacity:.7;margin-bottom:2px}
.toc{margin-top:clamp(40px,5vw,72px);display:grid;grid-template-columns:repeat(3,minmax(0,1fr));border-top:1px solid var(--line)}
.toc a{padding:18px 0;border-bottom:1px solid var(--line);font-size:clamp(20px,1.8vw,28px);font-weight:500;letter-spacing:-.02em;transition:color .2s,padding .3s var(--ease)}
.toc a:hover{color:var(--sage-light);padding-left:8px}
.not{padding-top:clamp(80px,10vw,140px);padding-bottom:clamp(100px,12vw,160px);border-top:1px solid var(--line)}
.not h2{max-width:16ch}
.not-list{margin-top:clamp(40px,5vw,64px);display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(24px,3vw,48px)}
.not-list div{border-top:1px solid var(--line);padding-top:20px}
.not-list b{display:block;font-size:20px;font-weight:500;letter-spacing:-.01em}
.not-list p{color:var(--muted);font-size:16px;margin-top:8px;max-width:34ch}
@media (max-width: 860px){
  .svc{grid-template-columns:1fr}
  .toc{grid-template-columns:1fr}
  .svc-head{position:static}
  .incl{columns:1}
  .not-list{grid-template-columns:1fr}
  .vg-shop{height:auto;grid-template-columns:1fr}
  .vg-shop .img{height:200px}
}
'''

def svc(id_, title, quiet, lead, body, incl, vignette):
    inc = ''.join(f'<li>{a}{(", " + b[0].lower() + b[1:]) if b else ""}</li>' for a, b in incl)
    return f'''<section class="svc pad" id="{id_}">
    <div class="svc-head"><h2>{title}</h2><p>{quiet}</p>{vignette}</div>
    <div class="svc-body"><p>{lead}</p>{body}<h3>Dazu gehört</h3><ul class="incl">{inc}</ul><a class="more" href="preise.html">Preis berechnen ''' + ARROW + '''</a></div>
  </section>'''

LEISTUNGEN_MAIN = '''
  <section class="page-hero pad">
    <h1>Leistungen</h1>
    <nav class="toc" aria-label="Leistungen auf dieser Seite"><a href="#websites">Websites</a><a href="#shops">Online-Shops</a><a href="#seo">SEO und Google Ads</a><a href="#hosting">Domains und Hosting</a><a href="#m365">Microsoft 365 und IT</a><a href="#ki">KI-Chatbots</a></nav>
  </section>
''' + svc('websites', 'Websites', 'Mit WordPress, damit Sie selbst ändern können.',
    'Wir bauen Firmenwebsites mit WordPress. So können Sie Öffnungszeiten, Fotos oder eine Aktion später selbst ändern, ohne jemanden anrufen zu müssen. Wenn Sie lieber anrufen, ist das auch in Ordnung, dann machen wir es.',
    '', [('Planung der Seiten und Inhalte',''),('Gestaltung für Ihren Betrieb',''),('Texte, wenn Sie möchten',''),('Deutsch, Französisch, Italienisch oder Englisch',''),('Optimiert fürs Handy',''),('Kontakt- oder Offertformular',''),('Einführung, damit Sie selbst ändern können',''),('Einrichtung bei Infomaniak','')],
    '<div class="vg vg-web"><div class="frame-b"><div class="bar"><i></i><i></i><i></i><span>keller-sanitaer.ch</span></div>' + strip_t(M1) + '</div></div>') + svc('shops', 'Online-Shops', 'Mit TWINT, Rechnung und Versand in der Schweiz.',
    'Ein Shop in der Schweiz braucht TWINT, Kauf auf Rechnung, Versand mit der Post und Preise mit 8,1 % MwSt. Das richten wir von Anfang an so ein. Haben Sie schon einen Shop, ziehen wir ihn um, mit allen Produkten, Kunden und Bestellungen.',
    '', [('Shopify oder WooCommerce',''),('TWINT, Karte und Rechnung',''),('Versandregeln für die Schweiz',''),('Produktimport aus Excel oder dem alten Shop',''),('Umzug mit Weiterleitungen für Google',''),('Kundenpreise und Bestellportal für B2B',''),('Schulung für Sie und Ihr Team','')],
    '<div class="vg vg-shop"><div class="img"></div><div class="info"><small>Armaturen</small><h4>Duschset Rondo, Chrom</h4><div class="pr">CHF 189.00</div><div class="pay">TWINT, Karte oder Rechnung</div><div class="cart">In den Warenkorb</div></div></div>') + svc('seo', 'SEO und Google Ads', 'Gefunden werden in Ihrer Region.',
    'Ihre Kunden suchen nach Dingen wie «Badsanierung Baden» oder «Hausarzt Wettingen». Dort sollten Sie auftauchen. Wir bringen die Technik in Ordnung, schreiben passende Seiten und richten Ihr Google Unternehmensprofil ein. Soll es schneller gehen, schalten wir Google Ads mit einem festen Monatsbudget. Gekaufte Links und Platz-Garantien gibt es bei uns nicht.',
    '', [('Google Unternehmensprofil und Maps',''),('Ladezeit und saubere Struktur',''),('Seiten zu dem, was Ihre Kunden suchen',''),('Google Ads mit festem Budget',''),('Monatliche Auswertung der Anfragen','')],
    '<div class="vg vg-seo"><div class="q"><i></i>badsanierung baden</div><div class="r"><small><b>1</b>keller-sanitaer.ch › badsanierung</small><h4>Badsanierung in Baden | Keller Sanitär</h4><p>Neues Bad mit Fixpreis und festem Termin. Beratung vor Ort in Baden, Wettingen und Umgebung.</p></div><div class="r2"><i></i><i></i></div></div>') + svc('hosting', 'Domains und Hosting', 'Bei Infomaniak in der Schweiz.',
    'Ihre Domain, Ihre Website und Ihre E-Mails liegen bei Infomaniak, einem Schweizer Anbieter aus Genf mit eigenen Rechenzentren in der Schweiz. Wir kümmern uns um Updates, Backups und Sicherheit. Wenn etwas klemmt, rufen Sie uns direkt an.',
    '', [('.ch-Domains registrieren und umziehen',''),('Hosting bei Infomaniak',''),('E-Mail-Adressen mit Ihrer Domain',''),('Tägliche Backups',''),('Updates für WordPress und Plugins',''),('SSL-Zertifikat, automatisch erneuert','')],
    '<div class="vg vg-host"><div class="t"><b>ihre-firma.ch</b><span><i></i>Online</span></div><div class="graph"></div><div class="row"><span>Letztes Backup</span><b>Heute, 03:00</b></div><div class="row"><span>SSL-Zertifikat</span><b>gültig bis 09/2027</b></div><div class="row"><span>Updates</span><b>alle installiert</b></div></div>') + svc('m365', 'Microsoft 365 und IT', 'E-Mail, Teams und Geräte fürs Büro.',
    'E-Mail, Teams, OneDrive und Kalender, sauber eingerichtet und verwaltet. Neue Mitarbeitende haben ihr Konto am ersten Tag, und wer geht, verliert den Zugriff am letzten. Dazu kommen Domains, Geräte und Hilfe, wenn der Drucker wieder einmal nicht will.',
    '', [('Einrichtung und Lizenzen',''),('E-Mail-Umzug vom alten Anbieter',''),('Ordnung in Teams und OneDrive',''),('Anmeldung mit zweitem Faktor',''),('Neue Laptops startklar machen',''),('Hilfe per Telefon und Fernwartung','')],
    '<div class="vg vg-it"><div class="t">Posteingang <span>info@ihre-firma.ch</span></div><div class="m"><i>MB</i><div><b>Offerte Badsanierung</b><span>Guten Tag, anbei die Masse unseres Badezimmers</span></div><em>09:12</em></div><div class="m"><i>RS</i><div><b>Lieferung am Dienstag</b><span>Die Platten kommen um 7 Uhr auf die Baustelle</span></div><em>08:40</em></div><div class="m"><i>TK</i><div><b>Teams: Wochenplanung</b><span>Montag, 07:30, Besprechung im Büro</span></div><em>Gestern</em></div></div>') + svc('ki', 'KI-Chatbots', 'Beantwortet häufige Fragen auf Ihrer Website.',
    'Viele Fragen kommen immer wieder: Öffnungszeiten, Preise, Parkplätze, freie Termine. Ein Chatbot beantwortet sie direkt auf Ihrer Website, mit Ihren Informationen. Was er nicht weiss, gibt er an Sie weiter.',
    '', [('Antworten nur aus Ihren Informationen',''),('In mehreren Sprachen',''),('Schwierige Fragen gehen an Sie weiter',''),('Datenschutz dokumentiert','')],
    '<div class="vg vg-ki"><div class="b in"><small>Besucherin</small>Haben Sie am Samstag offen?</div><div class="b out"><small>Chatbot</small>Ja, am Samstag von 9 bis 14 Uhr. Soll ich Ihnen einen Termin vorschlagen?</div><div class="b in">Gerne, am Vormittag.</div></div>') + '''
'''

# ---------------------------------------------------------------- Arbeiten
ARBEITEN_CSS = r'''
.ex{padding-top:clamp(56px,7vw,100px);padding-bottom:clamp(56px,7vw,100px);border-top:1px solid var(--line);display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2.2fr);gap:clamp(32px,5vw,96px);align-items:start}
.ex-info{position:sticky;top:110px}
.ex-info small{display:block;font-size:14px;color:var(--sage-light)}
.ex-info h2{font-size:clamp(32px,3.4vw,58px);line-height:1;font-weight:700;letter-spacing:-.05em;margin-top:10px}
.ex-info p{color:#BAC5BE;font-size:17px;line-height:1.65;margin-top:20px;max-width:36ch}
.ex-info dl{margin-top:28px;display:grid;grid-template-columns:auto 1fr;gap:10px 20px;font-size:15px}
.ex-info dt{color:var(--muted)}
.ex-info dd{color:var(--text)}
.ex-frame{min-width:0}
.note-box{margin:0 var(--pad) clamp(80px,10vw,140px);padding:clamp(28px,3vw,44px);border:1px solid var(--line);border-radius:16px;display:flex;justify-content:space-between;align-items:center;gap:32px;flex-wrap:wrap}
.note-box p{font-size:clamp(18px,1.5vw,22px);max-width:46ch;color:#BAC5BE}
@media (max-width: 860px){
  .ex{grid-template-columns:1fr}
  .ex-info{position:static}
}
'''

def ex(small, title, text, facts, frame):
    dl = ''.join(f'<dt>{a}</dt><dd>{b}</dd>' for a, b in facts)
    return f'''<section class="ex pad">
    <div class="ex-info"><small>{small}</small><h2>{title}</h2><p>{text}</p><dl>{dl}</dl></div>
    <div class="ex-frame">{frame}</div>
  </section>'''

ARBEITEN_MAIN = '''
  <section class="page-hero pad">
    <h1>Arbeiten</h1>
    <p>Drei Beispiel-Entwürfe für drei Branchen. Jeder hat eigene Farben, eine eigene Schrift und einen eigenen Weg zur Anfrage, weil ein Café andere Besucher hat als eine Arztpraxis.</p>
  </section>
''' + ex('Beispiel-Design, Handwerk', 'Sanitärbetrieb', 'Wer einen Rohrbruch hat, sucht eine Telefonnummer. Wer ein neues Bad plant, will Beispiele sehen und eine Offerte. Darum steht der Notfall-Service oben, und das Offertformular ist zwei Klicks entfernt.',
    [('Ziel','Mehr Offertanfragen für Badsanierungen'),('Umfang','8 Seiten, Offertformular, Google Profil'),('Schrift','Hanken Grotesk')],
    '<div class="frame-b"><div class="bar"><i></i><i></i><i></i><span>keller-sanitaer.ch</span></div>' + strip_t(M1) + '</div>') + ex('Beispiel-Design, Gesundheit', 'Hausarztpraxis', 'Patientinnen und Patienten wollen vor allem drei Dinge wissen: wann offen ist, wie sie einen Termin bekommen und wen sie im Notfall anrufen. Genau das steht auf der Startseite.',
    [('Ziel','Weniger Telefonate, mehr Online-Termine'),('Umfang','6 Seiten, zweisprachig, Terminbuchung'),('Schrift','Newsreader und Hanken Grotesk')],
    '<div class="frame-b"><div class="bar"><i></i><i></i><i></i><span>praxis-lindenplatz.ch</span></div>' + M2 + '</div>') + ex('Beispiel-Design, Gastronomie', 'Café und Bäckerei', 'Die Vitrine von heute steht gleich auf der Startseite. Geburtstagstorten lassen sich online bestellen und zu einer gewählten Zeit abholen. Das spart Anrufe mitten im Morgenbetrieb.',
    [('Ziel','Tortenbestellungen online statt per Telefon'),('Umfang','5 Seiten, kleiner Shop, Tageskarte'),('Schrift','Fraunces und Hanken Grotesk')],
    '<div class="frame-b"><div class="bar"><i></i><i></i><i></i><span>cafe-morgenrot.ch</span></div>' + M3 + '</div>') + '''
  <div class="note-box"><p>Echte Kundenprojekte zeigen wir Ihnen gern im persönlichen Gespräch.</p><a class="btn btn-sage" href="kontakt.html">Gespräch vereinbaren ''' + ARROW + '''</a></div>
'''

# ---------------------------------------------------------------- Preise
PREISE_CSS = r'''
.pv-wrap{padding-bottom:clamp(90px,11vw,160px)}
.pv-switch{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-bottom:clamp(40px,5vw,72px);padding-bottom:20px;border-bottom:1px solid var(--line)}
.pv-note{font-size:13px;color:var(--muted);margin-right:8px}
.pv-switch button{padding:9px 16px;border-radius:999px;border:1px solid var(--line);font-size:15px;color:#C9D3CD;transition:background .2s,color .2s,border-color .2s}
.pv-switch button[aria-selected="true"]{background:var(--sage);border-color:var(--sage);color:var(--ink);font-weight:500}
.pv{animation:pvIn .45s var(--ease)}
@keyframes pvIn{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:none}}

/* 1: Preisliste mit Punktlinien */
.pl-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(48px,6vw,110px) clamp(40px,6vw,120px)}
.pl-blk h2{font-size:clamp(24px,2vw,32px);font-weight:600;letter-spacing:-.025em;margin-bottom:18px}
.pl-blk ul{list-style:none}
.pl-blk li{display:flex;align-items:baseline;gap:10px;padding:9px 0;font-size:18px}
.pl-blk li span{color:#D6DDD9}
.pl-blk li i{flex:1;border-bottom:1.5px dotted #3E4A44;transform:translateY(-4px)}
.pl-blk li b{font-weight:500;font-variant-numeric:tabular-nums;white-space:nowrap}
.pl-blk p{margin-top:14px;font-size:15px;line-height:1.55;color:var(--muted);max-width:44ch}

/* 2: Drei Angebote nebeneinander */
.pc-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(32px,4vw,72px)}
.pc{display:flex;flex-direction:column}
.pc h2{font-size:clamp(26px,2.3vw,36px);font-weight:600;letter-spacing:-.03em;color:var(--sage-light)}
.pc h3{font-size:19px;font-weight:600;margin-top:10px}
.pc p{font-size:17px;line-height:1.65;color:#C7D0CA;margin-top:10px;flex:1}
.pc-price{font-size:22px;font-style:italic;font-variant-numeric:tabular-nums;margin-top:26px}
.pc-year{font-size:14px;color:var(--muted);margin-top:4px}
.pc a{display:inline-flex;align-items:center;gap:10px;margin-top:20px;font-size:16px;color:var(--sage-light);align-self:flex-start;padding-bottom:4px;border-bottom:1px solid var(--sage-deep)}
.pc a:hover{color:var(--text)}

/* 3: Schieberegler */
.ps{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(300px,.8fr);gap:clamp(40px,6vw,120px);align-items:start}
.ps-type{display:inline-flex;padding:4px;border-radius:999px;border:1px solid var(--line);margin-bottom:36px}
.ps-type button{padding:9px 20px;border-radius:999px;font-size:15px;color:#C9D3CD}
.ps-type button[aria-pressed="true"]{background:var(--sage);color:var(--ink);font-weight:500}
.ps-lbl{display:flex;justify-content:space-between;font-size:18px;margin-bottom:14px}
.ps-lbl b{color:var(--sage-light);font-variant-numeric:tabular-nums}
.ps input[type=range]{width:100%;-webkit-appearance:none;appearance:none;height:4px;border-radius:4px;background:#2A3430;outline:none}
.ps input[type=range]::-webkit-slider-thumb{-webkit-appearance:none;width:26px;height:26px;border-radius:50%;background:var(--sage);border:4px solid var(--bg);box-shadow:0 0 0 1px var(--sage);cursor:grab}
.ps input[type=range]::-moz-range-thumb{width:20px;height:20px;border-radius:50%;background:var(--sage);border:4px solid var(--bg);cursor:grab}
.ps-scale{display:flex;justify-content:space-between;font-size:12px;color:var(--muted);margin-top:10px}
.ps-prod{margin-top:34px}
.ps-opts{display:flex;flex-direction:column;gap:14px;margin-top:40px}
.ps-opts label{display:flex;align-items:center;gap:12px;font-size:17px;cursor:pointer}
.ps-opts input{width:20px;height:20px;accent-color:var(--sage)}
.ps-out{position:sticky;top:110px;border-left:1px solid var(--line);padding-left:clamp(24px,3vw,48px)}
.ps-out small{font-size:13px;color:var(--muted)}
.ps-total{display:flex;align-items:flex-start;gap:8px;font-size:clamp(64px,6vw,96px);font-weight:700;letter-spacing:-.05em;line-height:1;font-variant-numeric:tabular-nums;margin-top:6px}
.ps-total span{font-size:.22em;letter-spacing:0;font-weight:500;color:var(--sage-light);margin-top:.5em}
.ps-year{font-size:15px;color:var(--muted);margin-top:8px}
.ps-lines{margin:24px 0 28px;border-top:1px solid var(--line)}
.ps-lines div{display:flex;justify-content:space-between;gap:12px;padding:8px 0;border-bottom:1px solid var(--line-soft);font-size:14.5px;color:#C7D0CA}
.ps-lines b{font-weight:500;font-variant-numeric:tabular-nums}

.fine{margin:0 var(--pad) clamp(100px,12vw,160px);padding-top:40px;border-top:1px solid var(--line);display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:clamp(24px,5vw,96px)}
.fine h2{font-size:22px;font-weight:600}
.fine p{color:#C7D0CA;font-size:18px;line-height:1.75;max-width:62ch}
@media (max-width: 960px){
  .pl-grid,.pc-grid,.ps,.fine{grid-template-columns:minmax(0,1fr)}
  .ps-out{position:static;border-left:0;padding-left:0;border-top:1px solid var(--line);padding-top:28px}
}
@media (max-width: 560px){ .pl-blk li{font-size:16px} .pv-note{width:100%} }
'''

PREISE_MAIN = '''
  <section class="page-hero pad">
    <h1>Preise</h1>
    <p>Feste Preise, vorher bekannt. Sie zahlen die Hälfte bei Auftrag und den Rest, wenn die Website online ist.</p>
  </section>
  <section class="pad pv-wrap">
    <div class="pv-switch" role="tablist" aria-label="Darstellung wählen">
      <span class="pv-note">Entwurf, drei Varianten:</span>
      <button type="button" role="tab" data-v="v1" aria-selected="true">1 · Preisliste</button>
      <button type="button" role="tab" data-v="v2" aria-selected="false">2 · Drei Angebote</button>
      <button type="button" role="tab" data-v="v3" aria-selected="false">3 · Schieberegler</button>
    </div>
    <div class="pv" id="v1">
      <div class="pl-grid">
        <div class="pl-blk"><h2>Website</h2><ul><li><span>Bis 4 Seiten</span><i></i><b>590.–</b></li><li><span>Bis 6 Seiten</span><i></i><b>890.–</b></li><li><span>Bis 8 Seiten</span><i></i><b>1’190.–</b></li><li><span>Bis 10 Seiten</span><i></i><b>1’490.–</b></li><li><span>Jede weitere Seite</span><i></i><b>150.–</b></li></ul><p>Mit Gestaltung, Handy-Version, Kontaktformular, Google Maps und SSL.</p></div>
        <div class="pl-blk"><h2>Online-Shop</h2><ul><li><span>4 Seiten und bis 30 Produkte</span><i></i><b>1’890.–</b></li><li><span>Bis 150 Produkte</span><i></i><b>+ 490.–</b></li><li><span>Bis 500 Produkte</span><i></i><b>+ 990.–</b></li><li><span>Über 500 Produkte, mit Import</span><i></i><b>+ 1’890.–</b></li></ul><p>Mit TWINT, Karte und Versand. Das Shopify-Abo zahlen Sie direkt.</p></div>
        <div class="pl-blk"><h2>Dazu nach Wunsch</h2><ul><li><span>Texte von uns, pro Seite</span><i></i><b>90.–</b></li><li><span>Weitere Sprache, pro Seite</span><i></i><b>70.–</b></li><li><span>Online-Terminbuchung</span><i></i><b>290.–</b></li><li><span>News oder Blog</span><i></i><b>190.–</b></li><li><span>Google-Profil einrichten</span><i></i><b>150.–</b></li><li><span>Google Ads einrichten</span><i></i><b>390.–</b></li></ul></div>
        <div class="pl-blk"><h2>Hosting</h2><ul><li><span>Hosting und .ch-Domain, pro Monat</span><i></i><b>25.–</b></li><li><span>Die ersten 3 Monate, pro Monat</span><i></i><b>10.–</b></li></ul><p>Server bei Infomaniak in Genf. Mit SSL, E-Mail-Adresse und täglichen Backups.</p></div>
      </div>
    </div><div class="pv" id="v2" hidden>
      <div class="pc-grid">
        <div class="pc"><h2>Die kleine Website</h2><h3>Für den Start.</h3><p>Vier Seiten, die alles Wichtige sagen: was Sie machen, wer Sie sind, wie man Sie erreicht. Passt für Coiffeur, Kosmetik oder eine Einzelfirma.</p><div class="pc-price">CHF 590.–</div><div class="pc-year">Hosting CHF 25.– im Monat, die ersten 3 Monate CHF 10.–</div><a href="kontakt.html">Termin wählen ''' + ARROW + '''</a></div>
        <div class="pc"><h2>Die Firmenwebsite</h2><h3>Für Gewerbe und Praxen.</h3><p>Sechs bis zehn Seiten, eine pro Leistung, dazu Referenzen und Team. Passt für Handwerk, Praxen, Treuhand und alle, die über Google gefunden werden wollen.</p><div class="pc-price">CHF 890.– bis 1’490.–</div><div class="pc-year">Hosting CHF 25.– im Monat, die ersten 3 Monate CHF 10.–</div><a href="kontakt.html">Termin wählen ''' + ARROW + '''</a></div>
        <div class="pc"><h2>Der Online-Shop</h2><h3>Für alle, die verkaufen.</h3><p>Shop mit TWINT, Karte und Versand, fertig eingerichtet mit Ihren ersten 30 Produkten. Grössere Sortimente importieren wir.</p><div class="pc-price">CHF 1’890.– bis 3’780.–</div><div class="pc-year">Hosting CHF 25.– im Monat, die ersten 3 Monate CHF 10.–</div><a href="kontakt.html">Termin wählen ''' + ARROW + '''</a></div>
      </div>
    </div><div class="pv" id="v3" hidden>
      <div class="ps">
        <div class="ps-ctrl">
          <div class="ps-type" role="group" aria-label="Art"><button type="button" data-t="web" aria-pressed="true">Website</button><button type="button" data-t="shop" aria-pressed="false">Online-Shop</button></div>
          <label class="ps-lbl" for="psPages">Wie viele Seiten? <b id="psPagesOut">4</b></label>
          <input type="range" id="psPages" min="1" max="20" value="4">
          <div class="ps-scale"><span>1</span><span>5</span><span>10</span><span>15</span><span>20</span></div>
          <div class="ps-prod" id="psProd" hidden><label class="ps-lbl" for="psProducts">Wie viele Produkte? <b id="psProductsOut">bis 30</b></label><input type="range" id="psProducts" min="0" max="3" value="0"></div>
          <div class="ps-opts">
            <label><input type="checkbox" id="psTexts"><span>Texte schreiben wir</span></label>
            <label><input type="checkbox" id="psLang"><span>Zweite Sprache</span></label>
          </div>
        </div>
        <div class="ps-out">
          <small>Einmalig</small>
          <div class="ps-total"><span>CHF</span><b id="psTotal">590</b></div>
          <div class="ps-year" id="psYear">Dazu Hosting CHF 25 im Monat, die ersten 3 Monate CHF 10</div>
          <div class="ps-lines" id="psLines"></div>
          <a class="btn btn-sage" href="kontakt.html">Termin wählen ''' + ARROW + '''</a>
        </div>
      </div>
    </div>
  </section>
  <section class="fine">
    <h2>Gut zu wissen</h2>
    <p>In jedem Preis sind Gestaltung, Handy-Version, SSL, Kontaktformular, die Einrichtung bei Infomaniak und eine Einführung enthalten. Nicht enthalten sind Fotografen, gekaufte Bilder, das Shopify-Abo und die Gebühren der Zahlungsanbieter. Wenn so etwas dazukommt, steht es vorher in der Offerte.</p>
  </section>
'''

PREISE_JS = r'''
(function(){
  const tabs = [...document.querySelectorAll('.pv-switch button')];
  const show = v => { tabs.forEach(t => t.setAttribute('aria-selected', t.dataset.v === v)); document.querySelectorAll('.pv').forEach(p => p.hidden = p.id !== v); try { localStorage.setItem('websiten-preis-variante', v); } catch(e){} };
  tabs.forEach(t => t.onclick = () => show(t.dataset.v));
  try { const v = localStorage.getItem('websiten-preis-variante'); if(v && document.getElementById(v)) show(v); } catch(e){}

  const $ = id => document.getElementById(id), fmt = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '’');
  let type = 'web';
  const PROD = [['bis 30', 0], ['bis 150', 490], ['bis 500', 990], ['über 500', 1890]];
  function calc(){
    const pages = +$('psPages').value, shop = type === 'shop', L = [];
    $('psPagesOut').textContent = pages;
    L.push([shop ? 'Shop mit 4 Seiten' : 'Website mit 4 Seiten', shop ? 1890 : 590]);
    if(pages > 4) L.push([(pages - 4) + ' weitere Seite' + (pages > 5 ? 'n' : ''), (pages - 4)*150]);
    if(shop){ const p = PROD[+$('psProducts').value]; $('psProductsOut').textContent = p[0]; if(p[1]) L.push(['Produkte ' + p[0], p[1]]); }
    if($('psTexts').checked) L.push(['Texte für ' + pages + ' Seiten', pages*90]);
    if($('psLang').checked) L.push(['Zweite Sprache', pages*70]);
    const total = L.reduce((a, l) => a + l[1], 0);
    $('psTotal').textContent = fmt(total);
    $('psLines').innerHTML = L.map(l => `<div><span>${l[0]}</span><b>${fmt(l[1])}</b></div>`).join('');
  }
  document.querySelectorAll('.ps-type button').forEach(b => b.onclick = () => { document.querySelectorAll('.ps-type button').forEach(o => o.setAttribute('aria-pressed', o === b)); type = b.dataset.t; $('psProd').hidden = type !== 'shop'; calc(); });
  ['psPages','psProducts','psTexts','psLang'].forEach(id => $(id).addEventListener('input', calc));
  calc();
})();
'''

# ---------------------------------------------------------------- Über uns
UEBER_CSS = r'''
.page-hero .letter{font-size:clamp(24px,2.6vw,42px);line-height:1.35;color:var(--text);max-width:34ch;font-weight:500;letter-spacing:-.025em}
.beliefs{padding-bottom:clamp(80px,10vw,140px)}
.belief{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:clamp(24px,5vw,96px);padding:clamp(32px,4vw,56px) 0;border-top:1px solid var(--line);align-items:baseline}
.belief h2{font-size:clamp(30px,3.4vw,60px);line-height:1;font-weight:700;letter-spacing:-.05em}
.belief p{color:#BAC5BE;font-size:clamp(17px,1.3vw,19px);line-height:1.7;max-width:46ch}
.band{position:relative;background:var(--sage);color:var(--ink);overflow:hidden;padding-top:clamp(80px,10vw,150px);padding-bottom:clamp(80px,10vw,150px);display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(32px,5vw,96px);align-items:center}
.band > *:not(.grain){position:relative}
.band h2{font-size:clamp(36px,4.4vw,78px);line-height:.98;font-weight:700;letter-spacing:-.05em}
.band p{font-size:clamp(18px,1.4vw,21px);line-height:1.65;color:#17241F;max-width:46ch}
.band-mark{width:min(100%,360px);justify-self:end}
.band-mark .lm-l{fill:#C9DECE}.band-mark .lm-d{fill:var(--ink)}
.tools{padding-top:clamp(100px,12vw,180px);padding-bottom:clamp(100px,12vw,180px)}
.tools-t{margin-top:clamp(40px,5vw,64px);width:100%;border-collapse:collapse}
.tools-t th,.tools-t td{text-align:left;padding:22px 0;border-top:1px solid var(--line);vertical-align:baseline}
.tools-t tr:last-child th,.tools-t tr:last-child td{border-bottom:1px solid var(--line)}
.tools-t th{width:34%;font-size:clamp(22px,2vw,32px);font-weight:600;letter-spacing:-.03em}
.tools-t td{color:#C7D0CA;font-size:17px}
.tools-grid{margin-top:clamp(40px,5vw,72px);display:grid;grid-template-columns:repeat(3,1fr);gap:0 clamp(24px,3vw,48px)}
.tools-grid div{border-top:1px solid var(--line);padding:22px 0 34px}
.tools-grid b{display:block;font-size:clamp(22px,1.8vw,28px);font-weight:500;letter-spacing:-.02em}
.tools-grid p{color:var(--muted);font-size:16px;margin-top:8px;max-width:32ch}
@media (max-width: 860px){
  .belief,.band{grid-template-columns:1fr}
  .band-mark{justify-self:start;width:140px}
  .tools-t th{display:block;width:auto;padding-bottom:4px}
  .tools-t td{display:block;border-top:0;padding-top:0}
}
'''

UEBER_MAIN = '''
  <section class="page-hero pad">
    <h1>Über uns</h1>
    <p class="letter">websiten.ch baut Websites, Online-Shops und alles, was dazugehört, für Betriebe in der ganzen Schweiz. Für Handwerker, Praxen, Restaurants und Läden, die online gefunden werden wollen, ohne sich selbst um die Technik zu kümmern. Wir reden Klartext, halten Termine und machen Dinge, die funktionieren.</p>
  </section>
  <section class="beliefs pad">
    <div class="belief"><h2>Ein fester Preis ist ein fester Preis.</h2><p>Sie bekommen eine Offerte, und die gilt. Wenn Sie unterwegs etwas Neues möchten, besprechen wir das vorher. Überraschungen auf der Rechnung gibt es bei uns nicht.</p></div>
    <div class="belief"><h2>Sie verstehen, was wir tun.</h2><p>Wir erklären, was wir vorschlagen und warum, ohne Abkürzungen, die niemand kennt. Und wenn etwas für Ihren Betrieb keinen Sinn ergibt, sagen wir das, auch wenn wir daran verdienen könnten.</p></div>
    <div class="belief"><h2>Ihre Website gehört Ihnen.</h2><p>Domain, Inhalte und Zugänge laufen auf Ihren Namen. Wenn Sie einmal wechseln möchten, bekommen Sie alles, was Sie dafür brauchen.</p></div>
    <div class="belief"><h2>Ihre Daten bleiben in der Schweiz.</h2><p>Domains, Hosting und E-Mail laufen bei Infomaniak, einem Schweizer Anbieter aus Genf mit Rechenzentren in der Schweiz.</p></div>
  </section>
  <section class="band pad" data-sage>
    ''' + GRAIN + '''
    <div><h2>Eine Nummer für alles, was online ist.</h2><p style="margin-top:28px">Website, Shop, Google, Domains, E-Mail und Microsoft 365. Sie müssen nicht fünf Firmen koordinieren, die sich bei einem Problem gegenseitig die Schuld geben. Sie rufen an, und die Sache wird erledigt.</p></div>
    <svg class="band-mark" viewBox="12 10 174 188" aria-hidden="true"><path class="lm-l" d="''' + MARK_LIGHT + '''"/><path class="lm-d" d="''' + MARK_DARK + '''"/></svg>
  </section>
  <section class="tools pad">
    <h2 class="h-sec">Womit wir arbeiten</h2>
    <table class="tools-t">
      <tr><th>Infomaniak</th><td>Domains, Hosting und E-Mail bei einem Schweizer Anbieter aus Genf</td></tr>
      <tr><th>WordPress</th><td>Für Websites, die Sie danach selbst pflegen können</td></tr>
      <tr><th>Shopify</th><td>Für Online-Shops, die ohne Bastelei laufen sollen</td></tr>
      <tr><th>WooCommerce</th><td>Für einen Shop direkt in der bestehenden WordPress-Website</td></tr>
      <tr><th>Microsoft 365</th><td>E-Mail, Teams und OneDrive fürs Büro</td></tr>
      <tr><th>Google</th><td>Unternehmensprofil, Search Console und Google Ads</td></tr>
    </table>
  </section>
'''

# ---------------------------------------------------------------- Kontakt
KONTAKT_CSS = r'''
.k-hero{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,.9fr);gap:clamp(40px,6vw,120px);align-items:end}
.k-hero .direct div:last-child{border-bottom:1px solid var(--line)}
.direct div{padding:18px 0;border-top:1px solid var(--line);display:flex;justify-content:space-between;align-items:center;gap:16px;flex-wrap:wrap}
.direct small{display:block;color:var(--muted);font-size:14px}
.direct b{font-size:clamp(20px,1.7vw,26px);font-weight:500;letter-spacing:-.02em;user-select:all}
.copy{border:1px solid var(--line);border-radius:999px;padding:7px 14px;font-size:14px;color:#C9D3CD}
.copy:hover{border-color:var(--sage-light)}

#booker{scroll-margin-top:110px;min-width:0}
.book > *{min-width:0}
.book{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,.75fr);gap:clamp(40px,6vw,120px);padding-bottom:clamp(100px,12vw,180px);align-items:start}
.bk-step{border-top:1px solid var(--line);padding:28px 0 34px}
.bk-h{display:flex;align-items:baseline;justify-content:space-between;gap:16px;margin-bottom:20px}
.bk-h h2{font-size:22px;font-weight:600;letter-spacing:-.02em;display:flex;gap:14px;align-items:baseline}
.bk-h h2 i{font-style:normal;font-size:14px;font-weight:500;color:var(--sage-light);font-variant-numeric:tabular-nums}
.bk-h small{color:var(--muted);font-size:14px}
.days{display:flex;gap:8px;overflow-x:auto;scrollbar-width:none;padding-bottom:4px;scroll-snap-type:x proximity}
.days::-webkit-scrollbar{display:none}
.day{flex:0 0 76px;scroll-snap-align:start;border:1px solid var(--line);border-radius:14px;padding:12px 0 11px;display:flex;flex-direction:column;align-items:center;gap:2px;transition:background .2s,border-color .2s,color .2s}
.day small{font-size:13px;color:var(--muted)}
.day b{font-size:24px;font-weight:600;letter-spacing:-.03em;line-height:1.15;font-variant-numeric:tabular-nums}
.day span{font-size:12px;color:var(--muted)}
.day:hover:not(:disabled){border-color:var(--sage-deep)}
.day[aria-pressed="true"]{background:var(--sage);border-color:var(--sage);color:var(--ink)}
.day[aria-pressed="true"] small,.day[aria-pressed="true"] span{color:var(--ink-soft)}
.day:disabled{opacity:.35;cursor:not-allowed}
.day.wk{margin-left:14px}
.times{display:grid;grid-template-columns:repeat(auto-fill,minmax(92px,1fr));gap:8px}
.times button{border:1px solid var(--line);border-radius:999px;padding:11px 0;font-size:16px;font-variant-numeric:tabular-nums;color:#D3DBD6;transition:background .2s,border-color .2s,color .2s}
.times button:hover{border-color:var(--sage-deep)}
.times button[aria-pressed="true"]{background:var(--sage);border-color:var(--sage);color:var(--ink);font-weight:600}
.times-empty{color:var(--muted);font-size:16px}
.picked{font-size:17px;color:var(--muted);margin-bottom:22px}
.picked b{color:var(--text);font-weight:600}
form{display:grid;grid-template-columns:1fr 1fr;gap:22px 24px}
.f{display:flex;flex-direction:column;gap:8px;min-width:0}
.f.full{grid-column:1 / -1}
label,.lbl2{font-size:14px;color:var(--muted)}
input[type=text],input[type=email],input[type=tel],textarea{width:100%;background:transparent;border:0;border-bottom:1.5px solid #34403A;padding:12px 0;font-size:19px;color:var(--text);outline:none;transition:border-color .25s;border-radius:0}
input:focus,textarea:focus{border-color:var(--sage)}
input.bad{border-color:#C98B7A}
textarea{min-height:120px;resize:vertical;line-height:1.5}
.modes{display:flex;flex-wrap:wrap;gap:8px}
.modes button{border:1px solid var(--line);border-radius:999px;padding:9px 16px;font-size:15px;color:#C9D3CD;transition:background .2s,border-color .2s,color .2s}
.modes button[aria-pressed="true"]{background:var(--sage);border-color:var(--sage);color:var(--ink);font-weight:500}
.hp{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
.send{grid-column:1 / -1;display:flex;align-items:center;gap:24px;flex-wrap:wrap;margin-top:6px}
.send small{color:var(--muted);font-size:14px;max-width:42ch}
.btn[disabled]{opacity:.45;pointer-events:none}
.err{grid-column:1 / -1;color:#E3B1A3;font-size:15px}
.ok{border:1px solid var(--sage-deep);background:rgba(131,170,140,.08);border-radius:18px;padding:clamp(24px,3vw,40px)}
.ok h2{font-size:clamp(26px,2.4vw,36px);font-weight:600;letter-spacing:-.03em;margin-bottom:12px}
.ok p{color:#C7D0CA;font-size:17px;line-height:1.6;max-width:52ch}
.ok p + p{margin-top:10px}
.ok .demo{color:var(--sage-light)}
.side{display:flex;flex-direction:column;gap:44px;position:sticky;top:110px}
.side h3{font-size:20px;font-weight:600;margin-bottom:14px}
.next ol{list-style:none;counter-reset:s}
.next li{counter-increment:s;display:grid;grid-template-columns:36px 1fr;gap:12px;padding:14px 0;border-top:1px solid var(--line);font-size:16px;line-height:1.55;color:#BAC5BE}
.next li::before{content:counter(s);width:28px;height:28px;border-radius:50%;background:var(--surface);border:1px solid var(--line);display:grid;place-items:center;font-size:13px;color:var(--sage-light)}
.side p{color:#BAC5BE;font-size:16px;line-height:1.6}
.side a.u{color:var(--text);border-bottom:1px solid var(--sage-deep)}
@media (max-width: 960px){
  .book,.k-hero{grid-template-columns:minmax(0,1fr)}
  .side{position:static}
}
@media (max-width: 560px){
  form{grid-template-columns:minmax(0,1fr)}
  .day{flex-basis:66px}
  .times{grid-template-columns:repeat(4,minmax(0,1fr))}
  .times button{font-size:15px}
}
'''

KONTAKT_MAIN = '''
  <section class="page-hero pad k-hero">
    <div><h1>Termin wählen</h1><p>15 Minuten am Telefon oder per Video. Sie erzählen, was Sie vorhaben. Danach wissen Sie, was es kostet und wie lange es dauert. Das Gespräch ist kostenlos.</p></div>
    <div class="direct">
      <div><span><small>E-Mail</small><b>hallo@websiten.ch</b></span><button class="copy" type="button" data-copy="hallo@websiten.ch">Kopieren</button></div>
      <div><span><small>Telefon</small><b>[Telefon]</b></span></div>
    </div>
  </section>
  <section class="book pad" id="termin">
    <div id="booker">
      <div class="bk-step">
        <div class="bk-h"><h2><i>1</i>Tag</h2><small id="tzNote">Schweizer Zeit</small></div>
        <div class="days" id="days" role="group" aria-label="Tag wählen"><span class="times-empty">Termine werden geladen …</span></div>
      </div>
      <div class="bk-step">
        <div class="bk-h"><h2><i>2</i>Uhrzeit</h2><small>15 Minuten</small></div>
        <div class="times" id="times" role="group" aria-label="Uhrzeit wählen"></div>
      </div>
      <div class="bk-step">
        <div class="bk-h"><h2><i>3</i>Ihre Angaben</h2></div>
        <p class="picked" id="picked">Noch keine Zeit gewählt.</p>
        <form id="form" novalidate>
          <div class="f"><label for="name">Name</label><input type="text" id="name" autocomplete="name" maxlength="100" required></div>
          <div class="f"><label for="firma">Firma</label><input type="text" id="firma" autocomplete="organization" maxlength="120"></div>
          <div class="f"><label for="mail">E-Mail</label><input type="email" id="mail" autocomplete="email" maxlength="120" required></div>
          <div class="f"><label for="tel">Telefon</label><input type="tel" id="tel" autocomplete="tel" maxlength="40"></div>
          <div class="f full"><span class="lbl2" id="modeLbl">Wie sprechen wir?</span><div class="modes" role="group" aria-labelledby="modeLbl"><button type="button" data-m="phone" aria-pressed="true">Telefon, wir rufen Sie an</button><button type="button" data-m="meet" aria-pressed="false">Video mit Google Meet</button></div></div>
          <div class="f full"><label for="msg">Worum geht es? (freiwillig)</label><textarea id="msg" maxlength="3000" placeholder="Zum Beispiel: Neue Website für unseren Malerbetrieb, etwa 6 Seiten."></textarea></div>
          <div class="hp" aria-hidden="true"><label for="website">Website</label><input type="text" id="website" tabindex="-1" autocomplete="off"></div>
          <p class="err" id="err" hidden></p>
          <div class="send"><button class="btn btn-sage" type="submit" id="sendBtn" disabled>Termin buchen ''' + ARROW + '''</button><small>Sie bekommen eine Bestätigung per E-Mail und eine Einladung für Ihren Kalender.</small></div>
        </form>
      </div>
    </div>
    <aside class="side">
      <div class="next"><h3>So läuft es</h3><ol><li>Sie wählen eine Zeit. Der Termin steht sofort in unserem Kalender.</li><li>Wir rufen Sie an oder treffen uns per Video. 15 Minuten, ohne Verkaufsgespräch.</li><li>Am nächsten Arbeitstag haben Sie eine Offerte mit festem Preis. Erst dann entscheiden Sie.</li></ol></div>
      <div><h3>Keine Zeit passt?</h3><p>Schreiben Sie an <a class="u" href="mailto:hallo@websiten.ch">hallo@websiten.ch</a>, wir finden einen anderen Termin. Abends oder am Samstag geht auch.</p></div>
    </aside>
  </section>
'''

KONTAKT_JS = r'''
/* Terminbuchung
   BOOKING_API: Web-App-Adresse des Google Apps Script (siehe ANLEITUNG.md).
   Leer = Vorschau-Modus: Zeiten werden lokal berechnet, es wird nichts gebucht. */
const BOOKING_API = '%%BOOKING_API%%';

(function(){
  const $ = id => document.getElementById(id);
  const WD = ['So','Mo','Di','Mi','Do','Fr','Sa'], WDL = ['Sonntag','Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag'];
  const MO = ['Jan','Feb','März','Apr','Mai','Juni','Juli','Aug','Sept','Okt','Nov','Dez'], MOL = ['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember'];
  const st = {days:[], day:null, time:null, mode:'phone'};
  const dt = s => new Date(s + 'T12:00:00Z');
  const longLabel = (d, t) => { const x = dt(d); return WDL[x.getUTCDay()] + ', ' + x.getUTCDate() + '. ' + MOL[x.getUTCMonth()] + ', ' + t + ' Uhr'; };

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
      if(prevWd !== null && x.getUTCDay() < prevWd) b.classList.add('wk');
      prevWd = x.getUTCDay();
      b.setAttribute('aria-pressed', d.date === st.day);
      b.setAttribute('aria-label', WDL[x.getUTCDay()] + ', ' + x.getUTCDate() + '. ' + MOL[x.getUTCMonth()] + (d.slots.length ? ', ' + d.slots.length + ' Zeiten frei' : ', ausgebucht'));
      b.innerHTML = `<small>${WD[x.getUTCDay()]}</small><b>${x.getUTCDate()}</b><span>${d.slots.length ? MO[x.getUTCMonth()] : 'voll'}</span>`;
      b.onclick = () => { st.day = d.date; st.time = null; renderDays(); renderTimes(); renderPicked(); };
      box.appendChild(b);
    });
    if(!st.days.some(d => d.slots.length)) box.innerHTML = '<span class="times-empty">In den nächsten Wochen ist leider alles belegt. Schreiben Sie uns, wir finden einen Termin.</span>';
  }
  function renderTimes(){
    const box = $('times'), d = st.days.find(x => x.date === st.day);
    box.innerHTML = '';
    if(!d){ box.innerHTML = '<span class="times-empty">Wählen Sie zuerst einen Tag.</span>'; return; }
    d.slots.forEach(t => {
      const b = document.createElement('button'); b.type = 'button'; b.textContent = t;
      b.setAttribute('aria-pressed', t === st.time);
      b.onclick = () => { st.time = t; renderTimes(); renderPicked(); };
      box.appendChild(b);
    });
  }
  function renderPicked(){
    $('picked').innerHTML = st.time ? 'Gewählt: <b>' + longLabel(st.day, st.time) + '</b>' : 'Noch keine Zeit gewählt.';
    $('sendBtn').disabled = !st.time;
  }

  async function load(){
    if(!BOOKING_API){ st.days = demoSlots(); }
    else {
      try {
        const r = await fetch(BOOKING_API + '?action=slots', {cache:'no-store'});
        const j = await r.json(); if(!j.ok) throw 0; st.days = j.days;
      } catch(e){
        $('days').innerHTML = '<span class="times-empty">Der Kalender ist gerade nicht erreichbar. Schreiben Sie an hallo@websiten.ch oder versuchen Sie es in ein paar Minuten nochmals.</span>';
        return;
      }
    }
    const first = st.days.find(d => d.slots.length); st.day = first ? first.date : null;
    renderDays(); renderTimes(); renderPicked();
  }

  document.querySelectorAll('.modes button').forEach(b => b.addEventListener('click', () => {
    document.querySelectorAll('.modes button').forEach(o => o.setAttribute('aria-pressed', o === b)); st.mode = b.dataset.m;
  }));
  try { const v = localStorage.getItem('websiten-anfrage'); if(v && !$('msg').value) $('msg').value = v + '\n\n'; } catch(e){}

  const err = t => { $('err').textContent = t; $('err').hidden = !t; };
  $('form').addEventListener('submit', async e => {
    e.preventDefault(); err('');
    const name = $('name'), mail = $('mail'), tel = $('tel');
    [name, mail, tel].forEach(i => i.classList.remove('bad'));
    if(!st.time) return err('Bitte wählen Sie zuerst eine Uhrzeit.');
    if(!name.value.trim()){ name.classList.add('bad'); name.focus(); return err('Bitte tragen Sie Ihren Namen ein.'); }
    if(!/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(mail.value.trim())){ mail.classList.add('bad'); mail.focus(); return err('Bitte prüfen Sie die E-Mail-Adresse.'); }
    if(st.mode === 'phone' && tel.value.replace(/\D/g, '').length < 9){ tel.classList.add('bad'); tel.focus(); return err('Für den Anruf brauchen wir Ihre Telefonnummer.'); }
    const data = {date:st.day, time:st.time, mode:st.mode, name:name.value.trim(), firma:$('firma').value.trim(), email:mail.value.trim(), phone:tel.value.trim(), message:$('msg').value.trim(), website:$('website').value};
    const label = longLabel(st.day, st.time);
    if(!BOOKING_API){ return done(label, data, '', true); }
    const btn = $('sendBtn'); btn.disabled = true; btn.firstChild.textContent = 'Wird gebucht … ';
    try {
      const r = await fetch(BOOKING_API, {method:'POST', headers:{'Content-Type':'text/plain;charset=utf-8'}, body:JSON.stringify(data)});
      const j = await r.json();
      if(j.ok) return done(label, data, j.meet || '', false);
      if(j.error === 'taken'){ err('Diese Zeit wurde gerade vergeben. Bitte wählen Sie eine andere.'); st.time = null; await load(); }
      else err(j.message || 'Das hat nicht geklappt. Bitte versuchen Sie es nochmals oder schreiben Sie an hallo@websiten.ch.');
    } catch(e){ err('Keine Verbindung zum Kalender. Bitte versuchen Sie es nochmals oder schreiben Sie an hallo@websiten.ch.'); }
    btn.disabled = !st.time; btn.firstChild.textContent = 'Termin buchen ';
  });

  function done(label, d, meet, demo){
    const how = d.mode === 'meet' ? (meet ? `Den Link für Google Meet finden Sie in der E-Mail und in der Kalendereinladung.` : `Den Link für Google Meet bekommen Sie per E-Mail.`) : `Wir rufen Sie unter ${d.phone.replace(/</g, '')} an.`;
    $('booker').innerHTML = `<div class="ok" role="status"><h2>Gebucht: ${label}</h2><p>${how} Die Bestätigung geht an ${d.email.replace(/</g, '')}.</p><p>Etwas dazwischengekommen? Antworten Sie einfach auf die Bestätigung.</p>${demo ? '<p class="demo">Hinweis: Dies ist die Vorschau der Website. Der Kalender ist hier noch nicht verbunden, es wurde nichts gebucht.</p>' : ''}</div>`;
    try { localStorage.removeItem('websiten-anfrage'); } catch(e){}
    $('booker').scrollIntoView({block:'start', behavior:'smooth'});
  }
  load();
})();
'''

# ---------------------------------------------------------------- Rechtliches
LEGAL_CSS = r'''
.legal-text{padding-bottom:clamp(100px,12vw,160px);max-width:860px}
.legal-text h2{font-size:24px;font-weight:500;margin-top:44px;margin-bottom:10px;letter-spacing:-.01em}
.legal-text p,.legal-text li{color:#BAC5BE;font-size:17px;line-height:1.7}
.legal-text ul{padding-left:20px}
.draft{display:inline-block;margin-bottom:12px;font-size:14px;color:var(--ink);background:var(--sage);border-radius:999px;padding:4px 12px}
'''

IMPRESSUM_MAIN = '''
  <section class="page-hero pad"><h1>Impressum.</h1></section>
  <section class="legal-text pad">
    <h2>Betreiberin dieser Website</h2>
    <p>websiten.ch<br>Inhaber: Leandro Tschanzer<br>Postfach<br>8021 Zürich<br>Schweiz</p>
    <h2>Kontakt</h2>
    <p>E-Mail: hallo@websiten.ch<br>Termine: <a href="kontakt.html">online buchen</a>, das Gespräch findet per Video statt.</p>
    <h2>Rechtsform</h2>
    <p>Einzelunternehmen, nicht im Handelsregister eingetragen. Nicht mehrwertsteuerpflichtig.</p>
    <h2>Haftung</h2>
    <p>Wir prüfen die Inhalte dieser Website sorgfältig. Für Vollständigkeit, Richtigkeit und Aktualität übernehmen wir dennoch keine Gewähr. Haftungsansprüche wegen Schäden, die durch den Zugriff auf diese Website oder die Nutzung der Informationen entstehen, sind ausgeschlossen, soweit das Gesetz es zulässt.</p>
    <h2>Links auf andere Websites</h2>
    <p>Für Inhalte verlinkter Websites, zum Beispiel unserer Referenzen, sind deren Betreiber verantwortlich. Zum Zeitpunkt der Verlinkung waren keine rechtswidrigen Inhalte erkennbar.</p>
    <h2>Urheberrechte</h2>
    <p>Texte, Bilder und Gestaltung dieser Website gehören websiten.ch oder den genannten Rechteinhabern. Eine Verwendung braucht unsere schriftliche Zustimmung.</p>
    <h2>Bildnachweis</h2>
    <p>Fotos: Unsplash (unsplash.com/license). Abbildungen der Websites unserer Kunden KF Bauservice GmbH und Kastrati Trockenbau und Innenausbau.</p>
  </section>
'''

DATENSCHUTZ_MAIN = '''
  <section class="page-hero pad"><h1>Datenschutz.</h1></section>
  <section class="legal-text pad">
    <span class="draft">Entwurf nach revDSG, vor dem Livegang juristisch prüfen lassen</span>
    <h2>Wer ist verantwortlich?</h2>
    <p>websiten.ch, Inhaber Leandro Tschanzer, Postfach, 8021 Zürich, hallo@websiten.ch</p>
    <h2>Welche Daten wir bearbeiten</h2>
    <ul><li>Angaben, die Sie bei der Terminbuchung oder per E-Mail angeben, zum Beispiel Name, Firma, E-Mail, Telefonnummer und Ihre Nachricht.</li><li>Technische Daten beim Besuch der Website, zum Beispiel IP-Adresse, Browser und Zeitpunkt des Zugriffs. Diese speichert unser Hosting-Anbieter in Protokolldateien.</li></ul>
    <h2>Wozu wir sie verwenden</h2>
    <p>Wir verwenden Ihre Angaben, um Ihre Anfrage zu beantworten, Offerten zu erstellen und Aufträge abzuwickeln. Wir verkaufen keine Daten und geben sie nur weiter, wenn es für den Auftrag nötig ist oder das Gesetz es verlangt.</p>
    <h2>Wo Ihre Daten liegen</h2>
    <p>Website, E-Mail und Hosting laufen bei Infomaniak Network SA in Genf. Die Daten werden in der Schweiz gespeichert.</p>
    <h2>Terminbuchung</h2>
    <p>Wenn Sie einen Termin buchen, tragen wir ihn mit Ihren Angaben in unseren Google Kalender ein und senden Ihnen eine Bestätigung per E-Mail. Dafür nutzen wir Google Workspace beziehungsweise Google Kalender und Gmail der Google Ireland Limited. Dabei können Daten auch in Länder ausserhalb der Schweiz übertragen werden, zum Beispiel in die USA. Wir löschen die Termine spätestens zwölf Monate nach dem Gespräch, sofern daraus kein Auftrag entsteht.</p>
    <h2>Ihre Rechte</h2>
    <p>Sie können jederzeit Auskunft über Ihre gespeicherten Daten verlangen und deren Berichtigung oder Löschung beantragen. Schreiben Sie dafür an hallo@websiten.ch.</p>
    <h2>Stand</h2>
    <p>Oktober 2026</p>
  </section>
'''


# ---------------------------------------------------------------- Fragen
FRAGEN_CSS = r'''/* Fragen: links die Fragen, rechts die Antwort. Drüberfahren genügt. */
.faq{padding-top:clamp(80px,10vw,140px);padding-bottom:clamp(100px,12vw,180px)}
.faq .h-sec{max-width:14ch}
.fq-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(40px,6vw,120px);margin-top:clamp(40px,5vw,72px);align-items:start}
.fq-list{list-style:none;counter-reset:none;border-top:1px solid var(--line)}
.fq-list li{border-bottom:1px solid var(--line)}
.fq{position:relative;display:block;width:100%;text-align:left;padding:22px 0 22px 0;font-size:clamp(19px,1.55vw,24px);line-height:1.35;letter-spacing:-.015em;color:#7F8B84;transition:color .3s,padding-left .45s var(--ease)}
.fq::before{content:"";position:absolute;left:0;top:50%;width:0;height:2px;background:var(--sage);transition:width .45s var(--ease)}
.fq:hover{color:#C9D2CD}
.fq[aria-expanded="true"]{color:var(--text);padding-left:34px}
.fq[aria-expanded="true"]::before{width:20px}
.fa-m{display:none}
.fq-ans{position:sticky;top:120px;min-height:260px;display:flex;flex-direction:column}
.fa{display:none}
.fa.on{display:block;animation:faIn .5s var(--ease)}
.fa p{font-size:clamp(24px,2.3vw,36px);line-height:1.35;letter-spacing:-.025em;color:var(--text);max-width:24ch;text-wrap:pretty}
@keyframes faIn{from{opacity:0;transform:translateY(10px)}to{opacity:1;transform:none}}
.fq-more{display:inline-flex;align-items:center;gap:12px;margin-top:40px;align-self:flex-start;font-size:16px;color:var(--sage-light)}
.fq-more:hover{color:var(--text)}
.fq-more .ic{width:18px;height:18px}
@media (max-width: 860px){
  .fq-grid{grid-template-columns:minmax(0,1fr)}
  .fq-ans .fa{display:none!important}
  .fq-ans{position:static;min-height:0}
  .fq-more{margin-top:8px}
  .fa-m{display:grid;grid-template-rows:0fr;transition:grid-template-rows .45s var(--ease)}
  .fa-m p{overflow:hidden;min-height:0;font-size:18px;line-height:1.6;color:#C7D0CA}
  .fq[aria-expanded="true"] + .fa-m{grid-template-rows:1fr}
  .fq[aria-expanded="true"] + .fa-m p{padding-bottom:22px}
}
@media (prefers-reduced-motion: reduce){ .fa.on{animation:none} }
'''
FRAGEN_MAIN = '''
  <section class="page-hero pad">
    <h1>Häufige Fragen</h1>
    <p>Fahren Sie mit der Maus über eine Frage. Die Antwort steht rechts daneben.</p>
  </section>
  <section class="faq pad" id="fragen" style="padding-top:0">
        <div class="fq-grid">
      <ol class="fq-list"><li><button type="button" class="fq" id="fq0" aria-controls="fa0" aria-expanded="true"><span>Wie lange geht es, bis meine Website online ist?</span></button><div class="fa-m" id="fam0"><p>Eine kleine Firmenwebsite meistens drei bis vier Wochen, eine grössere fünf bis acht. Das Datum steht in der Offerte, und daran halten wir uns.</p></div></li><li><button type="button" class="fq" id="fq1" aria-controls="fa1" aria-expanded="false"><span>Gehört die Website danach mir?</span></button><div class="fa-m" id="fam1"><p>Ja. Domain, Inhalte und Zugänge laufen auf Ihren Namen. Wenn Sie einmal wechseln wollen, bekommen Sie alles.</p></div></li><li><button type="button" class="fq" id="fq2" aria-controls="fa2" aria-expanded="false"><span>Wo sind meine Daten gespeichert?</span></button><div class="fa-m" id="fam2"><p>In der Schweiz. Server, Domains und E-Mail laufen bei Infomaniak in Genf.</p></div></li><li><button type="button" class="fq" id="fq3" aria-controls="fa3" aria-expanded="false"><span>Bringt ihr mich bei Google auf Platz 1?</span></button><div class="fa-m" id="fam3"><p>Das kann niemand ehrlich versprechen. Wir machen die Seite technisch sauber und schreiben Inhalte zu dem, was Ihre Kunden suchen. Das ist die Grundlage, damit Sie gefunden werden.</p></div></li><li><button type="button" class="fq" id="fq4" aria-controls="fa4" aria-expanded="false"><span>Was zahle ich nach dem Start noch?</span></button><div class="fa-m" id="fam4"><p>CHF 25 im Monat für Hosting, .ch-Domain, SSL und Backups. Die ersten drei Monate kosten nur CHF 10.</p></div></li><li><button type="button" class="fq" id="fq5" aria-controls="fa5" aria-expanded="false"><span>Kann ich Texte und Bilder selber ändern?</span></button><div class="fa-m" id="fam5"><p>Ja, Sie bekommen eine kurze Einführung. Oder Sie schicken uns eine Nachricht, und wir machen es.</p></div></li></ol>
      <div class="fq-ans" aria-live="polite">
        <div class="fa on" id="fa0" role="region" aria-labelledby="fq0"><p>Eine kleine Firmenwebsite meistens drei bis vier Wochen, eine grössere fünf bis acht. Das Datum steht in der Offerte, und daran halten wir uns.</p></div><div class="fa" id="fa1" role="region" aria-labelledby="fq1"><p>Ja. Domain, Inhalte und Zugänge laufen auf Ihren Namen. Wenn Sie einmal wechseln wollen, bekommen Sie alles.</p></div><div class="fa" id="fa2" role="region" aria-labelledby="fq2"><p>In der Schweiz. Server, Domains und E-Mail laufen bei Infomaniak in Genf.</p></div><div class="fa" id="fa3" role="region" aria-labelledby="fq3"><p>Das kann niemand ehrlich versprechen. Wir machen die Seite technisch sauber und schreiben Inhalte zu dem, was Ihre Kunden suchen. Das ist die Grundlage, damit Sie gefunden werden.</p></div><div class="fa" id="fa4" role="region" aria-labelledby="fq4"><p>CHF 25 im Monat für Hosting, .ch-Domain, SSL und Backups. Die ersten drei Monate kosten nur CHF 10.</p></div><div class="fa" id="fa5" role="region" aria-labelledby="fq5"><p>Ja, Sie bekommen eine kurze Einführung. Oder Sie schicken uns eine Nachricht, und wir machen es.</p></div>
        <a class="fq-more" href="kontakt.html">Ihre Frage ist nicht dabei? Fragen Sie uns am Telefon. ''' + ARROW + '''</a>
      </div>
    </div>
  </section>
'''
FRAGEN_JS = r'''
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
/* Fragen: Drüberfahren oder Antippen zeigt die Antwort */
(function(){
  const qs = [...document.querySelectorAll('.fq')]; if(!qs.length) return;
  const show = i => qs.forEach((q, j) => { q.setAttribute('aria-expanded', i === j); document.getElementById('fa' + j).classList.toggle('on', i === j); });
  const desk = matchMedia('(hover: hover) and (min-width: 861px)');
  qs.forEach((q, i) => {
    q.addEventListener('mouseenter', () => { if(desk.matches) show(i); });
    q.addEventListener('focus', () => { if(desk.matches) show(i); });
    q.addEventListener('click', () => { if(!desk.matches && q.getAttribute('aria-expanded') === 'true') q.setAttribute('aria-expanded', 'false'); else show(i); });
  });
})();

'''
