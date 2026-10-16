# Alle sichtbaren deutschen Texte aus den fertigen Seiten (und ihrem JS) sammeln, für die englische Fassung.
import glob, html, json, os, re
from html.parser import HTMLParser

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
SKIP = {'version-2.html', 'optionen-leistungen.html', 'artifact-index.html'}
ATTRS = {'alt', 'aria-label', 'title', 'placeholder', 'data-copy-label'}
WORD = re.compile(r'[A-Za-zÄÖÜäöüß]{2,}')


def wanted(t):
    t = t.strip()
    if not WORD.search(t):
        return False
    if re.fullmatch(r'[\w.\-]+@[\w.\-]+|https?://\S+|websiten\.ch|CHF[\s\d’\'.]*|[\d\s’.,:/%+-]+', t):
        return False
    return True


class P(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.stack, self.texts, self.attrs, self.raw = [], [], [], None

    def handle_starttag(self, tag, at):
        if tag in ('script', 'style'):
            self.raw = tag
        for k, v in at:
            if v and (k in ATTRS or (tag == 'meta' and k == 'content' and dict(at).get('name') in ('description',) or dict(at).get('property', '').startswith('og:'))) and wanted(html.unescape(v)):
                if k == 'content' and tag != 'meta':
                    continue
                self.attrs.append(html.unescape(v))

    def handle_endtag(self, tag):
        if tag == self.raw:
            self.raw = None

    def handle_data(self, d):
        if self.raw:
            return
        t = html.unescape(d)
        if wanted(t):
            self.texts.append(re.sub(r'\s+', ' ', t).strip())

    def handle_entityref(self, n):
        pass


JS_STR = re.compile(r"""'((?:[^'\\\n]|\\.)*)'|"((?:[^"\\\n]|\\.)*)"|`((?:[^`\\]|\\.)*)`""")
GERMAN = re.compile(r'[äöüÄÖÜß]|\b(?:und|der|die|das|mit|für|Seite|Seiten|Sie|Ihr|Ihre|wir|ist|nicht|oder|ein|eine|im|zu|von|auf|bei|pro|Monat|Jahr|einmalig|weitere|Website|Websites|Termin|Kopiert|Menü|Bild|Video|Film|abspielen|pausieren|schliessen|öffnen|Vorher|Nachher|Suche|Bewertung|geöffnet|Uhr|Stunden|Minuten|Tag|Tage)\b')


def js_strings(src):
    out = []
    for m in JS_STR.finditer(src):
        s = next(g for g in m.groups() if g is not None)
        if '<' in s and '>' in s:
            # HTML im JS: Textteile einzeln
            p = P(); p.feed(s); out += p.texts + p.attrs
        elif wanted(s) and GERMAN.search(s) and not re.search(r'[{};=]|^\.|^#|\.(js|css|jpg|webp|png|mp4)\b|^[a-z-]+$', s):
            out.append(s)
    return out


if __name__ == '__main__':
    segs, where = {}, {}
    pages = [p for p in sorted(glob.glob(os.path.join(ROOT, '*.html'))) if os.path.basename(p) not in SKIP]
    for f in pages:
        s = open(f, encoding='utf-8').read()
        p = P(); p.feed(s)
        items = p.texts + p.attrs
        for src in re.findall(r'<script src="(assets/js/[0-9a-f]+\.js)"', s) + ['assets/site.js']:
            items += js_strings(open(os.path.join(ROOT, src), encoding='utf-8').read())
        for t in items:
            segs.setdefault(t, os.path.basename(f))
    json.dump(segs, open(os.path.join(ROOT, 'build/i18n/_segments.json'), 'w'), ensure_ascii=False, indent=0)
    print(len(segs), 'Segmente,', sum(len(k) for k in segs), 'Zeichen')
