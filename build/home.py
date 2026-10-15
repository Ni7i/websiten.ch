from parts import ARROW, GRAIN, MARK_LIGHT, MARK_DARK, WA, WA_ICON, LI

TITLE = 'websiten.ch'
DESC = 'Websites, Online-Shops und Hosting für Schweizer KMU. Mit festem Preis, Domains und Hosting in der Schweiz.'

CSS = r'''
/* Startseite */
.hero{position:relative;min-height:min(100svh,1000px);padding-top:clamp(140px,18vh,200px);padding-bottom:clamp(56px,9vh,110px);overflow:hidden;display:flex;flex-direction:column;justify-content:flex-end}
.hero-copy{position:relative;z-index:1;max-width:min(58vw,980px)}
.hero h1{font-size:clamp(48px,6.6vw,128px);line-height:.96;font-weight:700;letter-spacing:-.05em}
.hero h1 .quiet{color:#7E8C83}
.hero h1 span{display:block}
.hero-row{display:flex;align-items:center;gap:28px;margin-top:44px;flex-wrap:wrap}
.hero-row p{font-size:17px;line-height:1.55;color:var(--muted);max-width:32ch}

.statement{padding-top:clamp(110px,14vw,220px);padding-bottom:clamp(100px,12vw,180px)}
.statement h2{font-size:clamp(32px,3.8vw,68px);line-height:1.08;font-weight:600;letter-spacing:-.04em;max-width:24ch}
.two-col{display:grid;grid-template-columns:1fr 1fr;gap:clamp(32px,5vw,96px);margin-top:clamp(48px,6vw,96px);max-width:1300px}
.two-col p{color:#B9C2BF;font-size:19px;line-height:1.75;max-width:50ch}
/* Mehr über uns: Linie mit Schlaufe, darunter kurzer Text und Kontakt */
.ax{position:relative;margin-top:56px;padding-bottom:8px}
.ax-btn{position:relative;z-index:1;display:inline-flex;align-items:center;gap:14px;padding-bottom:10px;cursor:default;font-size:18px;color:var(--text);transition:color .2s}
.ax-btn:hover{color:var(--sage-light)}
.ax-ar{transition:transform .5s var(--ease)}
.ax.open .ax-ar{transform:rotate(90deg)}
.ax-svg{display:block;width:100%;height:64px;margin-top:-36px;overflow:visible;pointer-events:none}
.ax-svg path{fill:none;stroke-linecap:round;stroke-linejoin:round}
.ax-base{stroke:var(--text);stroke-width:1.5;transition:stroke .3s}
.ax-loop{stroke:var(--sage-light);stroke-width:1.5;stroke-dasharray:1;stroke-dashoffset:1;transition:stroke-dashoffset .5s var(--ease)}
.ax-dot{fill:var(--sage);opacity:0;transform-box:fill-box;transform-origin:center;transform:scale(0);transition:opacity .2s,transform .3s var(--ease)}
.ax.open .ax-base{stroke:var(--sage-light)}
.ax.open .ax-loop{stroke-dashoffset:0;transition:stroke-dashoffset 1.3s cubic-bezier(.6,.05,.2,1)}
.ax.open .ax-dot{opacity:1;transform:scale(1);transition-delay:1.15s}
.ax-panel{display:grid;grid-template-rows:0fr;transition:grid-template-rows .6s var(--ease) .1s}
.ax.open .ax-panel{grid-template-rows:1fr;transition-delay:.55s}
.ax-in{overflow:hidden;min-height:0;display:flex;justify-content:space-between;align-items:flex-end;gap:clamp(32px,6vw,120px);padding-top:28px}
.ax-in > *{opacity:0;transform:translateY(12px);transition:opacity .5s,transform .6s var(--ease)}
.ax.open .ax-in > *{opacity:1;transform:none}
.ax.open .ax-in > :nth-child(1){transition-delay:.85s}
.ax.open .ax-in > :nth-child(2){transition-delay:1s}
.ax-desc{font-size:clamp(20px,1.7vw,26px);line-height:1.5;letter-spacing:-.01em;color:#D3DAD6;max-width:40ch}
.ax-links{display:flex;flex-direction:column;gap:12px;flex:none;padding-bottom:6px}
.ax-links a{display:inline-flex;align-items:center;gap:12px;font-size:16px;color:#C9D2CD;transition:color .2s}
.ax-links a:hover{color:var(--sage-light)}
.ax-links .ic{width:18px;height:18px;color:var(--sage)}

/* Helle Abschnitte und Fotos */
.light{background:var(--sand);color:var(--ink)}
.statement.light h2{color:#141B18}
.statement.light .two-col p{color:#4A524D}
.strip{margin:clamp(64px,8vw,120px) calc(var(--pad) * -1) 0}
.strip-lbl{padding:0 var(--pad);font-size:14px;color:#7A7268;margin-bottom:18px}
.strip-view{overflow:hidden}
.strip-track{display:flex;align-items:flex-end;gap:clamp(14px,1.6vw,24px);width:max-content;padding-left:var(--pad);animation:drift 70s linear infinite}
.strip:hover .strip-track{animation-play-state:paused}
@keyframes drift{to{transform:translateX(calc(-50% - clamp(14px,1.6vw,24px) / 2))}}
.strip figure{margin:0;flex:none}
.strip img{display:block;width:clamp(220px,22vw,360px);height:auto;border-radius:4px;transition:transform .6s var(--ease)}
.strip figure:hover img{transform:translateY(-6px)}
.strip figcaption{font-size:14px;color:#5E6661;margin-top:12px}
.light .ax-btn{color:#141B18}
.light .ax-btn:hover{color:var(--clay)}
.light .ax-base{stroke:#141B18}
.light .ax-loop{stroke:var(--clay)}
.light .ax-dot{fill:var(--clay)}
.light .ax.open .ax-base{stroke:var(--clay)}
.light .ax-desc{color:#2C332F}
.light .ax-links a{color:#3A423D}
.light .ax-links a:hover{color:var(--clay)}
.light .ax-links .ic{color:var(--clay)}
@media (max-width: 700px){ .strip img{width:62vw} }
@media (prefers-reduced-motion: reduce){ .strip-track{animation:none} .strip-view{overflow-x:auto} }

/* Neue Startseite: hell, warm, mit Fotos */
.h2{position:relative;min-height:min(88svh,900px);display:flex;flex-direction:column;justify-content:flex-end;padding-top:clamp(140px,18vh,200px);padding-bottom:clamp(56px,8vh,96px)}
.h2-t{font-size:clamp(56px,9.4vw,180px);line-height:.95;font-weight:700;letter-spacing:-.055em;color:#141B18}
.h2-t .ln{display:block;white-space:nowrap}
.pill{display:inline-block;vertical-align:-.04em;height:.74em;width:0;border-radius:999px;overflow:hidden;background:#DCD3C4;margin:0 .06em;animation:pill 1.1s cubic-bezier(.16,1,.3,1) calc(.35s + var(--i) * .18s) forwards}
.pill img{width:100%;height:100%;object-fit:cover;display:block;opacity:0;transition:opacity .5s}
.pill img.ok{opacity:1}
@keyframes pill{to{width:1.55em}}
.h2-row{display:flex;justify-content:space-between;align-items:flex-end;gap:32px;flex-wrap:wrap;margin-top:clamp(36px,5vw,64px);padding-top:28px;border-top:1px solid #DCD3C4}
.h2-row p{font-size:clamp(18px,1.4vw,21px);line-height:1.55;color:#4A524D;max-width:40ch}
.h2-cta{display:flex;align-items:center;gap:28px;flex-wrap:wrap}
.h2-link{display:inline-flex;align-items:center;gap:10px;font-size:17px;color:#141B18;padding-bottom:4px;border-bottom:1.5px solid #141B18;transition:color .2s,border-color .2s}
.h2-link:hover{color:var(--clay);border-color:var(--clay)}
.statement.light{border-top:1px solid #E2DACC}
.sv{position:relative;padding-top:clamp(100px,12vw,180px);padding-bottom:clamp(100px,12vw,180px)}
.sv-head{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;margin-bottom:clamp(32px,4vw,56px)}
.sv-head .h-sec{color:#141B18}
.sv-list{list-style:none;border-top:1px solid #D6CDBE}
.sv-list a{position:relative;display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr) 40px;align-items:center;gap:24px;padding:clamp(22px,2.4vw,34px) 0;border-bottom:1px solid #D6CDBE;color:#141B18;transition:padding .45s var(--ease),color .3s}
.sv-list .t{font-size:clamp(30px,3.6vw,60px);font-weight:600;letter-spacing:-.04em;line-height:1}
.sv-list .d{font-size:17px;color:#5E6661}
.sv-list .ar{justify-self:end;opacity:.35;transition:opacity .3s,transform .4s var(--ease)}
.sv-list a:hover{color:var(--clay);padding-left:18px}
.sv-list a:hover .ar{opacity:1;transform:translateX(4px)}
.sv-float{position:fixed;left:0;top:0;z-index:5;width:280px;aspect-ratio:4/5;border-radius:6px;overflow:hidden;pointer-events:none;opacity:0;transform:translate(-50%,-50%) scale(.85) rotate(-3deg);transition:opacity .3s,transform .45s var(--ease)}
.sv-float.on{opacity:1;transform:translate(-50%,-50%) scale(1) rotate(-3deg)}
.sv-float img{width:100%;height:100%;object-fit:cover}
@media (max-width: 860px){
  .h2-t .ln{white-space:normal}
  .sv-list a{grid-template-columns:minmax(0,1fr) 30px;gap:6px 12px}
  .sv-list .d{grid-column:1;font-size:15px}
  .sv-list .ar{grid-row:1 / span 2;grid-column:2}
  .sv-float{display:none}
}
@media (prefers-reduced-motion: reduce){ .pill{animation:none;width:1.55em} }

@media (max-width: 860px){
  .ax-in{flex-direction:column;align-items:flex-start}
}

@media (prefers-reduced-motion: reduce){
  .ax-loop,.ax-panel,.ax-in > *,.ax-dot{transition:none!important}
}

.build{height:440vh}
.build-sticky{position:sticky;top:0;height:100vh;overflow:hidden}
#bcv{position:absolute;inset:0;width:100%;height:100%;pointer-events:none;z-index:2}
.build-copy{position:absolute;left:var(--pad);top:50%;transform:translateY(-50%);width:min(27vw,410px);z-index:3}
.steps{position:relative;min-height:300px}
.step{position:absolute;inset:0 0 auto 0;opacity:0;transform:translateY(16px);transition:opacity .5s,transform .6s var(--ease);pointer-events:none}
.step.on{opacity:1;transform:none}
.step h2{font-size:clamp(30px,2.8vw,50px);line-height:1.04;font-weight:700;letter-spacing:-.045em}
.step p{color:var(--muted);font-size:17px;line-height:1.6;margin-top:20px;max-width:36ch}
.bp{display:flex;gap:8px;margin-top:8px}
.bp i{width:44px;height:2px;background:#2C3634;border-radius:2px;overflow:hidden}
.bp b{display:block;height:100%;width:0;background:var(--sage-light)}
.build-stage{position:absolute;right:var(--pad);top:50%;transform:translateY(-50%);width:min(52vw,calc((100vh - 180px) * 1.58))}
#bsite{opacity:0}
.bnotif{position:absolute;right:-24px;top:34%;width:min(330px,60%);z-index:4;background:rgba(32,40,39,.9);backdrop-filter:blur(14px);-webkit-backdrop-filter:blur(14px);color:var(--text);border:1px solid #34403E;border-radius:18px;padding:14px 16px;box-shadow:0 24px 60px rgba(0,0,0,.45);opacity:0;transform:translateY(-14px) scale(.96)}
.bn-top{display:flex;align-items:center;gap:8px;font-size:12px;color:#A9B4B1;margin-bottom:4px}
.bn-logo{width:18px;height:auto;flex:none}
.bn-top span{margin-left:auto}
.bnotif strong{display:block;font-size:15px;font-weight:600}
.bnotif p{font-size:14px;line-height:1.4;color:#C9D1CE}




@media (max-width: 860px){
  .hero{min-height:0;padding-top:300px}
  .hero-copy{max-width:none}
  .hero h1 span{display:inline}
  .two-col{grid-template-columns:1fr}
  .build{height:400vh}
  .build-stage{left:16px;right:16px;width:auto;top:96px;transform:none}
  .build-copy{left:20px;right:20px;width:auto;top:auto;bottom:36px;transform:none}
  .steps{min-height:210px}
  .step h2{font-size:28px}
  .step p{font-size:15.5px;margin-top:12px}
  .bnotif{right:8px;top:auto;bottom:-40px;width:78%}
}
@media (prefers-reduced-motion: reduce){
  .build{height:auto}
  .build-sticky{position:relative;height:auto;min-height:100vh}
  #bcv{display:none}
  #bsite{opacity:1}
  .bnotif{opacity:1;transform:none}
}
'''

M1 = '''<div class="mock m1">
            <div class="k-top">
              <span class="k-logo" data-t><svg viewBox="0 0 20 24" aria-hidden="true"><path d="M10 1C10 1 2 10.5 2 15.5a8 8 0 0 0 16 0C18 10.5 10 1 10 1Z" fill="#163A5C"/></svg><span><b>Keller</b> Sanitär AG</span></span>
              <span class="k-links"><span data-t>Badumbau</span><span data-t>Heizung</span><span data-t>Service</span><span data-t>Über uns</span><span data-t>Kontakt</span></span>
              <span class="k-tel" data-t>056 222 14 80</span>
            </div>
            <div class="k-hero">
              <div class="k-copy">
                <p class="k-kick" data-t>Sanitär und Heizung in Baden, seit 1974</p>
                <h4 data-t>Badumbau aus einer Hand.</h4>
                <p class="k-p" data-t>Planung, Abbruch, Sanitär, Plättli und Elektro. Ein Team, ein Fixpreis, ein Termin, der hält.</p>
                <div class="k-acts"><span class="k-btn" data-t>Besichtigung vereinbaren</span><span class="k-more" data-t>Unsere Bäder</span></div>
              </div>
              <div class="k-photo" data-t><img src="%%PHOTO%%" alt="Badezimmer mit freistehender Wanne und zwei Lavabos"><span class="k-cap">Einfamilienhaus in Wettingen, Umbau in 5 Wochen</span></div>
            </div>
            <div class="k-strip">
              <span data-t><b>Badumbau</b>Vom Plan bis zur letzten Fuge</span>
              <span data-t><b>Heizungsersatz</b>Wärmepumpe statt Öl</span>
              <span data-t><b>Service</b>Boiler, Entkalkung, Leitungen</span>
              <span class="k-sos" data-t><b>Notfall 24 h</b>056 222 14 80</span>
            </div>
          </div>'''

M2 = '''<div class="mock m2">
            <div class="nav"><span class="lg">Praxis am Lindenplatz</span><span class="ln"><span>Team</span><span>Angebot</span><span>Notfall</span><span>Kontakt</span></span><span class="bt">Termin buchen</span></div>
            <div class="hero2">
              <div class="copy"><small>Hausarztpraxis in Wettingen</small><h4>Wir nehmen uns <em>Zeit für Sie.</em></h4><p>Allgemeine Innere Medizin für Erwachsene und Familien. Neue Patientinnen und Patienten sind herzlich willkommen.</p><div class="acts"><span class="bt">Termin online buchen</span><span>056 000 00 00</span></div></div>
              <div class="arch"><div class="hours"><h5>Öffnungszeiten</h5><div><span>Montag bis Donnerstag</span><b>08:00 bis 17:30</b></div><div><span>Freitag</span><b>08:00 bis 16:00</b></div><div class="sos"><span>Im Notfall</span><b>144</b></div></div></div>
            </div>
          </div>'''

M3 = '''<div class="mock m3">
            <div class="loaf"></div>
            <div class="nav"><span class="lg">Morgenrot</span><span class="ln"><span>Backstube</span><span>Café</span><span>Torten</span><span>Kontakt</span></span><span class="bt">Torte bestellen</span></div>
            <div class="hero3">
              <div class="copy"><h4>Frisch gebacken. <em>Jeden Morgen ab sechs.</em></h4><p>Brot, Gipfeli und Torten aus der eigenen Backstube. Bestellen Sie online und holen Sie ab, wann es Ihnen passt.</p></div>
              <div class="menu3"><h5>Heute in der Vitrine</h5><div><span>Buttergipfeli</span><b>1.80</b></div><div><span>Zopf, 500 g</span><b>6.50</b></div><div><span>Rüeblitorte, Stück</span><b>5.20</b></div><div><span>Nussgipfel</span><b>3.20</b></div></div>
            </div>
            <div class="foot3"><span>Bahnhofstrasse 12, Brugg</span><span>Montag bis Samstag, 6 bis 18 Uhr</span></div>
          </div>'''

def strip_t(s):
    return s.replace(' data-t', '')

MAIN = '''
  <section class="h2 light pad" id="hero" aria-label="Einstieg">
    <h1 class="h2-t">
      <span class="ln">Websites für <i class="pill" style="--i:0"><img data-from="s-coiffeur" alt=""></i></span>
      <span class="ln">Schweizer <i class="pill" style="--i:1"><img data-from="s-cafe" alt=""></i> KMU.</span>
    </h1>
    <div class="h2-row">
      <p>Gebaut, damit Ihr Telefon klingelt. Mit festem Preis, Server in Genf und einer Ansprechperson für alles.</p>
      <div class="h2-cta"><a class="btn btn-clay" href="kontakt.html">Projekt anfragen ''' + ARROW + '''</a><a class="h2-link" href="preise.html">Preise ansehen</a></div>
    </div>
  </section>

  <section class="statement pad light">
    <h2>Wir bauen Websites für Betriebe in der ganzen Schweiz und kümmern uns danach weiter darum.</h2>
    <div class="two-col">
      <p>Den Preis und den Termin kennen Sie, bevor wir anfangen. Nach dem Start bleiben wir da und erledigen Updates, Backups und kleine Änderungen. Sie müssen sich um die Technik nicht kümmern.</p>
      <p>Domains, Hosting und E-Mail laufen bei Infomaniak in Genf, Ihre Daten bleiben also in der Schweiz. Und für alles, was mit Ihrem Auftritt im Netz zu tun hat, brauchen Sie nur eine Telefonnummer.</p>
    </div>
    <div class="strip">
      <p class="strip-lbl">Für Betriebe wie diese</p>
      <div class="strip-view"><div class="strip-track"><figure><img src="%%IMG_CAFE%%" alt="Barista hinter der Theke" class="s-cafe"><figcaption>Café</figcaption></figure><figure><img src="%%IMG_COIFFEUR%%" alt="Haarschnitt im Salon" class="s-coiffeur"><figcaption>Coiffeur</figcaption></figure><figure><img src="%%IMG_RESTAURANT%%" alt="Koch beim Anrichten" class="s-restaurant"><figcaption>Restaurant</figcaption></figure><figure><img src="%%IMG_LADEN2%%" alt="Schaufenster eines Ladens" class="s-laden2"><figcaption>Laden</figcaption></figure><figure><img src="%%IMG_BAECKEREI%%" alt="Frisches Brot" class="s-baeckerei"><figcaption>Bäckerei</figcaption></figure></div></div>
    </div>
    <div class="ax" id="ax">
      <button class="ax-btn" type="button" id="axBtn" aria-expanded="false" aria-controls="axPanel">Mehr über uns <svg class="ax-ar" width="20" height="13" viewBox="0 0 22 14" aria-hidden="true"><path d="M1 7h19M14 1l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.6"/></svg></button>
      <svg class="ax-svg" id="axSvg" aria-hidden="true"><path class="ax-base" id="axBase"/><path class="ax-loop" id="axLoop" pathLength="1"/><circle class="ax-dot" id="axDot" r="4"/></svg>
      <div class="ax-panel" id="axPanel" role="region" aria-label="Über websiten.ch">
        <div class="ax-in">
          <p class="ax-desc">Bei websiten.ch haben Sie einen festen Ansprechpartner. Er baut Ihre Website und bleibt danach erreichbar, per Telefon oder E-Mail, ohne Ticketsystem und Warteschlaufe. Die Server stehen bei Infomaniak in Genf. Alles bleibt in der Schweiz.</p>
          <div class="ax-links">
            <a href="''' + LI + '''"><svg class="ic" width="18" height="18" viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="3" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 10.5V17M8 7.2v.1M11.5 17v-3.8c0-1.6 1-2.7 2.4-2.7s2.1 1 2.1 2.7V17M11.5 10.5V17" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>LinkedIn</a>
            <a href="ueber-uns.html">''' + ARROW + '''Ganze Seite lesen</a>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="build" id="build" aria-label="So entsteht Ihre Website">
    <div class="build-sticky">
      <canvas id="bcv" aria-hidden="true"></canvas>
      <div class="build-copy">
        <div class="steps">
          <div class="step on"><h2>Zuerst reden wir.</h2><p>Über Ihren Betrieb, Ihre Kunden und darüber, woher heute Ihre Anfragen kommen. Am Telefon oder bei Ihnen vor Ort.</p></div>
          <div class="step"><h2>Dann planen wir die Seiten.</h2><p>Welche Seiten es braucht, was draufsteht und wie ein Besucher zur Anfrage kommt. Das sehen Sie als einfaches Gerüst, bevor gestaltet wird.</p></div>
          <div class="step"><h2>Dann wird gestaltet.</h2><p>Farben, Schrift und Bilder passend zu Ihrem Betrieb. Sie sehen jeden Zwischenstand und sagen uns, was passt und was nicht.</p></div>
          <div class="step"><h2>Dann geht sie online.</h2><p>Und die ersten Anfragen kommen über das Formular. In den Wochen danach schauen wir, was gut läuft, und bessern nach.</p></div>
        </div>
        <div class="bp" aria-hidden="true"><i><b></b></i><i><b></b></i><i><b></b></i><i><b></b></i></div>
      </div>
      <div class="build-stage">
        <div class="frame-b" id="bsite">
          <div class="bar" data-t><i></i><i></i><i></i><span>keller-sanitaer.ch</span></div>
          ''' + M1 + '''
        </div>
        <div class="bnotif" id="bnotif" aria-hidden="true">
          <div class="bn-top"><svg class="bn-logo" viewBox="12 10 174 188" aria-hidden="true"><path fill="#83AA8C" d="''' + MARK_LIGHT + '''"/><path fill="#4F695A" d="''' + MARK_DARK + '''"/></svg>websiten.ch<span>jetzt</span></div>
          <strong>Neue Anfrage über keller-sanitaer.ch</strong>
          <p>Badsanierung, Einfamilienhaus in Wettingen. Wann hätten Sie Zeit für eine Besichtigung?</p>
        </div>
      </div>
    </div>
  </section>

  <section class="sv light pad" id="leistungen">
    <div class="sv-head"><h2 class="h-sec">Was wir machen</h2><a class="h2-link" href="leistungen.html">Alle Leistungen ''' + ARROW + '''</a></div>
    <ul class="sv-list">
      <li><a href="leistungen.html#websites" data-from="s-cafe"><span class="t">Websites</span><span class="d">Firmenwebsites ab CHF 590, fürs Handy gebaut</span><span class="ar">''' + ARROW + '''</span></a></li>
      <li><a href="leistungen.html#shops" data-from="s-laden2"><span class="t">Online-Shops</span><span class="d">Mit TWINT, Karte und Versand</span><span class="ar">''' + ARROW + '''</span></a></li>
      <li><a href="leistungen.html#seo" data-from="s-coiffeur"><span class="t">Google und SEO</span><span class="d">Gefunden werden, wo Ihre Kunden suchen</span><span class="ar">''' + ARROW + '''</span></a></li>
      <li><a href="leistungen.html#hosting" data-from="s-restaurant"><span class="t">Hosting in Genf</span><span class="d">CHF 25 im Monat, die ersten 3 Monate CHF 10</span><span class="ar">''' + ARROW + '''</span></a></li>
      <li><a href="leistungen.html#m365" data-from="s-baeckerei"><span class="t">Microsoft 365</span><span class="d">E-Mail, Teams und Konten, sauber eingerichtet</span><span class="ar">''' + ARROW + '''</span></a></li>
    </ul>
    <div class="sv-float" id="svFloat" aria-hidden="true"><img alt=""></div>
  </section>

'''

JS = r'''
const MAP = %%MAP%%;
const MARK_L = '%%ML%%', MARK_D = '%%MD%%';
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

/* Fotostreifen: zweite Runde per Script, damit die Bilder nur einmal im HTML stehen */
(function(){ const t = document.querySelector('.strip-track'); if(!t) return; [...t.children].forEach(f => { const c = f.cloneNode(true); c.setAttribute('aria-hidden', 'true'); c.querySelector('img').alt = ''; t.appendChild(c); }); })();

/* Fotos für Überschrift und Leistungsliste aus dem Fotostreifen übernehmen (Bilder nur einmal im HTML) */
(function(){
  const src = c => { const i = document.querySelector('.strip img.' + c); return i ? i.src : ''; };
  document.querySelectorAll('.pill img[data-from]').forEach(i => { i.onload = () => i.classList.add('ok'); i.src = src(i.dataset.from); });
  const fl = document.getElementById('svFloat'); if(!fl || !matchMedia('(hover: hover)').matches) return;
  const im = fl.querySelector('img'); let x = 0, y = 0, tx = 0, ty = 0, raf = 0;
  const move = () => { x += (tx - x)*.18; y += (ty - y)*.18; fl.style.left = x + 'px'; fl.style.top = y + 'px'; raf = Math.abs(tx - x) + Math.abs(ty - y) > .5 ? requestAnimationFrame(move) : 0; };
  document.querySelectorAll('.sv-list a').forEach(a => {
    a.addEventListener('mouseenter', e => { im.src = src(a.dataset.from); if(!fl.classList.contains('on')){ x = tx = e.clientX + 180; y = ty = e.clientY; } fl.classList.add('on'); });
    a.addEventListener('mousemove', e => { tx = e.clientX + 180; ty = e.clientY; if(!raf) raf = requestAnimationFrame(move); });
    a.addEventListener('mouseleave', () => fl.classList.remove('on'));
  });
})();

/* Mehr über uns: beim Drüberfahren zeichnet sich eine Linie mit Schlaufe, darunter erscheint der Firmenblock */
(function(){
  const ax = document.getElementById('ax'), btn = document.getElementById('axBtn');
  if(!ax) return;
  const svg = document.getElementById('axSvg'), base = document.getElementById('axBase'), loop = document.getElementById('axLoop'), dot = document.getElementById('axDot');
  function draw(){
    const W = svg.clientWidth, bw = btn.offsetWidth, B = 32, f = n => n.toFixed(1);
    base.setAttribute('d', `M0 ${B}H${f(bw)}`);
    const x = Math.min(bw + 150, W * .32), r = W - x, end = W - 6;
    loop.setAttribute('d',
      `M${f(bw)} ${B}C${f(bw + 50)} ${B} ${f(x - 50)} ${B + 16} ${f(x)} ${B + 16}` +
      `C${f(x + 62)} ${B + 16} ${f(x + 66)} ${B - 30} ${f(x + 30)} ${B - 30}` +
      `C${f(x - 4)} ${B - 30} ${f(x - 2)} ${B + 18} ${f(x + 62)} ${B + 20}` +
      `C${f(x + r * .3)} ${B + 24} ${f(x + r * .55)} ${B - 8} ${f(x + r * .78)} ${B - 4}` +
      `C${f(x + r * .9)} ${B - 2} ${f(end - 30)} ${B + 6} ${f(end)} ${B + 4}`);
    dot.setAttribute('cx', f(end)); dot.setAttribute('cy', B + 4);
  }
  draw(); addEventListener('resize', draw); if(document.fonts) document.fonts.ready.then(draw);
  let t;
  const set = o => { clearTimeout(t); ax.classList.toggle('open', o); btn.setAttribute('aria-expanded', o); };
  if(matchMedia('(hover: hover)').matches){
    btn.addEventListener('pointerenter', () => set(true));
    ax.addEventListener('pointerenter', () => { if(ax.classList.contains('open')) clearTimeout(t); });
    ax.addEventListener('pointerleave', () => { t = setTimeout(() => set(false), 350); });
  } else {
    btn.addEventListener('click', () => set(!ax.classList.contains('open')));
  }
  ax.addEventListener('focusin', () => set(true));
  ax.addEventListener('focusout', e => { if(!ax.contains(e.relatedTarget)) set(false); });
})();

/* Scroll-Passage: Schweizerkarte -> Punkte-Gerüst -> farbige Pixel -> echte Website */
(function(){
  const sec = document.getElementById('build'), st = sec.querySelector('.build-sticky'), cv = document.getElementById('bcv'), ctx = cv.getContext('2d');
  const site = document.getElementById('bsite'), notif = document.getElementById('bnotif');
  const steps = [...sec.querySelectorAll('.step')], bars = [...sec.querySelectorAll('.bp b')];
  const C = new Path2D(MAP.country), L = new Path2D(MAP.lakes);
  let W, H, dpr, parts = [], F, sp, R = null, RD = null, cur = 0, tgt = 0, running = false, step = -1, ready = false;
  const small = document.createElement('canvas'), sctx = small.getContext('2d');
  const clamp = (v, a, b) => Math.max(a, Math.min(b, v)), ease = t => t < .5 ? 4*t*t*t : 1 - Math.pow(-2*t + 2, 3)/2;
  const rgb = s => { const m = s && s.match(/[\d.]+/g); return m ? m.map(Number) : null; };

  // Die echte Website einmal grob abmalen: Flächen, Bild, Textzeilen. Daraus entstehen später die Pixel.
  function raster(){
    const sr = site.getBoundingClientRect();
    R = document.createElement('canvas'); R.width = Math.max(1, Math.round(sr.width)); R.height = Math.max(1, Math.round(sr.height));
    const r = R.getContext('2d');
    r.fillStyle = '#0E1211'; r.fillRect(0, 0, R.width, R.height);
    const all = [site, ...site.querySelectorAll('*')];
    for(const el of all){
      if(el instanceof SVGElement && el.tagName !== 'svg') continue;
      const b = el.getBoundingClientRect(); if(!b.width || !b.height) continue;
      const x = b.left - sr.left, y = b.top - sr.top, cs = getComputedStyle(el);
      const bg = rgb(cs.backgroundColor);
      if(bg && (bg.length < 4 || bg[3] > .05)){ r.fillStyle = cs.backgroundColor; r.fillRect(x, y, b.width, b.height); }
      const bt = parseFloat(cs.borderBottomWidth); if(bt > 0 && cs.borderBottomStyle !== 'none'){ r.fillStyle = cs.borderBottomColor; r.fillRect(x, y + b.height - bt, b.width, bt); }
      const bl = parseFloat(cs.borderTopWidth); if(bl > 0 && cs.borderTopStyle !== 'none'){ r.fillStyle = cs.borderTopColor; r.fillRect(x, y, b.width, bl); }
      if(el.tagName === 'IMG' && el.complete && el.naturalWidth){
        const iw = el.naturalWidth, ih = el.naturalHeight, k = Math.max(b.width/iw, b.height/ih), w = b.width/k, h = b.height/ih*ih/k;
        r.drawImage(el, (iw - w)*.5, (ih - h)*.6, w, h, x, y, b.width, b.height);
      }
      if(el.tagName === 'svg'){ r.fillStyle = '#163A5C'; r.fillRect(x + b.width*.2, y + b.height*.2, b.width*.6, b.height*.7); }
    }
    const tw = document.createTreeWalker(site, NodeFilter.SHOW_TEXT), rg = document.createRange();
    let n; while((n = tw.nextNode())){
      if(!n.nodeValue.trim()) continue;
      const pe = n.parentElement, cs = getComputedStyle(pe); r.fillStyle = cs.color; r.globalAlpha = .55;
      rg.selectNodeContents(n);
      for(const q of rg.getClientRects()){ r.fillRect(q.left - sr.left, q.top - sr.top + q.height*.22, q.width, q.height*.56); }
      r.globalAlpha = 1;
    }
    RD = r.getImageData(0, 0, R.width, R.height).data;
  }
  const sample = (x, y) => { if(!RD) return [169,191,187]; const i = (clamp(Math.round(y), 0, R.height - 1)*R.width + clamp(Math.round(x), 0, R.width - 1))*4; return [RD[i], RD[i+1], RD[i+2]]; };

  function layout(){
    dpr = Math.min(2, devicePixelRatio || 1); W = st.clientWidth; H = st.clientHeight;
    cv.width = Math.round(W*dpr); cv.height = Math.round(H*dpr);
    const sr = st.getBoundingClientRect(), fr = site.getBoundingClientRect();
    F = {x: fr.left - sr.left, y: fr.top - sr.top, w: fr.width, h: fr.height};
    sp = W < 860 ? 4.5 : 6.5; const T = [];
    site.querySelectorAll('[data-t]').forEach(el => { const b = el.getBoundingClientRect(), r = {x: b.left - sr.left, y: b.top - sr.top, w: b.width, h: b.height}; for(let y = r.y + sp/2; y < r.y + r.h; y += sp) for(let x = r.x + sp/2; x < r.x + r.w; x += sp) T.push([x, y, 1]); });
    for(let x = F.x; x <= F.x + F.w; x += sp){ T.push([x, F.y, 2]); T.push([x, F.y + F.h, 2]); }
    for(let y = F.y; y <= F.y + F.h; y += sp){ T.push([F.x, y, 2]); T.push([F.x + F.w, y, 2]); }
    const S = Math.min(F.w*.92/MAP.w, F.h*.92/MAP.h), mx = F.x + (F.w - MAP.w*S)/2, my = F.y + (F.h - MAP.h*S)/2;
    const m = new DOMMatrix([S,0,0,S,mx,my]), cp = new Path2D(), lp = new Path2D(); cp.addPath(C, m); lp.addPath(L, m);
    ctx.setTransform(1,0,0,1,0,0);
    const Pp = []; for(let y = my; y < my + MAP.h*S; y += sp) for(let x = mx; x < mx + MAP.w*S; x += sp) if(ctx.isPointInPath(cp, x, y) && !ctx.isPointInPath(lp, x, y)) Pp.push([x, y]);
    T.sort((a, b) => a[0] - b[0] || a[1] - b[1]); Pp.sort((a, b) => a[0] - b[0] || a[1] - b[1]);
    raster();
    parts = T.map((t, i) => { const s = Pp[Math.floor(i*Pp.length/T.length)]; return {sx: s[0] + (Math.random() - .5)*sp*.8, sy: s[1] + (Math.random() - .5)*sp*.8, tx: t[0], ty: t[1], edge: t[2] === 2, d: (t[0] - F.x)/F.w*.55 + Math.random()*.45, w: (Math.random() - .5)*2, c: sample(t[0] - F.x, t[1] - F.y), cd: Math.random()*.5 + (t[1] - F.y)/F.h*.3}; });
    ready = true;
  }
  function mosaic(b, alpha){
    if(!R || alpha <= 0) return;
    const sw = Math.max(1, Math.ceil(F.w/b)), sh = Math.max(1, Math.ceil(F.h/b));
    small.width = sw; small.height = sh; sctx.imageSmoothingEnabled = true; sctx.drawImage(R, 0, 0, sw, sh);
    ctx.save(); ctx.globalAlpha = alpha; ctx.imageSmoothingEnabled = false;
    ctx.beginPath(); ctx.rect(F.x, F.y, F.w, F.h); ctx.clip();
    ctx.drawImage(small, F.x, F.y, sw*b, sh*b); ctx.restore();
  }
  function draw(p){
    if(!ready) return;
    ctx.setTransform(1,0,0,1,0,0); ctx.clearRect(0, 0, cv.width, cv.height); ctx.setTransform(dpr,0,0,dpr,0,0);
    const morph = clamp((p - .12)/.34, 0, 1), col = clamp((p - .47)/.11, 0, 1), res = clamp((p - .58)/.16, 0, 1);
    // 1) Punkte: Karte -> Gerüst, danach färben sie sich und werden zu Quadraten
    if(res < .02){
      const grey = [[94,119,117],[169,191,187],[126,150,147]], rad = [1.6,1.7,1.3];
      if(col > 0) mosaic(sp, ease(col)*.9);
      for(const q of parts){
        const k = ease(clamp(morph*1.7 - q.d*.7, 0, 1)), x = q.sx + (q.tx - q.sx)*k, y = q.sy + (q.ty - q.sy)*k + Math.sin(k*Math.PI)*q.w*60;
        const g = q.edge && k > .9 ? 2 : (k > .98 ? 1 : 0), cc = ease(clamp(col*1.6 - q.cd, 0, 1));
        const base = grey[g], c = cc > 0 ? [base[0] + (q.c[0] - base[0])*cc, base[1] + (q.c[1] - base[1])*cc, base[2] + (q.c[2] - base[2])*cc] : base;
        ctx.fillStyle = `rgb(${c[0]|0},${c[1]|0},${c[2]|0})`;
        if(cc > 0){ const s = rad[g]*2 + (sp - rad[g]*2)*cc; ctx.fillRect(x - s/2, y - s/2, s, s); }
        else { ctx.beginPath(); ctx.arc(x, y, rad[g], 0, 6.283); ctx.fill(); }
      }
    }
    // 2) Pixel werden feiner, bis die echte Website scharf da ist
    const fade = clamp((res - .72)/.28, 0, 1);
    if(res >= .02){ const b = Math.max(1, Math.round(1 + (sp - 1)*(1 - ease(Math.min(res/.75, 1))))); mosaic(b, 1 - fade); }
    site.style.opacity = res > .5 ? 1 : 0;
    const n = clamp((p - .8)/.07, 0, 1); notif.style.opacity = n; notif.style.transform = `translateY(${(1 - n)*-14}px) scale(${.96 + n*.04})`;
    const s = p < .2 ? 0 : p < .47 ? 1 : p < .76 ? 2 : 3;
    if(s !== step){ step = s; steps.forEach((el, i) => el.classList.toggle('on', i === s)); }
    const edges = [0, .2, .47, .76, 1]; bars.forEach((b, i) => b.style.width = clamp((p - edges[i])/(edges[i + 1] - edges[i]), 0, 1)*100 + '%');
  }
  const read = () => { const r = sec.getBoundingClientRect(); tgt = clamp(-r.top/(r.height - innerHeight), 0, 1); };
  function loop(){ cur += (tgt - cur)*.14; if(Math.abs(tgt - cur) < .0004) cur = tgt; draw(cur); if(cur !== tgt) requestAnimationFrame(loop); else running = false; }
  if(reduce){ steps.forEach((el, i) => el.classList.toggle('on', i === 3)); return; }
  const img = site.querySelector('img');
  Promise.all([document.fonts ? document.fonts.ready : 0, img && img.decode ? img.decode().catch(() => 0) : 0]).then(() => { layout(); read(); cur = tgt; draw(cur); });
  addEventListener('scroll', () => { read(); if(!running){ running = true; requestAnimationFrame(loop); } }, {passive:true});
  let rt; addEventListener('resize', () => { clearTimeout(rt); rt = setTimeout(() => { layout(); read(); draw(cur); }, 150); });
})();
'''
