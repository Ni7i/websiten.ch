# Startseite nach dem alten Konzept (index 6), mit den später gewünschten Verbesserungen
import re, home3
from grey import grey
from parts import ARROW, LI

DESC = 'Websites, Online-Shops und Hosting für Schweizer KMU. Mit festem Preis, Domains und Hosting in der Schweiz.'

_old = open('legacy_index6.html').read()
_css = re.findall(r'<style>(.*?)</style>', _old, re.S)[1]
_js = re.findall(r'<script>(.*?)</script>', _old, re.S)[1]

# Einstieg und Text mit "Mehr über uns" genau wie im alten Konzept
HERO = _old[_old.index('<section class="hero pad"'):_old.index('<section class="build"')].rstrip()
# LinkedIn neben "Ganze Seite lesen"
HERO = HERO.replace('<a class="ax-link" href="ueber-uns.html">', '<a class="ax-link" href="' + LI + '">LinkedIn ' + ARROW + '</a><a class="ax-link" href="ueber-uns.html">', 1)

SV = [
    ('websites', 'Websites', 'cafe', 'Gestaltet für Ihren Betrieb und gebaut fürs Handy. Mit Texten, die Ihre Kunden verstehen, und einem Formular, das Anfragen bringt.', ['Firmenwebsites', 'Onepager', 'Relaunch', 'Mehrsprachig']),
    ('shops', 'Online-Shops', 'laden2', 'Verkaufen mit TWINT, Karte und Rechnung. Versand in der Schweiz ist eingerichtet, Produkte und Bestellungen verwalten Sie selbst.', ['Shopify', 'WooCommerce', 'Shop-Umzug', 'B2B-Portal']),
    ('seo', 'Google und SEO', 'restaurant', 'Damit man Sie findet, wenn jemand in Ihrer Region sucht. Mit Unternehmensprofil, sauberer Technik und Google Ads mit festem Budget.', ['Google Maps', 'Lokale SEO', 'Google Ads', 'Auswertung']),
    ('hosting', 'Hosting in Genf', 'werkstatt', 'Domain, Website und E-Mail bei Infomaniak in Genf. Wir machen Updates, Backups und Sicherheit, Sie müssen sich um nichts kümmern.', ['.ch-Domains', 'E-Mail', 'Backups', 'Updates']),
    ('m365', 'Microsoft 365', 'planung', 'E-Mail, Teams und Dateien für Ihr Team, sauber eingerichtet. Neue Leute haben ihr Konto am ersten Tag.', ['Einrichtung', 'E-Mail-Umzug', 'Teams', 'Fernwartung']),
    ('ki', 'KI-Chatbots', 'coiffeur', 'Beantwortet häufige Fragen direkt auf Ihrer Website, mit Ihren Informationen. Was er nicht weiss, gibt er an Sie weiter.', ['Ihre Inhalte', 'Mehrsprachig', 'Übergabe an Sie', 'Datenschutz']),
]
from parts import MARK_LIGHT as _ML, MARK_DARK as _MD
_imgs = ''.join('<image class="sv2-im" data-i="%d" href="%%%%I_%s%%%%" x="12" y="10" width="174" height="188" preserveAspectRatio="xMidYMid slice" opacity="%d"/>' % (k, p, 1 if k == 0 else 0) for k, (_, _, p, _, _) in enumerate(SV))
_items = ''.join(f'<li class="sv2-i{" on" if k == 0 else ""}" data-i="{k}"><span class="n">0{k + 1}</span><h3>{t}</h3><p>{d}</p><ul>' + ''.join(f'<li>{x}</li>' for x in subs) + f'</ul><a href="leistungen.html#{i}">Mehr zu {t} ' + ARROW + '</a></li>' for k, (i, t, p, d, subs) in enumerate(SV))
SERVICES = """<section class="sv2 pad" id="leistungen" aria-labelledby="sv2T">
    <div class="sv2-grid">
      <div class="sv2-left"><div class="sv2-stick">
        <h2 id="sv2T">Was wir machen</h2>
        <svg class="sv2-mask" viewBox="12 10 174 188" aria-hidden="true"><defs><clipPath id="sv2cp"><path d=\"""" + _ML + """\"/><path d=\"""" + _MD + """\"/></clipPath></defs><g clip-path="url(#sv2cp)"><rect x="0" y="0" width="200" height="210" fill="#222"/>""" + _imgs + """</g></svg>
        <a class="wm-all" href="leistungen.html">Alle Leistungen """ + ARROW + """</a>
      </div></div>
      <ol class="sv2-list">""" + _items + """</ol>
    </div>
  </section>"""

# Neues Logo auch im Einstieg und im Firmenblock
from parts import MARK_LIGHT, MARK_DARK
HERO = re.sub(r'<svg class="hero-art" id="heroArt"[^>]*>.*?</svg>', '<svg class="hero-art" id="heroArt" viewBox="12 10 174 188" aria-hidden="true"><g class="gd"><g><path class="pd" d="' + MARK_DARK + '"/></g></g><g class="gl"><g><path class="pl" d="' + MARK_LIGHT + '"/></g></g></svg>', HERO, count=1, flags=re.S)
HERO = re.sub(r'(<div class="ax-co">\s*)<svg viewBox="12 10 174 188"[^>]*>.*?</svg>', lambda m: m.group(1) + '<svg viewBox="12 10 174 188" aria-hidden="true"><path fill="#4A5350" d="' + MARK_LIGHT + '"/><path fill="#ECF0EE" d="' + MARK_DARK + '"/></svg>', HERO, count=1, flags=re.S)
BUILD = home3.BUILD.replace('fill="#83AA8C"', 'fill="#5B6461"').replace('fill="#4F695A"', 'fill="#ECF0EE"')


# Film direkt nach dem Einstieg
FILM = """<section class="film pad" aria-label="Kurzfilm websiten.ch">
    <div class="film-box">
      <video id="film" muted playsinline loop preload="metadata" poster="%%FILMPOSTER%%"><source src="assets/websiten-film.mp4" type="video/mp4"></video>
      <button class="film-btn" id="filmBtn" type="button" aria-label="Film pausieren"><svg class="i-pause" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14M16 5v14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg><svg class="i-play" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg></button>
    </div>
  </section>"""
_i = HERO.index('<section class="statement')
HERO = HERO[:_i] + FILM + '\n\n  ' + HERO[_i:]

MAIN = '\n  ' + HERO + '\n\n  ' + BUILD + '\n\n  ' + SERVICES + '\n'

# Alte Seiten-Styles ohne die alte Passage (die neue mit echtem Foto kommt dazu)
_a = _css.index('.build{height:440vh}'); _b = _css.index('.teaser{')
OLD_CSS = _css[:_a] + _css[_b:]

CSS = OLD_CSS + r'''
/* Kurzfilm */
.film{padding-top:clamp(24px,4vw,64px)}
.film-box{position:relative;aspect-ratio:16/9;max-width:100%;border-radius:22px;overflow:hidden;background:#151515;border:1px solid var(--line)}
.film-box video{display:block;width:100%;height:100%;object-fit:cover}
.film-btn{position:absolute;right:18px;bottom:18px;width:46px;height:46px;border-radius:50%;display:grid;place-items:center;color:var(--text);background:rgba(21,21,21,.55);border:1px solid rgba(255,255,255,.18);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);opacity:.75;transition:opacity .2s,background .2s}
.film-btn:hover{opacity:1;background:rgba(21,21,21,.8)}
.film-btn svg{width:20px;height:20px}
.film-btn .i-play,.film-box.paused .film-btn .i-pause{display:none}
.film-box.paused .film-btn .i-play{display:block}
@media (max-width: 860px){ .film-box{border-radius:14px} .film-btn{right:10px;bottom:10px;width:40px;height:40px} }
.hero-art .pl{fill:#4A504E}.hero-art .pd{fill:#2A2F2D}
/* Was wir machen: Logo als Bildfenster bleibt stehen, rechts laufen die Leistungen */
.sv2{padding-top:clamp(100px,12vw,180px);padding-bottom:clamp(60px,8vw,120px)}
.sv2-grid{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(40px,7vw,140px)}
.sv2-stick{position:sticky;top:clamp(90px,12vh,130px)}
.sv2 h2{font-size:clamp(40px,4.6vw,80px);line-height:1;font-weight:700;letter-spacing:-.05em}
.sv2-mask{display:block;width:min(100%,calc((100vh - 360px) * 174 / 188));height:auto;margin:clamp(28px,4vh,48px) 0 clamp(24px,3vh,40px)}
.sv2-im{transition:opacity .6s ease}
.sv2-list{list-style:none;padding:clamp(20px,8vh,120px) 0 0;margin:0}
.sv2-i{min-height:62vh;padding:28px 0;border-top:1px solid var(--line);opacity:.32;transition:opacity .45s}
.sv2-i.on{opacity:1}
.sv2-i .n{font-size:14px;color:var(--muted);font-variant-numeric:tabular-nums}
.sv2-i h3{font-size:clamp(34px,3.6vw,60px);line-height:1;font-weight:700;letter-spacing:-.05em;margin-top:14px}
.sv2-i p{font-size:clamp(17px,1.3vw,20px);line-height:1.6;color:#BDBDBD;margin-top:22px;max-width:40ch}
.sv2-i ul{list-style:none;display:flex;flex-wrap:wrap;gap:8px 22px;margin:22px 0 0;padding:0;font-size:15.5px;color:var(--muted)}
.sv2-i ul li::before{content:"";display:inline-block;width:5px;height:5px;border-radius:50%;background:currentColor;margin-right:9px;vertical-align:middle;opacity:.7}
.sv2-i a{display:inline-flex;align-items:center;gap:12px;margin-top:28px;font-size:16.5px;padding-bottom:5px;border-bottom:1px solid var(--text);transition:gap .3s var(--ease)}
.sv2-i a:hover{gap:18px}
.wm-all{display:inline-flex;align-items:center;gap:12px;font-size:17px;padding-bottom:6px;border-bottom:1px solid var(--text)}
@media (max-width: 860px){
  .sv2-grid{grid-template-columns:1fr;gap:0}
  .sv2-stick{position:static}
  .sv2-mask{width:min(72vw,300px);margin:32px 0 8px}
  .sv2-left .wm-all{display:none}
  .sv2-list{padding-top:24px}
  .sv2-i{min-height:0;opacity:1;padding:32px 0}
}
.ax-in .ax-link + .ax-link{grid-column:auto}
@media (max-width: 860px){
  .wm-list a{grid-template-columns:minmax(0,1fr) 26px;gap:8px 12px}
  .wm-list .d{grid-column:1;font-size:15.5px}
  .wm-list .a{grid-row:1 / span 2;grid-column:2}
}
''' + home3.BUILD_CSS

# Alte Skripte für Einstieg und "Mehr über uns", danach die neue Passage
_a = _js.index('/* Hero:'); _b = _js.index('/* Scroll-Passage')
JS = '''const MAP = %%MAP%%;
/* Was wir machen: das Element in der Bildschirmmitte ist aktiv, das Foto im Logo wechselt mit */
(function(){
  const items = [...document.querySelectorAll('.sv2-i')], ims = [...document.querySelectorAll('.sv2-im')];
  if(!items.length) return;
  let cur = 0, tk = false;
  const set = k => { if(k === cur) return; cur = k; items.forEach((e, i) => e.classList.toggle('on', i === k)); ims.forEach((e, i) => e.setAttribute('opacity', i === k ? 1 : 0)); };
  const upd = () => { tk = false; const mid = innerHeight * .5; let best = 0, bd = 1e9; items.forEach((e, i) => { const r = e.getBoundingClientRect(), d = Math.abs(r.top + Math.min(r.height, innerHeight * .4) / 2 - mid); if(d < bd){ bd = d; best = i; } }); set(best); };
  addEventListener('scroll', () => { if(!tk){ tk = true; requestAnimationFrame(upd); } }, {passive: true}); upd();
})();
/* Kurzfilm: läuft, solange er sichtbar ist; Knopf zum Anhalten */
(function(){
  const v = document.getElementById('film'), box = v && v.closest('.film-box'), btn = document.getElementById('filmBtn');
  if(!v) return;
  let userPaused = matchMedia('(prefers-reduced-motion: reduce)').matches, visible = false;
  const sync = () => { box.classList.toggle('paused', v.paused); btn.setAttribute('aria-label', v.paused ? 'Film abspielen' : 'Film pausieren'); };
  const go = () => { if(visible && !userPaused){ const p = v.play(); if(p) p.catch(() => {}); } else v.pause(); };
  v.addEventListener('play', sync); v.addEventListener('pause', sync); sync();
  btn.addEventListener('click', () => { userPaused = !v.paused; if(userPaused) v.pause(); else { userPaused = false; v.play(); } });
  new IntersectionObserver(es => es.forEach(e => { visible = e.isIntersecting; go(); }), {threshold: .35}).observe(v);
})();
const MARK_L = '%%ML%%', MARK_D = '%%MD%%';
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
''' + _js[_a:_b] + home3.BUILD_JS

# Alles in Grau statt Grün
CSS = grey(CSS)
JS = grey(JS)
MAIN = grey(MAIN)
