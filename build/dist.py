# Deploy-Ordner ../dist zusammenstellen: alle Seiten und genau die Dateien, auf die sie verweisen.
# Ausführen nach build.py:  cd build && python3 dist.py
# Danach im Ordner dist:  vercel deploy --prod --yes   (oder Cloudflare Pages / Netlify: Ordner dist hochladen)
import glob, os, re, shutil
import i18n

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
OUT = os.path.join(ROOT, 'dist')
SKIP = {'version-2.html', 'optionen-leistungen.html', 'artifact-index.html'}
# Bilder, die das JavaScript erst zur Laufzeit zusammensetzt ('assets/img/' + name)
DYNAMIC = ['assets/img/mac-frame.webp', 'assets/img/scr-*', 'assets/img/dev-*', 'assets/img/live-*', 'assets/img/shop-*']
REF = re.compile(r'''(assets/[A-Za-z0-9_./-]+\.[a-z0-9]+)''')
CSS_URL = re.compile(r'url\(([^)"\']+)\)')

pages = [p for p in sorted(glob.glob(os.path.join(ROOT, '*.html'))) if os.path.basename(p) not in SKIP]
need, todo = set(), []
for p in pages:
    todo.append(p)
while todo:
    f = todo.pop()
    if not f.endswith(('.html', '.css', '.js')):
        continue
    text = open(f, encoding='utf-8', errors='ignore').read()
    refs = set(REF.findall(text))
    if f.endswith('.css'):  # relative url() in CSS, z.B. fonts/... in assets/site.css
        base = os.path.relpath(os.path.dirname(f), ROOT)
        refs |= {os.path.normpath(os.path.join(base, u)) for u in CSS_URL.findall(text) if not u.startswith(('data:', 'http', '#'))}
    for r in refs:
        a = os.path.join(ROOT, r)
        if os.path.isfile(a) and r not in need:
            need.add(r)
            todo.append(a)
for pat in DYNAMIC:
    need |= {os.path.relpath(x, ROOT) for x in glob.glob(os.path.join(ROOT, pat))}

shutil.rmtree(OUT, ignore_errors=True)
os.makedirs(OUT)
# Englisch (Standard) an der Wurzel, Deutsch unter /de/
missing = {}
for p in pages:
    slug = os.path.basename(p)[:-5]
    src = open(p, encoding='utf-8').read()
    for lang in ('en', 'de'):
        out = i18n.build_page(src, slug, lang, OUT)
        name = (i18n.SLUG_EN[slug] or 'index') if lang == 'en' else slug
        dst = os.path.join(OUT, '' if lang == 'en' else 'de', name + '.html')
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        open(dst, 'w', encoding='utf-8').write(out)
        if lang == 'en':
            for t in i18n.leftovers(out):
                missing.setdefault(t, slug)
for r in sorted(need):
    os.makedirs(os.path.join(OUT, os.path.dirname(r)), exist_ok=True)
    shutil.copy2(os.path.join(ROOT, r), os.path.join(OUT, r))
for f in ('vercel.json', '_headers', 'favicon.ico', 'speculation.json'):
    shutil.copy2(os.path.join(ROOT, f), OUT)

size = sum(os.path.getsize(os.path.join(d, f)) for d, _, fs in os.walk(OUT) for f in fs)
print(f'dist: {len(pages)} Seiten, {len(need)} Dateien, {size / 1e6:.1f} MB')
# Prüfung aus CLAUDE.md: keine Gedankenstriche im HTML
bad = [os.path.relpath(p, OUT) for p in glob.glob(os.path.join(OUT, '**/*.html'), recursive=True) if re.search('[–—]', open(p, encoding='utf-8').read())]
if bad:
    print('ACHTUNG Gedankenstriche in:', ', '.join(bad))
if missing:
    print(f'Englisch: {len(missing)} Texte noch deutsch (build/i18n/en.json ergänzen):')
    for t, f in sorted(missing.items(), key=lambda x: x[1]):
        print(f'  [{f}] {t[:110]}')
