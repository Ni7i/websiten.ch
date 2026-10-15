import home3
from parts import ARROW

DESC = 'Websites und Online-Shops für Schweizer KMU. Fester Preis, eine Ansprechperson, Server bei Infomaniak in Genf.'

_c = home3.CSS
CAFE_CSS = _c[_c.index('/* Café Linde'):_c.index('/* Musterseiten')]
MOCK_CSS = _c[_c.index('/* Gemeinsame Basis der Muster */'):_c.index('/* Drei Zahlen */')]

SV = [
    ('websites', 'Websites', 'Gestaltet für Ihren Betrieb, gebaut fürs Handy, mit Texten, die Ihre Kunden verstehen.'),
    ('shops', 'Online-Shops', 'Mit TWINT, Rechnung und Versand in der Schweiz. Sie verwalten alles selbst.'),
    ('seo', 'Google und SEO', 'Damit man Sie findet, wenn jemand in Ihrer Region sucht.'),
    ('hosting', 'Domains und Hosting', 'Bei Infomaniak in Genf. Mit Updates, Backups und E-Mail.'),
    ('m365', 'Microsoft 365 und IT', 'E-Mail, Teams und Dateien für Ihr Team, eingerichtet und betreut.'),
    ('ki', 'KI-Chatbots', 'Beantwortet häufige Fragen direkt auf Ihrer Website, mit Ihren Informationen.'),
]
SV_HTML = ''.join(f'<li><a href="leistungen.html#{i}"><span class="s-t">{t}</span><span class="s-d">{d}</span><span class="s-a">{ARROW}</span></a></li>' for i, t, d in SV)

EX = [
    ('baeckerei-brunner.ch', home3.MOCK_A, 'Bäckerei', '5 Seiten, Bestellformular'),
    ('salon-nord.ch', home3.MOCK_B, 'Coiffeur', '4 Seiten, Online-Termine'),
    ('sonne-aarau.ch', home3.MOCK_C, 'Restaurant', '6 Seiten, Tagesmenü, Reservation'),
    ('lumen-leuchten.ch', home3.MOCK_D, 'Laden mit Shop', 'Online-Shop mit TWINT'),
]
EX_HTML = ''.join(f'<figure class="ex rv"><div class="fr"><div class="fr-bar"><i></i><i></i><i></i><span>{u}</span></div>{m}</div><figcaption><b>{t}</b><span>{d}</span></figcaption></figure>' for u, m, t, d in EX)

MAIN = '''
  <section class="h pad" id="hero">
    <div class="h-copy">
      <h1>Websites und Online-Shops für Schweizer KMU.</h1>
      <div class="h-side">
        <p>Gestaltet, gebaut und betreut von einer Ansprechperson. Mit festem Preis und Servern in Genf.</p>
        <div class="h-acts"><a class="b-dark" href="kontakt.html">Termin wählen ''' + ARROW + '''</a><a class="b-text" href="#beispiele">Beispiele ansehen</a></div>
      </div>
    </div>
    <div class="h-stage" id="hStage">
      <div class="fr fr-hero" id="hFrame"><div class="fr-bar"><i></i><i></i><i></i><span>cafe-linde.ch</span></div><div class="h-site">''' + home3.CAFE + '''</div></div>
      <p class="h-cap">Beispiel: Website für ein Café in Baden. Auf dem Handy ordnet sie sich von selbst neu.</p>
    </div>
  </section>

  <section class="facts pad" aria-label="Wie wir arbeiten">
    <div class="f-grid">
      <div class="rv"><span class="n">01</span><h2>Fester Preis</h2><p>Sie kennen den Preis, bevor wir anfangen. Die Offerte gilt.</p></div>
      <div class="rv"><span class="n">02</span><h2>Eine Ansprechperson</h2><p>Vom ersten Gespräch bis lange nach dem Start. Kein Ticketsystem.</p></div>
      <div class="rv"><span class="n">03</span><h2>Server in Genf</h2><p>Domains, Hosting und E-Mail bei Infomaniak. Ihre Daten bleiben in der Schweiz.</p></div>
    </div>
    ''' + home3.AX + '''
  </section>

  <section class="svs pad" id="leistungen" aria-labelledby="svT">
    <div class="svs-head"><h2 id="svT">Was wir machen</h2><a class="b-text" href="leistungen.html">Alle Leistungen</a></div>
    <ul class="svs-list">''' + SV_HTML + '''</ul>
  </section>

  ''' + home3.BUILD + '''

  <section class="exs pad" id="beispiele" aria-labelledby="exT">
    <div class="svs-head"><h2 id="exT">Beispiele</h2><p>Vier Musterseiten für Branchen, mit denen wir oft arbeiten. Die Betriebe sind erfunden, Ihre Website gestalten wir eigens für Sie.</p></div>
    <div class="ex-grid">''' + EX_HTML + '''</div>
  </section>

  <section class="end pad" id="kontakt-cta" aria-labelledby="endT">
    <h2 id="endT">Reden wir über Ihre Website.</h2>
    <p>15 Minuten am Telefon oder per Video, gratis. Danach wissen Sie, was es kostet und wie lange es dauert.</p>
    <div class="end-acts"><a class="b-dark" href="kontakt.html">Termin wählen ''' + ARROW + '''</a><span class="end-mail">hallo@websiten.ch</span></div>
  </section>
'''

CSS = r'''
:root{--l-bg:#F4F5F2;--l-ink:#0E1513;--l-mut:#5B6560;--l-ln:#DCE1DB;--l-g:#4F695A;--l-gl:#83AA8C;--l-btn:#16241E;--disp:"Archivo","Arial Narrow",sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace}
.h,.facts,.svs,.exs{background:var(--l-bg);color:var(--l-ink)}
.b-dark{display:inline-flex;align-items:center;gap:12px;background:var(--l-btn);color:#F4F5F2;padding:15px 24px;border-radius:999px;font-size:16.5px;font-weight:500;white-space:nowrap;transition:background .25s}
.b-dark:hover{background:var(--l-g)}
.b-dark svg{transition:transform .3s var(--ease)}
.b-dark:hover svg{transform:translateX(3px)}
.b-text{font-size:16.5px;font-weight:500;color:var(--l-ink);border-bottom:1px solid currentColor;padding-bottom:2px;transition:color .2s}
.b-text:hover{color:var(--l-g)}

/* Einstieg */
.h{padding-top:calc(env(safe-area-inset-top,0px) + clamp(140px,17vh,190px));padding-bottom:clamp(80px,9vw,140px)}
.h-copy{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:clamp(32px,5vw,96px);align-items:end}
.h h1{font-size:clamp(44px,5.6vw,96px);line-height:1;font-weight:500;letter-spacing:-.045em;text-wrap:balance}
.h-side p{font-size:clamp(17px,1.35vw,20px);line-height:1.55;color:var(--l-mut);max-width:36ch}
.h-acts{display:flex;align-items:center;gap:24px;flex-wrap:wrap;margin-top:28px}
.h-stage{margin-top:clamp(56px,7vw,110px)}
.fr{border-radius:16px;overflow:hidden;background:#fff;border:1px solid rgba(14,21,19,.1);box-shadow:0 1px 0 rgba(255,255,255,.8) inset,0 40px 80px -40px rgba(14,30,22,.35),0 12px 24px -16px rgba(14,30,22,.2)}
.fr-bar{display:flex;align-items:center;gap:6px;padding:11px 14px;background:rgba(244,245,242,.75);-webkit-backdrop-filter:blur(16px);backdrop-filter:blur(16px);border-bottom:1px solid rgba(14,21,19,.07)}
.fr-bar i{width:10px;height:10px;border-radius:50%;background:#D5DAD3}
.fr-bar span{margin:0 auto;font-size:12.5px;color:var(--l-mut);background:rgba(255,255,255,.8);border:1px solid rgba(14,21,19,.06);padding:3px 16px;border-radius:7px;transform:translateX(-24px)}
.fr-hero{transform-origin:50% 0;will-change:transform}
.h-site .cf{height:auto}
.h-cap{margin-top:18px;font-size:14.5px;color:var(--l-mut)}

/* Drei Punkte */
.facts{padding-bottom:clamp(90px,10vw,160px)}
.f-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(24px,3vw,56px);border-top:1px solid var(--l-ln);padding-top:36px}
.f-grid .n{font-size:13px;color:var(--l-g);font-variant-numeric:tabular-nums}
.f-grid h2{font-size:clamp(24px,2vw,32px);font-weight:500;letter-spacing:-.03em;margin-top:14px}
.f-grid p{font-size:16.5px;line-height:1.55;color:var(--l-mut);margin-top:10px;max-width:32ch}
.facts .ax{margin-top:clamp(56px,6vw,90px)}
.facts .ax-btn{color:var(--l-ink);font-weight:500}
.facts .ax-btn:hover{color:var(--l-g)}
.facts .ax-base{stroke:var(--l-ink)}
.facts .ax-loop{stroke:var(--l-g)}
.facts .ax-dot{fill:var(--l-gl)}
.facts .ax.open .ax-base{stroke:var(--l-g)}
.facts .ax-desc{color:var(--l-ink)}
.facts .ax-links a{color:var(--l-ink)}
.facts .ax-links a:hover{color:var(--l-g)}
.facts .ax-links .ic{color:var(--l-g)}

/* Leistungen */
.svs{padding-top:clamp(40px,5vw,80px);padding-bottom:clamp(100px,11vw,170px)}
.svs-head{display:flex;justify-content:space-between;align-items:flex-end;gap:24px 48px;flex-wrap:wrap}
.svs-head h2{font-size:clamp(36px,3.8vw,64px);font-weight:500;letter-spacing:-.045em;line-height:1}
.svs-head p{font-size:17px;line-height:1.55;color:var(--l-mut);max-width:44ch}
.svs-list{list-style:none;margin:clamp(40px,5vw,64px) 0 0;padding:0;border-top:1px solid var(--l-ln)}
.svs-list li{border-bottom:1px solid var(--l-ln)}
.svs-list a{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.1fr) 28px;gap:24px;align-items:center;padding:clamp(20px,2.2vw,30px) 0}
.s-t{font-size:clamp(24px,2.3vw,38px);font-weight:500;letter-spacing:-.035em;transition:transform .45s var(--ease),color .25s}
.s-d{font-size:16px;line-height:1.5;color:var(--l-mut)}
.s-a{justify-self:end;color:var(--l-mut);transition:transform .35s var(--ease),color .25s}
.svs-list a:hover .s-t{transform:translateX(12px);color:var(--l-g)}
.svs-list a:hover .s-a{transform:translateX(4px);color:var(--l-g)}

/* Beispiele */
.exs{padding-top:clamp(100px,11vw,170px);padding-bottom:clamp(100px,11vw,170px)}
.ex-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(28px,3.4vw,56px) clamp(20px,2.4vw,40px);margin-top:clamp(40px,5vw,64px)}
.ex .fr{border-radius:12px}
.ex .fr-bar{padding:8px 12px}
.ex .fr-bar i{width:8px;height:8px}
.ex .fr-bar span{font-size:11px;padding:2px 12px}
.ex figcaption{display:flex;justify-content:space-between;gap:16px;margin-top:16px;font-size:15px}
.ex figcaption b{font-weight:500}
.ex figcaption span{color:var(--l-mut)}
.ex .fr{transition:transform .5s var(--ease),box-shadow .5s}
.ex:hover .fr{transform:translateY(-6px)}

/* Schluss */
.end{background:#E4EBE5;color:var(--l-ink);text-align:center;padding-top:clamp(110px,12vw,190px);padding-bottom:clamp(110px,12vw,190px)}
.end h2{font-size:clamp(40px,5vw,84px);font-weight:500;letter-spacing:-.045em;line-height:1.02;text-wrap:balance;max-width:16ch;margin:0 auto}
.end p{font-size:clamp(17px,1.35vw,20px);line-height:1.55;color:var(--l-mut);max-width:44ch;margin:24px auto 0}
.end-acts{display:flex;justify-content:center;align-items:center;gap:28px;flex-wrap:wrap;margin-top:36px}
.end-mail{font-size:17px;user-select:all}

/* Einblenden */
.rv{opacity:0;transform:translateY(22px);transition:opacity .8s var(--ease),transform .9s var(--ease)}
.rv.in{opacity:1;transform:none}
.ex-grid .ex:nth-child(2n){transition-delay:.08s}

@media (max-width: 860px){
  .h-copy{grid-template-columns:1fr;gap:24px}
  .h{padding-top:calc(env(safe-area-inset-top,0px) + 120px)}
  .f-grid{grid-template-columns:1fr;gap:28px}
  .svs-list a{grid-template-columns:minmax(0,1fr) 24px;gap:6px 12px}
  .s-d{grid-column:1;font-size:15px}
  .s-a{grid-row:1 / span 2;grid-column:2}
  .ex-grid{grid-template-columns:1fr}
  .fr-bar span{transform:none}
}
@media (prefers-reduced-motion: reduce){ .rv{opacity:1;transform:none;transition:none} .fr-hero{transform:none!important} }
''' + CAFE_CSS + MOCK_CSS + home3.AX_CSS + home3.BUILD_CSS

JS = r'''
const MAP = %%MAP%%;
const MARK_L = '%%ML%%', MARK_D = '%%MD%%';
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* Sanft einblenden */
(function(){
  const els = document.querySelectorAll('.rv');
  if(reduce || !('IntersectionObserver' in window)){ els.forEach(e => e.classList.add('in')); return; }
  const io = new IntersectionObserver(es => es.forEach(e => { if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } }), {threshold: .15});
  els.forEach(e => io.observe(e));
})();

/* Website im Einstieg: wächst beim Scrollen leicht auf volle Grösse */
(function(){
  const f = document.getElementById('hFrame'); if(!f || reduce) return;
  let t = false;
  const upd = () => { t = false; const r = f.getBoundingClientRect(), p = Math.max(0, Math.min(1, 1 - (r.top - innerHeight * .25) / (innerHeight * .6))); f.style.transform = `scale(${.94 + .06 * p})`; };
  addEventListener('scroll', () => { if(!t){ t = true; requestAnimationFrame(upd); } }, {passive: true}); upd();
})();

''' + home3.AX_JS + home3.BUILD_JS
