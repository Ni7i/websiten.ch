# Zwei Fassungen der Startseite: V1 nach Wunsch des Kunden, V2 nach unserer Empfehlung
import re, home6, svopts
from parts import ARROW

DESC = home6.DESC

# "Mehr über uns" entfernen
STATEMENT = re.sub(r'\s*<div class="ax" id="ax">.*?(?=\s*</section>)', '', home6.STATEMENT, flags=re.S)
assert 'id="ax"' not in STATEMENT

# Gerüst-Punkte in der gleichen Farbe wie die Schweizerkarte
JS_BASE = re.sub(r'const grey = \[\[.*?\]\]', 'const grey = [[104,130,112],[104,130,112],[104,130,112]]', home6.JS)
assert '[[104,130,112],[104,130,112],[104,130,112]]' in JS_BASE

def version(v):
    if v == 1:
        name, desc, sh, sc, sj = svopts.o1()
        main = '\n  ' + home6.HERO + '\n\n  ' + STATEMENT + '\n\n  ' + home6.BUILD + '\n\n  ' + sh + '\n'
        return main, home6.CSS + svopts.BASE_CSS + sc, JS_BASE + sj
    # V2: klarer Ablauf: Was, Wie, Was kostet es, Gespräch
    hero = home6.HERO.replace('<a class="btn btn-sage" href="kontakt.html">Projekt anfragen ' + ARROW + '</a>', '<a class="btn btn-sage" href="kontakt.html">Termin wählen ' + ARROW + '</a><a class="btn btn-line hv-2nd" href="preise.html">Preise ansehen</a>')
    hero = hero.replace('<p>Design, Technik und Betreuung aus einer Hand. Domains und Hosting in der Schweiz.</p>', '')
    hero = hero.replace('</div>\n    </div>\n    <button class="vid-btn"', '</div>\n      <ul class="hv-facts"><li>Fester Preis vor Projektstart</li><li>Eine Ansprechperson</li><li>Server bei Infomaniak in Genf</li></ul>\n    </div>\n    <button class="vid-btn"', 1)
    assert 'hv-facts' in hero and 'Preise ansehen' in hero
    name, desc, sh, sc, sj = svopts.o4()
    price = '''<section class="pb pad" aria-labelledby="pbT">
    <div class="pb-head"><h2 id="pbT">Was es kostet</h2><p>Fixpreise, bevor wir anfangen. Den genauen Betrag für Ihr Projekt rechnen Sie in einer Minute selbst aus.</p></div>
    <div class="pb-grid">
      <div><span class="pb-v"><small>CHF</small>590.–</span><b>Website mit 4 Seiten</b><span>Jede weitere Seite CHF 150.–</span></div>
      <div><span class="pb-v"><small>ab CHF</small>1’890.–</span><b>Online-Shop</b><span>Mit TWINT, Karte und Versand</span></div>
      <div><span class="pb-v"><small>CHF</small>25.–<small>/ Monat</small></span><b>Hosting und Domain</b><span>Die ersten 3 Monate CHF 10.–</span></div>
    </div>
    <a class="sv-all" href="preise.html">Zum Preisrechner ''' + ARROW + '''</a>
  </section>'''
    css = r'''
.hv-2nd{color:var(--text);border:1px solid rgba(255,255,255,.28)}
.hv-2nd:hover{border-color:var(--text)}
.hv-facts{list-style:none;display:flex;flex-wrap:wrap;gap:10px 28px;margin:36px 0 0;padding:0;font-size:15px;color:var(--muted)}
.hv-facts li::before{content:"";display:inline-block;width:6px;height:6px;border-radius:50%;background:var(--muted);margin-right:10px;vertical-align:middle}
.pb{padding-top:clamp(100px,12vw,180px);padding-bottom:clamp(100px,12vw,180px);border-top:1px solid var(--line)}
.pb-head{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,5vw,96px);align-items:end}
.pb-head h2{font-size:clamp(40px,4.6vw,80px);line-height:1;font-weight:700;letter-spacing:-.05em}
.pb-head p{font-size:clamp(17px,1.35vw,20px);line-height:1.6;color:#BDBDBD;max-width:42ch}
.pb-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(16px,2vw,28px);margin:clamp(40px,5vw,72px) 0 clamp(32px,4vw,48px)}
.pb-grid > div{display:flex;flex-direction:column;gap:6px;padding:clamp(24px,2.4vw,36px);border:1px solid var(--line);border-radius:20px;background:#191919}
.pb-v{display:flex;align-items:baseline;gap:8px;font-size:clamp(40px,4vw,68px);font-weight:700;letter-spacing:-.05em;line-height:1;margin-bottom:18px;font-variant-numeric:tabular-nums}
.pb-v small{font-size:15px;font-weight:500;letter-spacing:0;color:var(--muted)}
.pb-grid b{font-size:19px;font-weight:600}
.pb-grid span:last-child{font-size:15px;color:var(--muted)}
@media (max-width: 860px){ .pb-head,.pb-grid{grid-template-columns:1fr} .hv-2nd{margin-left:0} }
'''
    main = '\n  ' + hero + '\n\n  ' + STATEMENT + '\n\n  ' + sh + '\n\n  ' + home6.BUILD + '\n\n  ' + price + '\n'
    return main, home6.CSS + svopts.BASE_CSS + sc + css, JS_BASE + sj

def options():
    secs = ''
    css = svopts.BASE_CSS
    js = ''
    for k, f in enumerate(svopts.ALL, 1):
        name, desc, h, c, j = f('opt' + str(k))
        secs += f'<div class="ol pad"><span class="ol-n">Möglichkeit {k}</span><h3>{name}</h3><p>{desc}</p></div>\n' + h + '\n'
        css += c; js += j
    intro = '<section class="oi pad"><h1>Was wir machen: fünf Möglichkeiten</h1><p>Alle fünf zeigen die gleichen sechs Leistungen. Scrollen Sie durch, fahren Sie mit der Maus darüber und sagen Sie mir, welche Nummer es werden soll.</p></section>'
    css += r'''
.oi{padding-top:clamp(140px,16vh,200px);padding-bottom:40px}
.oi h1{font-size:clamp(40px,4.8vw,84px);line-height:1;font-weight:700;letter-spacing:-.05em;max-width:16ch}
.oi p{font-size:19px;line-height:1.6;color:#BDBDBD;max-width:52ch;margin-top:24px}
.ol{margin-top:clamp(80px,9vw,140px);padding-top:28px;padding-bottom:28px;background:#1E1E1E;border-top:1px solid #2E2E2E;border-bottom:1px solid #2E2E2E}
.ol-n{display:inline-block;font-size:13px;font-weight:600;letter-spacing:.06em;text-transform:uppercase;color:#151515;background:#D6D8D7;padding:5px 12px;border-radius:99px}
.ol h3{font-size:clamp(26px,2.4vw,38px);font-weight:700;letter-spacing:-.04em;margin-top:14px}
.ol p{font-size:17px;line-height:1.6;color:#BDBDBD;max-width:70ch;margin-top:8px}
.ol + .svx{padding-top:clamp(56px,6vw,90px)}
'''
    return '\n  ' + intro + '\n' + secs, home6.CSS + css, 'const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;\n' + js
