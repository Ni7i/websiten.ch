# Fünf Möglichkeiten für "Was wir machen". Jede liefert (Name, Beschreibung, HTML, CSS, JS).
from parts import ARROW

SV = [
    ('websites', 'Websites', 'cafe', 'Für Ihren Betrieb gestaltet, fürs Handy gebaut.', 'Gestaltet für Ihren Betrieb und gebaut fürs Handy. Mit Texten, die Ihre Kunden verstehen, und einem Formular, das Anfragen bringt.', ['Firmenwebsites', 'Onepager', 'Relaunch', 'Mehrsprachig']),
    ('shops', 'Online-Shops', 'laden2', 'Mit TWINT, Karte, Rechnung und Versand.', 'Verkaufen mit TWINT, Karte und Rechnung. Der Versand in der Schweiz ist eingerichtet, Produkte und Bestellungen verwalten Sie selbst.', ['Shopify', 'WooCommerce', 'Shop-Umzug', 'B2B-Portal']),
    ('seo', 'Google und SEO', 'restaurant', 'Gefunden werden, wo Ihre Kunden suchen.', 'Damit man Sie findet, wenn jemand in Ihrer Region sucht. Mit Unternehmensprofil, sauberer Technik und Google Ads mit festem Budget.', ['Google Maps', 'Lokale SEO', 'Google Ads', 'Auswertung']),
    ('hosting', 'Domains und Hosting', 'werkstatt', 'Bei Infomaniak in Genf, mit Backups und Updates.', 'Domain, Website und E-Mail bei Infomaniak in Genf. Updates, Backups und Sicherheit übernehmen wir.', ['.ch-Domains', 'E-Mail', 'Backups', 'Updates']),
    ('m365', 'Microsoft 365', 'planung', 'E-Mail, Teams und Dateien für Ihr Team.', 'E-Mail, Teams und Dateien für Ihr Team, sauber eingerichtet und betreut. Neue Leute haben ihr Konto am ersten Tag.', ['Einrichtung', 'E-Mail-Umzug', 'Teams', 'Fernwartung']),
    ('ki', 'KI-Chatbots', 'coiffeur', 'Beantwortet häufige Fragen auf Ihrer Website.', 'Beantwortet häufige Fragen direkt auf Ihrer Website, mit Ihren Informationen. Was er nicht weiss, gibt er an Sie weiter.', ['Ihre Inhalte', 'Mehrsprachig', 'Übergabe an Sie', 'Datenschutz']),
]
IMG = lambda p: '%%I_' + p + '%%'

def head(sid):
    return f'<div class="sv-head"><h2 id="{sid}T">Was wir machen</h2><a class="sv-all" href="leistungen.html">Alle Leistungen {ARROW}</a></div>'

BASE_CSS = r'''
.svx{padding-top:clamp(100px,12vw,180px);padding-bottom:clamp(100px,12vw,180px)}
.sv-head{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap;margin-bottom:clamp(40px,5vw,72px)}
.sv-head h2{font-size:clamp(40px,4.6vw,80px);line-height:1;font-weight:700;letter-spacing:-.05em}
.sv-all{display:inline-flex;align-items:center;gap:12px;font-size:17px;padding-bottom:6px;border-bottom:1px solid var(--text);transition:gap .3s var(--ease)}
.sv-all:hover{gap:18px}
'''

# 1) Grosse Liste, Foto erscheint beim Drüberfahren
def o1(sid='o1'):
    rows = ''.join(f'<li><a href="leistungen.html#{i}"><span class="n">0{k + 1}</span><span class="t">{t}</span><span class="d">{s}</span><span class="a">{ARROW}</span><img class="th" src="{IMG(p)}" alt="" loading="lazy"></a></li>' for k, (i, t, p, s, d, sub) in enumerate(SV))
    html = f'<section class="svx o1 pad" id="{sid}" aria-labelledby="{sid}T">{head(sid)}<ul class="o1-list">{rows}</ul><div class="o1-float" aria-hidden="true"><img alt=""></div></section>'
    css = r'''
.o1-list{list-style:none;margin:0;padding:0;border-top:1px solid var(--line)}
.o1-list li{border-bottom:1px solid var(--line)}
.o1-list a{display:grid;grid-template-columns:56px minmax(0,1fr) minmax(0,1fr) 28px;gap:20px;align-items:center;padding:clamp(22px,2.4vw,34px) 0}
.o1 .n{font-size:14px;color:var(--muted);font-variant-numeric:tabular-nums}
.o1 .t{font-size:clamp(30px,3.6vw,60px);line-height:1;font-weight:700;letter-spacing:-.05em;transition:transform .45s var(--ease),color .25s}
.o1 .d{font-size:17px;color:var(--muted);transition:color .25s}
.o1 .a{justify-self:end;color:var(--muted);transition:transform .35s var(--ease),color .25s}
.o1 .th{display:none}
.o1-list:hover a .t{color:#6E6E6E}
.o1-list a:hover .t{color:var(--text);transform:translateX(14px)}
.o1-list a:hover .d{color:var(--text)}
.o1-list a:hover .a{transform:translateX(4px);color:var(--text)}
.o1-float{position:fixed;left:0;top:0;width:320px;aspect-ratio:4/3;border-radius:14px;overflow:hidden;pointer-events:none;z-index:40;opacity:0;transform:translate(-50%,-50%) scale(.85);transition:opacity .25s,transform .35s var(--ease)}
.o1-float.on{opacity:1;transform:translate(-50%,-50%) scale(1)}
.o1-float img{width:100%;height:100%;object-fit:cover}
@media (max-width: 860px){
  .o1-list a{grid-template-columns:72px minmax(0,1fr) 22px;gap:4px 16px}
  .o1 .n{display:none}
  .o1 .th{display:block;grid-row:1 / span 2;grid-column:1;width:72px;height:72px;object-fit:cover;border-radius:10px}
  .o1 .t{grid-column:2;font-size:28px}
  .o1 .d{grid-column:2;font-size:15px}
  .o1 .a{grid-row:1 / span 2;grid-column:3}
  .o1-float{display:none}
}
'''
    js = r'''
(function(){
  document.querySelectorAll('.o1').forEach(sec => {
    const fl = sec.querySelector('.o1-float'), im = fl.querySelector('img');
    if(!matchMedia('(hover: hover)').matches) return;
    let x = 0, y = 0, tx = 0, ty = 0, raf = 0;
    const mv = () => { x += (tx - x) * .2; y += (ty - y) * .2; fl.style.left = x + 'px'; fl.style.top = y + 'px'; raf = Math.abs(tx - x) + Math.abs(ty - y) > .5 ? requestAnimationFrame(mv) : 0; };
    sec.querySelectorAll('.o1-list a').forEach(a => {
      a.addEventListener('mouseenter', e => { im.src = a.querySelector('.th').src; if(!fl.classList.contains('on')){ x = tx = e.clientX + 200; y = ty = e.clientY; } fl.classList.add('on'); });
      a.addEventListener('mousemove', e => { tx = e.clientX + 200; ty = e.clientY; if(!raf) raf = requestAnimationFrame(mv); });
      a.addEventListener('mouseleave', () => fl.classList.remove('on'));
    });
  });
})();
'''
    return ('Grosse Liste, Foto beim Drüberfahren', 'Ruhig und klar. Die Leistungen stehen gross untereinander. Fährt man über eine Zeile, schwebt neben der Maus ein passendes Foto mit. Auf dem Handy steht ein kleines Foto links.', html, css, js)

# 2) Karten zum Wischen
def o2(sid='o2'):
    cards = ''.join(f'<a class="o2-c" href="leistungen.html#{i}"><span class="o2-img"><img src="{IMG(p)}" alt="" loading="lazy"></span><span class="n">0{k + 1}</span><b>{t}</b><span class="d">{s}</span></a>' for k, (i, t, p, s, d, sub) in enumerate(SV))
    arrows = '<div class="o2-nav"><button type="button" class="o2-prev" aria-label="Zurück"><svg viewBox="0 0 22 14" width="20" height="13" aria-hidden="true"><path d="M21 7H2M8 1L2 7l6 6" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></button><button type="button" class="o2-next" aria-label="Weiter">' + ARROW + '</button></div>'
    html = f'<section class="svx o2 pad" id="{sid}" aria-labelledby="{sid}T"><div class="sv-head"><h2 id="{sid}T">Was wir machen</h2>{arrows}</div><div class="o2-row">{cards}</div><a class="sv-all o2-all" href="leistungen.html">Alle Leistungen {ARROW}</a></section>'
    css = r'''
.o2{overflow:hidden}
.o2-nav{display:flex;gap:10px}
.o2-nav button{width:52px;height:52px;border-radius:50%;border:1px solid var(--line);color:var(--text);display:grid;place-items:center;transition:background .2s,border-color .2s}
.o2-nav button:hover{background:#222;border-color:#444}
.o2-row{display:flex;gap:clamp(16px,1.8vw,26px);overflow-x:auto;scroll-snap-type:x mandatory;scrollbar-width:none;margin-right:calc(var(--pad) * -1);padding-right:var(--pad)}
.o2-row::-webkit-scrollbar{display:none}
.o2-c{flex:none;width:clamp(250px,25vw,370px);scroll-snap-align:start;display:flex;flex-direction:column}
.o2-img{display:block;aspect-ratio:3/4;border-radius:16px;overflow:hidden;background:#222;margin-bottom:18px}
.o2-img img{width:100%;height:100%;object-fit:cover;filter:saturate(.8);transition:transform .8s var(--ease),filter .4s}
.o2-c:hover .o2-img img{transform:scale(1.05);filter:none}
.o2 .n{font-size:13px;color:var(--muted)}
.o2-c b{font-size:clamp(22px,1.9vw,30px);font-weight:700;letter-spacing:-.04em;margin-top:6px}
.o2 .d{font-size:15.5px;line-height:1.5;color:var(--muted);margin-top:6px}
.o2-all{margin-top:clamp(36px,4vw,56px)}
@media (max-width: 860px){ .o2-nav{display:none} .o2-c{width:74vw} }
'''
    js = r'''
(function(){
  document.querySelectorAll('.o2').forEach(sec => {
    const row = sec.querySelector('.o2-row'), w = () => row.querySelector('.o2-c').offsetWidth + 24;
    sec.querySelector('.o2-next').addEventListener('click', () => row.scrollBy({left: w(), behavior: 'smooth'}));
    sec.querySelector('.o2-prev').addEventListener('click', () => row.scrollBy({left: -w(), behavior: 'smooth'}));
  });
})();
'''
    return ('Karten zum Wischen', 'Hohe Bildkarten in einer Reihe, die man seitwärts wischt oder mit den Pfeilen weiterschiebt. Wirkt wie ein Portfolio und ist auf dem Handy sehr angenehm.', html, css, js)

# 3) Aufklappen
def o3(sid='o3'):
    items = ''.join(f'<div class="o3-i{" open" if k == 0 else ""}"><button type="button" class="o3-b" aria-expanded="{"true" if k == 0 else "false"}"><span class="n">0{k + 1}</span><span class="t">{t}</span><span class="pl" aria-hidden="true"></span></button><div class="o3-p"><div class="o3-in"><div><p>{d}</p><ul>' + ''.join(f'<li>{x}</li>' for x in sub) + f'</ul><a class="sv-all" href="leistungen.html#{i}">Mehr zu {t} {ARROW}</a></div><span class="o3-img"><img src="{IMG(p)}" alt="" loading="lazy"></span></div></div></div>' for k, (i, t, p, s, d, sub) in enumerate(SV))
    html = f'<section class="svx o3 pad" id="{sid}" aria-labelledby="{sid}T">{head(sid)}<div class="o3-list">{items}</div></section>'
    css = r'''
.o3-list{border-top:1px solid var(--line)}
.o3-i{border-bottom:1px solid var(--line)}
.o3-b{width:100%;display:grid;grid-template-columns:56px 1fr 28px;align-items:center;gap:20px;padding:clamp(22px,2.4vw,32px) 0;text-align:left;color:var(--text)}
.o3 .n{font-size:14px;color:var(--muted)}
.o3 .t{font-size:clamp(28px,3.2vw,54px);line-height:1;font-weight:700;letter-spacing:-.05em;transition:color .25s}
.o3-i:not(.open) .t{color:#8A8A8A}
.o3-b:hover .t{color:var(--text)}
.pl{position:relative;width:22px;height:22px;justify-self:end}
.pl::before,.pl::after{content:"";position:absolute;left:0;right:0;top:50%;height:1.6px;background:currentColor;transition:transform .35s var(--ease)}
.pl::after{transform:rotate(90deg)}
.o3-i.open .pl::after{transform:rotate(0)}
.o3-p{display:grid;grid-template-rows:0fr;transition:grid-template-rows .5s var(--ease)}
.o3-i.open .o3-p{grid-template-rows:1fr}
.o3-in{overflow:hidden;min-height:0;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,4vw,72px);padding-left:76px}
.o3-in > div{padding-bottom:36px}
.o3-in p{font-size:clamp(17px,1.4vw,21px);line-height:1.6;color:#BDBDBD;max-width:44ch}
.o3-in ul{list-style:none;display:flex;flex-wrap:wrap;gap:8px;margin:22px 0 28px;padding:0}
.o3-in li{font-size:14.5px;color:var(--muted);border:1px solid var(--line);border-radius:99px;padding:7px 14px}
.o3-img{display:block;aspect-ratio:16/10;border-radius:14px;overflow:hidden;margin-bottom:36px}
.o3-img img{width:100%;height:100%;object-fit:cover}
@media (max-width: 860px){ .o3-b{grid-template-columns:1fr 24px} .o3 .n{display:none} .o3-in{grid-template-columns:1fr;padding-left:0} .o3-img{order:-1;margin-bottom:20px} }
'''
    js = r'''
(function(){
  document.querySelectorAll('.o3').forEach(sec => {
    const items = [...sec.querySelectorAll('.o3-i')];
    items.forEach(it => it.querySelector('.o3-b').addEventListener('click', () => { const open = !it.classList.contains('open'); items.forEach(o => { o.classList.remove('open'); o.querySelector('.o3-b').setAttribute('aria-expanded', 'false'); }); if(open){ it.classList.add('open'); it.querySelector('.o3-b').setAttribute('aria-expanded', 'true'); } }));
  });
})();
'''
    return ('Aufklappen', 'Sechs Zeilen, eine ist offen. Klickt man eine andere an, klappt sie auf und zeigt Text, Stichworte und ein Foto. Viel Inhalt auf wenig Platz.', html, css, js)

# 4) Bento-Raster
def o4(sid='o4'):
    def tile(k, cls):
        i, t, p, s, d, sub = SV[k]
        photo = cls.startswith('ph')
        img = f'<img src="{IMG(p)}" alt="" loading="lazy">' if photo else ''
        return f'<a class="o4-t {cls}" href="leistungen.html#{i}">{img}<span class="o4-tx"><span class="n">0{k + 1}</span><b>{t}</b><span class="d">{d if photo else s}</span></span><span class="o4-a">{ARROW}</span></a>'
    html = f'<section class="svx o4 pad" id="{sid}" aria-labelledby="{sid}T">{head(sid)}<div class="o4-grid">' + tile(0, 'ph big') + tile(1, 'ph wide') + tile(2, 'tx') + tile(3, 'tx') + tile(4, 'tx half') + tile(5, 'tx half') + '</div></section>'
    css = r'''
.o4-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));grid-auto-rows:clamp(190px,17vw,260px);gap:clamp(12px,1.4vw,20px)}
.o4-t{position:relative;border-radius:20px;overflow:hidden;background:#1E1E1E;border:1px solid #262626;display:flex;flex-direction:column;justify-content:flex-end;padding:clamp(20px,2vw,30px);isolation:isolate;transition:border-color .25s,background .25s}
.o4-t:hover{border-color:#3A3A3A;background:#222}
.o4-t.big{grid-column:span 2;grid-row:span 2}
.o4-t.wide,.o4-t.half{grid-column:span 2}
.o4-t img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;z-index:-2;transition:transform .9s var(--ease)}
.o4-t.ph::after{content:"";position:absolute;inset:0;z-index:-1;background:linear-gradient(0deg,rgba(14,14,14,.88) 0%,rgba(14,14,14,.25) 55%,rgba(14,14,14,0) 80%)}
.o4-t:hover img{transform:scale(1.04)}
.o4 .n{font-size:13px;color:var(--muted)}
.o4-t b{display:block;font-size:clamp(22px,2vw,34px);line-height:1.05;font-weight:700;letter-spacing:-.04em;margin-top:6px}
.o4-t.big b{font-size:clamp(32px,3.4vw,56px)}
.o4 .d{display:block;font-size:15.5px;line-height:1.5;color:#B5B5B5;margin-top:8px;max-width:42ch}
.o4-a{position:absolute;right:clamp(18px,2vw,28px);top:clamp(18px,2vw,26px);width:40px;height:40px;border-radius:50%;display:grid;place-items:center;background:rgba(255,255,255,.08);transition:transform .35s var(--ease),background .25s}
.o4-t:hover .o4-a{transform:rotate(-45deg);background:rgba(255,255,255,.16)}
@media (max-width: 860px){ .o4-grid{grid-template-columns:1fr;grid-auto-rows:auto} .o4-t,.o4-t.big,.o4-t.wide,.o4-t.half{grid-column:auto;grid-row:auto;min-height:150px} .o4-t.ph{min-height:260px} }
'''
    return ('Bento-Raster', 'Ein Raster aus grossen und kleinen Flächen. Websites und Online-Shops bekommen grosse Bilder, die übrigen Leistungen ruhige Textflächen. Die Hauptleistungen fallen so sofort auf.', html, css, '')

# 5) Nur Typografie
def o5(sid='o5'):
    cells = ''.join(f'<a class="o5-c" href="leistungen.html#{i}"><span class="o5-n">0{k + 1}</span><b>{t}</b><span class="d">{d}</span><span class="o5-s">' + ' · '.join(sub) + '</span></a>' for k, (i, t, p, s, d, sub) in enumerate(SV))
    html = f'<section class="svx o5 pad" id="{sid}" aria-labelledby="{sid}T">{head(sid)}<div class="o5-grid">{cells}</div></section>'
    css = r'''
.o5-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));column-gap:clamp(24px,3vw,56px)}
.o5-c{display:flex;flex-direction:column;padding:28px 0 clamp(40px,4vw,64px);border-top:1px solid var(--line);transition:border-color .3s}
.o5-c:hover{border-color:var(--text)}
.o5-n{font-size:clamp(56px,5.6vw,96px);line-height:.9;font-weight:700;letter-spacing:-.05em;color:#3A3A3A;transition:color .3s}
.o5-c:hover .o5-n{color:var(--text)}
.o5-c b{font-size:clamp(22px,1.9vw,30px);font-weight:700;letter-spacing:-.04em;margin-top:22px}
.o5 .d{font-size:16px;line-height:1.6;color:#B5B5B5;margin-top:12px;max-width:38ch}
.o5-s{font-size:14px;color:var(--muted);margin-top:16px}
@media (max-width: 1000px){ .o5-grid{grid-template-columns:repeat(2,minmax(0,1fr))} }
@media (max-width: 640px){ .o5-grid{grid-template-columns:1fr} }
'''
    return ('Nur Schrift, ohne Fotos', 'Drei Spalten mit grossen Nummern, Titel, zwei Sätzen und Stichworten. Sehr ruhig und seriös. Fährt man darüber, wird die Nummer weiss und die Linie hell.', html, css, '')

ALL = [o1, o2, o3, o4, o5]
