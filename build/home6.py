# Startseite: altes Konzept, Film als Hintergrund im Einstieg, Leistungen als Bildkacheln
import re, home3
from grey import grey
from parts import ARROW, LI, MARK_LIGHT, MARK_DARK

DESC = 'Websites, Online-Shops und Hosting für Schweizer KMU. Mit festem Preis, Domains und Hosting in der Schweiz.'

_old = open('legacy_index6.html').read()
_css = re.findall(r'<style>(.*?)</style>', _old, re.S)[1]
_js = re.findall(r'<script>(.*?)</script>', _old, re.S)[1]

PAUSE = '<svg class="i-pause" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14M16 5v14" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/></svg><svg class="i-play" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>'

HERO = '''<section class="hero hv pad" id="hero" aria-label="Einstieg">
    <video class="hv-vid" id="heroVid" muted playsinline autoplay loop preload="auto" poster="%%HEROPOSTER%%" aria-hidden="true"><source media="(max-width: 860px)" src="assets/websiten-hero-m.mp4" type="video/mp4"><source src="assets/websiten-hero.mp4" type="video/mp4"></video>
    <div class="hv-shade" aria-hidden="true"></div>
    <div class="hero-copy">
      <h1><span>Websites für </span><span>Schweizer KMU. </span><span class="quiet">Gebaut, damit Ihr </span><span class="quiet">Telefon klingelt.</span></h1>
      <div class="hero-row">
        <a class="btn btn-sage" href="kontakt.html">Projekt anfragen ''' + ARROW + '''</a>
        <p>Design, Technik und Betreuung aus einer Hand. Domains und Hosting in der Schweiz.</p>
      </div>
    </div>
    <button class="vid-btn" id="heroBtn" type="button" aria-label="Hintergrundfilm anhalten">''' + PAUSE + '''</button>
  </section>'''

# Text mit "Mehr über uns" aus dem alten Konzept
STATEMENT = _old[_old.index('<section class="statement pad">'):_old.index('<section class="build"')].rstrip()
STATEMENT = STATEMENT.replace('Und für alles, was mit Ihrem Auftritt im Netz zu tun hat, brauchen Sie nur eine Telefonnummer.', 'Und für alles, was mit Ihrem Auftritt im Netz zu tun hat, haben Sie eine Ansprechperson.')
STATEMENT = STATEMENT.replace('<a class="ax-link" href="ueber-uns.html">', '<a class="ax-link" href="' + LI + '">LinkedIn ' + ARROW + '</a><a class="ax-link" href="ueber-uns.html">', 1)
STATEMENT = re.sub(r'(<div class="ax-co">\s*)<svg viewBox="12 10 174 188"[^>]*>.*?</svg>', lambda m: m.group(1) + '<svg viewBox="12 10 174 188" aria-hidden="true"><path fill="#4A4A4A" d="' + MARK_LIGHT + '"/><path fill="#ECECEC" d="' + MARK_DARK + '"/></svg>', STATEMENT, count=1, flags=re.S)
assert 'Telefonnummer' not in STATEMENT

BUILD = home3.BUILD.replace('fill="#83AA8C"', 'fill="#5B5B5B"').replace('fill="#4F695A"', 'fill="#ECECEC"')

SV = [
    ('websites', 'Websites', 'cafe', 'Für Ihren Betrieb gestaltet, fürs Handy gebaut.'),
    ('shops', 'Online-Shops', 'laden2', 'Mit TWINT, Karte, Rechnung und Versand.'),
    ('seo', 'Google und SEO', 'restaurant', 'Gefunden werden, wo Ihre Kunden suchen.'),
    ('hosting', 'Hosting in Genf', 'werkstatt', 'Domains, E-Mail, Backups und Updates.'),
    ('m365', 'Microsoft 365', 'planung', 'E-Mail, Teams und Dateien für Ihr Team.'),
    ('ki', 'KI-Chatbots', 'coiffeur', 'Beantwortet häufige Fragen auf Ihrer Website.'),
]
TILES = ''.join(f'<li><a class="st" href="leistungen.html#{i}"><span class="st-img"><img src="%%I_{p}%%" alt="" loading="lazy"></span><span class="st-tx"><span class="n">0{k + 1}</span><span class="st-t">{t}</span><span class="st-d">{d}</span></span><span class="st-ar">{ARROW}</span></a></li>' for k, (i, t, p, d) in enumerate(SV))
SERVICES = '''<section class="svt pad" id="leistungen" aria-labelledby="svtT">
    <div class="svt-head"><h2 id="svtT">Was wir machen</h2><a class="wm-all" href="leistungen.html">Alle Leistungen ''' + ARROW + '''</a></div>
    <ul class="svt-grid">''' + TILES + '''</ul>
  </section>'''

MAIN = '\n  ' + HERO + '\n\n  ' + STATEMENT + '\n\n  ' + BUILD + '\n\n  ' + SERVICES + '\n'

_a = _css.index('.build{height:440vh}'); _b = _css.index('.teaser{')
CSS = _css[:_a] + _css[_b:] + r'''
/* Einstieg mit Film im Hintergrund */
.hv{position:relative;min-height:max(100svh,640px);justify-content:center;background:#151515;isolation:isolate}
.hv-vid{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:0% 50%;z-index:-2}
.hv h1{font-size:clamp(44px,5.4vw,104px)}
.hv-shade{position:absolute;inset:0;z-index:-1;background:linear-gradient(90deg,#151515 0%,rgba(21,21,21,.92) 26%,rgba(21,21,21,.35) 52%,rgba(21,21,21,0) 70%),linear-gradient(0deg,#151515 0%,rgba(21,21,21,0) 22%)}
.hv .hero-copy{max-width:min(54vw,920px)}
.vid-btn{position:absolute;right:var(--pad);bottom:clamp(24px,4vh,48px);width:44px;height:44px;border-radius:50%;display:grid;place-items:center;color:var(--text);background:rgba(21,21,21,.5);border:1px solid rgba(255,255,255,.18);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);opacity:.6;transition:opacity .2s}
.vid-btn:hover{opacity:1}
.vid-btn svg{width:18px;height:18px}
.vid-btn .i-play,.paused .vid-btn .i-pause{display:none}
.paused .vid-btn .i-play{display:block}

/* Was wir machen: sechs Bildkacheln */
.svt{padding-top:clamp(100px,12vw,180px);padding-bottom:clamp(100px,12vw,180px)}
.svt-head{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap}
.svt-head h2{font-size:clamp(40px,4.6vw,80px);line-height:1;font-weight:700;letter-spacing:-.05em}
.wm-all{display:inline-flex;align-items:center;gap:12px;font-size:17px;padding-bottom:6px;border-bottom:1px solid var(--text)}
.svt-grid{list-style:none;margin:clamp(40px,5vw,72px) 0 0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(28px,3vw,48px) clamp(16px,2vw,28px)}
.st{position:relative;display:block}
.st-img{display:block;aspect-ratio:4/3;border-radius:14px;overflow:hidden;background:#222}
.st-img img{width:100%;height:100%;object-fit:cover;display:block;filter:saturate(.75) brightness(.92);transform:scale(1.001);transition:transform .8s var(--ease),filter .5s}
.st:hover .st-img img{transform:scale(1.05);filter:none}
.st-tx{display:grid;grid-template-columns:auto 1fr;column-gap:14px;align-items:baseline;padding:18px 40px 0 0}
.st .n{font-size:13px;color:var(--muted);font-variant-numeric:tabular-nums}
.st-t{font-size:clamp(22px,1.9vw,30px);line-height:1.1;font-weight:700;letter-spacing:-.04em}
.st-d{grid-column:2;font-size:15.5px;line-height:1.5;color:var(--muted);margin-top:6px}
.st-ar{position:absolute;right:0;top:calc(100% - 52px);color:var(--muted);transition:transform .35s var(--ease),color .2s}
.st:hover .st-ar{transform:translateX(4px);color:var(--text)}
@media (max-width: 1000px){ .svt-grid{grid-template-columns:repeat(2,minmax(0,1fr))} }
@media (max-width: 860px){
  .hv{justify-content:flex-end;padding-top:56vh;padding-bottom:48px}
  .hv-vid{object-position:50% 30%;height:72%}
  .hv-shade{background:linear-gradient(0deg,#151515 30%,rgba(21,21,21,.6) 45%,rgba(21,21,21,0) 62%)}
  .hv .hero-copy{max-width:none}
  .vid-btn{top:calc(env(safe-area-inset-top,0px) + 84px);bottom:auto;right:16px;width:38px;height:38px}
  .svt-grid{grid-template-columns:1fr}
}
''' + home3.BUILD_CSS

_ax = _js[_js.index('/* Mehr über uns'):_js.index('/* Scroll-Passage')]
JS = '''const MAP = %%MAP%%;
const MARK_L = '%%ML%%', MARK_D = '%%MD%%';
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
/* Film im Einstieg: läuft, solange sichtbar; Knopf zum Anhalten */
(function(){
  const v = document.getElementById('heroVid'), sec = document.getElementById('hero'), btn = document.getElementById('heroBtn');
  if(!v) return;
  /* Handy: eigenes Vorschaubild, passend zum Handy-Film (Ausschnitt ums Logo) */
  if(matchMedia('(max-width: 860px)').matches) v.poster = 'assets/img/hero-poster-m.jpg';
  let userPaused = reduce, visible = true;
  const sync = () => { sec.classList.toggle('paused', v.paused); btn.setAttribute('aria-label', v.paused ? 'Hintergrundfilm abspielen' : 'Hintergrundfilm anhalten'); };
  const go = () => { if(visible && !userPaused){ const p = v.play(); if(p) p.catch(() => {}); } else v.pause(); };
  v.addEventListener('play', sync); v.addEventListener('pause', sync);
  btn.addEventListener('click', () => { userPaused = !v.paused; go(); });
  new IntersectionObserver(es => es.forEach(e => { visible = e.isIntersecting; go(); }), {threshold: .05}).observe(sec);
  if(reduce) v.removeAttribute('autoplay');
  go(); sync();
})();
''' + _ax + home3.BUILD_JS

CSS = grey(CSS); JS = grey(JS); MAIN = grey(MAIN)
