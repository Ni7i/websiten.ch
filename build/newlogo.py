# Neues Logo (flach): hinten die helle Fahne, vorne das dunkle Parallelogramm.
# Gemessen am Bild des Kunden, auf den bisherigen viewBox "12 10 174 188" umgerechnet.
import math

def _rounded(pts, r):
    n = len(pts); d = ''
    for i in range(n):
        p0, p1, p2 = pts[i - 1], pts[i], pts[(i + 1) % n]
        def toward(a, b, dist):
            dx, dy = b[0] - a[0], b[1] - a[1]; L = math.hypot(dx, dy); k = min(dist, L / 2) / L
            return (a[0] + dx * k, a[1] + dy * k)
        rr = r[i] if isinstance(r, (list, tuple)) else r
        a = toward(p1, p0, rr); b = toward(p1, p2, rr)
        d += ('M' if i == 0 else 'L') + f'{a[0]:.2f} {a[1]:.2f}Q{p1[0]:.2f} {p1[1]:.2f} {b[0]:.2f} {b[1]:.2f}'
    return d + 'Z'

# Bildkoordinaten
FRONT = [(92, 99.1), (217, 156.4), (217, 266.2), (92, 200.5)]
BACK = [(143, 97.9), (284, 30.7), (284, 185), (236, 209), (236, 142.4)]
X0, Y0, X1, Y1 = 92, 30.7, 284, 266.2
s = min(174 / (X1 - X0), 188 / (Y1 - Y0))
ox = 12 + (174 - (X1 - X0) * s) / 2; oy = 10 + (188 - (Y1 - Y0) * s) / 2
T = lambda p: (ox + (p[0] - X0) * s, oy + (p[1] - Y0) * s)
MARK_FRONT = _rounded([T(p) for p in FRONT], 11 * s)
MARK_BACK = _rounded([T(p) for p in BACK], [7 * s, 9 * s, 9 * s, 9 * s, 11 * s])
