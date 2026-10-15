import sys, re
sys.path.insert(0, '.')
from parts import page
import fast
import home, home3, home4, home5, home6, home7, home8, home9, pages as P, pages2 as P2, pages3 as P3
# Web-App-Adresse des Google Apps Script für die Terminbuchung. Leer = Vorschau-Modus.
BOOKING_API = ''
import base64
PHOTO2 = 'data:image/jpeg;base64,' + base64.b64encode(open('../assets/img/hero-salon-1200.jpg','rb').read()).decode()
from parts import MARK_LIGHT, MARK_DARK
I3 = {k: 'data:image/jpeg;base64,' + base64.b64encode(open('../assets/img/' + k + ('.jpg' if k=='cafe' else '-s.jpg'),'rb').read()).decode() for k in ('cafe','coiffeur','restaurant','laden2','baeckerei')}
IMG = {k: 'data:image/jpeg;base64,' + base64.b64encode(open('../assets/img/' + k + '-s.jpg','rb').read()).decode() for k in ('cafe','coiffeur','restaurant','laden2','baeckerei')}
PHOTO = 'data:image/jpeg;base64,' + base64.b64encode(open('../assets/img/bad-keller-1200.jpg','rb').read()).decode()
MAP = open('swissmap.json').read()
H4MAIN = home4.MAIN.replace('%%PHOTO%%', PHOTO)
for k, v in I3.items(): H4MAIN = H4MAIN.replace('%%I_' + k + '%%', v)
I5 = {k: 'data:image/jpeg;base64,' + base64.b64encode(open('../assets/img/' + k + '-s.jpg','rb').read()).decode() for k in ('cafe','laden2','restaurant','werkstatt','planung','coiffeur')}
H5MAIN = home5.MAIN.replace('%%PHOTO%%', PHOTO).replace('%%FILMPOSTER%%', 'data:image/jpeg;base64,' + base64.b64encode(open('../video/poster.jpg','rb').read()).decode())
for k, v in I5.items(): H5MAIN = H5MAIN.replace('%%I_' + k + '%%', v)
H6MAIN = home6.MAIN.replace('%%PHOTO%%', PHOTO).replace('%%HEROPOSTER%%', 'data:image/jpeg;base64,' + base64.b64encode(open('../video/bg-poster.jpg','rb').read()).decode())
for k, v in I5.items(): H6MAIN = H6MAIN.replace('%%I_' + k + '%%', v)
def _fill(m):
    m = m.replace('%%PHOTO%%', PHOTO).replace('%%HEROPOSTER%%', 'data:image/jpeg;base64,' + base64.b64encode(open('../video/bg-poster.jpg','rb').read()).decode())
    for k, v in I5.items(): m = m.replace('%%I_' + k + '%%', v)
    return m
def _js(j): return j.replace('%%MAP%%', MAP).replace('%%ML%%', MARK_LIGHT).replace('%%MD%%', MARK_DARK)
_m, _c, _j = home7.version(1); V1 = (_fill(_m), _c, _js(_j))
_S = {k: 'data:image/jpeg;base64,' + base64.b64encode(open('../assets/img/sv-' + k + '.jpg','rb').read()).decode() for k in ('websites','shops','seo','hosting','m365','ki')}
_PG = 'data:image/jpeg;base64,' + base64.b64encode(open('../assets/img/bad-keller-1200-g.jpg','rb').read()).decode()
_m = home8.MAIN.replace('%%PHOTO%%', _PG)
for k, v in _S.items(): _m = _m.replace('%%S_' + k + '%%', v)
V8 = (_fill(_m), home8.CSS, _js(home8.JS))
_m = home9.MAIN.replace('%%PHOTO%%', _PG)
_b64 = lambda p, t: 'data:' + t + ';base64,' + base64.b64encode(open(p,'rb').read()).decode()
for _k in ('kf','ka'): _m = _m.replace('%%DEV_' + _k + '%%', _b64('../assets/img/dev-' + _k + '.webp', 'image/webp'))
_m = _m.replace('%%MACFRAME%%', _b64('../assets/img/mac-frame.webp', 'image/webp'))
for _k in ('websites','shops','seo','hosting','m365','ki'): _m = _m.replace('%%SCR_' + _k + '%%', _b64('../assets/img/scr-' + _k + '.jpg', 'image/jpeg'))
for _k in ('kf','ka'):
    for _t in ('d','m'):
        _m = _m.replace('%%R_' + _k + '_' + _t + '%%', 'data:image/jpeg;base64,' + base64.b64encode(open('../assets/img/ref-' + _k + '-' + _t + '.jpg','rb').read()).decode())
V9 = (_fill(_m), home9.CSS, _js(home9.JS))
_m, _c, _j = home7.version(2); V2 = (_fill(_m), _c, _js(_j))
_m, _c, _j = home7.options(); VO = (_fill(_m), _c, _j)
out = {
 'index.html': ('websiten.ch', home9.DESC, *V9),
 'version-2.html': ('websiten.ch', home7.DESC, *V2),
 'optionen-leistungen.html': ('Was wir machen: Möglichkeiten | websiten.ch', 'Fünf Möglichkeiten für die Leistungen auf der Startseite.', *VO),
 'leistungen.html': (*P3.leistungen(), P3.CSS, P3.JS),
 'preise.html': (*P3.preise(), P3.CSS, P3.PREISE_JS),
 'ueber-uns.html': (*P3.ueber(), P3.CSS + P3.FILM_CSS, P3.FILM_JS),
 'kontakt.html': (lambda t, d, m, c, j: (t, d, m, c + P3.CSS, j.replace('%%BOOKING_API%%', BOOKING_API)))(*P3.kontakt()),
 'fragen.html': (lambda t, d, m, c, j: (t, d, m, c + P3.CSS, j))(*P3.fragen()),
 'impressum.html': ('Impressum | websiten.ch', 'Impressum von websiten.ch.', P3.legal('i'), P.LEGAL_CSS + P3.CSS, ''),
 'datenschutz.html': ('Datenschutz | websiten.ch', 'Datenschutzerklärung von websiten.ch.', P3.legal('d'), P.LEGAL_CSS + P3.CSS, ''),
}
for _f, (_t, _d, _m) in P3.SERVICE_PAGES.items(): out[_f] = (_t, _d, _m, P3.CSS, P3.JS)
for fn, (t, d, m, c, j) in out.items():
    closing = fn not in ('kontakt.html', 'optionen-leistungen.html')
    open('../' + fn, 'w').write(fast.finish(page(t, d, m, c, j, closing=closing, full=True)))
# Artefakt-Startseite ohne eigenes Grundgerüst
import os, shutil
A = '../_art/'
os.makedirs(A + 'assets', exist_ok=True)
fix = lambda s: s.replace('href="index.html#', 'href="./#').replace('href="index.html"', 'href="./"')
t, d, m, c, j = out['index.html']
open(A + 'index.html', 'w').write(fix(page(t, d, m, c, j, closing=True, full=False)))
for fn, (t, d, m, c, j) in out.items():
    if fn == 'index.html': continue
    open(A + fn, 'w').write(fix(page(t, d, m, c, j, closing=fn not in ('kontakt.html', 'optionen-leistungen.html'), full=True)))
for f in os.listdir('../assets'):
    if os.path.isdir('../assets/' + f): continue
    shutil.copy('../assets/' + f, A + 'assets/' + f)
print('ok')
