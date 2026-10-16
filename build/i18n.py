# Zwei Sprachen aus einer Quelle: Englisch ist Standard (websiten.ch/...), Deutsch liegt unter /de/.
# Gebaut wird weiterhin nur die deutsche Fassung (build.py). Dieses Modul macht daraus beim Zusammenstellen
# von dist (dist.py) beide Sprachen:
#   - Texte und Attribute (alt, aria-label, title, placeholder, meta description) über build/i18n/en.json
#   - Texte im Seiten-JS (nur ganze String-Literale, dazu wenige feste Ersetzungen in JS_EN)
#   - Adressen: englische Slugs (SLUG_EN), deutsche unter /de/, Assets immer absolut (/assets/...)
#   - Umschalter EN DE neben dem Menü-Knopf, hreflang-Links im <head>
# Neue deutsche Texte ohne Übersetzung meldet leftovers(); dann en.json ergänzen.
import hashlib, html, json, os, re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
EN = json.load(open(os.path.join(ROOT, 'build/i18n/en.json'), encoding='utf-8'))
EN_NORM = {re.sub(r'\s+', ' ', k).strip(): v for k, v in EN.items()}
SITE = 'https://websiten.ch'

# deutscher Dateiname (ohne .html) -> englischer Slug
SLUG_EN = {'index': '', 'leistungen': 'services', 'preise': 'pricing', 'ueber-uns': 'about', 'kontakt': 'contact',
           'fragen': 'faq', 'impressum': 'legal-notice', 'datenschutz': 'privacy', 'websites': 'websites',
           'online-shops': 'online-shops', 'google-seo': 'google-seo', 'hosting': 'hosting',
           'microsoft-365': 'microsoft-365', 'ki-chatbots': 'ai-chatbots'}

# feste Ersetzungen im englischen JS (Wochentage, Monate, Mehrzahl)
JS_EN = [
    ("['So','Mo','Di','Mi','Do','Fr','Sa']", "['Sun','Mon','Tue','Wed','Thu','Fri','Sat']"),
    ("['Sonntag','Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag']", "['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']"),
    ("['Jan','Feb','März','Apr','Mai','Juni','Juli','Aug','Sept','Okt','Nov','Dez']", "['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']"),
    ("['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember']", "['January','February','March','April','May','June','July','August','September','October','November','December']"),
    ("? 'n' : ''", "? 's' : ''"),
    (": 'voll'", ": 'full'"),
    ("'Sprache' : 'Sprachen'", "'language' : 'languages'"),
    ("'Seite' : 'Seiten'", "'page' : 'pages'"),
    ("'Nochmals zeigen'", "'Show again'"),
    ("'de-CH'", "'en-GB'"),
    ("Gebucht: ${label}", "Booked: ${label}"),
    ("'Gewählt: <b>'", "'Selected: <b>'"),
    ("${how} Die Bestätigung geht an ${", "${how} The confirmation goes to ${"),
]


def tr(s):
    """Text übersetzen, Leerraum am Rand bleibt. Unbekanntes bleibt deutsch (leftovers() meldet es)."""
    core = re.sub(r'\s+', ' ', s).strip()
    if not core:
        return s
    if core in EN_NORM:
        lead, trail = s[:len(s) - len(s.lstrip())], s[len(s.rstrip()):]
        return lead + EN_NORM[core] + trail
    return s


def _tr_text(m):
    raw = m.group(0)
    t = html.unescape(raw)
    out = tr(t)
    return raw if out == t else html.escape(out, quote=False)


ATTR = re.compile(r'\b(alt|aria-label|title|placeholder|data-copy-label)="([^"]*)"')
META = re.compile(r'(<meta (?:name="description"|property="og:[a-z]+") content=")([^"]*)(")')


def _tr_attr(m):
    v = html.unescape(m.group(2))
    out = tr(v)
    return m.group(0) if out == v else f'{m.group(1)}="{html.escape(out)}"'


def translate_html(s):
    """Texte zwischen Tags und übersetzbare Attribute; <script>/<style> bleiben unberührt."""
    parts = re.split(r'(<script\b.*?</script>|<style\b.*?</style>)', s, flags=re.S)
    for i in range(0, len(parts), 2):
        p = parts[i]
        p = re.sub(r'(?<=>)[^<>]+(?=<)', _tr_text, p)
        p = re.sub(r'<title>([^<]*)</title>', lambda m: '<title>' + html.escape(tr(html.unescape(m.group(1))), quote=False) + '</title>', p)
        p = ATTR.sub(_tr_attr, p)
        p = META.sub(lambda m: m.group(1) + html.escape(tr(html.unescape(m.group(2)))) + m.group(3), p)
        parts[i] = p
    return ''.join(parts)


JS_STR = re.compile(r"""'((?:[^'\\\n]|\\.)*)'|"((?:[^"\\\n]|\\.)*)"|`((?:[^`\\]|\\.)*)`""")


def translate_js(src):
    for a, b in JS_EN:
        src = src.replace(a, b)

    def lit(m):
        q = m.group(0)[0]
        body = next(g for g in m.groups() if g is not None)
        # nur übersetzte Stücke escapen, der Rest ist schon gültiger Quelltext
        esc = lambda t: t if q == '`' else t.replace('\\', '\\\\').replace(q, '\\' + q)
        def t1(t):
            out = tr(t)
            # typografischer Apostroph: sicher in jeder Art von JS-String, auch verschachtelt
            return t if out == t else esc(out.replace("'", '’'))
        if '<' in body and '>' in body:
            new = re.sub(r'(?<=>)[^<>`$]+(?=<)', lambda t: t1(t.group(0)), body)
            new = ATTR.sub(lambda a: f'{a.group(1)}="{t1(a.group(2))}"', new)
        else:
            new = t1(body)
        return m.group(0) if new == body else q + new + q
    return JS_STR.sub(lit, src)


def absolute_assets(s):
    """assets/... immer ab der Wurzel, damit auch /de/... die Dateien findet."""
    return re.sub(r'''(?<=["'(,\s=])assets/''', '/assets/', s)


def href_for(slug_de, lang, anchor=''):
    if lang == 'de':
        return ('/de' if slug_de == 'index' else '/de/' + slug_de) + anchor
    return '/' + SLUG_EN[slug_de] + anchor


def relink(s, lang):
    def fix(m):
        slug, anchor = m.group(1) or 'index', m.group(2) or ''
        if slug not in SLUG_EN:
            return m.group(0)
        return f'href="{href_for(slug, lang, anchor)}"'
    return re.sub(r'href="/([a-z0-9-]*)(#[^"]*)?"', fix, s)


def switcher(slug, lang):
    en, de = href_for(slug, 'en'), href_for(slug, 'de')
    cur = lambda l: ' aria-current="true"' if l == lang else ''
    return (f'<nav class="lang" aria-label="{"Language" if lang == "en" else "Sprache"}">'
            f'<a href="{en}" hreflang="en" lang="en"{cur("en")}>EN</a>'
            f'<a href="{de}" hreflang="de" lang="de"{cur("de")}>DE</a></nav>')


def localize(s, slug, lang):
    s = absolute_assets(s)
    s = relink(s, lang)
    if lang == 'en':
        s = s.replace('<html lang="de-CH">', '<html lang="en">', 1)
    alt = (f'<link rel="alternate" hreflang="en" href="{SITE}{href_for(slug, "en")}">\n'
           f'<link rel="alternate" hreflang="de" href="{SITE}{href_for(slug, "de")}">\n'
           f'<link rel="alternate" hreflang="x-default" href="{SITE}{href_for(slug, "en")}">\n'
           f'<link rel="canonical" href="{SITE}{href_for(slug, lang)}">\n')
    s = s.replace('<link rel="icon"', alt + '<link rel="icon"', 1)
    s = s.replace('<button class="menu-btn"', switcher(slug, lang) + '\n<button class="menu-btn"', 1)
    return s


def js_file(src_text, out_dir, lang):
    """JS für eine Sprache ablegen (Name mit Hash), Pfad zurückgeben."""
    text = absolute_assets(src_text)
    if lang == 'en':
        text = translate_js(text)
    data = text.encode('utf-8')
    rel = f'assets/js/{hashlib.sha256(data).hexdigest()[:12]}.js'
    os.makedirs(os.path.join(out_dir, 'assets/js'), exist_ok=True)
    with open(os.path.join(out_dir, rel), 'wb') as f:
        f.write(data)
    return '/' + rel


def build_page(src_html, slug, lang, out_dir):
    s = src_html
    if lang == 'en':
        s = translate_html(s)

    def js(m):
        path = m.group(1).split('?')[0]
        return f'<script src="{js_file(open(os.path.join(ROOT, path), encoding="utf-8").read(), out_dir, lang)}"'
    s = re.sub(r'<script src="(assets/[^"]+\.js(?:\?v=[0-9a-f]+)?)"', js, s)
    return localize(s, slug, lang)


GERMAN = re.compile(r'[äöüÄÖÜ]|\b(?:und|der|die|das|mit|für|Sie|Ihr|Ihre|wir|ist|nicht|oder|eine|einen|zum|zur|von|auf|bei|pro|Seite|Seiten|Monat|weitere|Termin|wählen|Bitte|Uhr)\b')


def leftovers(en_html):
    """Sichtbare Texte in der englischen Seite, die noch deutsch aussehen."""
    body = re.sub(r'<script\b.*?</script>|<style\b.*?</style>|<svg\b.*?</svg>', '', en_html, flags=re.S)
    found = [html.unescape(t).strip() for t in re.findall(r'(?<=>)[^<>]+(?=<)', body)]
    found += [html.unescape(v) for _, v in ATTR.findall(body)]
    return sorted({t for t in found if t and GERMAN.search(t)})
