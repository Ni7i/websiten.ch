import re
import home
from parts import ARROW, MARK_LIGHT, MARK_DARK, LI

DESC = 'Websites und Online-Shops für Schweizer KMU. Fester Preis, eine Ansprechperson, Server bei Infomaniak in Genf.'

# Teile aus der bisherigen Startseite, die bleiben: Scroll-Passage und "Mehr über uns"
_m = home.MAIN
BUILD = _m[_m.index('<section class="build"'):]
BUILD = BUILD[:BUILD.index('</section>') + len('</section>')]
AX = _m[_m.index('<div class="ax" id="ax">'):]
AX = AX[:AX.index('</section>')].rstrip()
AX = AX[:AX.rindex('</div>') + 6] if AX.count('<div') < AX.count('</div>') else AX
_c = home.CSS
BUILD_CSS = _c[_c.index('.build{height:440vh}'):]
AX_CSS = _c[_c.index('/* Mehr über uns'):_c.index('/* Helle Abschnitte')] + '@media (max-width: 860px){ .ax-in{flex-direction:column;align-items:flex-start} }\n'
_j = home.JS
AX_JS = _j[_j.index('/* Mehr über uns'):_j.index('/* Scroll-Passage')]
BUILD_JS = _j[_j.index('/* Scroll-Passage'):]

STAR = '<svg class="sb" viewBox="0 0 40 40" aria-hidden="true"><path d="M20 0l3.6 11.3L34.1 5.9l-5.4 10.5L40 20l-11.3 3.6 5.4 10.5-10.5-5.4L20 40l-3.6-11.3-10.5 5.4 5.4-10.5L0 20l11.3-3.6L5.9 5.9l10.5 5.4z"/></svg>'

def band(words):
    one = ''.join(f'<span>{w}</span>{STAR}' for w in words)
    return f'<div class="bd-track"><div class="bd-run">{one}</div></div>'

def badge(pid, text):
    return f'''<svg class="bdg-ring" viewBox="0 0 200 200" aria-hidden="true"><defs><path id="{pid}" d="M100,100 m-76,0 a76,76 0 1,1 152,0 a76,76 0 1,1 -152,0"/></defs><text><textPath href="#{pid}" textLength="474">{text}</textPath></text></svg>'''

BIG_ARROW = '<svg class="bdg-ar" viewBox="0 0 40 40" aria-hidden="true"><path d="M9 31L31 9M14 9h17v17" fill="none" stroke="currentColor" stroke-width="3.2" stroke-linecap="square"/></svg>'

CH = '<svg viewBox="0 0 32 32" aria-hidden="true"><rect x=".5" y=".5" width="31" height="31" rx="7" fill="rgba(255,255,255,.12)" stroke="rgba(255,255,255,.5)"/><path d="M13 6h6v7h7v6h-7v7h-6v-7H6v-6h7z" fill="#fff"/></svg>'

LAMPS = ''.join(f'<div class="d-p"><i class="lamp l{i}"></i><span>{n}</span><b>CHF {p}</b></div>' for i, (n, p) in enumerate([('Pendel Opal', "289.–"), ('Tischleuchte Kugel', "149.–"), ('Stehleuchte Bogen', "540.–"), ('Wandleuchte Messing', "198.–")], 1))

MOCK_A = '''<div class="mk mk-a">
  <div class="a-nav"><b>Brunner</b><span>Backstube</span><span>Café</span><span>Torten</span><span>Kontakt</span><i>Torte bestellen</i></div>
  <div class="a-hero">
    <div class="a-copy"><small>Bäckerei in Brugg, seit 1961</small><h4>Brot wie früher. <em>Jeden Morgen ab sechs.</em></h4><p>Sauerteig, viel Zeit und Mehl aus der Region. Bestellen Sie bis 18 Uhr, abholen am nächsten Morgen.</p><i>Online bestellen</i></div>
    <div class="a-img"><img id="im-baeckerei" src="%%I_baeckerei%%" alt="Frische Brote auf dem Tisch"></div>
  </div>
  <div class="a-list"><span>Buttergipfeli<b>1.80</b></span><span>Zopf, 500 g<b>6.50</b></span><span>Ruchbrot<b>4.90</b></span><span>Nussgipfel<b>3.20</b></span></div>
</div>'''

MOCK_B = '''<div class="mk mk-b">
  <div class="b-nav"><span>Salon Nord</span><span class="b-ln">Preise&nbsp;&nbsp;Team&nbsp;&nbsp;Kontakt</span><i>Termin buchen</i></div>
  <div class="b-img"><img id="im-coiffeur" src="%%I_coiffeur%%" alt="Haarschnitt im Salon"></div>
  <div class="b-big">Salon<br>Nord</div>
  <div class="b-side"><p>Schnitt, Farbe und Bart. Zürich Kreis 4, Dienstag bis Samstag.</p><i>Freie Termine ansehen</i></div>
</div>'''

MOCK_C = '''<div class="mk mk-c">
  <div class="c-img"><img id="im-restaurant" src="%%I_restaurant%%" alt="Koch beim Anrichten"></div>
  <div class="c-main">
    <div class="c-nav"><b>Sonne</b><span>Karte</span><span>Mittag</span><span>Anlässe</span><i>Tisch reservieren</i></div>
    <h4>Gekocht wird, was die Saison bringt.</h4>
    <div class="c-menu"><h5>Mittagsmenü heute</h5><span>Kürbissuppe mit Kernöl<b>9.50</b></span><span>Kalbsbratwurst, Zwiebelsauce, Rösti<b>24.50</b></span><span>Risotto mit Waldpilzen<b>22.00</b></span></div>
    <small>Restaurant Sonne, Aarau&nbsp;&nbsp;·&nbsp;&nbsp;Dienstag bis Samstag</small>
  </div>
</div>'''

MOCK_D = '''<div class="mk mk-d">
  <div class="d-nav"><b>LUMEN</b><span>Pendel</span><span>Tisch</span><span>Stehend</span><span>Laden</span><i>Warenkorb (2)</i></div>
  <div class="d-hero"><img id="im-laden2" src="%%I_laden2%%" alt="Schaufenster eines Leuchtenladens"><div class="d-hc"><small>Leuchtenladen in Basel</small><h4>Licht für jeden Raum.</h4></div></div>
  <div class="d-grid">''' + LAMPS + '''</div>
</div>'''

def frame(url, mock):
    return f'<div class="mf"><div class="mf-bar"><i></i><i></i><i></i><span>{url}</span></div>{mock}</div>'

CAFE = '''<div class="cf" id="cf">
  <header class="cf-nav"><b class="cf-logo">Café Linde</b><nav><span>Frühstück</span><span>Mittag</span><span>Rösterei</span><span>Kontakt</span></nav><i class="cf-res">Tisch reservieren</i><span class="cf-burger"><i></i><i></i><i></i></span></header>
  <div class="cf-hero">
    <div class="cf-copy"><small>Café und Rösterei in Baden</small><h4>Kaffee aus der eigenen Rösterei.</h4><p>Frühstück bis halb zwölf, mittags zwei Menüs, am Nachmittag Kuchen aus der Backstube nebenan.</p><i class="cf-btn">Tisch reservieren</i></div>
    <div class="cf-img"><img id="im-cafe" src="%%I_cafe%%" alt="Barista hinter der Theke"></div>
  </div>
  <div class="cf-cards">
    <div><b>Frühstück</b><span>Mo bis Sa, 7 bis 11.30 Uhr</span></div>
    <div><b>Mittagsmenü</b><span>Zwei Menüs, ab CHF 19.50</span></div>
    <div><b>Bohnen zum Mitnehmen</b><span>Frisch geröstet, 250 g</span></div>
  </div>
</div>'''

SERVICES = [
    ('websites', 'Websites', 'Gestaltet für Ihren Betrieb, gebaut für Handy und Bildschirm, mit Texten, die Ihre Kunden verstehen.', 'cob'),
    ('shops', 'Online-Shops', 'Produkte, Zahlung mit TWINT und Karte, Versand und Rechnungen. Sie verwalten alles selbst.', 'tan'),
    ('seo', 'SEO und Google Ads', 'Damit man Sie findet, wenn jemand in Ihrer Region nach Ihrem Angebot sucht.', 'pnk'),
    ('hosting', 'Hosting und Domains', 'Bei Infomaniak in Genf. Mit Backups, Updates und E-Mail-Adressen auf Ihre Domain.', 'but'),
    ('m365', 'Microsoft 365', 'E-Mail, Kalender und Dateien für Ihr Team. Eingerichtet und betreut.', 'sag'),
]
SV = ''.join(f'<li class="sv-{c}"><a href="leistungen.html#{a}"><span class="sv-n">0{i}</span><span class="sv-t">{t}</span><span class="sv-d">{d}</span><span class="sv-ar">{ARROW}</span></a></li>' for i, (a, t, d, c) in enumerate(SERVICES, 1))

MAIN = '''
  <section class="xh" id="hero">
    <div class="xh-glow" aria-hidden="true"><i></i><i></i><i></i><i></i></div>
    <div class="xh-meta pad"><span>Webagentur für KMU</span><span class="geo">Server: 46.20° N, 6.14° O, Genf</span></div>
    <h1 class="xh-t pad" aria-label="Websites und Online-Shops für KMU.">
      <span class="fl" aria-hidden="true"><span class="fi">Websites</span></span>
      <span class="fl o" aria-hidden="true"><span class="fi">&amp; Online-Shops</span></span>
      <span class="fl p" aria-hidden="true"><span class="fi">für KMU.</span></span>
    </h1>
    <div class="stks" aria-hidden="false">
      <a class="stk s-badge" href="kontakt.html" aria-label="Termin wählen, 15 Minuten, gratis" style="--r:-8deg"><span class="stk-in"><span class="bdg glass">''' + badge('bc1', 'TERMIN WÄHLEN * 15 MINUTEN * GRATIS * ') + BIG_ARROW + '''</span></span></a>
      <div class="stk s-shot" style="--r:-5deg" aria-hidden="true"><span class="stk-in"><span class="shot-g glass"><span class="shot"><span class="shot-bar"><i></i><i></i><i></i><em>cafe-linde.ch</em></span><img data-from="cafe" alt=""><span class="shot-cap"><b>Kaffee aus der eigenen Rösterei.</b><u>Tisch reservieren</u></span></span></span></span></div>
      <div class="stk s-phone" style="--r:7deg" aria-hidden="true"><span class="stk-in"><span class="phone glass"><span class="ph-in"><span class="ph-nav">SALON NORD<i></i></span><img data-from="coiffeur" alt=""><span class="ph-t">Schnitt, Farbe, Bart.</span><span class="ph-b">Termin buchen</span></span></span></span></div>
      <div class="stk s-ch" style="--r:-11deg" aria-hidden="true"><span class="stk-in"><span class="ch glass">''' + CH + '''<span>Daten bleiben<br>in der Schweiz</span></span></span></div>
      <div class="stk s-drag" style="--r:4deg" aria-hidden="true"><span class="stk-in"><span class="drag glass">Zum Verschieben<svg viewBox="0 0 60 30" aria-hidden="true"><path d="M2 26C14 6 34 2 52 10M44 3l9 7-10 5" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg></span></span></div>
    </div>
    <div class="xh-row pad">
      <p>Wir gestalten und bauen Websites und Online-Shops für Betriebe in der ganzen Schweiz. Mit festem Preis, einer Ansprechperson und Servern in Genf.</p>
      <div class="xh-acts"><a class="xbtn xbtn-paper" href="kontakt.html">Termin wählen ''' + ARROW + '''</a><a class="xbtn xbtn-glass glass" href="#muster">Muster ansehen</a></div>
    </div>
  </section>

  <div class="bands" aria-hidden="true">
    <div class="bd bd-1" data-dir="-1">''' + band(['Websites', 'Online-Shops', 'SEO', 'Google Ads', 'Hosting in Genf', 'Microsoft 365']) + '''</div>
    <div class="bd bd-2" data-dir="1">''' + band(['Fester Preis', 'Eine Ansprechperson', 'Daten in der Schweiz', '15 Minuten gratis', 'Updates inklusive']) + '''</div>
  </div>

  <section class="rz pad" id="geraete" aria-labelledby="rzT">
    <div class="rz-head">
      <h2 class="xd" id="rzT">Passt auf<br>jedes Gerät.</h2>
      <div class="rz-txt">
        <p>Ziehen Sie das Fenster schmaler. Genau so verhält sich jede Website, die wir bauen: auf dem Handy, dem Tablet und dem grossen Bildschirm.</p>
        <div class="rz-read glass-l"><b id="rzW">1200 px</b><span id="rzD">Bildschirm</span></div>
      </div>
    </div>
    <div class="rz-stage" id="rzStage">
      <div class="rz-box" id="rzBox">
        <div class="rz-frame" id="rzFrame"><div class="mf-bar"><i></i><i></i><i></i><span>cafe-linde.ch</span></div><div class="rz-site" id="rzSite">''' + CAFE + '''</div></div>
        <button class="rz-h" id="rzH" type="button" aria-label="Fensterbreite ändern"><i></i><i></i></button>
      </div>
    </div>
    <label class="rz-sl"><span>Breite</span><input type="range" id="rzR" min="360" max="1200" value="1200" step="1"></label>
  </section>

  ''' + BUILD + '''

  <section class="ms" id="muster" aria-labelledby="msT">
    <div class="ms-sticky">
      <div class="ms-track" id="msTrack">
        <div class="ms-intro">
          <h2 class="xd" id="msT">Muster&shy;seiten.</h2>
          <p>Damit Sie sehen, wie wir arbeiten: vier Beispiele für Branchen, mit denen wir oft zu tun haben. Die Betriebe sind erfunden. Ihre Website gestalten wir eigens für Sie.</p>
          <span class="ms-cnt"><b id="msN">01</b> / 04</span>
        </div>
        <article class="ms-card" style="--t:-2deg"><span class="ms-tag glass-l">Muster</span>''' + frame('baeckerei-brunner.ch', MOCK_A) + '''<div class="ms-cap"><span class="ms-no">01</span><h3>Bäckerei</h3><p>5 Seiten, Bestellformular, Öffnungszeiten</p></div></article>
        <article class="ms-card" style="--t:1.5deg"><span class="ms-tag glass-l">Muster</span>''' + frame('salon-nord.ch', MOCK_B) + '''<div class="ms-cap"><span class="ms-no">02</span><h3>Coiffeur</h3><p>4 Seiten, Online-Termine, Preisliste</p></div></article>
        <article class="ms-card" style="--t:-1deg"><span class="ms-tag glass-l">Muster</span>''' + frame('sonne-aarau.ch', MOCK_C) + '''<div class="ms-cap"><span class="ms-no">03</span><h3>Restaurant</h3><p>6 Seiten, Tagesmenü, Reservation</p></div></article>
        <article class="ms-card" style="--t:2deg"><span class="ms-tag glass-l">Muster</span>''' + frame('lumen-leuchten.ch', MOCK_D) + '''<div class="ms-cap"><span class="ms-no">04</span><h3>Laden mit Shop</h3><p>Online-Shop, TWINT, Abholung im Laden</p></div></article>
      </div>
    </div>
  </section>

  <section class="nm pad" aria-labelledby="nmT">
    <div class="nm-glow" aria-hidden="true"><i></i><i></i><i></i></div>
    <h2 class="xd" id="nmT">Drei Zahlen.</h2>
    <div class="nm-grid">
      <div class="nm-i glass"><span class="nm-v"><b data-to="15">15</b><small>Min.</small></span><p><strong>Das erste Gespräch.</strong> Gratis und ohne Verpflichtung. Danach bekommen Sie eine Offerte mit festem Preis.</p></div>
      <div class="nm-i glass"><span class="nm-v"><b data-to="1">1</b><small>Person</small></span><p><strong>Ihre Ansprechperson.</strong> Vom ersten Gespräch bis lange nach dem Start. Kein Ticketsystem, keine Warteschlaufe.</p></div>
      <div class="nm-i glass"><span class="nm-v"><b data-to="100">100</b><small>%</small></span><p><strong>Schweiz.</strong> Domains, Hosting und E-Mail bei Infomaniak in Genf. Ihre Daten bleiben im Land.</p></div>
    </div>
    ''' + AX + '''
  </section>

  <section class="xs pad" id="leistungen" aria-labelledby="xsT">
    <div class="xs-head"><h2 class="xd" id="xsT">Was wir<br>machen.</h2><a class="xlink dark" href="leistungen.html">Alle Leistungen</a></div>
    <ul class="xs-list">''' + SV + '''</ul>
  </section>

  <section class="xc pad" id="kontakt-cta" aria-labelledby="xcT">
    <div class="xc-glow" aria-hidden="true"><i></i><i></i></div>
    <h2 class="xc-t" id="xcT" aria-label="Reden wir."><span class="fl" aria-hidden="true"><span class="fi">Reden wir.</span></span></h2>
    <div class="xc-row">
      <div>
        <p>Über Ihre Website, Ihren Shop oder Ihr Hosting. Eine Viertelstunde am Telefon oder per Video, gratis. Danach wissen Sie, was es kostet und wie lange es dauert.</p>
        <span class="mail">hallo@websiten.ch</span>
      </div>
      <a class="xc-badge" href="kontakt.html" aria-label="Termin wählen"><span class="bdg glass">''' + badge('bc2', 'TERMIN WÄHLEN * 15 MINUTEN * GRATIS * ') + BIG_ARROW + '''</span></a>
    </div>
  </section>
'''

CSS = r'''
:root{--cob:#2B37F2;--tan:#83AA8C;--tl:#B3CDB9;--pnk:#FFC4DE;--but:#FFE45E;--pap:#EFF1ED;--k:#0E1513;--disp:"Archivo","Arial Narrow",Impact,sans-serif;--mono:"IBM Plex Mono",ui-monospace,monospace}
.xd{font-family:var(--disp);font-stretch:62%;font-weight:800;text-transform:uppercase;line-height:.84;letter-spacing:-.01em;font-size:clamp(64px,10vw,190px);text-wrap:balance}
.xbtn{display:inline-flex;align-items:center;gap:12px;padding:17px 28px;border-radius:999px;font-size:17px;font-weight:600;white-space:nowrap;transition:transform .3s var(--ease),background .25s,color .25s}
.xbtn:hover{transform:translateY(-2px) rotate(-1deg)}
.xbtn svg{transition:transform .3s var(--ease)}
.xbtn:hover svg{transform:translateX(4px)}
.xbtn-paper{background:var(--pap);color:var(--k)}
.xbtn-paper:hover{background:#fff}
.xlink{font-size:17px;font-weight:500;border-bottom:2px solid currentColor;padding-bottom:3px;transition:opacity .2s}
.xlink:hover{opacity:.7}

/* Hero */
.xh{position:relative;min-height:max(100svh,700px);background:var(--cob);color:var(--pap);display:flex;flex-direction:column;padding-top:calc(env(safe-area-inset-top,0px) + 108px);padding-bottom:calc(clamp(150px,15vw,230px) / 2 + 36px);overflow:hidden;isolation:isolate}
.xh-meta{display:flex;justify-content:space-between;gap:20px;font-family:var(--mono);font-size:13px;letter-spacing:.06em;text-transform:uppercase;opacity:.85}
.xh-t{margin-top:clamp(20px,4vh,48px);font-family:var(--disp);font-stretch:62%;font-weight:800;text-transform:uppercase;line-height:.84;letter-spacing:-.005em;position:relative;z-index:1}
.fl{display:block;white-space:nowrap}
.fi{display:inline-block}
.xh-t .o .fi{color:transparent;-webkit-text-stroke:2px var(--pap)}
.xh-t .p .fi{color:var(--tl)}
.xh-row{margin-top:auto;padding-top:40px;display:flex;justify-content:space-between;align-items:flex-end;gap:32px;flex-wrap:wrap;position:relative;z-index:3}
.xh-row p{font-size:clamp(17px,1.3vw,20px);line-height:1.5;max-width:44ch}
.xh-acts{display:flex;align-items:center;gap:28px;flex-wrap:wrap}

/* Sticker */
.stks{position:absolute;inset:0;z-index:2;pointer-events:none}
.stk{position:absolute;pointer-events:auto;touch-action:none;cursor:grab;user-select:none;-webkit-user-select:none;transform:translate(var(--x,0px),var(--y,0px)) rotate(calc(var(--r,0deg) + var(--w,0deg)));transition:filter .2s}
.stk img{pointer-events:none;-webkit-user-drag:none}
.stk.grab{cursor:grabbing;filter:drop-shadow(0 26px 30px rgba(0,0,30,.35))}
.stk-in{display:block;animation:bob 6s ease-in-out infinite;animation-delay:var(--dl,0s);transition:transform .35s var(--ease)}
.stk.grab .stk-in{animation-play-state:paused;transform:scale(1.06)}
@keyframes bob{50%{translate:0 -8px}}
.s-badge{right:4%;top:17%;--dl:-1s}
.s-shot{right:10%;top:37%;--dl:-3s}
.s-phone{right:3%;top:45%;--dl:-2s}
.s-ch{right:20%;top:20%;--dl:-4s}
.s-hoi{right:32%;top:63%;--dl:-.5s}
.s-drag{right:26%;top:68%;--dl:-5s}
.bdg{position:relative;display:grid;place-items:center;width:clamp(120px,11vw,168px);aspect-ratio:1;border-radius:50%;background:var(--tan);color:var(--k)}
.bdg-ring{position:absolute;inset:0;width:100%;height:100%;animation:spin 14s linear infinite}
.bdg-ring text{font-family:var(--disp);font-stretch:75%;font-weight:800;font-size:21px;letter-spacing:.04em;fill:currentColor}
.bdg-ar{width:34%;height:34%;transition:transform .4s var(--ease)}
.stk:hover .bdg-ar,.xc-badge:hover .bdg-ar{transform:rotate(45deg)}
@keyframes spin{to{transform:rotate(360deg)}}
.shot{display:block;width:clamp(200px,17vw,260px);background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 30px 60px -20px rgba(0,0,40,.55);color:#2A1F17}
.shot-bar{display:flex;align-items:center;gap:5px;padding:8px 10px;background:#EEE9E1}
.shot-bar i{width:8px;height:8px;border-radius:50%;background:#D6CEC2}
.shot-bar em{font-style:normal;font-family:var(--mono);font-size:10.5px;color:#7A6E62;margin-left:8px}
.shot img{display:block;width:100%;aspect-ratio:16/10;object-fit:cover}
.shot-cap{display:flex;flex-direction:column;gap:8px;padding:12px 14px 14px;font-family:Fraunces,Georgia,serif}
.shot-cap b{font-size:17px;line-height:1.15;font-weight:600}
.shot-cap u{text-decoration:none;align-self:flex-start;background:#2A1F17;color:#F7F1E8;font:600 11px var(--sans);padding:6px 11px;border-radius:99px}
.phone{display:block;width:clamp(110px,9vw,140px);aspect-ratio:9/19;background:#0B0B0B;border-radius:22px;padding:6px;box-shadow:0 30px 60px -20px rgba(0,0,40,.6)}
.ph-in{display:flex;flex-direction:column;height:100%;border-radius:17px;overflow:hidden;background:#0B0B0B;color:#fff}
.ph-nav{display:flex;justify-content:space-between;align-items:center;padding:16px 10px 8px;font-family:var(--disp);font-stretch:62%;font-weight:800;font-size:15px;letter-spacing:.02em}
.ph-nav i{width:14px;height:8px;border-top:2px solid #fff;border-bottom:2px solid #fff}
.phone img{width:100%;flex:1;min-height:0;object-fit:cover}
.ph-t{font-family:var(--disp);font-stretch:62%;font-weight:800;text-transform:uppercase;font-size:17px;line-height:.9;padding:10px 10px 6px}
.ph-b{margin:0 10px 12px;background:#EDE3D6;color:#0B0B0B;font-size:10px;font-weight:700;text-align:center;padding:6px;border-radius:99px}
.ch{display:flex;flex-direction:column;align-items:center;gap:8px}
.ch svg{width:clamp(64px,5.4vw,84px);height:auto;filter:drop-shadow(0 12px 18px rgba(0,0,40,.35))}
.ch span{background:var(--pap);color:var(--k);font-family:var(--mono);font-size:11px;line-height:1.3;text-align:center;padding:6px 10px;border-radius:4px;text-transform:uppercase;letter-spacing:.04em}
.hoi{position:relative;display:grid;place-items:center;width:clamp(96px,8vw,124px);aspect-ratio:1}
.hoi-s{position:absolute;inset:0;width:100%;height:100%;fill:var(--but);animation:spin 30s linear infinite reverse}
.hoi b{position:relative;font-family:var(--disp);font-stretch:62%;font-weight:800;font-size:clamp(30px,2.6vw,40px);color:var(--k);text-transform:uppercase}
.drag{display:inline-flex;align-items:center;gap:8px;background:var(--pnk);color:var(--k);font-family:var(--mono);font-size:12.5px;font-weight:500;padding:9px 14px;border-radius:6px;text-transform:uppercase;letter-spacing:.04em}
.drag svg{width:34px;height:17px}

/* Bänder */
.bands{position:relative;z-index:4;height:clamp(150px,15vw,230px);margin-top:calc(clamp(150px,15vw,230px) / -2);margin-bottom:calc(clamp(150px,15vw,230px) / -2);pointer-events:none;overflow:hidden}
.bd{position:absolute;left:-5%;right:-5%;top:50%;padding:clamp(10px,1vw,16px) 0;overflow:hidden;box-shadow:0 18px 40px -18px rgba(0,0,0,.4)}
.bd-1{background:var(--tan);color:var(--k);transform:translateY(-62%) rotate(-3.4deg)}
.bd-2{background:var(--but);color:var(--k);transform:translateY(-38%) rotate(2.6deg)}
.bd-track{display:flex;width:max-content;will-change:transform}
.bd-run{display:flex;align-items:center;flex:none}
.bd-run span{font-family:var(--disp);font-stretch:62%;font-weight:800;text-transform:uppercase;font-size:clamp(34px,3.6vw,64px);line-height:1;padding:0 clamp(16px,1.6vw,28px);white-space:nowrap}
.sb{width:clamp(22px,2vw,34px);height:auto;flex:none;fill:currentColor}
.bd-2 .sb{fill:var(--tan)}

/* Fenster zum Ziehen */
.rz{background:var(--pap);color:var(--k);padding-top:clamp(150px,16vw,260px);padding-bottom:clamp(80px,9vw,140px);overflow:hidden}
.rz-head{display:grid;grid-template-columns:minmax(0,1.2fr) minmax(0,1fr);gap:40px;align-items:end}
.rz-txt p{font-size:clamp(17px,1.35vw,21px);line-height:1.55;max-width:40ch}
.rz-read{display:flex;align-items:baseline;gap:14px;margin-top:22px;font-family:var(--mono);font-size:14px;text-transform:uppercase;letter-spacing:.05em}
.rz-read b{font-family:var(--disp);font-stretch:62%;font-weight:800;font-size:44px;letter-spacing:0;font-variant-numeric:tabular-nums;min-width:4.2ch}
.rz-read span{background:var(--k);color:var(--pap);padding:4px 10px;border-radius:99px}
.rz-stage{margin-top:clamp(40px,5vw,72px);position:relative}
.rz-box{position:relative;display:inline-block;vertical-align:top}
.rz-frame{border-radius:14px;overflow:hidden;background:#fff;border:2px solid var(--k);box-shadow:14px 14px 0 var(--k)}
.mf-bar{display:flex;align-items:center;gap:6px;padding:10px 14px;background:#E9E3D8;border-bottom:2px solid var(--k)}
.mf-bar i{width:10px;height:10px;border-radius:50%;background:#C9BFB0}
.mf-bar i:first-child{background:var(--tan)}
.mf-bar i:nth-child(2){background:#C9BFB0}
.mf-bar span{font-family:var(--mono);font-size:12px;color:#5D554B;margin-left:10px}
.rz-site{height:560px;overflow:hidden;position:relative}
.rz-site .cf{transform-origin:0 0}
.rz-h{position:absolute;top:50%;right:-30px;width:44px;height:96px;margin-top:-48px;border-radius:99px;background:var(--tan);border:2px solid var(--k);cursor:ew-resize;display:flex;align-items:center;justify-content:center;gap:5px;touch-action:none;transition:transform .2s var(--ease)}
.rz-h:hover{transform:scale(1.08)}
.rz-h i{width:3px;height:34px;background:var(--k);border-radius:2px}
.rz-sl{display:none;align-items:center;gap:14px;margin-top:28px;font-family:var(--mono);font-size:13px;text-transform:uppercase}
.rz-sl input{flex:1;accent-color:var(--tan)}

/* Café Linde: echte responsive Seite im Fenster */
.cf{container-type:inline-size;background:#FBF7F0;color:#2A1F17;font-family:var(--sans);height:100%;width:100%}
.cf i{font-style:normal}
.cf-nav{display:flex;align-items:center;gap:28px;padding:18px 32px;border-bottom:1px solid #E7DED0}
.cf-logo{font-family:Fraunces,Georgia,serif;font-size:24px;font-weight:600;letter-spacing:-.02em;margin-right:auto}
.cf-nav nav{display:flex;gap:24px;font-size:14.5px;color:#5C4E40}
.cf-res{background:#2A1F17;color:#FBF7F0;font-size:13.5px;font-weight:600;padding:9px 16px;border-radius:99px}
.cf-burger{display:none;width:22px;height:14px;position:relative}
.cf-burger i{position:absolute;left:0;right:0;height:2px;background:#2A1F17}
.cf-burger i:nth-child(1){top:0}.cf-burger i:nth-child(2){top:6px}.cf-burger i:nth-child(3){top:12px}
.cf-hero{display:grid;grid-template-columns:1fr 1.05fr;gap:40px;align-items:center;padding:44px 32px 32px}
.cf-copy small{font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#A0522D;font-weight:600}
.cf-copy h4{font-family:Fraunces,Georgia,serif;font-weight:600;font-size:52px;line-height:1.02;letter-spacing:-.03em;margin:14px 0 16px}
.cf-copy p{font-size:16px;line-height:1.55;color:#5C4E40;max-width:36ch}
.cf-btn{display:inline-block;margin-top:22px;background:#A0522D;color:#fff;font-size:14.5px;font-weight:600;padding:12px 20px;border-radius:99px}
.cf-img{border-radius:18px;overflow:hidden;aspect-ratio:4/3}
.cf-img img{width:100%;height:100%;object-fit:cover;display:block}
.cf-cards{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;padding:0 32px 32px}
.cf-cards div{background:#F1E8DA;border-radius:14px;padding:16px 18px;display:flex;flex-direction:column;gap:4px}
.cf-cards b{font-family:Fraunces,Georgia,serif;font-size:18px;font-weight:600}
.cf-cards span{font-size:13.5px;color:#6F6152}
@container (max-width: 900px){
  .cf-nav nav{gap:16px;font-size:13.5px}
  .cf-copy h4{font-size:40px}
  .cf-hero{gap:28px}
}
@container (max-width: 760px){
  .cf-nav{padding:16px 22px}
  .cf-nav nav,.cf-res{display:none}
  .cf-burger{display:block}
  .cf-hero{grid-template-columns:1fr;padding:24px 22px;gap:22px}
  .cf-img{order:-1;aspect-ratio:16/9}
  .cf-copy h4{font-size:38px}
  .cf-cards{grid-template-columns:1fr 1fr;padding:0 22px 22px}
}
@container (max-width: 480px){
  .cf-hero{padding:16px 16px 18px}
  .cf-copy h4{font-size:31px;margin:10px 0 10px}
  .cf-copy p{font-size:15px}
  .cf-btn{display:block;text-align:center}
  .cf-cards{grid-template-columns:1fr;padding:0 16px 16px}
  .cf-logo{font-size:21px}
}

/* Musterseiten: seitlich scrollen */
.ms{position:relative;background:#E3E8E3;color:var(--k)}
.ms-sticky{position:sticky;top:0;height:100vh;overflow:hidden;display:flex;align-items:center}
.ms-track{display:flex;align-items:center;gap:clamp(40px,5vw,90px);padding:0 var(--pad);will-change:transform}
.ms-intro{flex:none;width:min(520px,38vw)}
.ms-intro .xd{font-size:clamp(70px,9.6vw,180px);hyphens:manual}
.ms-intro p{font-size:clamp(17px,1.3vw,20px);line-height:1.55;margin-top:28px;max-width:38ch}
.ms-cnt{display:inline-block;margin-top:30px;font-family:var(--mono);font-size:14px}
.ms-cnt b{font-family:var(--disp);font-stretch:62%;font-size:40px;font-weight:800;font-variant-numeric:tabular-nums}
.ms-card{position:relative;flex:none;width:min(62vw,calc((100vh - 230px) * 1.6),1060px);transform:rotate(var(--t));transition:transform .5s var(--ease)}
.ms-card:hover{transform:rotate(0) scale(1.01)}
.mf{border:2px solid var(--k);border-radius:14px;overflow:hidden;background:#fff;box-shadow:12px 12px 0 var(--k)}
.ms-tag{position:absolute;z-index:2;top:-16px;right:28px;background:var(--but);color:var(--k);font-family:var(--mono);font-size:12.5px;font-weight:500;text-transform:uppercase;letter-spacing:.08em;padding:7px 14px;border:2px solid var(--k);border-radius:6px;transform:rotate(5deg)}
.ms-cap{display:flex;align-items:baseline;gap:18px;margin-top:26px;flex-wrap:wrap}
.ms-no{font-family:var(--mono);font-size:14px}
.ms-cap h3{font-family:var(--disp);font-stretch:62%;font-weight:800;text-transform:uppercase;font-size:clamp(40px,4.2vw,76px);line-height:.85}
.ms-cap p{font-size:15.5px;margin-left:auto}

/* Gemeinsame Basis der Muster */
.mk{container-type:inline-size;aspect-ratio:16/10;position:relative;overflow:hidden}
.mk i{font-style:normal}
.mk img{display:block;width:100%;height:100%;object-fit:cover}
/* A Bäckerei */
.mk-a{background:#F4EBDD;color:#3B2A1E;font-family:Fraunces,Georgia,serif;display:grid;grid-template-rows:auto 1fr auto}
.a-nav{display:flex;align-items:center;gap:2.6cqw;padding:2.2cqw 3.4cqw;font-family:var(--sans);font-size:1.3cqw;color:#6A5442}
.a-nav b{font-family:Fraunces,Georgia,serif;font-style:italic;font-size:2.6cqw;color:#3B2A1E;margin-right:auto}
.a-nav i{background:#3B2A1E;color:#F4EBDD;padding:.8cqw 1.6cqw;border-radius:99px;font-weight:600}
.a-hero{display:grid;grid-template-columns:1fr 1fr;gap:3cqw;padding:1cqw 3.4cqw;align-items:center;min-height:0}
.a-copy small{font-family:var(--sans);font-size:1.15cqw;letter-spacing:.14em;text-transform:uppercase;color:#B0602C;font-weight:600}
.a-copy h4{font-size:5cqw;line-height:1;font-weight:600;letter-spacing:-.03em;margin:1.4cqw 0}
.a-copy h4 em{color:#B0602C}
.a-copy p{font-family:var(--sans);font-size:1.45cqw;line-height:1.5;color:#6A5442;max-width:34ch}
.a-copy i{display:inline-block;margin-top:2cqw;font-family:var(--sans);font-size:1.35cqw;font-weight:600;background:#B0602C;color:#fff;padding:1cqw 2cqw;border-radius:99px}
.a-img{height:100%;max-height:34cqw;border-radius:1.6cqw;overflow:hidden}
.a-list{display:grid;grid-template-columns:repeat(4,1fr);border-top:1px solid #DCCDB8;margin:0 3.4cqw;padding:1.6cqw 0 2.2cqw;font-family:var(--sans);font-size:1.35cqw;gap:2cqw}
.a-list span{display:flex;justify-content:space-between;border-right:1px solid #DCCDB8;padding-right:2cqw}
.a-list span:last-child{border:0}
/* B Coiffeur */
.mk-b{background:#0C0C0C;color:#fff;font-family:var(--sans)}
.b-nav{position:absolute;z-index:3;left:0;right:0;top:0;display:flex;align-items:center;gap:3cqw;padding:2.2cqw 3cqw;font-size:1.35cqw}
.b-nav > span:first-child{font-family:var(--disp);font-stretch:62%;font-weight:800;font-size:2.4cqw;text-transform:uppercase;letter-spacing:.02em;margin-right:auto}
.b-nav i{background:#EDE3D6;color:#0C0C0C;font-weight:700;padding:.8cqw 1.8cqw;border-radius:99px}
.b-img{position:absolute;right:0;top:0;bottom:0;width:54%}
.b-img::after{content:"";position:absolute;inset:0;background:linear-gradient(90deg,#0C0C0C,transparent 40%)}
.b-big{position:absolute;z-index:2;left:3cqw;top:10cqw;font-family:var(--disp);font-stretch:62%;font-weight:800;text-transform:uppercase;font-size:17cqw;line-height:.8;letter-spacing:-.01em}
.b-side{position:absolute;z-index:2;left:3.4cqw;bottom:3.4cqw;width:36cqw;display:flex;flex-direction:column;gap:1.6cqw;font-size:1.6cqw;line-height:1.45;color:#D9D9D9}
.b-side i{align-self:flex-start;border:1px solid #EDE3D6;color:#EDE3D6;padding:.9cqw 1.8cqw;border-radius:99px;font-weight:600;font-size:1.35cqw}
/* C Restaurant */
.mk-c{background:#1E3A2B;color:#F3EBDD;display:grid;grid-template-columns:38% 1fr;font-family:var(--sans)}
.c-img{height:100%;min-height:0}
.c-main{display:flex;flex-direction:column;padding:2.4cqw 3.4cqw 2.6cqw;min-width:0}
.c-nav{display:flex;align-items:center;gap:2.4cqw;font-size:1.3cqw;color:#C9D4C4}
.c-nav b{font-family:Newsreader,Georgia,serif;font-size:3cqw;font-weight:500;color:#F3EBDD;margin-right:auto;font-style:italic}
.c-nav i{border:1px solid #D88A4B;color:#F2B482;padding:.8cqw 1.6cqw;border-radius:99px;font-weight:600}
.c-main h4{font-family:Newsreader,Georgia,serif;font-weight:500;font-size:4.6cqw;line-height:1.02;letter-spacing:-.02em;margin:5cqw 0 3cqw;max-width:16ch}
.c-menu{background:#F3EBDD;color:#1E3A2B;border-radius:1.4cqw;padding:2cqw 2.4cqw;display:flex;flex-direction:column;gap:1cqw;font-size:1.45cqw}
.c-menu h5{font-family:Newsreader,Georgia,serif;font-size:2cqw;font-weight:500;color:#B5652B}
.c-menu span{display:flex;justify-content:space-between;gap:2cqw;border-top:1px dashed #C7BBA6;padding-top:1cqw}
.c-main small{margin-top:auto;font-size:1.2cqw;color:#9FB09B;letter-spacing:.05em}
/* D Laden */
.mk-d{background:#fff;color:#1D2A6B;font-family:var(--sans);display:grid;grid-template-rows:auto 1fr auto}
.d-nav{display:flex;align-items:center;gap:2.6cqw;padding:2cqw 3cqw;font-size:1.3cqw;border-bottom:1px solid #E4E7F2}
.d-nav b{font-size:2.3cqw;letter-spacing:.3em;margin-right:auto;font-weight:700}
.d-nav i{background:#1D2A6B;color:#fff;padding:.8cqw 1.6cqw;border-radius:99px;font-weight:600}
.d-hero{position:relative;margin:2cqw 3cqw 0;border-radius:1.4cqw;overflow:hidden;min-height:0}
.d-hc{position:absolute;left:2.4cqw;bottom:2.2cqw;background:#fff;border-radius:1.2cqw;padding:1.6cqw 2.2cqw}
.d-hc small{font-size:1.15cqw;letter-spacing:.12em;text-transform:uppercase;color:#E2683C;font-weight:700}
.d-hc h4{font-size:3.4cqw;line-height:1;font-weight:700;letter-spacing:-.03em;margin-top:.6cqw}
.d-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:1.6cqw;padding:2cqw 3cqw 2.4cqw}
.d-p{display:grid;grid-template-columns:auto 1fr;grid-template-rows:auto auto;column-gap:1.2cqw;align-items:center;font-size:1.25cqw}
.d-p b{font-weight:700;color:#E2683C}
.lamp{grid-row:span 2;width:5cqw;height:5cqw;border-radius:1cqw;background:#F1F2F8;position:relative}
.lamp::before,.lamp::after{content:"";position:absolute;left:50%;transform:translateX(-50%)}
.l1::before{top:0;width:1px;height:45%;background:#1D2A6B}.l1::after{top:42%;width:58%;height:34%;border-radius:50% 50% 8% 8%;background:#F4E6C8;box-shadow:0 0 0 1px #E0C98F}
.l2::after{bottom:18%;width:46%;height:46%;border-radius:50%;background:#FFE7A8}.l2::before{bottom:14%;width:30%;height:6%;background:#1D2A6B;border-radius:2px}
.l3::before{bottom:12%;width:1px;height:70%;background:#1D2A6B;left:40%}.l3::after{top:12%;left:60%;width:34%;height:20%;border-radius:50% 50% 10% 10%;background:#E2683C}
.l4::after{top:28%;width:40%;height:40%;border-radius:50%;background:#D9B25E}.l4::before{top:44%;left:22%;width:20%;height:8%;background:#1D2A6B}

/* Drei Zahlen */
.nm{background:#0A0F0D;color:var(--pap);padding-top:clamp(100px,11vw,180px);padding-bottom:clamp(90px,10vw,160px)}
.nm-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));margin-top:clamp(48px,6vw,90px)}
.nm-i{padding:28px clamp(16px,2.4vw,40px) 10px 0;border-right:2px solid var(--k)}
.nm-i + .nm-i{padding-left:clamp(16px,2.4vw,40px)}
.nm-i:last-child{border-right:0}
.nm-v{display:flex;align-items:flex-start;gap:10px;font-family:var(--disp);font-stretch:62%;font-weight:800;line-height:.8}
.nm-v b{font-size:clamp(110px,13vw,250px);letter-spacing:-.02em;font-variant-numeric:tabular-nums}
.nm-v small{font-size:clamp(26px,2.4vw,44px);text-transform:uppercase;margin-top:.3em}
.nm-i p{font-size:17px;line-height:1.55;margin-top:24px;max-width:34ch}
.nm .ax{margin-top:clamp(56px,6vw,90px)}
.nm .ax-btn{color:var(--pap);font-weight:600}
.nm .ax-btn:hover{color:var(--tl)}
.nm .ax-base{stroke:var(--pap)}
.nm .ax-loop{stroke:var(--tl);stroke-width:2}
.nm .ax-dot{fill:var(--tan)}
.nm .ax.open .ax-base{stroke:var(--tl)}
.nm .ax-desc{color:#D8D6D2}
.nm .ax-links a{color:var(--pap)}
.nm .ax-links a:hover{color:var(--tl)}
.nm .ax-links .ic{color:var(--tl)}

/* Leistungen */
.xs{background:var(--pap);color:var(--k);padding-top:clamp(100px,11vw,180px);padding-bottom:clamp(90px,10vw,160px)}
.xs-head{display:flex;justify-content:space-between;align-items:flex-end;gap:24px;flex-wrap:wrap}
.xs-list{list-style:none;margin:clamp(48px,6vw,90px) 0 0;padding:0;border-top:2px solid var(--k)}
.xs-list li{border-bottom:2px solid var(--k)}
.xs-list a{position:relative;display:grid;grid-template-columns:70px minmax(0,1fr) minmax(0,30ch) 40px;align-items:center;gap:24px;padding:clamp(18px,2vw,30px) 0;isolation:isolate;overflow:hidden}
.xs-list a::before{content:"";position:absolute;inset:0 calc(var(--pad) * -1);z-index:-1;background:var(--c);transform:scaleY(0);transform-origin:bottom;transition:transform .5s cubic-bezier(.7,0,.2,1)}
.xs-list a:hover::before,.xs-list a:focus-visible::before{transform:none}
.xs-list li{--c:var(--k);--f:var(--pap)}
.xs-list a:hover .sv-ar{color:var(--tl)}
.xs-list a:hover{color:var(--f)}
.sv-n{font-family:var(--mono);font-size:14px}
.sv-t{font-family:var(--disp);font-stretch:62%;font-weight:800;text-transform:uppercase;font-size:clamp(46px,6.6vw,124px);line-height:.86;transition:transform .5s var(--ease)}
.xs-list a:hover .sv-t{transform:translateX(24px)}
.sv-d{font-size:16px;line-height:1.5}
.sv-ar{justify-self:end;transition:transform .4s var(--ease)}
.sv-ar svg{width:30px;height:20px}
.xs-list a:hover .sv-ar{transform:rotate(-45deg)}

/* Schluss */
.xc{background:var(--tan);color:var(--k);padding-top:clamp(100px,11vw,180px);padding-bottom:clamp(80px,9vw,140px);overflow:hidden}
.xc-t{font-family:var(--disp);font-stretch:62%;font-weight:800;text-transform:uppercase;line-height:.82}
.xc-row{display:grid;grid-template-columns:minmax(0,1fr) auto;gap:40px;align-items:end;margin-top:clamp(40px,5vw,72px);padding-top:32px;border-top:2px solid var(--k)}
.xc-row p{font-size:clamp(18px,1.5vw,22px);line-height:1.5;max-width:42ch;margin-bottom:28px}
.xc .mail{border-color:var(--k)}
.xc-badge{display:block;transition:transform .3s var(--ease)}
.xc-badge .bdg{width:clamp(150px,15vw,220px);background:var(--k);color:var(--pap)}
.xc-badge:hover .bdg{background:var(--cob)}

/* Passage etwas bunter */
.build .bp b{background:var(--tan)}

@media (max-width: 860px){
  .xh{min-height:0;padding-top:calc(env(safe-area-inset-top,0px) + 96px)}
  .xh-meta .geo{display:none}
  .stks{position:relative;inset:auto;height:390px;margin-top:14px}
  .s-badge{right:3%;top:0}
  .s-shot{left:1%;right:auto;top:24px}
  .s-phone{right:6%;top:134px}
  .s-ch,.s-drag{display:none}
  .s-hoi{left:46%;right:auto;top:200px}
  .s-drag{left:30%;right:auto;top:6px}
  .shot{width:200px}
  .xh-row{padding-top:24px}
  .rz-head{grid-template-columns:1fr}
  .rz-h{display:none}
  .rz-sl{display:flex}
  .rz-site{height:520px}
  .ms-sticky{position:relative;height:auto;display:block;padding:clamp(140px,30vw,200px) 0 90px}
  .ms-track{flex-direction:column;align-items:stretch;gap:72px;transform:none!important}
  .ms-intro{width:auto}
  .ms-cnt{display:none}
  .ms-card{width:auto}
  .mf{box-shadow:8px 8px 0 var(--k)}
  .ms-cap p{margin-left:0;width:100%}
  .nm-grid{grid-template-columns:1fr}
  .nm-i{padding:24px 0 28px!important}
  .xs-list a{grid-template-columns:minmax(0,1fr) 30px;gap:8px 12px}
  .sv-n{display:none}
  .sv-d{grid-column:1;font-size:15px}
  .sv-ar{grid-row:1 / span 2;grid-column:2}
  .xc-row{grid-template-columns:1fr}
  .xc-badge{justify-self:start}
}
@media (prefers-reduced-motion: reduce){
  .stk-in,.bdg-ring,.hoi-s{animation:none}
  .ms-sticky{position:relative;height:auto;display:block;padding:120px 0}
  .ms-track{flex-wrap:wrap;transform:none!important}
}

/* Glas-Ebene */
.xh{background:#070B0A}
.xh-glow,.nm-glow,.xc-glow{position:absolute;inset:0;pointer-events:none;overflow:hidden;z-index:0}
.xh-glow i,.nm-glow i,.xc-glow i{position:absolute;border-radius:50%;filter:blur(90px);animation:drift 20s ease-in-out infinite alternate}
.xh-glow i:nth-child(1){width:52vw;height:52vw;left:50%;top:-10%;background:#4F695A;opacity:.8}
.xh-glow i:nth-child(2){width:34vw;height:34vw;left:68%;top:44%;background:#83AA8C;opacity:.4;animation-duration:24s}
.xh-glow i:nth-child(3){width:30vw;height:26vw;left:26%;top:50%;background:#B3CDB9;opacity:.16;animation-duration:17s}
.xh-glow i:nth-child(4){width:36vw;height:30vw;left:-8%;top:-10%;background:#22332C;opacity:.7;animation-duration:28s}
@keyframes drift{0%{transform:translate(0,0) scale(1)}50%{transform:translate(4vw,-3vw) scale(1.12)}100%{transform:translate(-3vw,3vw) scale(.92)}}
.xh > :not(.xh-glow){position:relative}
.xh .stks{position:absolute}
.bdg.glass{background:linear-gradient(135deg,rgba(179,205,185,.42),rgba(79,105,90,.28));border-color:rgba(214,234,220,.5);color:#fff}
.shot-g{display:block;padding:9px;border-radius:18px}
.shot{box-shadow:none}
.phone.glass{background:linear-gradient(135deg,rgba(255,255,255,.28),rgba(255,255,255,.08));padding:7px}
.ch.glass{flex-direction:row;padding:10px 14px 10px 10px;border-radius:18px;gap:12px}
.ch.glass svg{width:40px;filter:none}
.ch.glass span{background:none;color:#fff;padding:0;text-align:left}
.drag.glass{background:linear-gradient(135deg,rgba(255,255,255,.2),rgba(255,255,255,.06));color:#fff;border-radius:99px}
.xbtn-glass{color:#fff}
.xbtn-glass:hover{background:rgba(255,255,255,.26)}
.bd-2{color:var(--pap);background:rgba(14,15,18,.82);-webkit-backdrop-filter:blur(16px) saturate(160%);backdrop-filter:blur(16px) saturate(160%);box-shadow:inset 0 1px 0 rgba(255,255,255,.7),0 18px 40px -18px rgba(0,0,0,.4)}
.rz-read{display:inline-flex;padding:10px 14px 10px 20px;border-radius:99px}
.rz-read b{font-size:36px}
.rz{position:relative}
.rz::before{content:none;position:absolute;width:44vw;height:44vw;right:-12vw;top:14%;border-radius:50%;background:radial-gradient(circle,rgba(255,196,222,.75),transparent 65%);pointer-events:none}
.rz > *{position:relative}
.ms-tag{border:1px solid var(--k);border-radius:99px;top:-18px;background:var(--k);color:var(--pap);transform:rotate(3deg)}
.nm{position:relative;overflow:hidden}
.nm > :not(.nm-glow){position:relative}
.nm-glow i:nth-child(1){width:40vw;height:40vw;left:-6%;top:30%;background:#4F695A;opacity:.75}
.nm-glow i:nth-child(2){width:36vw;height:36vw;left:42%;top:46%;background:#83AA8C;opacity:.3;animation-duration:24s}
.nm-glow i:nth-child(3){width:30vw;height:30vw;left:76%;top:20%;background:#22332C;opacity:.8;animation-duration:30s}
.nm-grid{border-top:0;gap:clamp(14px,1.6vw,24px)}
.nm-i,.nm-i + .nm-i{border:0;border-radius:28px;padding:clamp(24px,2.4vw,40px)}
.nm-i.glass,.nm-i.glass:last-child{border:1px solid rgba(255,255,255,.22)}
.xc{position:relative}
.xc > :not(.xc-glow){position:relative}
.xc-glow i:nth-child(1){width:46vw;height:46vw;left:58%;top:30%;background:#4F695A;opacity:.55}
.xc-glow i:nth-child(2){width:34vw;height:34vw;left:-10%;top:-20%;background:#C9DFCF;opacity:.6;animation-duration:26s}
.xc-badge .bdg.glass{background:linear-gradient(135deg,rgba(18,18,18,.82),rgba(18,18,18,.62));border-color:rgba(255,255,255,.35);color:var(--pap)}
.xc-badge:hover .bdg.glass{background:linear-gradient(135deg,rgba(255,255,255,.95),rgba(255,255,255,.8));color:var(--k)}
@media (max-width: 860px){
  .xh .stks{position:relative}
  .xh-glow i{filter:blur(60px)}
  .xh-glow i:nth-child(1){width:90vw;height:90vw;left:30%;top:10%}
  .xh-glow i:nth-child(2){width:70vw;height:70vw;left:-20%;top:50%}
  .nm-i,.nm-i + .nm-i{padding:24px!important}
}
@media (prefers-reduced-motion: reduce){ .xh-glow i,.nm-glow i,.xc-glow i{animation:none} }
''' + AX_CSS + BUILD_CSS

JS = r'''
const MAP = %%MAP%%;
const MARK_L = '%%ML%%', MARK_D = '%%MD%%';
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
const clamp = (v, a, b) => Math.max(a, Math.min(b, v));

/* Bilder, die mehrfach vorkommen, stehen nur einmal im HTML */
document.querySelectorAll('img[data-from]').forEach(i => { const s = document.getElementById('im-' + i.dataset.from); if(s) i.src = s.src; });

/* Grosse Zeilen auf Breite setzen, mit Obergrenze für die Höhe */
function fitLines(){
  const hero = document.querySelector('.xh-t');
  if(hero){
    const lines = [...hero.querySelectorAll('.fi')], box = (hero.clientWidth - parseFloat(getComputedStyle(hero).paddingLeft) * 2) * (innerWidth > 1100 ? .7 : innerWidth > 860 ? .78 : 1);
    const mob = innerWidth < 861;
    const cap = mob ? 999 : Math.max(90, (innerHeight - 420) / (lines.length * .84));
    lines.forEach(l => { l.style.fontSize = '100px'; const w = l.offsetWidth; l.style.fontSize = Math.min(100 * box / w, cap) + 'px'; });
  }
  document.querySelectorAll('.xc-t .fi').forEach(l => { const box = l.closest('.xc').clientWidth - parseFloat(getComputedStyle(l.closest('.xc')).paddingLeft) * 2; l.style.fontSize = '100px'; l.style.fontSize = (100 * box / l.offsetWidth) + 'px'; });
}
fitLines(); if(document.fonts) document.fonts.ready.then(fitLines);
let fitT; addEventListener('resize', () => { clearTimeout(fitT); fitT = setTimeout(fitLines, 120); });

/* Sticker zum Herumziehen */
(function(){
  let z = 10;
  document.querySelectorAll('.stk').forEach(s => {
    let on = false, moved = false, sx, sy, ox = 0, oy = 0, x = 0, y = 0, lx = 0, w = 0;
    s.addEventListener('pointerdown', e => {
      on = true; moved = false; sx = e.clientX; sy = e.clientY; ox = x; oy = y; lx = e.clientX;
      s.setPointerCapture(e.pointerId); s.classList.add('grab'); s.style.zIndex = ++z;
    });
    s.addEventListener('pointermove', e => {
      if(!on) return;
      const dx = e.clientX - sx, dy = e.clientY - sy;
      if(Math.abs(dx) + Math.abs(dy) > 5) moved = true;
      x = ox + dx; y = oy + dy;
      w = clamp(w * .7 + (e.clientX - lx) * .9, -18, 18); lx = e.clientX;
      s.style.setProperty('--x', x + 'px'); s.style.setProperty('--y', y + 'px'); s.style.setProperty('--w', w + 'deg');
    });
    const up = () => { if(!on) return; on = false; s.classList.remove('grab'); w = 0; s.style.setProperty('--w', '0deg'); };
    s.addEventListener('pointerup', up); s.addEventListener('pointercancel', up);
    s.addEventListener('click', e => { if(moved) e.preventDefault(); });
    s.addEventListener('dragstart', e => e.preventDefault());
  });
})();

/* Bänder: laufen von selbst, beim Scrollen schneller */
(function(){
  const bands = [...document.querySelectorAll('.bd')].map(b => {
    const t = b.querySelector('.bd-track'), r = t.querySelector('.bd-run');
    for(let i = 0; i < 3; i++) t.appendChild(r.cloneNode(true));
    return {t, r, dir: +b.dataset.dir, x: 0};
  });
  if(reduce) return;
  let last = scrollY, v = 0;
  (function loop(){
    const d = scrollY - last; last = scrollY; v = v * .9 + d * .1;
    bands.forEach(b => {
      const w = b.r.offsetWidth; b.x += b.dir * (0.6 + Math.abs(v) * .5);
      if(b.x < -w) b.x += w; if(b.x > 0) b.x -= w;
      b.t.style.transform = `translate3d(${b.x}px,0,0)`;
    });
    requestAnimationFrame(loop);
  })();
})();

/* Fenster zum Ziehen: die Website darin ist echt responsive */
(function(){
  const stage = document.getElementById('rzStage'), box = document.getElementById('rzBox'), site = document.getElementById('rzSite'), cf = document.getElementById('cf');
  const h = document.getElementById('rzH'), r = document.getElementById('rzR'), wl = document.getElementById('rzW'), dl = document.getElementById('rzD');
  if(!stage) return;
  let W = 1200, touched = false;
  const avail = () => stage.clientWidth - (innerWidth > 860 ? 40 : 14);
  const maxW = () => innerWidth > 860 ? Math.min(1200, avail()) : 1200;
  function set(v){
    W = Math.round(clamp(v, 360, maxW()));
    const a = avail(), s = Math.min(1, a / W);
    cf.style.width = W + 'px'; cf.style.transform = s < 1 ? `scale(${s})` : '';
    box.style.width = (W * s + 4) + 'px';
    cf.style.height = (site.clientHeight / s) + 'px';
    wl.textContent = W + ' px'; dl.textContent = W < 600 ? 'Handy' : W < 1000 ? 'Tablet' : 'Bildschirm';
    r.max = maxW(); r.value = W;
  }
  set(innerWidth > 860 ? maxW() : 390);
  addEventListener('resize', () => set(W));
  r.addEventListener('input', () => { touched = true; set(+r.value); });
  let on = false, sx = 0, sw = 0;
  h.addEventListener('pointerdown', e => { touched = true; on = true; sx = e.clientX; sw = W; h.setPointerCapture(e.pointerId); });
  h.addEventListener('pointermove', e => { if(on) set(sw + (e.clientX - sx)); });
  h.addEventListener('pointerup', () => on = false);
  h.addEventListener('keydown', e => { if(e.key === 'ArrowLeft') set(W - 40); if(e.key === 'ArrowRight') set(W + 40); });
  if(reduce) return;
  const io = new IntersectionObserver(es => es.forEach(e => {
    if(!e.isIntersecting) return; io.disconnect();
    const a = W, b = 375, t0 = performance.now(), D = 3600;
    (function go(now){
      if(touched) return;
      const p = clamp((now - t0) / D, 0, 1), k = p < .5 ? p * 2 : (1 - p) * 2, e2 = k < .5 ? 2 * k * k : 1 - Math.pow(-2 * k + 2, 2) / 2;
      set(a + (b - a) * e2);
      if(p < 1) requestAnimationFrame(go);
    })(t0 + 1);
  }), {threshold: .55});
  setTimeout(() => io.observe(stage), 400);
})();

/* Musterseiten: senkrecht scrollen, seitlich fahren */
(function(){
  const sec = document.getElementById('muster'), track = document.getElementById('msTrack'), n = document.getElementById('msN');
  if(!sec) return;
  const cards = [...track.querySelectorAll('.ms-card')];
  let d = 0, on = false;
  function size(){
    on = innerWidth > 860 && !reduce;
    if(!on){ sec.style.height = ''; track.style.transform = ''; return; }
    d = Math.max(0, track.scrollWidth - innerWidth);
    sec.style.height = (d + innerHeight) + 'px'; move();
  }
  function move(){
    if(!on) return;
    const r = sec.getBoundingClientRect(), p = clamp(-r.top / (sec.offsetHeight - innerHeight || 1), 0, 1);
    track.style.transform = `translate3d(${-p * d}px,0,0)`;
    let best = 0, bd = 1e9; cards.forEach((c, i) => { const b = c.getBoundingClientRect(), m = Math.abs(b.left + b.width / 2 - innerWidth / 2); if(m < bd){ bd = m; best = i; } });
    n.textContent = '0' + (best + 1);
  }
  addEventListener('scroll', move, {passive: true}); addEventListener('resize', size);
  size(); if(document.fonts) document.fonts.ready.then(size); addEventListener('load', size);
})();

/* Zahlen zählen hoch */
(function(){
  const els = document.querySelectorAll('.nm-v b[data-to]');
  if(reduce) return;
  els.forEach(b => b.textContent = '0');
  const io = new IntersectionObserver(es => es.forEach(e => {
    if(!e.isIntersecting) return; io.unobserve(e.target);
    const b = e.target, to = +b.dataset.to, t0 = performance.now(), D = 1100 + to * 4;
    (function go(now){ const p = clamp((now - t0) / D, 0, 1); b.textContent = Math.round(to * (1 - Math.pow(1 - p, 3))); if(p < 1) requestAnimationFrame(go); })(t0);
  }), {threshold: .6});
  els.forEach(b => io.observe(b));
})();

/* Runder Knopf am Schluss folgt der Maus ein wenig */
(function(){
  const b = document.querySelector('.xc-badge'); if(!b || !matchMedia('(hover: hover)').matches) return;
  b.addEventListener('pointermove', e => { const r = b.getBoundingClientRect(); b.style.transform = `translate(${(e.clientX - r.left - r.width / 2) * .25}px,${(e.clientY - r.top - r.height / 2) * .25}px)`; });
  b.addEventListener('pointerleave', () => b.style.transform = '');
})();

''' + AX_JS + BUILD_JS
