# Grüntöne in neutrales Grau umrechnen (Helligkeit bleibt), andere Farben bleiben
import re, colorsys
def _g(r, g, b):
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    if s < .04 or not (70 / 360 <= h <= 175 / 360):
        return None
    y = round(.299 * r + .587 * g + .114 * b)
    return y
def _hex(m):
    v = m.group(0); x = v[1:]
    if len(x) == 3: x = ''.join(c * 2 for c in x)
    r, g, b = int(x[0:2], 16), int(x[2:4], 16), int(x[4:6], 16)
    y = _g(r, g, b)
    return v if y is None else '#%02X%02X%02X' % (y, y, y)
def _rgb(m):
    r, g, b = int(m.group(2)), int(m.group(3)), int(m.group(4))
    y = _g(r, g, b)
    return m.group(0) if y is None else f'{m.group(1)}({y},{y},{y}{m.group(5)}'
def grey(s):
    s = re.sub(r'#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3}\b(?![0-9A-Fa-f])', _hex, s)
    s = re.sub(r'(rgba?)\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*(\)|,[^)]*\))', _rgb, s)
    s = re.sub(r'\[(\d+), ?(\d+), ?(\d+)\]', lambda m: (lambda y: m.group(0) if y is None else f'[{y}, {y}, {y}]')(_g(*map(int, m.groups()))), s)
    return s
