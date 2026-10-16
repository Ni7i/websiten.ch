# Unterseiten, dritte Fassung: jede Leistung zeigt sich selbst (Live-Demo), keine Trennlinien, keine Halbgeviertstriche
import json, re, home9, pages as P, pages2 as P2
from parts import ARROW, LI, GRAIN, MARK_LIGHT, MARK_DARK

FILES = P2.FILES
ORDER = P2.ORDER
NAMES = P2.NAMES
UP = home9.UP
MAP = json.load(open('swissmap.json'))

PLUS = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M8 2v12M2 8h12" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'
MINUS = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M2 8h12" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'
CHECK = '<svg viewBox="0 0 16 16" aria-hidden="true"><path d="M3 8.5l3.2 3L13 4.5" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>'


def nodash(s):
    """Preise ohne Halbgeviertstrich: 590.– wird 590"""
    return s.replace('.–', '').replace('–', '')


# ------------------------------------------------------------------ Bausteine
def hero(h1, intro, visual='', second=('Was es kostet', '#preis')):
    cls = 'xh pad' + ('' if visual else ' xh-solo')
    vis = f'<div class="xh-vis">{visual}</div>' if visual else ''
    return f'''<section class="{cls}">
    <div class="xh-tx">
      <h1>{h1}</h1>
      <p class="xh-in">{intro}</p>
      <div class="xh-act"><a class="btn btn-sage" href="kontakt.html">Termin wählen {ARROW}</a><a class="btn btn-out" href="{second[1]}">{second[0]}</a></div>
    </div>
    {vis}
  </section>'''


def head(h2, p='', id_=''):
    i = f' id="{id_}"' if id_ else ''
    pp = f'<p>{p}</p>' if p else ''
    return f'<div class="xs-h"><h2{i}>{h2}</h2>{pp}</div>'


def gets(items):
    # kompakt: nur die Titel mit Häkchen, zwei Spalten
    body = ''.join(f'<li>{CHECK}<span>{t}</span></li>' for t, d in items)
    return f'<section class="xs pad" aria-labelledby="getT">{head("Das bekommen Sie", id_="getT")}<ul class="getc">{body}</ul></section>'


def steps(items):
    # ohne grosse Zahlen: die Woche steht klein in Salbei über dem Titel, die Reihenfolge bleibt eine <ol>
    body = ''.join(f'<li><span class="sw">{w}</span><h3>{t}</h3><p>{d}</p></li>' for t, d, w in items)
    return f'<section class="xs pad" aria-labelledby="stT">{head("So läuft es", "Sie wissen in jedem Schritt, wo wir stehen und was als Nächstes kommt.", "stT")}<ol class="stp3">{body}</ol></section>'


def price(rows, label, note=''):
    """Was es kostet: ruhige Liste, Leistung links, Preis rechts. Die erste Zeile ist das Hauptangebot."""
    lst = '<dl class="plist">' + ''.join(f'<div{" class=\'pmain\'" if i == 0 else ""}><dt>{a}</dt><dd>{b}</dd></div>' for i, (a, b) in enumerate(rows)) + '</dl>'
    n = f'<p class="pnote">{note}</p>' if note else ''
    return f"""<section class="xs pad" id="preis" aria-labelledby="prT">
    {head("Was es kostet", label, "prT")}
    {lst}{n}
    <div class="xp-act"><a class="btn btn-sage" href="kontakt.html">Termin wählen {ARROW}</a><a class="lnk" href="preise.html">Zum Preisrechner {ARROW}</a></div>
  </section>"""


def price_offer(text):
    return f"""<section class="xs pad" id="preis" aria-labelledby="prT">
    {head("Was es kostet", "Fester Preis, nach einem Gespräch.", "prT")}
    <p class="pnote pbig">{text}</p>
    <div class="xp-act"><a class="btn btn-sage" href="kontakt.html">Termin wählen {ARROW}</a></div>
  </section>"""


def faq(items):
    qs = ''.join(f'<details><summary><span>{q}</span><i class="pm2" aria-hidden="true">{PLUS}</i></summary><p>{a}</p></details>' for q, a in items)
    return f'''<section class="xs xq pad" aria-labelledby="fqT">
    <div><h2 id="fqT">Häufige Fragen</h2><a class="lnk" href="fragen.html">Alle Fragen {ARROW}</a></div>
    <div class="qa2">{qs}</div>
  </section>'''


def more(cur):
    links = ''.join(f'<a href="{FILES[k]}">{NAMES[k]}</a>' for k in ORDER if k != cur)
    return f'<section class="xs xm pad" aria-labelledby="mrT"><h2 id="mrT">Auch von uns</h2><nav class="mr" aria-label="Weitere Leistungen">{links}</nav></section>'


# ------------------------------------------------------------------ Geräte: MacBook und iPhone als echte HTML-Szene
def macbook(screen):
    """Gezeichnetes MacBook ohne Notch. screen: Inhalt des Bildschirms (854 x 534 px)."""
    return f'<div class="sc-mbp"><div class="sc-lid"><div class="sc-bez"><i class="sc-cam"></i><div class="sc-scr">{screen}<div class="sc-glare"></div></div></div></div><div class="sc-hinge"></div><div class="sc-base"></div></div>'


def scene(shots):
    """shots: Liste von (key, desktopbild, mobilbild, alt). Bilder scrollen im Gerät."""
    d = ''.join(f'<img class="sc-shot{" on" if i == 0 else ""}" data-proj="{i}" src="assets/img/{dk}" width="{dw}" height="{dh}" alt="{alt}, Ansicht am Computer"{"" if i == 0 else " loading=lazy"}>' for i, (k, (dk, dw, dh), m, alt) in enumerate(shots))
    m = ''.join(f'<img class="sc-shot{" on" if i == 0 else ""}" data-proj="{i}" src="assets/img/{mk}" width="{mw}" height="{mh}" alt="{alt}, Ansicht am Handy"{"" if i == 0 else " loading=lazy"}>' for i, (k, dd, (mk, mw, mh), alt) in enumerate(shots))
    return f'''<div class="stage" data-stage="1200x800"><div class="st-in sc">
      <div class="sc-shm"></div>
      {macbook(d)}
      <div class="sc-shp"></div>
      <div class="sc-pw"><div class="sc-ph" data-phone3d>
        <div class="sc-front"><div class="sc-glass"><div class="sc-ps"><div class="sc-island"></div><div class="sc-sbar"><span>9:41</span><span class="sc-ic"><i style="width:3px;height:5px"></i><i style="width:3px;height:7px"></i><i style="width:3px;height:9px"></i><i style="width:3px;height:11px"></i><i class="sc-bat"></i></span></div><div class="sc-pv">{m}</div><div class="sc-pgl"></div></div></div></div>
      </div></div>
    </div></div>'''


from PIL import Image as _I
def _dim(f): w, h = _I.open('../assets/img/' + f).size; return (f, w, h)
SHOTS = [('kf', _dim('live-kf-d.jpg'), _dim('live-kf-m.jpg'), 'Website von KF Bauservice GmbH'),
         ('ka', _dim('live-ka-d.jpg'), _dim('live-ka-m.jpg'), 'Website von Kastrati Trockenbau und Innenausbau')]


def web_scrub():
    proj = ''.join(f'''<div class="pj{" on" if i == 0 else ""}" data-proj="{i}"><h3>{name}</h3><p class="pj-p">{place}</p><p>{text}</p><a class="lnk" href="{url}" target="_blank" rel="noopener">Website öffnen {UP}</a></div>'''
                   for i, (key, name, place, url, host, text, tags) in enumerate(home9.REFS))
    return f'''<section class="scrub web-s pad pc-only" data-scrub="web" aria-labelledby="wsT">
    <div class="scrub-in">
      <div class="web-tx">
        <h2 id="wsT">Zwei echte Websites. <em class="hl">Scrollen Sie durch.</em></h2>
        <div class="pjs">{proj}</div>
      </div>
      <div class="web-dev">{scene(SHOTS)}</div>
    </div>
  </section>'''


def web_work():
    """Handy-Fassung: zwei echte Websites ruhig untereinander, jede im eigenen MacBook und iPhone (ohne Mitscrollen)."""
    rows = ''.join(f'''<div class="wk2{" flip" if i % 2 else ""}"><div class="wk2-tx"><h3>{name}</h3><p class="wk2-p">{place}</p><p>{text}</p><a class="lnk" href="{url}" target="_blank" rel="noopener">Website öffnen {UP}</a></div><div class="wk2-dev">{scene([SHOTS[i]])}</div></div>'''
                   for i, (key, name, place, url, host, text, tags) in enumerate(home9.REFS))
    return f'''<section class="xs pad web-w m-only" aria-labelledby="wsTm">
    {head('Zwei echte Websites. <em class="hl">Beide sind online.</em>', 'Schauen Sie sie sich ruhig selbst an, am Computer und am Handy.', 'wsTm')}
    {rows}
  </section>'''


# ------------------------------------------------------------------ Online-Shop: Einkauf im iPhone
def shop_scrub():
    st = [('Produkt wählen', 'Klare Fotos, Preis mit MwSt. und Lieferzeit auf einen Blick.'),
          ('Warenkorb', 'Versandkosten sind sofort sichtbar. Ab CHF 50 ist der Versand gratis.'),
          ('Bezahlen', 'Mit TWINT, Karte oder auf Rechnung. So, wie Ihre Kunden es gewohnt sind.'),
          ('Bestellt', 'Bestätigung per E-Mail, Versand mit der Post. Sie sehen alles in Shopify.')]
    steps_html = ''.join(f'<li class="{"on" if i == 0 else ""}" data-st="{i}"><span class="sn">{i + 1}</span><div><h3>{t}</h3><p>{d}</p></div></li>' for i, (t, d) in enumerate(st))
    bag = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 8h14l-1 12H6zM9 8V6a3 3 0 0 1 6 0v2" fill="none" stroke="currentColor" stroke-width="1.6"/></svg>'
    top = f'<div class="sp-top"><b>Rösterei Linde</b><span class="sp-bag">{bag}<i>2</i></span></div>'
    s0 = f'''<div class="ph-scr on" data-i="0">{top}<div class="sp-img" style="background-image:url('assets/img/shop-bag.jpg')"></div>
        <div class="sp-pad"><span class="sp-k">Frisch geröstet in Baden</span><h4>Hausmischung</h4><span class="sp-m">Bohnen, kräftig und rund</span>
        <div class="sp-sz"><i>250 g</i><i class="on">500 g</i><i>1 kg</i></div>
        <div class="sp-pr"><b>CHF 18.50</b><small>inkl. 8,1 % MwSt.</small></div>
        <span class="sp-btn">In den Warenkorb</span><span class="sp-note">Lieferung in 1 bis 2 Arbeitstagen</span></div></div>'''
    s1 = f'''<div class="ph-scr" data-i="1">{top}<div class="sp-pad"><h4 class="sp-h">Warenkorb</h4>
        <div class="sp-item"><span class="sp-th" style="background-image:url('assets/img/shop-bag.jpg')"></span><div><b>Hausmischung</b><span>500 g, Bohnen</span><span class="sp-q"><i>{MINUS}</i>2<i>{PLUS}</i></span></div><b>37.00</b></div>
        <div class="sp-sum"><div><span>Zwischensumme</span><span>CHF 37.00</span></div><div><span>Versand mit der Post</span><span>CHF 7.00</span></div><div class="sp-tot"><span>Total</span><span>CHF 44.00</span></div></div>
        <div class="sp-free"><span style="width:74%"></span></div><p class="sp-fn">Noch CHF 13.00 bis zum Gratisversand</p>
        <span class="sp-btn">Zur Kasse</span></div></div>'''
    s2 = f'''<div class="ph-scr" data-i="2">{top}<div class="sp-pad"><h4 class="sp-h">Bezahlen</h4>
        <div class="sp-pay on"><i></i><b>TWINT</b><span>Mit der App bestätigen</span></div>
        <div class="sp-pay"><i></i><b>Karte</b><span>Visa, Mastercard</span></div>
        <div class="sp-pay"><i></i><b>Rechnung</b><span>Zahlbar in 30 Tagen</span></div>
        <div class="sp-sum"><div class="sp-tot"><span>Total</span><span>CHF 44.00</span></div></div>
        <span class="sp-btn">Mit TWINT bezahlen</span></div></div>'''
    s3 = f'''<div class="ph-scr" data-i="3">{top}<div class="sp-pad sp-done"><span class="sp-ok">{CHECK}</span><h4>Danke, Herr Meier.</h4><p>Bestellung 1042 ist bezahlt.</p>
        <div class="sp-sum"><div><span>Versand</span><span>morgen, mit der Post</span></div><div><span>Bestätigung</span><span>per E-Mail</span></div></div>
        <span class="sp-btn sp-btn2">Weiter einkaufen</span></div></div>'''
    return f'''<section class="scrub shop-s pad" data-scrub="shop" aria-labelledby="ssT">
    <div class="scrub-in">
      <div class="shop-tx"><h2 id="ssT">Ein Einkauf, wie Ihre Kunden <em class="hl">ihn erwarten.</em></h2><ol class="shop-st">{steps_html}</ol></div>
      <div class="shop-dev"><div class="stage" data-stage="400x760"><div class="st-in fph-w"><div class="fph"><div class="fph-g"><div class="fph-s"><div class="fph-i"></div><div class="fph-sb"><span>9:41</span><span class="sc-ic"><i style="width:3px;height:5px"></i><i style="width:3px;height:7px"></i><i style="width:3px;height:9px"></i><i style="width:3px;height:11px"></i><i class="sc-bat"></i></span></div><div class="fph-v">{s0}{s1}{s2}{s3}</div></div></div></div></div></div><p class="demo-n">Beispiel-Shop, erfunden für diese Seite</p></div>
    </div>
  </section>'''


# ------------------------------------------------------------------ Google: Suche, vorher und nachher
def seo_demo():
    """Google-Suche in einem Browserfenster im MacBook. Gebaut in 1280 x 800 und verkleinert, damit Schrift und Dichte wie auf einem echten Bildschirm wirken."""
    ic = lambda d, c='#5F6368', w=20: f'<svg viewBox="0 0 24 24" width="{w}" height="{w}" aria-hidden="true"><path d="{d}" fill="{c}"/></svg>'
    mag = ic('M15.5 14h-.79l-.28-.27A6.47 6.47 0 0 0 16 9.5 6.5 6.5 0 1 0 9.5 16c1.61 0 3.09-.59 4.23-1.57l.27.28v.79l5 4.99L20.49 19zm-6 0C7.01 14 5 11.99 5 9.5S7.01 5 9.5 5 14 7.01 14 9.5 11.99 14 9.5 14')
    mic = ic('M12 14a3 3 0 0 0 3-3V5a3 3 0 1 0-6 0v6a3 3 0 0 0 3 3m5-3a5 5 0 0 1-10 0H5a7 7 0 0 0 6 6.92V21h2v-3.08A7 7 0 0 0 19 11z', '#4285F4')
    xx = ic('M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z', '#70757A', 22)
    lock = ic('M18 8h-1V6A5 5 0 0 0 7 6v2H6a2 2 0 0 0-2 2v10a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V10a2 2 0 0 0-2-2m-6 9a2 2 0 1 1 0-4 2 2 0 0 1 0 4m3.1-9H8.9V6a3.1 3.1 0 0 1 6.2 0z', '#5F6368', 14)
    pin = lambda x, y, c, s=1: f'<g transform="translate({x} {y}) scale({s})"><path d="M0 0c-7-9-11-14-11-20a11 11 0 0 1 22 0c0 6-4 11-11 20z" fill="{c}"/><circle cy="-20" r="4" fill="#fff"/></g>'
    mapsvg = f"""<svg class="gs-map" viewBox="0 0 620 150" preserveAspectRatio="xMidYMid slice" aria-hidden="true"><rect width="620" height="150" fill="#E8EDE6"/>
      <path d="M-10 122C90 98 170 132 260 108S430 60 630 80" fill="none" stroke="#B9D3E3" stroke-width="13"/>
      <path d="M0 40h620M0 96h620M90 0v150M260 0v150M420 0v150M540 0v150M0 12L620 140" fill="none" stroke="#fff" stroke-width="6"/>
      <path d="M170 0l50 150M360 0l-34 150M480 0l30 150" fill="none" stroke="#fff" stroke-width="3"/>
      <g fill="#C9D9C4"><rect x="300" y="48" width="70" height="38" rx="3"/><rect x="455" y="104" width="62" height="30" rx="3"/></g>
      {pin(140, 84, '#8E9693', .8)}{pin(470, 62, '#8E9693', .8)}<g class="gs-pin">{pin(318, 92, '#EA4335', 1.1)}</g></svg>"""
    stars = lambda n, r: f'<span class="gs-rt">{r}</span><span class="gs-st">{"★" * n}{"☆" * (5 - n)}</span>'
    fav = lambda t, bg, fg='#fff': f'<i class="gs-fav" style="background:{bg};color:{fg}">{t}</i>'

    def res(fv, site, url, title, snip, links=''):
        return f'<div class="gs-r"><div class="gs-src">{fv}<div><b>{site}</b><span>{url}</span></div></div><a>{title}</a><p>{snip}</p>{links}</div>'

    ad = f'<div class="gs-r"><div class="gs-src"><span class="gs-ad">Gesponsert</span></div><div class="gs-src">{fav("S", "#1E5BB8")}<div><b>Sanitär Meier AG</b><span>www.sanitaer-meier.ch</span></div></div><a>Badsanierung zum Fixpreis | Offerte in 48 Stunden</a><p>Komplettbad aus einer Hand. Beratung, Planung und Umsetzung im ganzen Aargau.</p></div>'
    portal = res(fav('v', '#F29900'), 'Vergleichsportal', 'https://www.vergleichsportal.ch › sanitaer › baden', 'Sanitär in Baden: 14 Betriebe im Vergleich', 'Offerten von Sanitärfirmen in Baden und Umgebung vergleichen. Kostenlos und unverbindlich.')
    before = '<div class="gs-list" data-v="0"><div class="gs-main">' + ad + portal + ''.join([
        res(fav('b', '#188038'), 'Bauratgeber', 'https://www.bauratgeber.ch › bad › kosten', 'Was kostet eine Badsanierung? Preise 2026', '15.03.2026 · Richtwerte für Bad, Dusche und Plattenarbeiten in der Schweiz, mit Beispielen.'),
        res(fav('f', '#5F6368'), 'Firmenverzeichnis', 'https://www.firmenverzeichnis.ch › baden', 'Sanitär Baden: Adressen und Öffnungszeiten', 'Alle Einträge in Baden AG, sortiert nach Ort und Bewertung.'),
    ]) + '</div></div>'
    after = f"""<div class="gs-list" data-v="1"><div class="gs-main">
        <div class="gs-loc"><b class="gs-h">Unternehmen</b>{mapsvg}
          <div class="gs-biz"><div><b>Keller Sanitär</b><span>{stars(5, '4,9')} (38) · Sanitärbetrieb</span><span>Baden · <em>Geöffnet</em> · Schliesst um 17:00</span></div><span class="gs-bt"><i>Website</i><i>Route</i></span></div>
          <div class="gs-biz"><div><b>Sanitär Meier AG</b><span>{stars(4, '4,2')} (17) · Sanitärbetrieb</span><span>Wettingen · <em>Geöffnet</em> · Schliesst um 18:00</span></div><span class="gs-bt"><i>Website</i><i>Route</i></span></div>
        </div>
        {res(fav('K', '#2E5E3F'), 'Keller Sanitär', 'https://www.keller-sanitaer.ch › badsanierung', 'Badsanierung in Baden | Keller Sanitär', 'Neues Bad mit Fixpreis und festem Termin. Beratung vor Ort in Baden, Wettingen und Umgebung.', '<span class="gs-sl"><a>Ablauf</a><a>Referenzen</a><a>Offerte anfragen</a></span>')}
        {portal}
      </div>
      <aside class="gs-kp"><img src="assets/img/bad-keller-1200.jpg" alt="" width="1200" height="800"><div class="gs-kpb"><b>Keller Sanitär</b><span>{stars(5, '4,9')} 38 Google-Rezensionen</span><span class="gs-mut">Sanitärbetrieb in Baden</span>
        <span class="gs-bt"><i>Website</i><i>Route</i><i>Speichern</i></span>
        <p><b>Adresse:</b> Bruggerstrasse 12, 5400 Baden</p><p><b>Öffnungszeiten:</b> <em>Geöffnet</em> · Schliesst um 17:00</p></div></aside></div>"""
    page = f"""<div class="gs-in">
      <div class="gs-top"><div class="gs-bar">{mag}<span class="sr-q" data-q="badsanierung baden"></span><span class="sr-c"></span><span class="gs-ico">{xx}<i></i>{mic}</span></div><i class="gs-av">K</i></div>
      <div class="gs-tabs"><b>Alle</b><span>Maps</span><span>Bilder</span><span>News</span><span>Videos</span><span>Mehr</span><span class="gs-tl">Tools</span></div>
      <div class="gs-res">{before}{after}</div></div>"""
    screen = f"""<div class="gs" aria-hidden="true"><div class="gs-win">
      <div class="gs-chrome"><span class="gs-dots"><i></i><i></i><i></i></span><span class="gs-tab">badsanierung baden - Google Suche</span></div>
      <div class="gs-addr">{lock}<span>google.ch/search?q=badsanierung+baden</span></div>
      {page}</div></div>"""
    return f"""<div class="sd" id="seoDemo">
      <div class="stage" data-stage="1040x660"><div class="st-in sd-in"><div class="sc-shm"></div>{macbook(screen)}</div></div>
      <div class="sd-ctl"><div class="sr-sw" role="group" aria-label="Suchergebnis zeigen"><button type="button" data-v="0" aria-pressed="false">Vorher</button><button type="button" data-v="1" aria-pressed="true">Nachher</button></div>
        <p class="sd-cap" data-v="0">Keller Sanitär ist nicht auf Seite 1.</p><p class="sd-cap" data-v="1">Keller Sanitär steht ganz oben, mit Karte und Bewertungen.</p></div>
      <p class="demo-n">Beispiel mit einem erfundenen Betrieb</p>
    </div>"""


# ------------------------------------------------------------------ Hosting: Schweizer Karte, alles läuft nach Genf
def host_demo():
    g = MAP['cities']['Genf']
    arcs, dots = '', ''
    names = {'Zuerich': 'Zürich', 'Basel': 'Basel', 'Bern': 'Bern', 'Luzern': 'Luzern', 'StGallen': 'St. Gallen', 'Lugano': 'Lugano', 'Lausanne': 'Lausanne', 'Chur': 'Chur'}
    for i, (k, n) in enumerate(names.items()):
        x, y = MAP['cities'][k]
        mx, my = (x + g[0]) / 2, (y + g[1]) / 2
        dist = ((x - g[0]) ** 2 + (y - g[1]) ** 2) ** .5
        cx, cy = mx, my - dist * .32
        arcs += f'<path class="hm-a" style="--d:{i * .12:.2f}s" d="M{x:.1f} {y:.1f}Q{cx:.1f} {cy:.1f} {g[0]:.1f} {g[1]:.1f}" pathLength="1"/>'
        dots += f'<g class="hm-c"><circle cx="{x:.1f}" cy="{y:.1f}" r="5"/><text x="{x + 10:.1f}" y="{y + 5:.1f}">{n}</text></g>'
    svg = f'''<svg class="hm" viewBox="0 0 920 597" role="img" aria-label="Karte der Schweiz: Websites aus der ganzen Schweiz liegen in Genf">
      <defs><pattern id="hmDots" width="11" height="11" patternUnits="userSpaceOnUse"><circle cx="5.5" cy="5.5" r="2.4" fill="#46544A"/></pattern></defs>
      <path d="{MAP['country']}" fill="url(#hmDots)"/>
      <path d="{MAP['lakes']}" fill="#151515"/>
      {arcs}{dots}
      <g class="hm-g"><circle class="hm-p" cx="{g[0]}" cy="{g[1]}" r="16"/><circle cx="{g[0]}" cy="{g[1]}" r="9" fill="#A3C2AA"/><text x="{g[0] + 20}" y="{g[1] + 6}">Genf</text></g>
    </svg>'''
    panel = '''<div class="hs" aria-label="Beispiel einer Statusanzeige">
        <div class="hs-t"><b>ihre-firma.ch</b><span class="hs-on"><i></i>Online</span></div>
        <dl>
          <div><dt>Online ohne Unterbruch</dt><dd id="hsUp">214 Tage</dd></div>
          <div><dt>Letztes Backup</dt><dd>Heute, 03:00</dd></div>
          <div><dt>SSL-Zertifikat</dt><dd>gültig</dd></div>
          <div><dt>Updates</dt><dd>alle installiert</dd></div>
          <div><dt>Standort</dt><dd>Genf, Schweiz</dd></div>
        </dl>
      </div>'''
    return f'<div class="hmw" id="hostMap">{svg}{panel}</div>'


# ------------------------------------------------------------------ Microsoft 365: erster Arbeitstag
def m365_demo():
    items = ['Konto marco.keller@ihre-firma.ch erstellt', 'Lizenz Microsoft 365 Business Standard zugewiesen', 'Postfach und Kalender bereit',
             'Teams: Kanal «Baustellen» hinzugefügt', 'OneDrive: Ordner «Projekte» freigegeben', 'Anmeldung mit zweitem Faktor aktiv', 'Laptop eingerichtet und angemeldet']
    li = ''.join(f'<li><i class="ob-i">{CHECK}</i><span>{t}</span><em></em></li>' for t in items)
    return f'''<div class="ob" id="onb">
      <div class="ob-h"><span class="ob-av">MK</span><div><b>Marco Keller</b><span>Bauleiter, Start am Montag um 07:30</span></div></div>
      <ul class="ob-l">{li}</ul>
      <div class="ob-f"><p class="ob-s" aria-live="polite">Bereit zum Einrichten.</p><button class="btn btn-sage ob-b" type="button">Konto einrichten</button></div>
    </div>'''


# ------------------------------------------------------------------ KI-Chatbot: zum Ausprobieren
CHAT = [('Was kostet eine Website?', 'Eine Website mit 4 Seiten kostet CHF 590. Jede weitere Seite kostet CHF 150. Hosting und Domain kosten CHF 25 im Monat.'),
        ('Wo liegen meine Daten?', 'Bei Infomaniak in Genf. Website, Domain und E-Mails bleiben in der Schweiz.'),
        ('Wie schnell ist meine Website online?', 'Eine Website mit 4 Seiten ist meistens in drei bis vier Wochen online. Das Datum steht in der Offerte.'),
        ('Macht ihr auch Logos?', 'Dazu habe ich keine sichere Information. Ich gebe Ihre Frage gerne an das Team weiter. Sie bekommen die Antwort per E-Mail.')]


def ki_demo():
    chips = ''.join(f'<button type="button" data-i="{i}">{q}</button>' for i, (q, a) in enumerate(CHAT))
    data = json.dumps([a for q, a in CHAT], ensure_ascii=False).replace('</', '<\\/')
    return f'''<div class="cb" id="chat" data-a='{data.replace("'", "&#39;")}'>
      <div class="cb-h"><svg viewBox="12 10 174 188" aria-hidden="true"><path fill="#4E5E53" d="{MARK_LIGHT}"/><path fill="#A3C2AA" d="{MARK_DARK}"/></svg><div><b>Fragen an websiten.ch</b><span><i></i>antwortet sofort</span></div></div>
      <div class="cb-m" aria-live="polite"><div class="cb-b cb-bot">Grüezi. Ich beantworte Fragen zu Websites, Preisen und Terminen. Was möchten Sie wissen?</div></div>
      <div class="cb-c">{chips}</div>
      <div class="cb-in"><span>Wählen Sie oben eine Frage</span><i>{ARROW}</i></div>
    </div>'''


# ------------------------------------------------------------------ Inhalte pro Leistung
G = {
 'websites': [('Gestaltung für Ihren Betrieb', 'Mit Ihrem Logo, Ihren Farben und Ihren Fotos. Keine Vorlage, die jeder hat.'),
              ('Fürs Handy gebaut', 'Die meisten Besucher kommen übers Handy. Darauf bauen wir zuerst.'),
              ('Ein Formular, das Anfragen bringt', 'Anfragen landen direkt in Ihrem Postfach, mit Schutz gegen Spam.'),
              ('Schnell und sauber', 'Kurze Ladezeit und eine Struktur, die Google versteht.'),
              ('Texte und Sprachen', 'Auf Wunsch schreiben wir die Texte, auch auf Französisch, Italienisch oder Englisch.'),
              ('Sie ändern selbst', 'Nach einer kurzen Einführung passen Sie Texte und Bilder selbst an.')],
 'shops': [('Shopify, sauber eingerichtet', 'Zahlungen, Steuern, Versand und rechtliche Seiten. Vollständig und geprüft.'),
           ('Zahlen wie in der Schweiz üblich', 'TWINT, Karte und Kauf auf Rechnung.'),
           ('Versand mit der Post', 'Versandkosten, Gratisversand ab einem Betrag und Abholung im Laden.'),
           ('Ihre Produkte', 'Die ersten 30 erfassen wir. Grosse Sortimente importieren wir aus Excel oder dem alten Shop.'),
           ('Umzug ohne Verlust', 'Von WooCommerce, Wix oder einem anderen System. Mit Kunden, Bestellungen und Weiterleitungen.'),
           ('Schulung', 'Sie lernen, wie Sie Produkte, Bestellungen und Rabatte selbst verwalten.')],
 'seo': [('Google-Unternehmensprofil', 'Öffnungszeiten, Fotos und Leistungen. Damit Sie auf Google Maps richtig erscheinen.'),
         ('Saubere Technik', 'Ladezeit, Struktur und Titel, die Google versteht.'),
         ('Seiten für Ihre Region', 'Eine Seite pro Leistung und Ort. Geschrieben für Menschen.'),
         ('Google Ads mit festem Budget', 'Sie legen das Monatsbudget fest und sehen, was es bringt.'),
         ('Search Console', 'Wir verbinden Ihre Website mit Google und beheben, was Google bemängelt.'),
         ('Monatliche Auswertung', 'Besucher, Anfragen und woher sie kommen. Kurz und verständlich.')],
 'hosting': [('.ch-Domain', 'Neu registriert oder umgezogen. Sie läuft auf Ihren Namen.'),
             ('E-Mail mit Ihrer Domain', 'Zum Beispiel info@ihre-firma.ch, auf Handy und Computer eingerichtet.'),
             ('Tägliche Backups', 'Geht etwas schief, holen wir den Stand vom Vortag zurück.'),
             ('Updates', 'WordPress und Plugins halten wir aktuell, geprüft und ohne Ausfall.'),
             ('SSL-Zertifikat', 'Das Schloss im Browser. Es erneuert sich automatisch.'),
             ('Kleine Änderungen', 'Neue Öffnungszeiten oder ein neues Foto? Schreiben Sie uns, wir erledigen es.')],
 'm365': [('Einrichtung und Lizenzen', 'Die passenden Lizenzen, sauber eingerichtet. Sie laufen auf Ihren Namen.'),
          ('E-Mail-Umzug', 'Vom alten Anbieter zu Microsoft 365, mit allen Ordnern und Kontakten.'),
          ('Teams und OneDrive', 'Klare Ordner und Kanäle, damit jeder findet, was er sucht.'),
          ('Sichere Anmeldung', 'Mit zweitem Faktor. Das schützt vor den häufigsten Angriffen.'),
          ('Ein- und Austritte', 'Neue Leute sind am ersten Tag startklar. Wer geht, verliert den Zugriff.'),
          ('Hilfe per Fernwartung', 'Klemmt etwas, schalten wir uns auf Ihren Bildschirm und lösen es.')],
 'ki': [('Nur Ihre Inhalte', 'Er antwortet mit dem, was auf Ihrer Website und in Ihren Unterlagen steht.'),
        ('In mehreren Sprachen', 'Er antwortet in der Sprache, in der man ihn fragt.'),
        ('Übergabe an Sie', 'Bei schwierigen Fragen nimmt er Name und E-Mail auf und gibt sie an Sie weiter.'),
        ('Termine', 'Auf Wunsch schlägt er freie Termine vor oder führt zur Buchung.'),
        ('Passt zu Ihrer Website', 'Mit Ihren Farben und in Ihrem Ton.'),
        ('Datenschutz', 'Was gespeichert wird, ist dokumentiert und steht in Ihrer Datenschutzerklärung.')],
}

HERO = {
 'websites': ('Websites, die <em class="hl">Anfragen bringen.</em>', 'Gestaltet für Ihren Betrieb, gebaut fürs Handy und so geschrieben, dass Ihre Kunden sofort verstehen, was Sie machen. Ab CHF 590, in drei bis vier Wochen online.'),
 'shops': ('Online-Shops, die in der Schweiz <em class="hl">verkaufen.</em>', 'Wir richten Ihren Shopify-Account auf professionellem Niveau ein. Mit TWINT, Karte, Rechnung und Versand mit der Post. Ab CHF 1’890.'),
 'seo': ('Gefunden werden, wo Ihre Kunden <em class="hl">suchen.</em>', 'Wer «Badsanierung Baden» sucht, soll Sie finden. Wir richten Ihr Google-Profil ein, bringen die Technik in Ordnung und schreiben Seiten zu dem, was Ihre Kunden suchen.'),
 'hosting': ('Ihre Website liegt in Genf. <em class="hl">Wir kümmern uns darum.</em>', 'Domain, Website und E-Mail bei Infomaniak, in Rechenzentren in der Schweiz. Updates, Backups und SSL übernehmen wir. Für CHF 25 im Monat.'),
 'm365': ('Microsoft 365, <em class="hl">sauber eingerichtet.</em>', 'E-Mail, Kalender, Teams und Dateien für Ihr Team. Wir arbeiten selbst jeden Tag mit Microsoft 365 und richten es bei Ihnen so ein, dass neue Leute am ersten Tag loslegen.'),
 'ki': ('Ein Chatbot, der Ihre <em class="hl">Antworten kennt.</em>', 'Er beantwortet die Fragen, die jeden Tag kommen. Nur mit Ihren Informationen. Was er nicht weiss, gibt er an Sie weiter. Probieren Sie ihn gleich hier aus.'),
}

PRICE = {
 'websites': lambda: price([('Website mit 4 Seiten', 'CHF 590'), ('Bis 6 Seiten', 'CHF 890'), ('Bis 8 Seiten', 'CHF 1’190'), ('Bis 10 Seiten', 'CHF 1’490'), ('Jede weitere Seite', 'CHF 150'), ('Weitere Sprache', 'CHF 50'), ('Hosting und Domain', 'CHF 25 im Monat')],
                           'Gestaltung, Handy-Version, Kontaktformular, SSL und Einführung sind immer dabei.'),
 'shops': lambda: price([('Shop mit 4 Seiten, bis 30 Produkte', 'ab CHF 1’890'), ('Bis 150 Produkte', '+ CHF 490'), ('Bis 500 Produkte', '+ CHF 990'), ('Über 500, mit Import', '+ CHF 1’890')],
                        'Mit TWINT, Karte, Rechnung und Versand.', 'Das Shopify-Abo zahlen Sie direkt an Shopify.'),
 'seo': lambda: price([('Google-Unternehmensprofil einrichten', 'CHF 150'), ('Google Ads einrichten', 'CHF 390')],
                      'Profil mit Fotos, Leistungen und Öffnungszeiten.', 'Das Werbebudget zahlen Sie direkt an Google. Seiten für Ihre Region und die laufende Betreuung rechnen wir nach Umfang, mit fester Offerte.'),
 'hosting': lambda: price([('Hosting, Domain und E-Mail', 'CHF 25 im Monat')], 'Alles, damit Ihre Website läuft. Ohne Zusatzkosten.'),
 'm365': lambda: price_offer('Der Preis hängt davon ab, wie viele Personen und Geräte Sie haben. Nach dem ersten Gespräch bekommen Sie eine Offerte mit festem Preis. Die Lizenzen laufen auf Ihren Namen.'),
 'ki': lambda: price_offer('Der Preis hängt davon ab, wie viele Inhalte der Chatbot kennen soll und ob er Termine vorschlägt. Nach dem ersten Gespräch bekommen Sie eine Offerte mit festem Preis.'),
}

DESC = {k: nodash(v['desc']) for k, v in P2.SVC.items()}


def service(k):
    s = P2.SVC[k]
    h1, intro = HERO[k]
    vis = {'seo': seo_demo, 'hosting': host_demo, 'm365': m365_demo, 'ki': ki_demo}.get(k)
    parts = [hero(h1, intro, vis() if vis else '')]
    if k == 'websites': parts += [web_scrub(), web_work()]  # Computer: Mitscrollen, Handy: ruhig
    if k == 'shops': parts.append(shop_scrub())
    parts += [gets(G[k]), steps(s['steps']), PRICE[k](), faq([(q, nodash(a)) for q, a in s['faq']]), more(k)]
    main = '\n  ' + '\n\n  '.join(parts) + '\n'
    return (f'{NAMES[k]} | websiten.ch', DESC[k], main)


# ------------------------------------------------------------------ Leistungen: Liste links, MacBook rechts bleibt stehen
def leistungen():
    subs = {i: s for i, t, d, s in home9.SV}
    blocks = ''.join(f'''<article class="ov2-b{" on" if i == 0 else ""}" data-k="{i}">
        <div class="ov2-m">{P2.mac(k, "Beispiel: " + NAMES[k], eager=i == 0)}</div>
        <h2><a href="{FILES[k]}">{NAMES[k]}</a></h2><p>{nodash(P2.SHORT[k])}</p>
        <ul>{"".join(f"<li>{x}</li>" for x in subs[k])}</ul>
        <a class="lnk" href="{FILES[k]}">Mehr zu {NAMES[k]} {ARROW}</a></article>''' for i, k in enumerate(ORDER))
    screens = ''.join(f'<img class="ov2-s{" on" if i == 0 else ""}" data-k="{i}" src="assets/img/scr-{k}.jpg" alt="" width="1600" height="1000"{"" if i == 0 else " loading=lazy"}>' for i, k in enumerate(ORDER))
    sticky = f'<div class="ov2-dev" aria-hidden="true"><div class="mac"><div class="mac-scr">{screens}<span class="mac-gl"></span></div><img class="mac-fr" src="assets/img/mac-frame.webp" alt=""></div></div>'
    why = [('Eine Ansprechperson', 'Sie erklären Ihr Anliegen einmal. Wir kennen Ihren Betrieb, Ihre Website und Ihre Zugänge.'),
           ('Fester Preis', 'Sie kennen den Betrag, bevor wir anfangen. Kommt etwas dazu, besprechen wir es vorher.'),
           ('Daten in der Schweiz', 'Domains, Hosting und E-Mail laufen bei Infomaniak in Genf.')]
    main = '\n  ' + '\n\n  '.join([
        hero('Alles, was Ihr Betrieb <em class="hl">online braucht.</em>', 'Sechs Leistungen von einer Ansprechperson. Mit festem Preis und Servern in der Schweiz. Sie nehmen, was Sie brauchen, den Rest lassen Sie weg.', second=('Preise ansehen', 'preise.html')),
        f'<section class="ov2 pad" aria-label="Unsere Leistungen"><div class="ov2-list">{blocks}</div>{sticky}</section>',
        f'<section class="xs pad" aria-label="Aus einer Hand"><div class="oneh"><span class="oneh-l">Aus einer Hand</span><ul>' + ''.join(f'<li>{CHECK}<span>{t}</span></li>' for t, d in why) + '</ul></div></section>',
    ]) + '\n'
    return ('Leistungen | websiten.ch', 'Websites, Online-Shops, Google und SEO, Hosting bei Infomaniak, Microsoft 365 und KI-Chatbots für Schweizer KMU.', main)


# ------------------------------------------------------------------ Preise: Satz zum Ausfüllen
def preise():
    def stepper(id_, val, label):
        return f'<span class="cf-st" role="group" aria-label="{label}"><button type="button" data-step="{id_}" data-d="-1" aria-label="weniger">{MINUS}</button><output id="{id_}">{val}</output><button type="button" data-step="{id_}" data-d="1" aria-label="mehr">{PLUS}</button></span>'
    extras = [('book', 'Online-Terminbuchung', 290), ('blog', 'News oder Blog', 190), ('gmb', 'Google-Profil', 150), ('ads', 'Google Ads', 390)]
    ex = ' '.join(f'<button type="button" class="cf-x" data-x="{k}" data-p="{p}" aria-pressed="false"><i aria-hidden="true">{PLUS}</i>{t}</button>' for k, t, p in extras)
    conf = f'''<section class="cf pad" id="rechner" aria-labelledby="cfT">
    <h2 id="cfT" class="vh">Preisrechner</h2>
    <div class="cf-s">
      <p>Ich brauche <span class="cf-sw" role="group" aria-label="Art"><button type="button" data-t="web" aria-pressed="true">eine Website</button> <button type="button" data-t="shop" aria-pressed="false">einen Online-Shop</button></span>
      mit <span class="nw">{stepper('cfPages', 4, 'Anzahl Seiten')} <span id="cfPagesW">Seiten</span></span><span id="cfProdW" hidden> und <span class="nw">{stepper('cfProd', 'bis 30', 'Anzahl Produkte')} Produkten</span></span>
      in <span class="nw">{stepper('cfLang', 1, 'Anzahl Sprachen')} <span id="cfLangW">Sprache</span>.</span></p>
      <p>Die Texte <span class="cf-sw" role="group" aria-label="Texte"><button type="button" data-tx="0" aria-pressed="true">schreibe ich selbst</button> <button type="button" data-tx="1" aria-pressed="false">schreibt ihr</button></span>.</p>
      <p>Dazu nehme ich {ex}</p>
    </div>
    <div class="cf-out" aria-live="polite">
      <div class="cf-tot"><small>Einmalig</small><div class="big"><span class="big-pre">CHF</span><span class="big-v" id="cfTotal">590</span></div><p id="cfMonth">Dazu Hosting und Domain für CHF 25 im Monat.</p></div>
      <div class="cf-br"><ul id="cfLines"></ul><a class="btn btn-sage" id="cfGo" href="kontakt.html">Mit dieser Auswahl Termin wählen {ARROW}</a></div>
    </div>
  </section>'''
    groups = [('Website', [('4 Seiten', 'CHF 590'), ('6 Seiten', 'CHF 890'), ('8 Seiten', 'CHF 1’190'), ('10 Seiten', 'CHF 1’490'), ('Jede weitere Seite', 'CHF 150')], 'Mit Gestaltung, Handy-Version, Kontaktformular, Google Maps und SSL.'),
              ('Online-Shop', [('4 Seiten, bis 30 Produkte', 'CHF 1’890'), ('Bis 150 Produkte', '+ CHF 490'), ('Bis 500 Produkte', '+ CHF 990'), ('Über 500, mit Import', '+ CHF 1’890')], 'Mit TWINT, Karte, Rechnung und Versand. Das Shopify-Abo zahlen Sie direkt an Shopify.'),
              ('Dazu nach Wunsch', [('Texte von uns, pro Seite', 'CHF 90'), ('Weitere Sprache', 'CHF 50'), ('Online-Terminbuchung', 'CHF 290'), ('News oder Blog', 'CHF 190'), ('Google-Profil einrichten', 'CHF 150'), ('Google Ads einrichten', 'CHF 390')], ''),
              ('Hosting', [('Hosting und .ch-Domain', 'CHF 25 im Monat')], 'Server bei Infomaniak in Genf. Mit SSL, E-Mail-Adresse, Backups und Updates.')]
    gl = ''.join(f'<div class="pg"><h3>{h}</h3><dl class="tiers">' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in rows) + '</dl>' + (f'<p class="pnote">{n}</p>' if n else '') + '</div>' for h, rows, n in groups)
    allp = f'<section class="xs pad" aria-labelledby="apT">{head("Alle Preise", "In CHF, einmalig, wenn nichts anderes steht.", "apT")}<div class="pgs">{gl}</div></section>'
    fine = f'''<section class="xs pad" aria-labelledby="gwT">{head("Gut zu wissen", id_="gwT")}<ul class="get get3">
      <li><h3>Immer dabei</h3><p>Gestaltung, Handy-Version, SSL, Kontaktformular, die Einrichtung bei Infomaniak und eine Einführung.</p></li>
      <li><h3>Nicht dabei</h3><p>Fotografen, gekaufte Bilder, das Shopify-Abo und die Gebühren der Zahlungsanbieter. Kommt so etwas dazu, steht es vorher in der Offerte.</p></li>
      <li><h3>Bezahlung</h3><p>Die Hälfte bei Auftrag, der Rest, wenn alles online ist. Hosting monatlich.</p></li></ul></section>'''
    main = '\n  ' + '\n\n  '.join([hero('Feste Preise. <em class="hl">Vorher bekannt.</em>', 'Füllen Sie den Satz unten aus. Der Betrag, den Sie sehen, steht so auch in der Offerte.', second=('Alle Preise', '#alle')), conf, allp.replace('<section class="xs pad"', '<section class="xs pad" id="alle"', 1), fine]) + '\n'
    return ('Preise | websiten.ch', 'Feste Preise für Websites, Online-Shops und Hosting. Website mit 4 Seiten CHF 590, Hosting CHF 25 im Monat. Mit Preisrechner.', main)


# ------------------------------------------------------------------ Film auf "Über uns" (Websiten Ad v3)
FILM = '''<section class="xs pad" aria-label="Film über websiten.ch">
    <div class="film">
      <video id="adFilm" playsinline preload="none" poster="assets/websiten-ad-poster.jpg"><source src="assets/websiten-ad.mp4" type="video/mp4"></video>
      <button class="film-play" id="adPlay" type="button" aria-label="Film mit Ton abspielen"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z" fill="currentColor"/></svg>Film abspielen</button>
    </div>
  </section>'''

FILM_CSS = r'''
.film{position:relative;aspect-ratio:16/9;border-radius:26px;overflow:hidden;background:#FAFAF8}
.film video{display:block;width:100%;height:100%;object-fit:cover}
.film-play{position:absolute;left:50%;bottom:clamp(16px,4%,40px);transform:translateX(-50%);display:flex;align-items:center;gap:10px;padding:14px 22px 14px 18px;border:0;border-radius:999px;background:#151515;color:#fff;font:600 16px/1 "Hanken Grotesk",system-ui,sans-serif;cursor:pointer;transition:opacity .3s,transform .3s}
.film-play svg{width:20px;height:20px}
.film-play:hover{transform:translateX(-50%) scale(1.04)}
.film.on .film-play{opacity:0;pointer-events:none}
@media (max-width:700px){.film{border-radius:18px}.film-play{bottom:10px;font-size:13px;padding:9px 14px 9px 11px;gap:7px}.film-play svg{width:16px;height:16px}}
'''

FILM_JS = r'''
(() => {
  const v = document.getElementById('adFilm'), b = document.getElementById('adPlay');
  if (!v || !b) return;
  b.addEventListener('click', () => { v.muted = false; v.controls = true; v.play(); v.parentNode.classList.add('on'); });
  v.addEventListener('ended', () => { v.controls = false; v.currentTime = 0; v.parentNode.classList.remove('on'); });
})();
'''


# ------------------------------------------------------------------ Über uns
def ueber():
    bel = [('Ein fester Preis ist ein fester Preis.', 'Sie bekommen eine Offerte, und die gilt. Möchten Sie unterwegs etwas Neues, besprechen wir das vorher. Überraschungen auf der Rechnung gibt es bei uns nicht.'),
           ('Sie verstehen, was wir tun.', 'Wir erklären, was wir vorschlagen und warum. Ohne Abkürzungen, die niemand kennt. Ergibt etwas für Ihren Betrieb keinen Sinn, sagen wir es, auch wenn wir daran verdienen würden.'),
           ('Ihre Website gehört Ihnen.', 'Domain, Inhalte und Zugänge laufen auf Ihren Namen. Möchten Sie einmal wechseln, bekommen Sie alles, was Sie dafür brauchen.'),
           ('Ihre Daten bleiben in der Schweiz.', 'Domains, Hosting und E-Mail laufen bei Infomaniak, einem Schweizer Anbieter aus Genf mit Rechenzentren in der Schweiz.')]
    tools = [('Infomaniak', 'Domains, Hosting und E-Mail in Genf'), ('Microsoft 365', 'Unsere eigenen E-Mails und Dateien, und die vieler Kunden'), ('WordPress', 'Websites, die Sie selbst pflegen können'),
             ('Shopify', 'Online-Shops, die ohne Bastelei laufen'), ('WooCommerce', 'Shops direkt in WordPress'), ('Google', 'Unternehmensprofil, Search Console und Ads')]
    main = '\n  ' + '\n\n  '.join([
        hero('Klartext, feste Preise und <em class="hl">Termine, die halten.</em>', 'websiten.ch baut Websites, Online-Shops und alles, was dazugehört, für Betriebe in der ganzen Schweiz. Für Handwerker, Praxen, Restaurants und Läden, die online gefunden werden wollen, ohne sich selbst um die Technik zu kümmern.', second=('Leistungen ansehen', 'leistungen.html')),
        FILM,
        '<section class="xs pad" aria-label="Woran Sie uns messen können"><div class="bel2">' + ''.join(f'<div><h2>{t}</h2><p>{d}</p></div>' for t, d in bel) + '</div></section>',
        f'''<section class="band2 pad" data-sage>
    {GRAIN}
    <div><h2>Eine Ansprechperson für alles, was online ist.</h2><p>Website, Shop, Google, Domains, E-Mail und Microsoft 365. Sie müssen nicht fünf Firmen koordinieren, die sich bei einem Problem gegenseitig die Schuld geben. Sie schreiben uns, und die Sache wird erledigt.</p></div>
    <svg class="band2-mark" viewBox="12 10 174 188" aria-hidden="true"><path class="lm-l" d="{MARK_LIGHT}"/><path class="lm-d" d="{MARK_DARK}"/></svg>
  </section>''',
        f'<section class="xs pad" aria-labelledby="tlT">{head("Womit wir arbeiten", "Was wir Ihnen empfehlen, nutzen wir selbst jeden Tag.", "tlT")}<ul class="tl2">' + ''.join(f'<li><b>{a}</b><span>{b}</span></li>' for a, b in tools) + f'</ul><p class="li2"><a class="lnk" href="{LI}" target="_blank" rel="noopener">websiten.ch auf LinkedIn {UP}</a></p></section>',
    ]) + '\n'
    return ('Über uns | websiten.ch', 'Wie websiten.ch arbeitet: feste Preise, klare Worte, eine Ansprechperson und Daten in der Schweiz.', main)


# ------------------------------------------------------------------ Kontakt, Fragen, Rechtliches
def kontakt():
    t, d, m, c, j = P2.kontakt()
    m = re.sub(r'<nav class="crumb".*?</nav>', '', m, flags=re.S)
    return t, d, m, c, j


def fragen():
    t, d, m, c, j = P2.fragen()
    m = re.sub(r'<nav class="crumb".*?</nav>', '', m, flags=re.S)
    return t, d, nodash(m), c, j


def legal(which):
    return re.sub(r'<nav class="crumb".*?</nav>', '', P2.legal(which), flags=re.S)


# ------------------------------------------------------------------ Gestaltung
CSS = r'''
.hl{font-style:normal;color:var(--acc-s)}
.btn-sage{background:var(--acc-s);color:#0C201A}
.btn-sage:hover{background:var(--acc-a1);color:#0C201A}
.btn-out{border:1px solid rgba(255,255,255,.24);color:var(--text)}
.btn-out:hover{border-color:var(--text)}
.vh{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);white-space:nowrap}
.lnk{display:inline-flex;align-items:center;gap:10px;font-size:16.5px;color:var(--text);transition:gap .3s var(--ease),color .2s}
.lnk svg{color:var(--acc-s)}
.lnk:hover{gap:15px;color:var(--acc-a1)}
.demo-n{font-size:13px;color:#6F6F6F;margin-top:14px}

/* Einstieg */
.xh{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:clamp(36px,5vw,100px);align-items:center;padding-top:clamp(130px,13vw,190px);padding-bottom:clamp(70px,8vw,120px);min-height:min(100svh,960px)}
.xh-solo{grid-template-columns:minmax(0,1fr);min-height:0;padding-bottom:clamp(40px,5vw,72px)}
.xh h1{font-size:clamp(46px,5.6vw,104px);line-height:.97;font-weight:700;letter-spacing:-.058em;max-width:13ch}
.xh-solo h1{max-width:15ch;font-size:clamp(50px,7vw,132px)}
.xh-in{font-size:clamp(18px,1.4vw,22px);line-height:1.55;color:#C4C4C4;max-width:44ch;margin-top:clamp(24px,2.6vw,38px)}
.xh-act{display:flex;flex-wrap:wrap;gap:12px;margin-top:clamp(28px,3vw,44px)}
@keyframes xUp{from{opacity:0;transform:translateY(22px)}to{opacity:1;transform:none}}
.xh-tx > *{animation:xUp .9s var(--ease) both}
.xh-tx > *:nth-child(2){animation-delay:.07s}.xh-tx > *:nth-child(3){animation-delay:.14s}
.xh-vis{animation:xUp 1.1s .12s var(--ease) both;min-width:0}
@media (prefers-reduced-motion: reduce){ .xh-tx > *,.xh-vis{animation:none} }

/* Abschnitte: Abstand statt Linien */
.xs{padding-top:clamp(90px,11vw,170px);padding-bottom:0}
.xs:has(+ .closing){padding-bottom:clamp(90px,11vw,170px)}
.xs-h{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:clamp(20px,6vw,120px);align-items:end;margin-bottom:clamp(40px,5vw,80px)}
.xs-h h2,.xq h2,.xm h2{font-size:clamp(38px,4.6vw,80px);line-height:1;font-weight:700;letter-spacing:-.055em}
.xs-h p{font-size:clamp(17px,1.3vw,20px);line-height:1.6;color:#B9B9B9;max-width:42ch}
.get{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(40px,4.5vw,72px) clamp(28px,4vw,72px)}
.get h3{font-size:clamp(21px,1.75vw,27px);line-height:1.15;font-weight:700;letter-spacing:-.035em}
.get p{font-size:17px;line-height:1.6;color:#ABABAB;margin-top:12px;max-width:34ch}
.oneh{display:flex;flex-wrap:wrap;align-items:center;gap:18px clamp(28px,4vw,64px)}
.oneh-l{font-size:15px;font-weight:600;color:var(--acc-s)}
.oneh ul{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:16px clamp(28px,4vw,64px)}
.oneh li{display:flex;align-items:center;gap:12px;font-size:clamp(20px,1.7vw,26px);font-weight:600;letter-spacing:-.025em}
.oneh svg{flex:none;width:24px;height:24px;padding:4px;border-radius:50%;color:var(--acc-s);background:rgba(163,194,170,.12)}
.getc{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:20px clamp(28px,5vw,96px);max-width:980px}
.getc li{display:flex;align-items:center;gap:14px;font-size:clamp(19px,1.5vw,23px);font-weight:600;letter-spacing:-.025em;line-height:1.3}
.getc svg{flex:none;width:24px;height:24px;padding:4px;border-radius:50%;color:var(--acc-s);background:rgba(163,194,170,.12)}
.stp3{list-style:none;margin:0;padding:0;display:grid;gap:clamp(14px,1.6vw,22px)}
.stp3 li{display:grid;grid-template-columns:minmax(0,150px) minmax(0,280px) minmax(0,1fr);gap:clamp(16px,3vw,48px);align-items:baseline}
.stp3 .sw{font-size:14px;font-weight:600;letter-spacing:.01em;color:var(--acc-s)}
.stp3 h3{font-size:clamp(20px,1.6vw,24px);font-weight:700;letter-spacing:-.03em}
.stp3 p{font-size:16.5px;line-height:1.55;color:#ABABAB}
.shop-st .sn{display:block;font-size:clamp(64px,6vw,104px);line-height:.85;font-weight:700;letter-spacing:-.06em;color:var(--acc-s);font-variant-numeric:tabular-nums}

/* Preis als Aussage */
.xp{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.05fr);gap:clamp(32px,6vw,120px);align-items:end}
.big{display:flex;align-items:flex-start;gap:.12em;line-height:.8;font-weight:700;letter-spacing:-.07em;font-variant-numeric:tabular-nums;color:var(--text)}
.big-v{font-size:clamp(110px,15vw,270px)}
.big-pre{font-size:clamp(18px,1.6vw,26px);letter-spacing:0;font-weight:600;color:var(--acc-s);margin-top:.5em}
.big small{align-self:flex-end;font-size:clamp(18px,1.6vw,26px);letter-spacing:0;font-weight:600;color:var(--acc-s);margin:0 0 .25em .2em}
.big-t{font-size:clamp(46px,6vw,110px);line-height:.95;letter-spacing:-.06em;max-width:11ch}
.xp-l{font-size:clamp(18px,1.45vw,22px);line-height:1.55;color:#D6D6D6;max-width:40ch}
.tiers{margin:28px 0 0;display:grid;gap:12px}
.tiers div{display:flex;justify-content:space-between;align-items:baseline;gap:24px;font-size:clamp(17px,1.3vw,20px)}
.tiers dt{color:#A9A9A9}
.tiers dd{margin:0;font-weight:600;font-variant-numeric:tabular-nums;white-space:nowrap}
.inwords{list-style:none;margin:26px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:12px 26px;font-size:17px;color:#D6D6D6}
.inwords li{display:inline-flex;align-items:center;gap:9px}
.inwords svg{width:16px;height:16px;color:var(--acc-s)}
.pnote{font-size:15.5px;line-height:1.6;color:#8E8E8E;margin-top:22px;max-width:52ch}
.plist{max-width:760px;margin:0}
.plist > div{display:flex;justify-content:space-between;align-items:baseline;gap:24px;padding:9px 0}
.plist dt{font-size:clamp(17px,1.3vw,19px);color:#C4C4C4}
.plist dd{margin:0;font-size:clamp(17px,1.3vw,19px);font-weight:600;color:var(--text);white-space:nowrap;font-variant-numeric:tabular-nums}
.plist .pmain{padding-bottom:16px}
.plist .pmain dt{font-size:clamp(21px,1.8vw,27px);font-weight:700;letter-spacing:-.03em;color:var(--text)}
.plist .pmain dd{font-size:clamp(21px,1.8vw,27px);font-weight:700;letter-spacing:-.03em;color:var(--acc-s)}
.pnote.pbig{font-size:clamp(18px,1.45vw,22px);line-height:1.55;color:#D6D6D6;max-width:46ch}
.xp-act{display:flex;flex-wrap:wrap;align-items:center;gap:20px 30px;margin-top:36px}

/* Fragen */
.xq{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.2fr);gap:clamp(32px,6vw,120px);align-items:start}
.xq h2{margin-bottom:28px}
.qa2{display:grid;gap:8px}
.qa2 details{background:#1A1A1A;border-radius:18px;transition:background .25s}
.qa2 details[open]{background:#1E1E1E}
.qa2 summary{list-style:none;cursor:pointer;display:flex;justify-content:space-between;align-items:center;gap:24px;padding:22px 26px;font-size:clamp(17px,1.4vw,21px);font-weight:500;letter-spacing:-.01em}
.qa2 summary::-webkit-details-marker{display:none}
.pm2{flex:none;width:30px;height:30px;border-radius:50%;display:grid;place-items:center;color:var(--acc-s);background:rgba(163,194,170,.1);transition:transform .35s var(--ease)}
.pm2 svg{width:13px;height:13px}
details[open] .pm2{transform:rotate(45deg)}
.qa2 p{font-size:17px;line-height:1.7;color:#BDBDBD;max-width:56ch;padding:0 26px 24px}

/* Weitere Leistungen */
.xm{padding-bottom:clamp(90px,11vw,170px)}
.xm h2{font-size:15px;letter-spacing:0;font-weight:500;color:var(--muted);margin-bottom:22px}
.mr{display:flex;flex-wrap:wrap;gap:4px clamp(22px,3vw,48px)}
.mr a{font-size:clamp(34px,4.6vw,80px);line-height:1.08;font-weight:700;letter-spacing:-.055em;color:#4D4D4D;transition:color .25s}
.mr a:hover,.mr a:focus-visible{color:var(--text)}

/* Bühne: feste Grösse, skaliert per Skript */
.stage{position:relative;width:100%;max-width:100%}
.st-in{position:absolute;left:0;top:0;transform-origin:0 0}

/* Szene MacBook und iPhone (wie die Geräte auf der Startseite, aber lebendig) */
.sc{width:1200px;height:800px;font-family:-apple-system,"Helvetica Neue",Arial,sans-serif}
.sc-mbp{position:absolute;left:214px;top:56px;width:900px}
.sc-lid{position:relative;width:900px;height:585px;border-radius:26px 26px 6px 6px;background:linear-gradient(180deg,#4a4a4e 0%,#2c2c2f 3%,#262628 100%);box-shadow:inset 0 0 0 1.5px #56565b,inset 0 2px 1px rgba(255,255,255,.25),0 0 0 .6px #121213}
.sc-bez{position:absolute;left:9px;right:9px;top:9px;bottom:6px;border-radius:19px 19px 3px 3px;background:#050505;overflow:hidden}
.sc-scr{position:absolute;left:14px;right:14px;top:16px;bottom:20px;border-radius:7px 7px 0 0;overflow:hidden;background:#fff}
.sc-cam{position:absolute;left:50%;top:5px;width:6px;height:6px;margin-left:-3px;border-radius:50%;background:#1a1d26;box-shadow:0 0 0 1px #0d0f14;z-index:3}
.sc-glare{position:absolute;inset:0;z-index:2;pointer-events:none;background:linear-gradient(118deg,rgba(255,255,255,.10) 0%,rgba(255,255,255,.035) 28%,rgba(255,255,255,0) 42%)}
.sc-hinge{width:860px;height:6px;margin:0 auto;background:linear-gradient(180deg,#0e0e0f,#2c2c2f);border-radius:0 0 2px 2px}
.sc-base{position:relative;width:1020px;height:30px;margin-left:-60px;border-radius:3px 3px 30px 30px / 3px 3px 24px 24px;background:linear-gradient(180deg,#77777c 0%,#4c4c50 12%,#38383b 45%,#232325 80%,#18181a 100%);box-shadow:inset 0 1px 0 rgba(255,255,255,.28),inset 0 -2px 3px rgba(0,0,0,.5)}
.sc-base::before{content:"";position:absolute;left:50%;top:0;width:160px;height:10px;margin-left:-80px;border-radius:0 0 14px 14px;background:linear-gradient(180deg,#1f1f21,#3a3a3d)}
.sc-shm{position:absolute;left:130px;top:650px;width:1100px;height:60px;border-radius:50%;background:radial-gradient(closest-side,rgba(0,0,0,.75),rgba(0,0,0,0));filter:blur(6px)}
.sc-shp{position:absolute;left:60px;top:712px;width:330px;height:50px;border-radius:50%;background:radial-gradient(closest-side,rgba(0,0,0,.85),rgba(0,0,0,0));filter:blur(8px)}
.sc-pw{position:absolute;left:78px;top:196px;width:262px;height:548px;perspective:1600px;perspective-origin:60% 40%}
.sc-ph{position:absolute;inset:0;transform-style:preserve-3d;transform:rotateY(28deg) rotateX(4deg) rotateZ(-2deg)}
.sc-slice{position:absolute;inset:0;border-radius:42px;background:var(--c)}
.sc-btn{position:absolute;left:-2.4px;width:4px;border-radius:2px;background:var(--c)}
.sc-front{position:absolute;inset:0;border-radius:42px;transform:translateZ(14px);background:linear-gradient(135deg,#d9d3c8,#a8a297 40%,#e6e1d7 60%,#9c968b);padding:3px}
.sc-glass{position:relative;width:100%;height:100%;border-radius:39px;background:#030303;padding:8px}
.sc-ps{position:relative;width:100%;height:100%;border-radius:32px;overflow:hidden;background:#fff;display:flex;flex-direction:column}
.sc-sbar,.fph-sb{flex:none;height:30px;background:#fff;display:flex;align-items:center;justify-content:space-between;padding:4px 22px 0 26px;font:600 12.5px -apple-system,"Helvetica Neue",Arial,sans-serif;color:#111;position:relative;z-index:2}
.sc-ic{display:flex;gap:2px;align-items:center}
.sc-ic i{display:block;background:#111;border-radius:1px}
.sc-ic .sc-bat{width:20px;height:10px;border-radius:3px;margin-left:5px}
.sc-island{position:absolute;left:50%;top:9px;width:70px;height:20px;margin-left:-35px;border-radius:11px;background:#000;z-index:3}
.sc-pv{position:relative;flex:1;min-height:0;overflow:hidden}
.sc-pgl{position:absolute;inset:0;z-index:2;border-radius:32px;pointer-events:none;background:linear-gradient(105deg,rgba(255,255,255,.16) 0%,rgba(255,255,255,.05) 30%,rgba(255,255,255,0) 46%)}
.sc-shot{position:absolute;left:0;top:0;width:100%;height:auto;opacity:0;transition:opacity .5s;will-change:transform}
.sc-shot.on{opacity:1}

/* Scroll-Passagen */
.scrub{position:relative}
.scrub-in{position:sticky;top:0;height:100svh;display:grid;align-items:center}
.web-s{height:340vh}
.web-s .scrub-in{grid-template-columns:minmax(0,.5fr) minmax(0,1.5fr);gap:clamp(10px,2vw,32px)}
.web-tx h2{font-size:clamp(34px,3.6vw,62px);line-height:1;font-weight:700;letter-spacing:-.055em;max-width:12ch}
.pjs{position:relative;margin-top:clamp(28px,4vw,56px);min-height:280px}
.pj{position:absolute;inset:0 0 auto 0;opacity:0;transform:translateY(14px);transition:opacity .45s,transform .6s var(--ease);pointer-events:none}
.pj.on{opacity:1;transform:none;pointer-events:auto}
.pj h3{font-size:clamp(24px,2vw,32px);font-weight:700;letter-spacing:-.04em;line-height:1.1}
.pj .pj-p{font-size:15px;color:var(--acc-s);margin-top:8px}
.pj p:not(.pj-p){font-size:16.5px;line-height:1.6;color:#B5B5B5;margin:16px 0 22px;max-width:36ch}
.pj-dots{display:flex;gap:8px}
.pj-dots i{width:28px;height:4px;border-radius:4px;background:#333;transition:background .3s,width .3s}
.pj-dots i.on{background:var(--acc-s);width:44px}
.web-dev{margin-right:calc(var(--pad) * -.9)}
.m-only{display:none}
.wk2{display:grid;grid-template-columns:minmax(0,.65fr) minmax(0,1.35fr);gap:clamp(24px,4vw,72px);align-items:center}
.wk2 + .wk2{margin-top:clamp(40px,6vw,96px)}
.wk2.flip{grid-template-columns:minmax(0,1.35fr) minmax(0,.65fr)}
.wk2.flip .wk2-tx{order:2}
.wk2 h3{font-size:clamp(24px,2vw,32px);font-weight:700;letter-spacing:-.04em;line-height:1.1}
.wk2-p{font-size:15px;color:var(--acc-s);margin-top:8px}
.wk2-tx p:not(.wk2-p){font-size:16.5px;line-height:1.6;color:#B5B5B5;margin:16px 0 22px;max-width:36ch}

.shop-s{height:420vh}
.shop-s .scrub-in{grid-template-columns:minmax(0,1fr) minmax(0,.8fr);gap:clamp(24px,5vw,96px)}
.shop-tx h2{font-size:clamp(34px,3.6vw,62px);line-height:1;font-weight:700;letter-spacing:-.055em;max-width:13ch}
.shop-st{list-style:none;margin:clamp(30px,4vw,56px) 0 0;padding:0;display:grid;gap:22px}
.shop-st li{display:grid;grid-template-columns:76px minmax(0,1fr);align-items:start;opacity:.28;transition:opacity .4s}
.shop-st li.on{opacity:1}
.shop-st .sn{font-size:62px}
.shop-st h3{font-size:clamp(21px,1.7vw,26px);font-weight:700;letter-spacing:-.03em;padding-top:4px}
.shop-st p{font-size:16.5px;line-height:1.55;color:#B5B5B5;margin-top:6px;max-width:34ch}
.shop-dev{justify-self:center;width:min(100%,380px)}

/* Flaches iPhone mit Shop */
.fph-w{width:400px;height:760px;display:grid;place-items:center}
.fph{position:relative;width:340px;height:700px;border-radius:58px;padding:4px;background:linear-gradient(140deg,#e1dcd2,#8d877c 38%,#e9e4da 62%,#99938a);box-shadow:0 60px 90px -40px rgba(0,0,0,.9),0 0 0 1px rgba(0,0,0,.4)}
.fph::before,.fph::after{content:"";position:absolute;left:-3px;width:4px;border-radius:2px;background:#8d877c}
.fph::before{top:150px;height:56px}.fph::after{top:220px;height:56px}
.fph-g{height:100%;border-radius:54px;background:#040404;padding:11px}
.fph-s{position:relative;height:100%;border-radius:44px;overflow:hidden;background:#F7F4EF;display:flex;flex-direction:column;color:#1C1A17;font-family:"Hanken Grotesk",system-ui,sans-serif}
.fph-i{position:absolute;left:50%;top:10px;width:96px;height:28px;margin-left:-48px;border-radius:16px;background:#000;z-index:5}
.fph-sb{background:#F7F4EF;height:44px;padding-top:6px}
.fph-v{position:relative;flex:1;min-height:0}
.ph-scr{position:absolute;inset:0;background:#F7F4EF;transform:translateX(100%);transition:transform .55s var(--ease);display:flex;flex-direction:column}
.ph-scr.on{transform:none;z-index:2}
.ph-scr.past{transform:translateX(-30%)}
.sp-top{display:flex;justify-content:space-between;align-items:center;padding:6px 20px 12px}
.sp-top b{font-family:Fraunces,Georgia,serif;font-weight:600;font-size:19px;letter-spacing:-.01em}
.sp-bag{position:relative;width:24px;height:24px}
.sp-bag svg{width:24px;height:24px}
.sp-bag i{position:absolute;right:-6px;top:-4px;min-width:16px;height:16px;border-radius:8px;background:#1C1A17;color:#fff;font:600 10px/16px system-ui;font-style:normal;text-align:center}
.sp-img{height:250px;background:#E8E2D8 center/cover}
.sp-pad{padding:18px 20px 20px;display:flex;flex-direction:column;flex:1}
.sp-k{font-size:11px;color:#8A6A44;font-weight:600}
.sp-pad h4{font-family:Fraunces,Georgia,serif;font-weight:600;font-size:26px;letter-spacing:-.02em;margin-top:4px}
.sp-m{font-size:13.5px;color:#6E675E;margin-top:2px}
.sp-sz{display:flex;gap:8px;margin-top:16px}
.sp-sz i{font-style:normal;font-size:13px;padding:8px 13px;border-radius:999px;background:#ECE6DC}
.sp-sz i.on{background:#1C1A17;color:#fff}
.sp-pr{display:flex;align-items:baseline;gap:10px;margin-top:16px}
.sp-pr b{font-size:21px}
.sp-pr small{font-size:12px;color:#6E675E}
.sp-btn{margin-top:auto;display:block;text-align:center;padding:15px;border-radius:14px;background:#1C1A17;color:#fff;font-weight:600;font-size:15px}
.sp-btn2{background:#E6DFD3;color:#1C1A17}
.sp-note{font-size:12px;color:#6E675E;text-align:center;margin-top:10px}
.sp-h{margin-bottom:16px}
.sp-item{display:grid;grid-template-columns:64px minmax(0,1fr) auto;gap:12px;align-items:center}
.sp-th{width:64px;height:64px;border-radius:12px;background:#E8E2D8 center/cover}
.sp-item b{font-size:14.5px}
.sp-item span{display:block;font-size:12.5px;color:#6E675E}
.sp-q{display:inline-flex!important;align-items:center;gap:10px;margin-top:6px;font-size:13px;color:#1C1A17!important}
.sp-q i{width:22px;height:22px;border-radius:50%;background:#ECE6DC;display:grid;place-items:center}
.sp-q svg{width:10px;height:10px}
.sp-sum{margin-top:20px;display:grid;gap:9px;font-size:13.5px;color:#4F4941}
.sp-sum div{display:flex;justify-content:space-between}
.sp-tot{font-weight:700;color:#1C1A17;font-size:15.5px;margin-top:6px}
.sp-free{height:6px;border-radius:6px;background:#ECE6DC;margin-top:18px;overflow:hidden}
.sp-free span{display:block;height:100%;background:#5F7F66;border-radius:6px}
.sp-fn{font-size:12px;color:#6E675E;margin-top:8px}
.sp-pay{display:grid;grid-template-columns:22px minmax(0,1fr);column-gap:12px;padding:14px;border-radius:14px;background:#EFEAE2;margin-bottom:8px}
.sp-pay i{grid-row:span 2;width:20px;height:20px;border-radius:50%;border:2px solid #B9B0A3;margin-top:2px}
.sp-pay.on{background:#fff;box-shadow:0 0 0 2px #1C1A17}
.sp-pay.on i{border:6px solid #1C1A17}
.sp-pay b{font-size:15px}
.sp-pay span{font-size:12.5px;color:#6E675E}
.sp-done{align-items:center;text-align:center;padding-top:60px}
.sp-ok{width:76px;height:76px;border-radius:50%;background:#5F7F66;color:#fff;display:grid;place-items:center}
.sp-ok svg{width:36px;height:36px}
.sp-done h4{margin-top:22px}
.sp-done p{font-size:14px;color:#6E675E;margin-top:6px}
.sp-done .sp-sum{width:100%;text-align:left;margin-top:30px}

/* Google-Suche im MacBook: Browserfenster in 1280 x 800, auf den Bildschirm (854 x 534) verkleinert */
.sd .sc-mbp{left:70px;top:8px}
.sd .sc-shm{left:0;width:1040px;top:598px}
.gs{position:absolute;inset:0;overflow:hidden;background:#fff}
.gs-win{position:absolute;left:0;top:0;width:1280px;height:800px;transform:scale(.66719);transform-origin:0 0;font-family:Arial,"Helvetica Neue",sans-serif;color:#202124;background:#fff}
.gs-chrome{height:38px;background:#DEE1E6;display:flex;align-items:flex-end;padding:0 12px;gap:18px}
.gs-dots{display:flex;gap:8px;align-self:center}
.gs-dots i{width:12px;height:12px;border-radius:50%;background:#FF5F57}
.gs-dots i:nth-child(2){background:#FEBC2E}.gs-dots i:nth-child(3){background:#28C840}
.gs-tab{height:30px;min-width:240px;padding:0 16px;display:flex;align-items:center;font-size:12px;color:#3C4043;background:#fff;border-radius:8px 8px 0 0}
.gs-addr{height:36px;display:flex;align-items:center;gap:10px;margin:0;padding:0 16px;background:#fff;box-shadow:0 1px 0 #E4E6EA}
.gs-addr span{flex:1;max-width:820px;height:26px;display:flex;align-items:center;padding:0 14px;border-radius:13px;background:#F1F3F4;font-size:13px;color:#202124}
.gs-in{position:relative;height:726px}
.gs-top{display:flex;align-items:center;padding:20px 28px 0 150px}
.gs-bar{width:692px;height:46px;display:flex;align-items:center;gap:14px;padding:0 8px 0 16px;border-radius:24px;box-shadow:0 1px 6px rgba(32,33,36,.28);font-size:16px}
.gs-ico{margin-left:auto;display:flex;align-items:center;gap:12px}
.gs-ico > i{width:1px;height:26px;background:#DADCE0}
.sr-q{white-space:pre}
.sr-c{width:1px;height:20px;background:#202124;animation:blink 1s steps(1) infinite}
@keyframes blink{50%{opacity:0}}
.gs-av{margin-left:auto;width:32px;height:32px;border-radius:50%;background:#2E5E3F;color:#fff;font-style:normal;font-size:14px;display:grid;place-items:center}
.gs-tabs{display:flex;gap:24px;padding:16px 0 0 166px;font-size:14px;color:#5F6368;box-shadow:0 1px 0 #EBEBEB}
.gs-tabs > *{padding:0 2px 11px}
.gs-tabs b{font-weight:400;color:#1A0DAB;box-shadow:inset 0 -3px 0 #1A0DAB}
.gs-tl{margin-left:auto;margin-right:40px}
.gs-res{position:relative;height:620px}
.gs-list{position:absolute;inset:0;display:flex;gap:56px;padding:20px 0 0 166px;opacity:0;transform:translateY(6px);transition:opacity .4s,transform .5s var(--ease)}
.gs-list.on{opacity:1;transform:none}
.gs-main{width:652px;flex:none}
.gs-r{margin-bottom:28px}
.gs-src{display:flex;align-items:center;gap:12px;margin-bottom:6px}
.gs-src b{display:block;font-size:14px;font-weight:400;color:#202124;line-height:20px}
.gs-src span{display:block;font-size:12px;color:#4D5156;line-height:18px}
.gs-fav{flex:none;width:28px;height:28px;border-radius:50%;display:grid;place-items:center;font-style:normal;font-size:13px;font-weight:700;box-shadow:0 0 0 1px #ECEDEF}
.gs-ad{font-size:14px;font-weight:700;color:#202124}
.gs-r > a{display:block;font-size:20px;line-height:26px;color:#1A0DAB}
.gs-r p{font-size:14px;line-height:22px;color:#4D5156;margin-top:4px}
.gs-sl{display:flex;gap:22px;margin-top:6px}
.gs-sl a{font-size:14px;color:#1A0DAB}
.gs-loc{margin-bottom:26px}
.gs-h{display:block;font-size:20px;font-weight:400;margin-bottom:12px}
.gs-map{display:block;width:100%;height:150px;border-radius:12px}
.gs-pin{transform-origin:318px 92px;animation:pinIn .7s var(--ease) both}
@keyframes pinIn{from{transform:translateY(-16px);opacity:0}to{transform:none;opacity:1}}
.gs-biz{display:flex;justify-content:space-between;align-items:center;padding:12px 0}
.gs-biz b{display:block;font-size:16px;font-weight:400;color:#1A0DAB}
.gs-biz > div > span{display:block;font-size:14px;color:#4D5156;margin-top:3px;line-height:20px}
.gs-biz em,.gs-kp em{font-style:normal;color:#188038}
.gs-rt{color:#4D5156;margin-right:4px}
.gs-st{color:#FBBC04;letter-spacing:-.04em}
.gs-bt{display:flex;gap:8px}
.gs-bt i{font-style:normal;font-size:14px;padding:7px 14px;border-radius:18px;box-shadow:0 0 0 1px #DADCE0;color:#1A0DAB}
.gs-kp{width:368px;flex:none;align-self:flex-start;border-radius:8px;box-shadow:0 0 0 1px #DADCE0;overflow:hidden}
.gs-kp img{display:block;width:100%;height:150px;object-fit:cover}
.gs-kpb{padding:14px 16px 18px}
.gs-kpb > b{display:block;font-size:22px;font-weight:400;line-height:28px}
.gs-kpb > span{display:block;font-size:14px;margin-top:4px}
.gs-mut{color:#70757A}
.gs-kpb .gs-bt{margin:14px 0}
.gs-kpb p{font-size:14px;line-height:22px;color:#202124}
.gs-kpb p b{font-weight:700}
.sd-ctl{display:flex;flex-wrap:wrap;align-items:center;gap:10px 18px;margin-top:clamp(14px,2vw,26px)}
.sr-sw{display:inline-flex;gap:4px;padding:4px;border-radius:999px;background:#1F1F1F}
.sr-sw button{padding:8px 16px;border-radius:999px;font-size:14px;color:#B9B9B9}
.sr-sw button[aria-pressed="true"]{background:var(--sage);color:#151515}
.sd-cap{display:none;font-size:15px;color:#C4C4C4}
.sd-cap.on{display:block}
.sd .demo-n{margin-top:10px}

/* Hosting: Karte */
.hmw{position:relative;margin:0 calc(var(--pad) * -.4) 0 -4%;padding-bottom:12%}
.hm{width:100%;height:auto;overflow:visible}
.hm-a{fill:none;stroke:var(--acc-s);stroke-width:1.6;stroke-dasharray:1;stroke-dashoffset:1;opacity:.75}
.hmw.go .hm-a{animation:draw 1.6s var(--d) var(--ease) forwards}
@keyframes draw{to{stroke-dashoffset:0}}
.hm-c circle{fill:#6B7A70}
.hm-c text,.hm-g text{font:500 17px "Hanken Grotesk",system-ui,sans-serif;fill:#8E8E8E}
.hm-g text{fill:var(--text);font-weight:700;font-size:22px}
.hm-p{fill:var(--acc-s);opacity:.35;transform-origin:center;transform-box:fill-box;animation:pulse 2.4s ease-out infinite}
@keyframes pulse{from{transform:scale(.6);opacity:.55}to{transform:scale(2.6);opacity:0}}
.hs{position:absolute;right:-2%;bottom:-30%;width:min(330px,62%);background:#1D1D1D;border-radius:22px;padding:22px 24px;box-shadow:0 40px 80px -30px rgba(0,0,0,.85)}
.hs-t{display:flex;justify-content:space-between;align-items:center;gap:12px;margin-bottom:14px}
.hs-t b{font-size:17px}
.hs-on{display:inline-flex;align-items:center;gap:7px;font-size:13px;color:var(--acc-s)}
.hs-on i{width:8px;height:8px;border-radius:50%;background:var(--acc-s);box-shadow:0 0 0 4px rgba(163,194,170,.18)}
.hs dl{margin:0;display:grid;gap:9px}
.hs dl div{display:flex;justify-content:space-between;gap:12px;font-size:14px}
.hs dt{color:#8E8E8E}
.hs dd{margin:0;font-variant-numeric:tabular-nums;text-align:right}

/* Microsoft 365: erster Arbeitstag */
.ob{background:#1C1C1C;border-radius:26px;padding:clamp(22px,2.4vw,34px);box-shadow:0 50px 90px -50px rgba(0,0,0,.9)}
.ob-h{display:flex;align-items:center;gap:16px}
.ob-av{width:52px;height:52px;border-radius:50%;background:#2E3D33;color:var(--acc-a1);display:grid;place-items:center;font-weight:700;font-size:17px;flex:none}
.ob-h b{display:block;font-size:20px;letter-spacing:-.02em}
.ob-h div span{display:block;font-size:14.5px;color:#8E8E8E;margin-top:2px}
.ob-l{list-style:none;margin:26px 0 0;padding:0;display:grid;gap:6px}
.ob-l li{display:grid;grid-template-columns:30px minmax(0,1fr) auto;align-items:center;gap:12px;padding:11px 14px;border-radius:14px;font-size:15.5px;color:#6A6A6A;transition:color .3s,background .3s}
.ob-i{width:26px;height:26px;border-radius:50%;display:grid;place-items:center;background:#262626;color:transparent;transition:background .3s,color .3s}
.ob-i svg{width:13px;height:13px}
.ob-l li em{font-style:normal;font-size:12.5px;color:#6F6F6F;font-variant-numeric:tabular-nums}
.ob-l li.run{background:#222}
.ob-l li.run .ob-i{background:transparent;box-shadow:inset 0 0 0 2px var(--acc-s);animation:spin 0.8s linear infinite;border-radius:50%;clip-path:polygon(50% 0,100% 0,100% 100%,0 100%,0 50%,50% 50%)}
@keyframes spin{to{transform:rotate(360deg)}}
.ob-l li.ok{color:var(--text)}
.ob-l li.ok .ob-i{background:var(--acc-s);color:#0C201A}
.ob-f{display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;margin-top:22px}
.ob-s{font-size:15px;color:#B5B5B5}
.ob-s b{color:var(--acc-s)}

/* KI-Chatbot */
.cb{background:#F6F6F3;color:#1D1D1B;border-radius:26px;overflow:hidden;box-shadow:0 50px 90px -50px rgba(0,0,0,.9);display:flex;flex-direction:column;height:min(620px,78svh);max-width:500px;margin-left:auto;font-family:"Hanken Grotesk",system-ui,sans-serif}
.cb-h{display:flex;align-items:center;gap:12px;padding:16px 20px;background:#1D2621;color:#fff}
.cb-h svg{width:30px;height:auto}
.cb-h b{display:block;font-size:16px}
.cb-h span{display:inline-flex;align-items:center;gap:6px;font-size:12.5px;color:#BFD3C4}
.cb-h span i{width:7px;height:7px;border-radius:50%;background:#8FD19E}
.cb-m{flex:1;min-height:0;overflow-y:auto;padding:20px 18px;display:flex;flex-direction:column;gap:10px;scroll-behavior:smooth}
.cb-b{max-width:82%;padding:12px 15px;border-radius:18px;font-size:15px;line-height:1.5}
.cb-bot{background:#fff;border-bottom-left-radius:6px;box-shadow:0 1px 2px rgba(0,0,0,.06)}
.cb-me{align-self:flex-end;background:#1D2621;color:#fff;border-bottom-right-radius:6px}
.cb-ty{display:inline-flex;gap:4px;padding:16px 16px}
.cb-ty i{width:7px;height:7px;border-radius:50%;background:#A8ADA9;animation:dot 1s infinite}
.cb-ty i:nth-child(2){animation-delay:.15s}.cb-ty i:nth-child(3){animation-delay:.3s}
@keyframes dot{0%,60%,100%{transform:none;opacity:.5}30%{transform:translateY(-4px);opacity:1}}
.cb-c{display:flex;flex-wrap:wrap;gap:8px;padding:4px 16px 14px}
.cb-c button{font-size:14px;padding:9px 14px;border-radius:999px;background:#fff;color:#1D2621;box-shadow:inset 0 0 0 1.5px #C9D6CC;transition:background .2s}
.cb-c button:hover{background:#E8F0EA}
.cb-c button:disabled{opacity:.35;cursor:default}
.cb-in{display:flex;justify-content:space-between;align-items:center;margin:0 14px 14px;padding:13px 16px;border-radius:999px;background:#fff;color:#9A9A96;font-size:14px}
.cb-in i{color:#B8BDB9}

/* Übersicht Leistungen */
.ov2{display:grid;grid-template-columns:minmax(0,.9fr) minmax(0,1.1fr);gap:clamp(30px,5vw,90px);align-items:start}
.ov2-b{min-height:78svh;display:flex;flex-direction:column;justify-content:center;padding:40px 0;opacity:.3;transition:opacity .45s}
.ov2-b.on{opacity:1}
.ov2-m{display:none}
.ov2-b h2{font-size:clamp(46px,5.4vw,96px);line-height:.95;font-weight:700;letter-spacing:-.06em}
.ov2-b p{font-size:clamp(17px,1.35vw,21px);line-height:1.55;color:#C0C0C0;margin-top:22px;max-width:40ch}
.ov2-b ul{list-style:none;margin:18px 0 26px;padding:0;display:flex;flex-wrap:wrap;gap:8px 20px;font-size:15px;color:var(--acc-s)}
.ov2-dev{position:sticky;top:calc(50svh - 22vw);margin-right:calc(var(--pad) * -.5)}
.mac{position:relative;width:100%;aspect-ratio:1060/690}
.mac-scr{position:absolute;left:9.717%;top:6.522%;width:80.566%;height:77.391%;overflow:hidden;background:#0B0B0B;border-radius:.6% .6% 0 0}
.mac-scr img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;object-position:top}
.ov2-s{opacity:0;transition:opacity .5s}
.ov2-s.on{opacity:1}
.mac-gl{position:absolute;inset:0;background:linear-gradient(118deg,rgba(255,255,255,.08),rgba(255,255,255,.02) 30%,rgba(255,255,255,0) 44%);pointer-events:none}
.mac-fr{position:absolute;inset:0;width:100%;height:100%;pointer-events:none}
.get3{grid-template-columns:repeat(3,minmax(0,1fr))}
.who2{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:10px}
.who2 li{font-size:clamp(17px,1.4vw,21px);padding:14px 22px;border-radius:999px;background:#1C1C1C;color:#D8D8D8}

/* Preise: Satz zum Ausfüllen */
.cf{padding-top:clamp(20px,3vw,40px)}
.cf-s{font-size:clamp(28px,3.1vw,56px);line-height:1.45;font-weight:600;letter-spacing:-.04em;color:#8A8A8A;max-width:30ch}
.cf-s p + p{margin-top:.4em}
.nw{white-space:nowrap}
.cf-sw{display:inline;white-space:normal}
.cf-sw button,.cf-x{font:inherit;letter-spacing:inherit;line-height:1.15;white-space:nowrap;color:#4A4A4A;padding:.02em .22em .06em;border-radius:.3em;transition:color .2s,background .2s;vertical-align:baseline}
.cf-sw button[aria-pressed="true"],.cf-x[aria-pressed="true"]{color:#0C201A;background:var(--acc-s)}
.cf-sw button[aria-pressed="false"]:hover,.cf-x[aria-pressed="false"]:hover{color:#BDBDBD;background:#1F1F1F}
.cf-x{display:inline-flex;align-items:center;gap:.22em;margin:.06em 0}
.cf-x i{display:inline-grid;place-items:center;width:.62em;height:.62em;border-radius:50%;background:#262626;color:var(--acc-s);transition:transform .3s var(--ease),background .2s,color .2s}
.cf-x i svg{width:.32em;height:.32em}
.cf-x[aria-pressed="true"] i{transform:rotate(45deg);background:rgba(12,32,26,.18);color:#0C201A}
.cf-st{display:inline-flex;align-items:center;gap:.14em;vertical-align:baseline;color:var(--text)}
.cf-st button{width:.82em;height:.82em;border-radius:50%;display:inline-grid;place-items:center;background:#222;color:var(--acc-s);transform:translateY(-.06em);transition:background .2s}
.cf-st button:hover{background:#2E2E2E}
.cf-st button svg{width:.38em;height:.38em}
.cf-st output{min-width:1.1ch;text-align:center;font-variant-numeric:tabular-nums;color:var(--text)}
.cf-out{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(30px,5vw,96px);align-items:end;margin-top:clamp(50px,6vw,100px);padding:clamp(28px,3.5vw,56px);border-radius:32px;background:#1B1B1B}
.cf-tot small{font-size:15px;color:var(--muted)}
.cf-tot .big{margin-top:10px}
.cf-tot .big-v{font-size:clamp(80px,10vw,190px)}
.cf-tot p{font-size:16px;color:#A9A9A9;margin-top:18px}
.cf-br ul{list-style:none;margin:0 0 28px;padding:0;display:grid;gap:10px}
.cf-br li{display:flex;justify-content:space-between;gap:20px;font-size:16px;color:#BDBDBD}
.cf-br li b{font-weight:600;color:var(--text);font-variant-numeric:tabular-nums;white-space:nowrap}
.pgs{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:clamp(50px,6vw,100px) clamp(40px,7vw,140px)}
.pg h3{font-size:clamp(26px,2.4vw,40px);font-weight:700;letter-spacing:-.045em}
.pg .tiers{margin-top:20px}

/* Über uns */
.bel2{display:grid;gap:clamp(56px,7vw,110px)}
.bel2 > div{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:clamp(24px,6vw,120px);align-items:start}
.bel2 h2{font-size:clamp(34px,4vw,70px);line-height:1;font-weight:700;letter-spacing:-.055em}
.bel2 p{font-size:clamp(17px,1.35vw,20px);line-height:1.65;color:#B5B5B5;max-width:44ch;padding-top:.4em}
.band2{position:relative;background:var(--sage);color:var(--ink);overflow:hidden;margin-top:clamp(90px,11vw,170px);padding-top:clamp(80px,10vw,150px);padding-bottom:clamp(80px,10vw,150px);display:grid;grid-template-columns:minmax(0,1.4fr) minmax(0,.6fr);gap:clamp(32px,5vw,96px);align-items:center}
.band2 > *:not(.grain){position:relative}
.band2 h2{font-size:clamp(36px,4.6vw,82px);line-height:.98;font-weight:700;letter-spacing:-.055em;max-width:15ch}
.band2 p{font-size:clamp(18px,1.4vw,21px);line-height:1.65;color:#17241F;max-width:50ch;margin-top:28px}
.band2-mark{width:min(100%,300px);justify-self:end}
.band2-mark .lm-l{fill:#B7CDBC}.band2-mark .lm-d{fill:var(--ink)}
.tl2{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:clamp(36px,4vw,64px) clamp(28px,4vw,72px)}
.tl2 b{display:block;font-size:clamp(28px,3vw,52px);line-height:1;font-weight:700;letter-spacing:-.05em}
.tl2 span{display:block;font-size:16px;line-height:1.5;color:#9E9E9E;margin-top:12px;max-width:28ch}
.li2{margin-top:clamp(40px,5vw,72px);padding-bottom:clamp(20px,3vw,40px)}

/* Kontakt, Fragen, Rechtliches: ohne Linien */
.ph{padding-top:clamp(130px,14vw,210px);padding-bottom:clamp(56px,7vw,100px)}
.ph h1{font-size:clamp(46px,5.6vw,104px);line-height:.97;font-weight:700;letter-spacing:-.058em;max-width:14ch}
.ph-s h1{font-size:clamp(42px,4.6vw,80px)}
.sp-in{font-size:clamp(18px,1.4vw,22px);line-height:1.55;color:#C4C4C4;max-width:46ch;margin-top:clamp(22px,2.4vw,34px)}
.k-hero .direct div,.k-hero .direct div:last-child{border:0;padding:12px 0}
.bk-step{border-top:0!important;padding:0 0 clamp(36px,4vw,52px)!important}
.bk-h h2 i{font-size:30px;font-weight:700;color:var(--acc-s);letter-spacing:-.04em}
.next li{border-top:0!important;padding:10px 0!important}
input[type=text],input[type=email],textarea{background:#1C1C1C!important;border:0!important;border-radius:14px!important;padding:15px 18px!important;font-size:17px!important;box-shadow:inset 0 0 0 1.5px transparent;transition:box-shadow .2s}
input:focus,textarea:focus{box-shadow:inset 0 0 0 1.5px var(--acc-s)}
.fq-list,.fq-list li{border:0!important}
.fq{padding:16px 0!important}
.legal-text h2{margin-top:52px}

/* Handy */
@media (max-width: 1000px){
  .get,.get3,.tl2{grid-template-columns:repeat(2,minmax(0,1fr))}
}
@media (max-width: 860px){
  .xh{grid-template-columns:minmax(0,1fr);min-height:0;padding-top:118px;gap:48px}
  .xs-h,.xp,.xq,.bel2 > div,.band2,.cf-out,.pgs{grid-template-columns:minmax(0,1fr)}
  .xs-h{gap:16px}
  .pc-only{display:none}
  .m-only{display:block}
  .wk2,.wk2.flip{grid-template-columns:minmax(0,1fr);gap:18px}
  .wk2.flip .wk2-tx{order:0}
  .shop-s{height:380vh}
  .shop-s .scrub-in{grid-template-columns:minmax(0,1fr);align-content:center;gap:10px;padding-top:64px}
  .shop-tx h2{font-size:28px;max-width:none}
  .shop-st{margin-top:12px;min-height:96px;position:relative}
  .shop-st li{position:absolute;inset:0 0 auto 0;opacity:0;transition:opacity .35s}
  .shop-st li.on{opacity:1}
  .shop-st .sn{font-size:44px}
  .shop-st li{grid-template-columns:52px minmax(0,1fr)}
  .shop-st p{font-size:15px}
  .shop-dev{width:min(64vw,270px)}
  .shop-dev .demo-n{display:none}
  .ov2{grid-template-columns:minmax(0,1fr)}
  .ov2-dev{display:none}
  .ov2-m{display:block;margin-bottom:22px}
  .ov2-b{min-height:0;opacity:1;padding:34px 0}
  .hs{position:relative;right:auto;bottom:auto;width:100%;margin-top:18px}
  .cb{margin:0 auto;height:560px}
  .band2-mark{justify-self:start;width:120px}
  .cf-s{font-size:clamp(26px,7.4vw,40px)}
}
@media (max-width: 560px){
  .get,.get3,.tl2,.getc{grid-template-columns:minmax(0,1fr)}
  .stp3 li{grid-template-columns:minmax(0,1fr);gap:4px}
  .xh-act .btn{flex:1 1 100%;justify-content:center}
  .qa2 summary{padding:18px 18px}
  .qa2 p{padding:0 18px 20px}
}
'''

JS = r'''
(function(){
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Bühnen mit fester Grösse auf die verfügbare Breite skalieren */
  document.querySelectorAll('[data-stage]').forEach(st => {
    const [w, h] = st.dataset.stage.split('x').map(Number), inn = st.firstElementChild;
    const fit = () => { const s = st.clientWidth / w; inn.style.transform = 'scale(' + s + ')'; st.style.height = (h * s) + 'px'; };
    new ResizeObserver(fit).observe(st); fit();
  });

  /* iPhone mit echter Dicke: viele Schichten hintereinander */
  document.querySelectorAll('[data-phone3d]').forEach(ph => {
    const N = 16, D = 27;
    for (let i = 0; i < N; i++) {
      const t = i / (N - 1), z = -D / 2 + D * t, k = Math.sin(t * Math.PI), l = Math.round(118 + 70 * k);
      const s = document.createElement('div'); s.className = 'sc-slice'; s.style.setProperty('--c', `rgb(${l},${l - 5},${l - 13})`); s.style.transform = `translateZ(${z}px)`;
      if (i > 3 && i < N - 4) for (const [top, h] of [[104, 26], [148, 46], [204, 46]]) { const b = document.createElement('i'); b.className = 'sc-btn'; b.style.top = top + 'px'; b.style.height = h + 'px'; b.style.setProperty('--c', `rgb(${l - 18},${l - 22},${l - 30})`); s.appendChild(b); }
      ph.insertBefore(s, ph.firstChild);
    }
  });

  /* Scroll-Passagen: Fortschritt 0 bis 1 */
  const H = {
    web(s, p){
      const k = p < .5 ? 0 : 1, q = k ? (p - .5) * 2 : p * 2, e = Math.min(1, Math.max(0, (q - .12) / .76));
      if (s._k !== k) { s._k = k; s.querySelectorAll('.pj').forEach(el => el.classList.toggle('on', +el.dataset.proj === k)); }
      s.querySelectorAll('.sc-shot').forEach(img => {
        const on = +img.dataset.proj === k; img.classList.toggle('on', on);
        if (on) { const range = Math.max(0, img.offsetHeight - img.parentElement.clientHeight); img.style.transform = 'translateY(' + (-range * e).toFixed(1) + 'px)'; }
      });
    },
    shop(s, p){
      const k = Math.min(3, Math.floor(p * 4.2));
      if (s._k === k) return; s._k = k;
      s.querySelectorAll('.shop-st li').forEach(el => el.classList.toggle('on', +el.dataset.st === k));
      s.querySelectorAll('.ph-scr').forEach(el => { const i = +el.dataset.i; el.classList.toggle('on', i === k); el.classList.toggle('past', i < k); });
    }
  };
  const scrubs = [...document.querySelectorAll('[data-scrub]')];
  if (scrubs.length) {
    let raf = 0;
    const tick = () => { raf = 0; scrubs.forEach(s => { if (!s.offsetHeight) return; const r = s.getBoundingClientRect(), span = r.height - innerHeight; const p = Math.min(1, Math.max(0, -r.top / (span || 1))); if (s._p !== p) { s._p = p; H[s.dataset.scrub](s, p); } }); };
    addEventListener('scroll', () => { if (!raf) raf = requestAnimationFrame(tick); }, {passive:true});
    addEventListener('resize', tick); addEventListener('load', tick); tick();
  }

  const inView = (el, fn, th = .35) => { if (!el) return; const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { io.disconnect(); fn(); } }), {threshold: th}); io.observe(el); };

  /* Google-Suche im MacBook: tippen, dann vorher und nachher */
  const sr = document.getElementById('seoDemo');
  if (sr) {
    const q = sr.querySelector('.sr-q'), txt = q.dataset.q, parts = sr.querySelectorAll('.gs-list,.sd-cap'), btns = sr.querySelectorAll('.sr-sw button');
    let auto = true;
    const show = v => { parts.forEach(l => l.classList.toggle('on', +l.dataset.v === v)); btns.forEach(b => b.setAttribute('aria-pressed', +b.dataset.v === v)); };
    btns.forEach(b => b.addEventListener('click', () => { auto = false; q.textContent = txt; show(+b.dataset.v); }));
    const run = () => {
      if (reduce) { q.textContent = txt; show(1); return; }
      let i = 0; show(-1);
      const t = setInterval(() => { q.textContent = txt.slice(0, ++i); if (i >= txt.length) { clearInterval(t); setTimeout(() => { if (auto) show(0); }, 350); setTimeout(() => { if (auto) show(1); }, 2600); } }, 75);
    };
    q.textContent = txt; show(1); inView(sr, run);
  }

  /* Hosting: Linien nach Genf, Laufzeit zählt mit */
  const hm = document.getElementById('hostMap');
  if (hm) {
    inView(hm, () => hm.classList.add('go'), .25);
    const up = document.getElementById('hsUp'), start = Date.now() - ((214 * 24 + 6) * 3600 + 12 * 60 + 9) * 1000;
    const pad = n => String(n).padStart(2, '0');
    const draw = () => { const s = Math.floor((Date.now() - start) / 1000), d = Math.floor(s / 86400); up.textContent = d + ' Tage, ' + pad(Math.floor(s % 86400 / 3600)) + ':' + pad(Math.floor(s % 3600 / 60)) + ':' + pad(s % 60); };
    draw(); if (!reduce) setInterval(draw, 1000);
  }

  /* Microsoft 365: Konto Schritt für Schritt */
  const ob = document.getElementById('onb');
  if (ob) {
    const li = [...ob.querySelectorAll('.ob-l li')], st = ob.querySelector('.ob-s'), btn = ob.querySelector('.ob-b');
    let busy = false;
    const go = () => {
      if (busy) return; busy = true; btn.disabled = true;
      li.forEach(l => { l.className = ''; l.querySelector('em').textContent = ''; });
      st.textContent = 'Wird eingerichtet …';
      let i = 0, clock = 7 * 60 + 41;
      const next = () => {
        if (i > 0) { li[i - 1].className = 'ok'; li[i - 1].querySelector('em').textContent = '07:' + String(clock++ % 60).padStart(2, '0'); }
        if (i === li.length) { st.innerHTML = '<b>Fertig.</b> Marco kann am Montag um 07:30 loslegen.'; btn.textContent = 'Nochmals zeigen'; btn.disabled = false; busy = false; return; }
        li[i].className = 'run'; i++; setTimeout(next, reduce ? 0 : 650);
      };
      next();
    };
    btn.addEventListener('click', go);
    inView(ob, () => setTimeout(go, 500), .5);
  }

  /* KI-Chatbot: vorbereitete Fragen */
  const cb = document.getElementById('chat');
  if (cb) {
    const A = JSON.parse(cb.dataset.a), box = cb.querySelector('.cb-m');
    const add = (cls, html) => { const d = document.createElement('div'); d.className = 'cb-b ' + cls; d.innerHTML = html; box.appendChild(d); box.scrollTop = box.scrollHeight; return d; };
    cb.querySelectorAll('.cb-c button').forEach(b => b.addEventListener('click', () => {
      if (cb._busy) return; cb._busy = true; b.disabled = true;
      add('cb-me', b.textContent);
      const ty = add('cb-bot cb-ty', '<i></i><i></i><i></i>');
      setTimeout(() => {
        ty.remove(); const a = A[+b.dataset.i], d = add('cb-bot', '');
        if (reduce) { d.textContent = a; cb._busy = false; return; }
        let i = 0; const t = setInterval(() => { i += 2; d.textContent = a.slice(0, i); box.scrollTop = box.scrollHeight; if (i >= a.length) { clearInterval(t); cb._busy = false; } }, 18);
      }, reduce ? 0 : 750);
    }));
  }

  /* Leistungen: aktiver Block wechselt den Bildschirm */
  const ovb = [...document.querySelectorAll('.ov2-b')];
  if (ovb.length) {
    const scr = [...document.querySelectorAll('.ov2-s')];
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { const k = +e.target.dataset.k; ovb.forEach((b, i) => b.classList.toggle('on', i === k)); scr.forEach((s, i) => { if (i === k) s.loading = 'eager'; s.classList.toggle('on', i === k); }); } }), {rootMargin: '-45% 0px -45% 0px'});
    ovb.forEach(b => io.observe(b));
  }
})();
'''

PREISE_JS = r'''
(function(){
  const $ = id => document.getElementById(id), fmt = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '’');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const PROD = [['bis 30', 0], ['bis 150', 490], ['bis 500', 990], ['über 500', 1890]];
  const S = {type:'web', pages:4, prod:0, lang:1, texts:0, x:{}};
  const LIM = {cfPages:[1, 30], cfProd:[0, 3], cfLang:[1, 4]};
  let shown = 590, anim = 0, last = '';
  const count = to => { cancelAnimationFrame(anim); if (reduce) { $('cfTotal').textContent = fmt(to); shown = to; return; } const from = shown, t0 = performance.now(); const step = t => { const k = Math.min(1, (t - t0) / 420), e = 1 - Math.pow(1 - k, 3); shown = Math.round(from + (to - from) * e); $('cfTotal').textContent = fmt(shown); if (k < 1) anim = requestAnimationFrame(step); }; anim = requestAnimationFrame(step); };
  function calc(){
    const shop = S.type === 'shop', L = [];
    $('cfPages').textContent = S.pages; $('cfPagesW').textContent = S.pages === 1 ? 'Seite' : 'Seiten';
    $('cfProd').textContent = PROD[S.prod][0]; $('cfProdW').hidden = !shop;
    $('cfLang').textContent = S.lang; $('cfLangW').textContent = S.lang === 1 ? 'Sprache' : 'Sprachen';
    L.push([shop ? 'Shop mit 4 Seiten und 30 Produkten' : 'Website mit 4 Seiten', shop ? 1890 : 590]);
    if (S.pages > 4) L.push([(S.pages - 4) + ' weitere Seite' + (S.pages > 5 ? 'n' : ''), (S.pages - 4) * 150]);
    if (shop && PROD[S.prod][1]) L.push(['Produkte ' + PROD[S.prod][0], PROD[S.prod][1]]);
    if (S.lang > 1) L.push([(S.lang - 1) + ' weitere Sprache' + (S.lang > 2 ? 'n' : ''), (S.lang - 1) * 50]);
    if (S.texts) L.push(['Texte für ' + S.pages + ' Seiten', S.pages * 90]);
    document.querySelectorAll('.cf-x').forEach(b => { if (S.x[b.dataset.x]) L.push([b.textContent, +b.dataset.p]); });
    const total = L.reduce((a, l) => a + l[1], 0);
    count(total);
    $('cfMonth').textContent = shop ? 'Dazu das Shopify-Abo, das Sie direkt an Shopify zahlen.' : 'Dazu Hosting und Domain für CHF 25 im Monat.';
    $('cfLines').innerHTML = L.map(l => `<li><span>${l[0]}</span><b>CHF ${fmt(l[1])}</b></li>`).join('');
    last = 'Preisrechner: ' + L.map(l => l[0] + ' (CHF ' + fmt(l[1]) + ')').join(', ') + '. Total CHF ' + fmt(total) + '.';
  }
  document.querySelectorAll('[data-t]').forEach(b => b.onclick = () => { document.querySelectorAll('[data-t]').forEach(o => o.setAttribute('aria-pressed', o === b)); S.type = b.dataset.t; calc(); });
  document.querySelectorAll('[data-tx]').forEach(b => b.onclick = () => { document.querySelectorAll('[data-tx]').forEach(o => o.setAttribute('aria-pressed', o === b)); S.texts = +b.dataset.tx; calc(); });
  document.querySelectorAll('.cf-x').forEach(b => b.onclick = () => { S.x[b.dataset.x] = !S.x[b.dataset.x]; b.setAttribute('aria-pressed', !!S.x[b.dataset.x]); calc(); });
  const key = {cfPages:'pages', cfProd:'prod', cfLang:'lang'};
  document.querySelectorAll('[data-step]').forEach(b => b.onclick = () => { const id = b.dataset.step, k = key[id], [lo, hi] = LIM[id]; S[k] = Math.min(hi, Math.max(lo, S[k] + +b.dataset.d)); calc(); });
  $('cfGo').addEventListener('click', () => { try { localStorage.setItem('websiten-anfrage', last); } catch(e){} });
  calc();
})();
'''

SERVICE_PAGES = {FILES[k]: service(k) for k in ORDER}
