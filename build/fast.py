# Schnell und sicher ausliefern: wird von build.py auf jede fertige Seite angewendet.
#
# - Bilder, die als data:-Text im HTML stecken, werden zu eigenen WebP-Dateien (assets/img/x/).
#   Der Browser lädt sie parallel, speichert sie zwischen und das HTML wird winzig.
# - CSS (auch site.css) steht direkt im HTML, damit die Seite ohne weiteren Abruf gezeichnet wird.
# - Seiten-JS kommt in eigene Dateien (assets/js/). Kein Inline-Script mehr, dadurch ist eine
#   strenge Content-Security-Policy möglich.
# - Alle Dateinamen enthalten einen Hash des Inhalts. Sie dürfen deshalb ein Jahr im Cache bleiben.
# - Bilder ausserhalb des ersten Abschnitts laden erst, wenn sie in die Nähe kommen.
import base64, hashlib, io, os, re
from PIL import Image

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
MAX_W = 2400          # breiter braucht kein Bild auf der Seite zu sein
WEBP_Q = 82
_cache = {}


def _h(data):
    return hashlib.sha256(data).hexdigest()[:12]


def _write(rel, data):
    path = os.path.join(ROOT, rel)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    if not os.path.exists(path):
        with open(path, 'wb') as f:
            f.write(data)
    return rel


def asset(kind, text, ext):
    """Text (CSS oder JS) als Datei mit Hash im Namen ablegen, Pfad zurückgeben."""
    data = text.encode('utf-8')
    return _write(f'assets/{kind}/{_h(data)}.{ext}', data)


def version(rel):
    """Bestehende Datei mit ?v=<hash> versehen, damit sie lange im Cache bleiben darf."""
    with open(os.path.join(ROOT, rel), 'rb') as f:
        return rel + '?v=' + _h(f.read())


def _image(m):
    return _convert(m.group(1), base64.b64decode(m.group(2)))


def _convert(mime, raw):
    key = hashlib.sha256(raw).hexdigest()
    if key in _cache:
        return _cache[key]
    if mime == 'svg+xml':
        rel = _write(f'assets/img/x/{_h(raw)}.svg', raw)
    else:
        im = Image.open(io.BytesIO(raw))
        im = im.convert('RGBA' if im.mode in ('RGBA', 'LA', 'P') else 'RGB')
        if im.width > MAX_W:
            im = im.resize((MAX_W, round(im.height * MAX_W / im.width)), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, 'WEBP', quality=WEBP_Q, method=6)
        out, ext = buf.getvalue(), 'webp'
        if len(raw) <= len(out) and im.width == Image.open(io.BytesIO(raw)).width:
            out, ext = raw, {'jpeg': 'jpg', 'jpg': 'jpg', 'png': 'png', 'gif': 'gif'}.get(mime, 'webp')
        rel = _write(f'assets/img/x/{_h(out)}.{ext}', out)
    _cache[key] = rel
    return rel


DATA_IMG = re.compile(r'data:image/(jpeg|jpg|png|webp|gif|svg\+xml);base64,([A-Za-z0-9+/=]+)')
FILE_IMG = re.compile(r'assets/img/([A-Za-z0-9_-]+)\.(jpg|jpeg|png)\b')


def _file_image(m):
    """Fest verlinkte JPG/PNG aus assets/img als WebP ausliefern (Original bleibt liegen)."""
    src = os.path.join(ROOT, m.group(0))
    if not os.path.exists(src):
        return m.group(0)
    with open(src, 'rb') as f:
        return _convert(m.group(2), f.read())


def _lazy(html):
    """loading=lazy für Bilder nach dem ersten Abschnitt, decoding=async für alle."""
    start = html.find('<main')
    first = html.find('</section>', start)
    cut = first if first > 0 else start

    def fix(m, lazy):
        tag = m.group(0)
        if 'decoding=' not in tag:
            tag = tag.replace('<img', '<img decoding="async"', 1)
        if lazy and 'loading=' not in tag:
            tag = tag.replace('<img', '<img loading="lazy"', 1)
        return tag
    head, tail = html[:cut], html[cut:]
    return re.sub(r'<img\b[^>]*>', lambda m: fix(m, False), head) + re.sub(r'<img\b[^>]*>', lambda m: fix(m, True), tail)


def finish(html):
    html = DATA_IMG.sub(_image, html)
    html = FILE_IMG.sub(_file_image, html)
    # CSS bleibt im HTML: kein zusätzlicher Weg zum Server vor dem ersten Bild (zählt am Handy am meisten).
    # Auch site.css wird eingebettet; die Schrift-Pfade darin zeigen dann von der Seite aus auf assets/fonts.
    with open(os.path.join(ROOT, 'assets/site.css'), encoding='utf-8') as f:
        site_css = f.read().replace('url(fonts/', 'url(assets/fonts/')
    html = html.replace('<link rel="stylesheet" href="assets/site.css">', '<style>\n' + site_css + '\n</style>')
    # Kommentare raus (kleiner, und keine Gedankenstriche aus Kommentaren im HTML)
    html = re.sub(r'<style>(.*?)</style>', lambda m: '<style>' + re.sub(r'/\*.*?\*/', '', m.group(1), flags=re.S) + '</style>', html, flags=re.S)
    # Seiten-JS auslagern (nur Inline-Scripts ohne src)
    def js(m):
        return f'<script src="{asset("js", m.group(1), "js")}" defer></script>'
    html = re.sub(r'<script>\n?(.*?)\n?</script>', js, html, flags=re.S)
    html = html.replace('<script src="assets/site.js"></script>', f'<script src="{version("assets/site.js")}" defer></script>')
    return _lazy(html)
