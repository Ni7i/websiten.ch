# Startseite: Einstieg mit Film, Text, Leistungen (schlicht, Schwarz-Weiss), Ablauf, Preise
import re, home6, home7, svzumo
from parts import ARROW

DESC = home6.DESC

SV = [
    ('websites', 'Websites', 'Für Ihren Betrieb gestaltet, fürs Handy gebaut.'),
    ('shops', 'Online-Shops', 'Mit TWINT, Karte, Rechnung und Versand.'),
    ('seo', 'Google und SEO', 'Gefunden werden, wo Ihre Kunden suchen.'),
    ('hosting', 'Domains und Hosting', 'Bei Infomaniak in Genf, mit Backups und Updates.'),
    ('m365', 'Microsoft 365', 'E-Mail, Teams und Dateien für Ihr Team.'),
    ('ki', 'KI-Chatbots', 'Beantwortet häufige Fragen auf Ihrer Website.'),
]
TILES = ''.join(f'<li><a class="sw" href="leistungen.html#{i}"><span class="sw-img"><img src="%%S_{i}%%" alt="" loading="lazy"></span><b>{t}</b><span>{d}</span></a></li>' for i, t, d in SV)
SERVICES = '''<section class="sws pad" id="leistungen" aria-labelledby="swsT">
    <div class="sws-head"><h2 id="swsT">Was wir machen</h2><a class="sv-all" href="leistungen.html">Alle Leistungen ''' + ARROW + '''</a></div>
    <ul class="sws-grid">''' + TILES + '''</ul>
  </section>'''

PRICES = '''<section class="pr pad" aria-labelledby="prT">
    <div class="pr-left">
      <h2 id="prT">Was es <em class="hl">kostet</em></h2>
      <p>Sie kennen den Preis, bevor wir anfangen. Den genauen Betrag für Ihr Projekt rechnen Sie selbst aus.</p>
      <a class="sv-all" href="preise.html">Zum Preisrechner ''' + ARROW + '''</a>
    </div>
    <dl class="pr-list">
      <div><dt>Website mit 4 Seiten<small>Jede weitere Seite CHF 150.–</small></dt><dd><small>CHF</small>590.–</dd></div>
      <div><dt>Online-Shop<small>Mit TWINT, Karte und Versand</small></dt><dd><small>ab CHF</small>1’890.–</dd></div>
      <div><dt>Hosting und Domain<small>Die ersten 3 Monate CHF 10.–</small></dt><dd><small>CHF</small>25.–<small>/ Monat</small></dd></div>
    </dl>
  </section>'''

MAIN = '\n  ' + home6.HERO + '\n\n  ' + home7.STATEMENT + '\n\n  ' + svzumo.section() + '\n\n  ' + home6.BUILD + '\n\n  ' + PRICES + '\n'

CSS = home6.CSS + r'''
.sv-all{display:inline-flex;align-items:center;gap:12px;font-size:17px;padding-bottom:6px;border-bottom:1px solid var(--text);transition:gap .3s var(--ease)}
.sv-all:hover{gap:18px}

/* Was wir machen: sechs Schwarz-Weiss-Fotos, Titel, eine Zeile */
.sws{padding-top:clamp(90px,10vw,160px);padding-bottom:clamp(90px,10vw,160px)}
.sws-head{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin-bottom:clamp(40px,5vw,72px)}
.sws-head h2,.pr h2{font-size:clamp(40px,4.6vw,80px);line-height:1;font-weight:700;letter-spacing:-.05em}
.sws-grid{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(36px,4vw,64px) clamp(16px,2vw,28px)}
.sw{display:block}
.sw-img{display:block;aspect-ratio:4/3;overflow:hidden;border-radius:4px;background:#1E1E1E;margin-bottom:18px}
.sw-img img{width:100%;height:100%;object-fit:cover;display:block;filter:brightness(.82) contrast(1.05);transition:filter .5s,transform .9s var(--ease)}
.sw:hover .sw-img img{filter:brightness(1);transform:scale(1.03)}
.sw b{display:block;font-size:clamp(21px,1.7vw,27px);font-weight:700;letter-spacing:-.035em}
.sw span:last-child{display:block;font-size:15.5px;line-height:1.5;color:var(--muted);margin-top:6px}

/* Was es kostet: ruhige Preisliste */
.pr{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);gap:clamp(40px,7vw,140px);padding-top:clamp(90px,10vw,160px);padding-bottom:clamp(90px,10vw,160px)}
.pr-left p{font-size:clamp(17px,1.35vw,20px);line-height:1.6;color:#BDBDBD;max-width:34ch;margin:24px 0 32px}
.pr-list{margin:0;border-top:1px solid var(--line)}
.pr-list > div{display:flex;justify-content:space-between;align-items:baseline;gap:24px;padding:clamp(22px,2.4vw,34px) 0;border-bottom:1px solid var(--line)}
.pr-list dt{font-size:clamp(19px,1.5vw,23px);font-weight:600;letter-spacing:-.02em}
.pr-list dt small{display:block;font-size:15px;font-weight:400;letter-spacing:0;color:var(--muted);margin-top:6px}
.pr-list dd{margin:0;white-space:nowrap;font-size:clamp(32px,3.2vw,54px);font-weight:700;letter-spacing:-.05em;line-height:1;font-variant-numeric:tabular-nums}
.pr-list dd small{font-size:14px;font-weight:500;letter-spacing:0;color:var(--muted);margin:0 8px}
.pr-list dd small:last-child{margin-right:0}

/* Ablauf: das Website-Beispiel am Schluss ruhig und dunkel */
.build .frame-b{background:#1A1A1A;border-color:#2A2A2A;box-shadow:none}
.build .m1{background:#1B1B1B;color:#D6D6D6}
.build .m1 .k-top,.build .m1 .k-strip{border-color:#2A2A2A}
.build .m1 .k-logo,.build .m1 .k-tel,.build .m1 .k-more{color:#E4E4E4;border-color:#5A5A5A}
.build .m1 .k-logo svg path{fill:#9A9A9A}
.build .m1 .k-links,.build .m1 .k-kick,.build .m1 .k-p,.build .m1 .k-strip span{color:#8E8E8E}
.build .m1 h4,.build .m1 .k-strip b{color:#EDEDED}
.build .m1 .k-btn{background:#E4E4E4;color:#151515}
.build .m1 .k-cap{background:#1B1B1B;color:#8E8E8E}
.build .m1 .k-strip span{border-color:#2A2A2A}
.build .m1 .k-strip .k-sos{background:#242424;color:#8E8E8E}
.build .m1 .k-sos b{color:#EDEDED}

@media (max-width: 1000px){ .sws-grid{grid-template-columns:repeat(2,minmax(0,1fr))} }
@media (max-width: 860px){ .pr{grid-template-columns:1fr} .pr-list dd{font-size:30px} }
@media (max-width: 560px){ .sws-grid{grid-template-columns:1fr} }
'''
CSS += svzumo.CSS
JS = home7.JS_BASE
