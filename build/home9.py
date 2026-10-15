# Startseite, überarbeitet: ruhig, schwarz-weiss, keine Kästen. Ein Bildelement (Logo-Fenster im Einstieg), sonst Schrift und Linien.
import re, home6, home7, home8
from parts import ARROW

DESC = home6.DESC

HERO = home6.HERO.replace('<a class="btn btn-sage" href="kontakt.html">Projekt anfragen ' + ARROW + '</a>', '<a class="btn btn-sage" href="kontakt.html">Termin wählen ' + ARROW + '</a>')
assert 'Termin wählen' in HERO
HERO = HERO.replace('<span class="quiet">Telefon klingelt.</span>', '<span class="quiet"><em class="hl">Telefon klingelt.</em></span>')
assert 'class="hl"' in HERO

FILES = {'websites': 'websites.html', 'shops': 'online-shops.html', 'seo': 'google-seo.html', 'hosting': 'hosting.html', 'm365': 'microsoft-365.html', 'ki': 'ki-chatbots.html'}
SV = [
    ('websites', 'Websites', 'Gestaltet für Ihren Betrieb und gebaut fürs Handy. Mit Texten, die Ihre Kunden verstehen, und einem Formular, das Anfragen bringt.', ['Firmenwebsites', 'Relaunch', 'Mehrsprachig', 'Texte']),
    ('shops', 'Online-Shops', 'Wir richten Ihren Shopify-Account auf professionellem Niveau ein. Mit TWINT, Karte, Rechnung und Versand in der Schweiz.', ['Shopify', 'WooCommerce', 'Shop-Umzug', 'B2B']),
    ('seo', 'Google und SEO', 'Damit man Sie findet, wenn jemand in Ihrer Region sucht. Mit Unternehmensprofil, sauberer Technik und Google Ads mit festem Budget.', ['Google Maps', 'Lokale SEO', 'Google Ads']),
    ('hosting', 'Domains und Hosting', 'Domain, Website und E-Mail bei Infomaniak in Genf. Updates, Backups und Sicherheit übernehmen wir, Sie sehen jederzeit, dass alles läuft.', ['.ch-Domains', 'Backups', 'Updates', 'SSL']),
    ('m365', 'Microsoft 365', 'E-Mail, Kalender, Teams und Dateien für Ihr Team, sauber eingerichtet und betreut. Neue Leute haben ihr Konto am ersten Tag.', ['E-Mail-Umzug', 'Teams', 'OneDrive', 'Fernwartung']),
    ('ki', 'KI-Chatbots', 'Beantwortet häufige Fragen direkt auf Ihrer Website, mit Ihren Informationen. Was er nicht weiss, gibt er an Sie weiter.', ['Ihre Inhalte', 'Mehrsprachig', 'Übergabe an Sie']),
]
ITEMS = ''.join(f'<li class="mv-i{" on" if k == 0 else ""}" data-k="{k}"><button type="button" aria-controls="mvScr" aria-pressed="{"true" if k == 0 else "false"}"><span class="mv-n">0{k + 1}</span><span class="mv-t">{t}</span></button><div class="mv-b"><div class="mv-bi"><p>{d}</p><ul>' + ''.join(f'<li>{x}</li>' for x in sub) + f'</ul><a href="{FILES[i]}">Mehr dazu {ARROW}</a></div></div></li>' for k, (i, t, d, sub) in enumerate(SV))
SCREENS = ''.join(f'<img class="mv-s{" on" if k == 0 else ""}" data-k="{k}" src="%%SCR_{i}%%" alt="Beispiel: {t}"' + ('' if k == 0 else ' loading="lazy"') + '>' for k, (i, t, d, sub) in enumerate(SV))
SERVICES = """<section class="mv pad" id="leistungen" aria-labelledby="mvT">
    <div class="lx-head"><h2 id="mvT">Was wir <em class="hl">machen</em></h2><p>Alles, was Ihr Betrieb online braucht. Von einer Ansprechperson, mit festem Preis.</p></div>
    <div class="mv-grid">
      <ol class="mv-list">""" + ITEMS + """</ol>
      <div class="mv-dev"><div class="mv-mac" id="mvScr"><div class="mv-screen">""" + SCREENS + """<span class="mv-glare"></span></div><img class="mv-frame" src="%%MACFRAME%%" alt="" aria-hidden="true"></div></div>
    </div>
  </section>"""

STATEMENT = '''<section class="statement pad">
    <h2>Wir bauen Ihre Website. Und wir sind auch danach <em class="hl">für Sie da.</em></h2>
    <div class="two-col">
      <p>Sie haben eine feste Ansprechperson, die Ihren Betrieb kennt. Den Preis und den Termin wissen Sie, bevor wir anfangen. Updates, Backups und kleine Änderungen erledigen wir für Sie, auch Jahre nach dem Start.</p>
      <p>Ihre Daten liegen bei Infomaniak in Genf und bleiben in der Schweiz. Wenn einmal etwas klemmt, schreiben Sie uns kurz. Wir melden uns rasch und <em class="hl-s">kümmern uns darum.</em></p>
    </div>
  </section>'''


UP = '<svg viewBox="0 0 14 14" width="13" height="13" aria-hidden="true"><path d="M3 11L11 3M5 3h6v6" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'
REFS = [
    ('kf', 'KF Bauservice GmbH', 'Buchs AG', 'https://kf-bauservice.ch/', 'kf-bauservice.ch',
     'Gipser, Maler, Trockenbau und Fassaden. Ein junger Betrieb, der zeigen wollte, wie sauber er arbeitet. Echte Fotos von den eigenen Baustellen, klare Leistungen und ein kurzer Weg zur Anfrage.',
     ['Webdesign', 'Umsetzung', 'Fürs Handy gebaut']),
    ('ka', 'Kastrati Trockenbau & Innenausbau', 'Rheda-Wiedenbrück, Deutschland', 'https://kastrati-trockenbau-innenausbau.de/', 'kastrati-trockenbau-innenausbau.de',
     'Trockenbau und Innenausbau vom Rohbau bis zum fertigen Raum. Die Website zeigt die eigenen Projekte gross und führt Bauherren direkt zur Anfrage.',
     ['Webdesign', 'Umsetzung', 'Fürs Handy gebaut']),
]
def _ref(k, r):
    key, name, place, url, host, text, tags = r
    return (f'<article class="wk{" flip" if k % 2 else ""}">'
            f'<div class="wk-tx"><span class="wk-n">0{k + 1}</span><h3>{name}</h3><span class="wk-p">{place}</span><p>{text}</p>'
            f'<ul>' + ''.join(f'<li>{t}</li>' for t in tags) + f'</ul>'
            f'<a class="wk-l" href="{url}" target="_blank" rel="noopener">Website ansehen {UP}</a></div>'
            f'<a class="wk-v" href="{url}" target="_blank" rel="noopener" aria-label="{host} öffnen">'
            f'<img src="%%DEV_{key}%%" alt="Website {host} auf MacBook und iPhone" loading="lazy" width="1200" height="800"></a></article>')
WORK = """<section class="wks pad" id="arbeiten" aria-labelledby="wksT">
    <div class="lx-head"><h2 id="wksT">Unsere <em class="hl">Arbeiten</em></h2><p>Zwei Websites, die wir zuletzt gebaut haben. Beide sind online, schauen Sie sie sich ruhig selbst an.</p></div>
    """ + ''.join(_ref(k, r) for k, r in enumerate(REFS)) + """
  </section>"""

PRICES = """<section class="pr pad" aria-labelledby="prT">
    <div class="pr-left">
      <h2 id="prT">Was es <em class="hl">kostet</em></h2>
      <p>Sie kennen den Preis, bevor wir anfangen. Den genauen Betrag für Ihr Projekt rechnen Sie selbst aus.</p>
      <a class="sv-all" href="preise.html">Zum Preisrechner """ + ARROW + """</a>
    </div>
    <dl class="pr-list">
      <div><dt>Website mit 4 Seiten<small>Jede weitere Seite CHF 150</small></dt><dd><small>CHF</small>590</dd></div>
      <div><dt>Hosting und Domain<small>Mit Backups, Updates und E-Mail</small></dt><dd><small>CHF</small>25<small>im Monat</small></dd></div>
    </dl>
  </section>"""

MAIN = '\n  ' + HERO + '\n\n  ' + STATEMENT + '\n\n  ' + home6.BUILD + '\n\n  ' + SERVICES + '\n\n  ' + WORK + '\n\n  ' + PRICES + '\n'

_c = home8.CSS
_c = _c[:_c.index('\n.zs{')] if '\n.zs{' in _c else _c
_c = _c[:_c.index('/* Was wir machen: sechs Schwarz-Weiss-Fotos')] + _c[_c.index('/* Was es kostet: ruhige Preisliste */'):]
CSS = _c.replace('<h2 id="prT">Was es kostet</h2>', '') + r'''
/* Farbige Wörter: warmer Verlauf */
:root{--hl:linear-gradient(100deg,var(--acc-a1),var(--acc-a2))}
.hl{font-style:normal;color:var(--acc-s)}
.hl-s{font-style:normal;color:var(--acc-s)}
.hero h1 .quiet .hl{color:var(--acc-s)}
.statement h2{max-width:22ch}
.lx-list a:hover .lx-t{color:var(--acc-s)}
.lx-list a:hover .lx-a{color:var(--acc-s)}
.pr-list dd{transition:color .3s}
.pr-list > div:hover dd{color:var(--acc-s)}
.btn-sage{background:var(--acc-s);color:#0C201A}
.btn-sage:hover{background:var(--acc-a1);color:#0C201A}
.lx-list .lx-a{color:var(--acc-d1)}
.sv-all{border-bottom:0;padding-bottom:0}
.sv-all svg{color:var(--acc-s)}
.pr-list dd small{color:var(--acc-s)}
.build .bp b{background:var(--acc-s)}
.build .bn-logo path:last-child{fill:var(--acc-s)}
.vid-btn{border-color:rgba(163,194,170,.35)}
/* Was wir machen: MacBook mit wechselndem Bildschirm */
.mv{padding-top:clamp(90px,10vw,160px);padding-bottom:clamp(90px,10vw,160px)}
.mv-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.9fr);gap:clamp(32px,5vw,90px);align-items:center}
.mv-list{list-style:none;margin:0;padding:0}
.mv-i button{width:100%;display:flex;align-items:baseline;gap:16px;padding:18px 0;text-align:left;color:var(--text);cursor:pointer}
.mv-n{font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums;width:22px;flex:none;transition:color .3s}
.mv-t{font-size:clamp(22px,1.9vw,30px);font-weight:700;letter-spacing:-.035em;color:#6C6C6C;transition:color .3s}
.mv-i button:hover .mv-t{color:#BDBDBD}
.mv-i.on .mv-t{color:var(--text)}
.mv-i.on .mv-n{color:var(--acc-s)}
.mv-b{display:grid;grid-template-rows:0fr;transition:grid-template-rows .5s var(--ease)}
.mv-bi{min-height:0;overflow:hidden}
.mv-i.on .mv-b{grid-template-rows:1fr}
.mv-b{overflow:hidden}
.mv-b p{font-size:16px;line-height:1.6;color:#BDBDBD;padding-left:38px;max-width:44ch}
.mv-b ul{list-style:none;display:flex;flex-wrap:wrap;gap:6px 16px;margin:12px 0 0;padding:0 0 0 38px;font-size:14px;color:var(--muted)}
.mv-b li::before{content:"";display:inline-block;width:4px;height:4px;border-radius:50%;background:var(--acc-s);margin-right:8px;vertical-align:middle}
.mv-b a{display:inline-flex;align-items:center;gap:10px;margin:16px 0 22px 38px;font-size:15px}
.mv-b a svg{width:16px;height:11px;color:var(--acc-s)}
.mv-mac{position:relative;width:100%;aspect-ratio:1060/690}
.mv-screen{position:absolute;left:9.717%;top:6.522%;width:80.566%;height:77.391%;overflow:hidden;background:#0B0B0B;border-radius:.6% .6% 0 0}
.mv-s{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top;opacity:0;transition:opacity .6s ease}
.mv-s.on{opacity:1}
.mv-glare{position:absolute;inset:0;background:linear-gradient(118deg,rgba(255,255,255,.08),rgba(255,255,255,.02) 30%,rgba(255,255,255,0) 44%);pointer-events:none}
.mv-frame{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
@media (max-width: 860px){
  .mv-grid{grid-template-columns:1fr;gap:28px}
  .mv-dev{order:-1;position:sticky;top:64px;z-index:2;background:var(--bg);padding:8px 0}
  .mv-t{font-size:22px}
}
/* Preisliste ohne Linien */
.pr-list,.pr-list > div{border:0!important}
.pr-list{display:grid;gap:clamp(26px,3vw,44px)}
.pr-list > div{padding:0!important}
.pr-list dd{font-size:clamp(48px,5vw,92px)!important}
/* Unsere Arbeiten */
.wks{padding-top:clamp(90px,10vw,160px);padding-bottom:clamp(60px,7vw,110px)}
.wk{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);gap:clamp(40px,7vw,140px);align-items:center;padding:clamp(40px,5vw,72px) 0}
.wk-n{font-size:14px;color:var(--acc-s);font-variant-numeric:tabular-nums}
.wk h3{font-size:clamp(26px,2.4vw,40px);line-height:1.08;font-weight:700;letter-spacing:-.04em;margin-top:14px}
.wk-p{display:block;font-size:15px;color:var(--muted);margin-top:8px}
.wk p{font-size:clamp(16px,1.2vw,18px);line-height:1.65;color:#C4C4C4;margin-top:22px;max-width:42ch}
.wk ul{list-style:none;display:flex;flex-wrap:wrap;gap:8px 18px;margin:22px 0 0;padding:0;font-size:14.5px;color:var(--muted)}
.wk li::before{content:"";display:inline-block;width:5px;height:5px;border-radius:50%;background:var(--acc-s);margin-right:8px;vertical-align:middle}
.wk-l{display:inline-flex;align-items:center;gap:10px;margin-top:30px;font-size:16.5px;transition:gap .3s var(--ease)}
.wk-l:hover{gap:14px}
.wk-l svg{color:var(--acc-s)}
.wk-v{display:block;margin:-3% -4% -4% -2%}
.wk-v img{display:block;width:100%;height:auto;transition:transform .8s var(--ease)}
.wk-v:hover img{transform:translateY(-6px) scale(1.01)}
.wk-d{display:block;border-radius:12px;overflow:hidden;background:#fff;border:1px solid #2C2C2C;box-shadow:0 40px 80px -40px rgba(0,0,0,.7);transition:transform .7s var(--ease)}
.wk-bar{display:flex;align-items:center;gap:6px;padding:9px 12px;background:#242424;border-bottom:1px solid #2C2C2C}
.wk-bar i{width:9px;height:9px;border-radius:50%;background:#444}
.wk-bar em{font-style:normal;font-size:12px;color:#9A9A9A;margin:0 auto;transform:translateX(-20px)}
.wk-d img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover;object-position:top}
.wk-m{position:absolute;right:0;bottom:0;width:clamp(110px,22%,170px);border-radius:22px;overflow:hidden;border:5px solid #0E0E0E;background:#0E0E0E;box-shadow:0 30px 60px -20px rgba(0,0,0,.8);transition:transform .7s var(--ease)}
.wk-m img{display:block;width:100%;aspect-ratio:9/19.5;object-fit:cover;object-position:top}
.wk-v:hover .wk-d{transform:translateY(-6px)}
.wk-v:hover .wk-m{transform:translateY(-12px)}
.wk.flip{grid-template-columns:minmax(0,1.35fr) minmax(0,1fr)}
.wk.flip .wk-tx{order:2}
@media (max-width: 860px){
  .wk,.wk.flip{grid-template-columns:1fr;gap:32px}
  .wk.flip .wk-tx{order:0}
  .wk-v{order:-1}
  .wk-bar em{transform:none}
}

.pr h2{font-size:clamp(40px,4.6vw,80px);line-height:1;font-weight:700;letter-spacing:-.05em}
/* Was wir machen: nur Schrift und Linien */
.lx{padding-top:clamp(90px,10vw,160px);padding-bottom:clamp(90px,10vw,160px);border-top:1px solid var(--line)}
.lx-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);gap:clamp(40px,7vw,140px);align-items:end;margin-bottom:clamp(48px,6vw,90px)}
.lx-head h2{font-size:clamp(40px,4.6vw,80px);line-height:1;font-weight:700;letter-spacing:-.05em}
.lx-head p{font-size:clamp(17px,1.35vw,20px);line-height:1.6;color:#BDBDBD;max-width:40ch}
.lx-list{list-style:none;margin:0 0 clamp(40px,5vw,64px);padding:0;border-top:1px solid var(--line)}
.lx-list li{border-bottom:1px solid var(--line)}
.lx-list a{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.35fr);column-gap:clamp(40px,7vw,140px);align-items:center;padding:clamp(24px,2.6vw,38px) 0;position:relative}
.lx-n{display:none}
.lx-t{font-size:clamp(28px,3vw,50px);line-height:1.05;font-weight:700;letter-spacing:-.045em;transition:color .3s,transform .45s var(--ease)}
.lx-d{font-size:clamp(16px,1.2vw,18px);line-height:1.55;color:var(--muted);padding-right:56px;max-width:52ch;transition:color .3s}
.lx-a{position:absolute;right:0;top:50%;transform:translateY(-50%);color:var(--muted);transition:transform .35s var(--ease),color .3s}
.lx-list:hover .lx-t{color:#5E5E5E}
.lx-list a:hover .lx-t{color:var(--text);transform:translateX(10px)}
.lx-list a:hover .lx-d{color:#D0D0D0}
.lx-list a:hover .lx-a{color:var(--text);transform:translate(4px,-50%)}
@media (max-width: 860px){
  .lx-head,.lx-list a{grid-template-columns:1fr}
  .lx-head{gap:18px}
  .lx-d{margin-top:8px;padding-right:40px}
  .lx-list:hover .lx-t{color:var(--text)}
}
'''
JS = home8.JS + r'''
/* Was wir machen: Klick oder Drüberfahren wechselt den Bildschirm, ohne Eingriff läuft es langsam weiter */
(function(){
  const items = [...document.querySelectorAll('.mv-i')], scr = [...document.querySelectorAll('.mv-s')];
  if(!items.length) return;
  let cur = 0, timer = 0, touched = false;
  const set = k => { cur = k; items.forEach((e, i) => { e.classList.toggle('on', i === k); e.querySelector('button').setAttribute('aria-pressed', i === k); }); scr.forEach((e, i) => { if(i === k && e.loading === 'lazy') e.loading = 'eager'; e.classList.toggle('on', i === k); }); };
  items.forEach((e, i) => {
    e.querySelector('button').addEventListener('click', () => { touched = true; set(i); });
    if(matchMedia('(hover: hover)').matches) e.querySelector('button').addEventListener('mouseenter', () => { touched = true; set(i); });
  });
  if(reduce) return;
  const sec = document.getElementById('leistungen');
  new IntersectionObserver(es => es.forEach(en => { clearInterval(timer); if(en.isIntersecting) timer = setInterval(() => { if(!touched) set((cur + 1) % items.length); }, 4200); }), {threshold: .4}).observe(sec);
})();
'''

