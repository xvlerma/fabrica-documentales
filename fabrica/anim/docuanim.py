# -*- coding: utf-8 -*-
"""DocuVox · módulo de animaciones explicativas (Manim Community, MIT).

Cada escena explica un MECANISMO y se sincroniza con la locución: lee un JSON de «cues»
(segundos desde el inicio del plano) y cada paso entra cuando el narrador lo nombra.

    ANIM_CUES=cues/hemiciclo.json manim -qh --fps 30 -r 1920,1080 docuanim.py Hemiciclo

Formato del JSON:  {"dur": 18.4, "t": {"mayoria": 6.2, "segunda": 11.0}, "p": {...parámetros...}}
Si falta un cue se usa el valor por defecto de la escena (útil para previsualizar sin voz).

Estilo: fondo oscuro institucional, tipografía Barlow Condensed grande (legible en móvil),
partidos SIEMPRE ficticios (A, B, C, D, E) en colores neutros. Mapas: Natural Earth (dominio público).
"""
import json, os, math
from manim import *

HERE = os.path.dirname(os.path.abspath(__file__))
config.background_color = '#0A1424'
FONT = 'Barlow Condensed'
# paleta «institucional moderno»
INK = '#F4F7FB'; MUTE = '#8FA3BF'; DIM = '#33445E'; LINE = '#22324A'; ACC = '#3D8BFF'; ACC2 = '#7FB6FF'; GOLD = '#F2C14E'; WARN = '#E76F51'
PANEL = '#13213A'
# partidos ficticios: colores neutros que no corresponden a ningún partido real
PARTY = {'A': '#2EC4B6', 'B': '#E9C46A', 'C': '#9AA8BD', 'D': '#B5838D', 'E': '#5F6B7A'}


def T(s, size=48, color=INK, w='BOLD', **kw):
    return Text(s, font=FONT, font_size=size, color=color, weight=w, **kw)


def num_es(x, dec=0):
    s = f'{x:,.{dec}f}'
    return s.replace(',', 'X').replace('.', ',').replace('X', '.')


class DocuScene(Scene):
    """Escena con reloj de cues. self.go(name) espera hasta el cue; self.end() rellena hasta la duración."""
    DEFAULT = {}
    DUR = 12.0

    def setup(self):
        path = os.environ.get('ANIM_CUES')
        d = json.load(open(path)) if path and os.path.exists(path) else {}
        self.cues = dict(self.DEFAULT); self.cues.update(d.get('t', {}))
        self.dur = d.get('dur', self.DUR); self.p = d.get('p', {})

    def now(self):
        return self.renderer.time

    def go(self, name, lead=0.0):
        t = self.cues.get(name, None) if isinstance(name, str) else name
        if t is None: return
        dt = t - lead - self.now()
        if dt > 1 / 30: self.wait(dt)

    def avail(self, name, cap=1.0, lead=0.0):
        """tiempo de animación disponible hasta el cue siguiente (para no pisar)"""
        t = self.cues.get(name) if isinstance(name, str) else name
        if t is None: return cap
        return max(0.25, min(cap, t - lead - self.now()))

    def end(self):
        dt = self.dur - self.now()
        if dt > 1 / 30: self.wait(dt)

    def header(self, title, sub=None):
        g = VGroup(T(title, 54, INK, 'BOLD'))
        if sub: g.add(T(sub, 30, MUTE, 'SEMIBOLD'))
        g.arrange(DOWN, aligned_edge=LEFT, buff=0.12).to_corner(UL, buff=0.55)
        bar = Rectangle(width=0.09, height=g.height, fill_color=ACC, fill_opacity=1, stroke_width=0).next_to(g, LEFT, buff=0.18)
        return VGroup(bar, g)

    def source(self, s):
        return T(s, 20, MUTE, 'SEMIBOLD').to_corner(DR, buff=0.35)


# ----------------------------------------------------------------- geometría
def hemicycle_positions(n, r0=1.5, r1=3.6, rows=None):
    """Posiciones de n escaños en hemiciclo (orden de izquierda a derecha por ángulo)."""
    rows = rows or max(3, round(math.sqrt(n / 3.2)))
    radii = [r0 + (r1 - r0) * i / max(1, rows - 1) for i in range(rows)]
    tot = sum(radii); counts = [max(1, round(n * r / tot)) for r in radii]
    while sum(counts) > n: counts[counts.index(max(counts))] -= 1
    while sum(counts) < n: counts[counts.index(max(counts))] += 1
    pts = []
    for r, c in zip(radii, counts):
        for k in range(c):
            a = math.pi * (1 - (k + 0.5) / c)
            pts.append((a, r))
    pts.sort(key=lambda x: -x[0])
    return [np.array([r * math.cos(a), r * math.sin(a), 0]) for a, r in pts]


def hemicycle(n, colors=None, r0=1.5, r1=3.6, dot=None, rows=None):
    P = hemicycle_positions(n, r0, r1, rows)
    rad = dot or max(0.035, min(0.16, 1.15 * (r1 - r0) / (max(3, round(math.sqrt(n / 3.2))) * 2.6)))
    g = VGroup(*[Dot(p, radius=rad, color=(colors[i] if colors else DIM)) for i, p in enumerate(P)])
    return g


def seat_colors(alloc, order='ABCDE'):
    out = []
    for k in order:
        out += [PARTY.get(k, MUTE)] * alloc.get(k, 0)
    return out


def dhondt(votes, seats, thr=0.0):
    tot = sum(votes.values()); ok = {k: v for k, v in votes.items() if v >= thr * tot}
    q = sorted([(v / d, k) for k, v in ok.items() for d in range(1, seats + 1)], reverse=True)[:seats]
    a = {k: 0 for k in votes}
    for _, k in q: a[k] += 1
    return a


# ----------------------------------------------------------------- mapas (Natural Earth)
def load_map(name):
    return json.load(open(os.path.join(HERE, 'data', name + '.json')))


def map_group(feats, box, center=None, lat0=None, fill=DIM, stroke=LINE, sw=0.6, keyf=None, shift=None):
    """Devuelve VGroup de polígonos ajustados a box=(ancho, alto) y dict clave→VGroup.
    shift: {clave: (dx, dy)} en grados (para recolocar Canarias, Alaska, etc.)."""
    shift = shift or {}
    allp = []
    for f in feats:
        dx, dy = shift.get((keyf or (lambda f: f['name']))(f), (0, 0))
        for r in f['rings']: allp += [(x + dx, y + dy) for x, y in r]
    xs = [p[0] for p in allp]; ys = [p[1] for p in allp]
    lat0 = lat0 if lat0 is not None else (min(ys) + max(ys)) / 2
    k = math.cos(math.radians(lat0))
    w = (max(xs) - min(xs)) * k; h = max(ys) - min(ys)
    s = min(box[0] / w, box[1] / h); cx = (max(xs) + min(xs)) / 2; cy = (max(ys) + min(ys)) / 2
    groups = {}; allg = VGroup()
    for f in feats:
        key = (keyf or (lambda f: f['name']))(f); dx, dy = shift.get(key, (0, 0))
        g = VGroup()
        for r in f['rings']:
            if len(r) < 3: continue
            pts = [np.array([((x + dx) - cx) * k * s, ((y + dy) - cy) * s, 0]) for x, y in r]
            poly = Polygon(*pts, stroke_color=stroke, stroke_width=sw, fill_color=fill, fill_opacity=1)
            g.add(poly)
        if len(g):
            groups.setdefault(key, VGroup()).add(*g); allg.add(g)
    if center is not None: allg.move_to(center)
    return allg, groups


def world(box=(13.2, 6.4), center=ORIGIN, fill=DIM):
    feats = [f for f in load_map('mundo')]
    for f in feats:  # recorta latitudes extremas para un encuadre de televisión
        f['rings'] = [[[x, max(-56, min(78, y))] for x, y in r] for r in f['rings']]
    return map_group(feats, box, center, lat0=25, fill=fill, keyf=lambda f: f['iso'], sw=0.4)


def lonlat_to_scene(lon, lat, ref_group_bounds):
    raise NotImplementedError


def pin(label, at, color=GOLD, size=30, direction=UP):
    d = Dot(at, radius=0.07, color=color)
    ring = Circle(radius=0.16, color=color, stroke_width=3).move_to(at)
    t = T(label, size, INK, 'BOLD')
    t.next_to(d, direction, buff=0.18)
    bg = BackgroundRectangle(t, color=config.background_color, fill_opacity=0.75, buff=0.08)
    return VGroup(ring, d, bg, t)


def chip(text, color=ACC, size=34, fg=INK, pad=0.22):
    t = T(text, size, fg, 'BOLD')
    r = RoundedRectangle(corner_radius=0.12, width=t.width + 2 * pad, height=t.height + 1.3 * pad, fill_color=color, fill_opacity=1, stroke_width=0)
    t.move_to(r)
    return VGroup(r, t)


def card(title, body=None, w=3.6, h=2.0, color=PANEL, edge=ACC, tsize=40, bsize=28):
    r = RoundedRectangle(corner_radius=0.16, width=w, height=h, fill_color=color, fill_opacity=1, stroke_color=edge, stroke_width=2.5)
    g = VGroup(T(title, tsize, INK, 'BOLD'))
    if body:
        g.add(Paragraph(*body.split('\n'), font=FONT, font_size=bsize, color=MUTE, alignment='center', line_spacing=0.8))
    g.arrange(DOWN, buff=0.15)
    if g.width > w - 0.3: g.scale_to_fit_width(w - 0.3)
    g.move_to(r)
    return VGroup(r, g)


def arrow(a, b, color=ACC2, label=None, size=26):
    ar = Arrow(a, b, buff=0.12, color=color, stroke_width=5, max_tip_length_to_length_ratio=0.18)
    if not label: return ar
    t = T(label, size, ACC2, 'SEMIBOLD').next_to(ar.get_center(), UP if abs(b[0] - a[0]) > abs(b[1] - a[1]) else RIGHT, buff=0.1)
    return VGroup(ar, t)


def bar_h(value, vmax, width, color, h=0.55):
    return Rectangle(width=max(0.02, width * value / vmax), height=h, fill_color=color, fill_opacity=1, stroke_width=0)


def world_proj(g):
    """Función lon/lat → punto de escena para un mapa creado con world()."""
    feats = load_map('mundo'); xs = []; ys = []
    for f in feats:
        for r in f['rings']:
            for x, y in r: xs.append(x); ys.append(max(-56, min(78, y)))
    k = math.cos(math.radians(25)); s = g.width / ((max(xs) - min(xs)) * k)
    cx = (max(xs) + min(xs)) / 2; cy = (max(ys) + min(ys)) / 2; c0 = g.get_center()
    return lambda lon, lat: c0 + np.array([(lon - cx) * k * s, (lat - cy) * s, 0])


def legend(items, cols=2, size=32, colw=6.2):
    """Leyenda: cuadrado de color + nombre + valor, en columnas."""
    rows = []
    for name, val, col in items:
        rows.append(VGroup(Square(0.34, fill_color=col, fill_opacity=1, stroke_width=0), T(name, size, INK, 'BOLD'), T(val, size, col, 'HEAVY')).arrange(RIGHT, buff=0.2))
    g = VGroup(*rows)
    for i, r in enumerate(rows):
        r.move_to(np.array([(i % cols) * colw, -(i // cols) * 0.62, 0]), aligned_edge=LEFT)
    return g



# =================================================================== ESCENAS
class Hemiciclo(DocuScene):
    """350 escaños, mayoría absoluta 176 y segunda votación (más síes que noes)."""
    DEFAULT = dict(mayoria=4.0, mitad=6.5, segunda=9.5, sies=13.0)
    DUR = 18

    def construct(self):
        h = self.header('CONGRESO DE LOS DIPUTADOS', '350 escaños')
        seats = hemicycle(350, r0=1.55, r1=3.75).shift(DOWN * 2.1)
        self.add(h)
        self.play(LaggedStart(*[FadeIn(s, scale=0.4) for s in seats], lag_ratio=0.004, run_time=2.4))
        self.go('mayoria', 0.3)
        maj = VGroup(*seats[:176]); rest = VGroup(*seats[176:])
        line = DashedLine(seats.get_center() + DOWN * 0.1 + UP * 0.0, seats.get_center() + UP * 4.0, color=GOLD, dash_length=0.12, stroke_width=4)
        line.move_to(np.array([seats[175].get_center()[0] * 0 , -2.1 + 1.95, 0]))
        lab = VGroup(T('176', 110, GOLD, 'HEAVY'), T('MAYORÍA ABSOLUTA', 36, INK, 'BOLD')).arrange(DOWN, buff=0.05).move_to(DOWN * 1.55)
        self.play(maj.animate.set_color(ACC), rest.animate.set_color(DIM), run_time=self.avail('mitad', 1.2))
        self.play(FadeIn(lab, shift=UP * 0.2), run_time=0.6)
        self.go('mitad', 0.1)
        self.play(Indicate(lab[0], color=GOLD, scale_factor=1.12), run_time=self.avail('segunda', 0.8, 0.4))
        self.go('segunda', 0.4)
        # segunda votación: basta mayoría simple
        self.play(FadeOut(lab), FadeOut(seats), run_time=0.5)
        v1 = VGroup(T('1.ª VOTACIÓN', 40, MUTE), T('176 síes', 72, ACC, 'HEAVY'), T('mayoría absoluta', 30, MUTE, 'SEMIBOLD')).arrange(DOWN, buff=0.12)
        v2 = VGroup(T('2.ª VOTACIÓN · 48 h después', 40, MUTE), T('más síes que noes', 72, GOLD, 'HEAVY'), T('mayoría simple', 30, MUTE, 'SEMIBOLD')).arrange(DOWN, buff=0.12)
        VGroup(v1, v2).arrange(RIGHT, buff=1.6).move_to(DOWN * 0.2)
        x = Line(v1.get_left() + LEFT * 0.1, v1.get_right() + RIGHT * 0.1, color=WARN, stroke_width=8)
        self.play(FadeIn(v1, shift=UP * 0.2), run_time=0.6)
        self.play(Create(x), v1.animate.set_opacity(0.45), run_time=0.5)
        self.play(FadeIn(v2, shift=UP * 0.2), run_time=0.7)
        self.go('sies', 0.2)
        si = bar_h(150, 180, 5.2, ACC); no = bar_h(140, 180, 5.2, DIM)
        bars = VGroup(VGroup(T('SÍ', 34, INK), si).arrange(RIGHT, buff=0.25), VGroup(T('NO', 34, INK), no).arrange(RIGHT, buff=0.25)).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        bars.next_to(v2, DOWN, buff=0.5)
        self.play(GrowFromEdge(si, LEFT), GrowFromEdge(no, LEFT), FadeIn(bars[0][0]), FadeIn(bars[1][0]), run_time=0.9)
        self.end()


class DhondtVotos(DocuScene):
    """Provincia ficticia: 5 escaños, 5 partidos y la barrera del 3 %."""
    DEFAULT = dict(A=3.2, B=4.6, C=5.8, D=6.9, E=8.0, barrera=10.5, fuera=14.0)
    DUR = 16
    V = dict(A=40000, B=30000, C=18000, D=9000, E=2500)

    def construct(self):
        self.add(self.header('UNA PROVINCIA FICTICIA', '5 escaños · 5 partidos'))
        W = 8.6; vmax = 40000; rows = VGroup()
        for i, (k, v) in enumerate(self.V.items()):
            lab = chip(f'PARTIDO {k}', PARTY[k], 34, '#0A1424').move_to(np.array([-5.6, 1.4 - i * 0.95, 0]))
            b = bar_h(v, vmax, W, PARTY[k], 0.62)
            b.move_to(np.array([lab.get_right()[0] + 0.35 + b.width / 2, lab.get_y(), 0]))
            n = T(num_es(v), 40, INK, 'BOLD').next_to(b, RIGHT, buff=0.3)
            rows.add(VGroup(lab, b, n))
        for k, row in zip(self.V, rows):
            self.go(k, 0.15)
            self.play(FadeIn(row[0], shift=RIGHT * 0.2), GrowFromEdge(row[1], LEFT), FadeIn(row[2]), run_time=self.avail(k, 0.6))
        self.go('barrera', 0.2)
        tot = sum(self.V.values()); thr = 0.03 * tot
        x0 = rows[0][1].get_left()[0]; xt = x0 + W * thr / vmax
        ln = DashedLine(np.array([xt, 1.95, 0]), np.array([xt, -2.75, 0]), color=WARN, stroke_width=5, dash_length=0.12)
        tl = VGroup(T('BARRERA 3 %', 38, WARN, 'HEAVY'), T(f'= {num_es(thr)} votos', 30, WARN, 'SEMIBOLD')).arrange(RIGHT, buff=0.3).next_to(ln, DOWN, buff=0.12, aligned_edge=LEFT).shift(LEFT * 0.1)
        self.play(Create(ln), FadeIn(tl), run_time=0.8)
        self.go('fuera', 0.2)
        e = rows[4]
        out = T('FUERA', 44, WARN, 'HEAVY').next_to(e[2], RIGHT, buff=0.4)
        self.play(e.animate.set_opacity(0.25), FadeIn(out, scale=1.3), run_time=0.6)
        self.end()


class DhondtTabla(DocuScene):
    """La tabla de divisiones: los 5 cocientes más altos se llevan los escaños."""
    DEFAULT = dict(divide=0.6, s1=5.0, s2=6.6, s3=8.2, s4=11.0, s5=12.6, resultado=15.0, cero=18.5)
    DUR = 21
    V = dict(A=40000, B=30000, C=18000, D=9000)

    def construct(self):
        self.add(self.header('LEY D\'HONDT', 'se divide entre 1, 2, 3, 4…'))
        cols = 4; x0 = -4.2; dx = 2.25; y0 = 1.35; dy = 0.95
        heads = VGroup(*[T(f'÷{d}', 40, ACC2, 'HEAVY').move_to(np.array([x0 + (d - 1) * dx + 1.6, y0 + 0.95, 0])) for d in range(1, cols + 1)])
        cells = {}; rowlabs = VGroup()
        for i, (k, v) in enumerate(self.V.items()):
            y = y0 - i * dy
            rowlabs.add(chip(k, PARTY[k], 40, '#0A1424').move_to(np.array([x0 - 0.55, y, 0])))
            for d in range(1, cols + 1):
                cells[(k, d)] = T(num_es(round(v / d)), 40, INK, 'BOLD').move_to(np.array([x0 + (d - 1) * dx + 1.6, y, 0]))
        self.go('divide', 0.2)
        self.play(FadeIn(rowlabs), FadeIn(heads), run_time=0.5)
        self.play(LaggedStart(*[FadeIn(cells[(k, d)], shift=DOWN * 0.1) for d in range(1, cols + 1) for k in self.V], lag_ratio=0.05, run_time=2.4))
        # mini hemiciclo de 5 escaños
        hp = hemicycle_positions(5, 0.9, 0.9, rows=1)
        seats = VGroup(*[Dot(p, radius=0.2, color=DIM) for p in hp]).shift(np.array([5.7, -0.4, 0]))
        st = T('5 ESCAÑOS', 28, MUTE, 'SEMIBOLD').next_to(seats, DOWN, buff=0.15)
        self.play(FadeIn(seats), FadeIn(st), run_time=0.5)
        order = [('A', 1), ('B', 1), ('A', 2), ('C', 1), ('B', 2)]
        for n, (k, d) in enumerate(order):
            self.go(f's{n + 1}', 0.25)
            c = cells[(k, d)]
            box = SurroundingRectangle(c, color=PARTY[k], buff=0.12, stroke_width=5, corner_radius=0.08)
            fly = Dot(c.get_center(), radius=0.2, color=PARTY[k])
            rt = self.avail(f's{n + 2}' if n < 4 else 'resultado', 1.0, 0.3)
            self.play(Create(box), c.animate.set_color(PARTY[k]), run_time=rt * 0.45)
            self.play(fly.animate.move_to(seats[n].get_center()), run_time=rt * 0.55)
            seats[n].set_color(PARTY[k]); self.remove(fly)
        # los demás cocientes se apagan
        rest = VGroup(*[cells[x] for x in cells if x not in order])
        self.play(rest.animate.set_opacity(0.3), run_time=0.4)
        self.go('resultado', 0.2)
        res = VGroup(chip('A · 2', PARTY['A'], 44, '#0A1424'), chip('B · 2', PARTY['B'], 44, '#0A1424'), chip('C · 1', PARTY['C'], 44, '#0A1424')).arrange(RIGHT, buff=0.3)
        res.move_to(np.array([-1.6, -2.75, 0]))
        self.play(LaggedStart(*[FadeIn(r, scale=1.2) for r in res], lag_ratio=0.25, run_time=1.0))
        self.go('cero', 0.3)
        d0 = VGroup(chip('D · 0', PARTY['D'], 44, '#0A1424'), T('≈ 9 % de los votos', 30, WARN, 'BOLD')).arrange(RIGHT, buff=0.25).next_to(res, RIGHT, buff=0.35)
        self.play(FadeIn(d0, scale=1.3), Indicate(rowlabs[3], color=WARN), run_time=0.8)
        self.end()


class SoriaMadrid(DocuScene):
    """Mínimo de dos diputados por provincia: habitantes por escaño en Soria y Madrid."""
    DEFAULT = dict(minimo=1.5, soria=6.0, madrid=12.0, veces=19.0)
    DUR = 22

    def construct(self):
        feats = load_map('espana_prov')
        g, by = map_group(feats, (6.0, 5.4), center=LEFT * 3.7 + DOWN * 0.45, shift={'Las Palmas': (6.5, 7.5), 'Santa Cruz de Tenerife': (6.5, 7.5)}, sw=0.8)
        self.add(self.header('UN ESCAÑO NO VALE LO MISMO EN TODAS PARTES'))
        self.play(FadeIn(g, lag_ratio=0.01), run_time=1.2)
        self.go('minimo', 0.2)
        mins = chip('MÍNIMO 2 DIPUTADOS POR PROVINCIA', PANEL, 32).next_to(g, DOWN, buff=0.1)
        self.play(LaggedStart(*[Indicate(p, color=ACC2, scale_factor=1.0) for p in by.values()], lag_ratio=0.01, run_time=1.3), FadeIn(mins))
        def side(name, pop, seats, per, color, x):
            box = VGroup(T(name.upper(), 58, color, 'HEAVY'), T(f'{num_es(pop)} hab.', 36, INK, 'SEMIBOLD'), T(f'{seats} escaños', 36, INK, 'SEMIBOLD'),
                         T('1 escaño por cada', 30, MUTE, 'SEMIBOLD'), T(num_es(per), 70, color, 'HEAVY'), T('habitantes', 30, MUTE, 'SEMIBOLD'))
            box.arrange(DOWN, aligned_edge=LEFT, buff=0.06).move_to(np.array([x, 0.65, 0]), aligned_edge=LEFT).set_y(0.65)
            return box
        self.go('soria', 0.2)
        self.play(by['Soria'].animate.set_fill(GOLD), run_time=0.5)
        bs = side('Soria', 90234, 2, 45117, GOLD, 0.9)
        self.play(FadeIn(bs, shift=LEFT * 0.3), run_time=0.8)
        self.go('madrid', 0.2)
        self.play(by['Madrid'].animate.set_fill(ACC), run_time=0.5)
        bm = side('Madrid', 7137031, 38, 187817, ACC, 4.2)
        self.play(FadeIn(bm, shift=LEFT * 0.3), run_time=0.8)
        self.go('veces', 0.3)
        big = VGroup(T('× 4', 110, INK, 'HEAVY'), T('un escaño de Madrid representa\na cuatro veces más personas', 32, MUTE, 'SEMIBOLD')).arrange(RIGHT, buff=0.35).move_to(np.array([3.3, -2.55, 0]))
        self.play(FadeIn(big, scale=1.2), run_time=0.8)
        self.add(self.source('Población oficial a 1-1-2025 (INE) · escaños: RD 806/2026').to_corner(UR, buff=0.35))
        self.end()


class Mayoritario(DocuScene):
    """Reino Unido: 650 distritos, gana uno por distrito. 2024: un tercio de los votos, casi dos tercios de los escaños."""
    DEFAULT = dict(distritos=1.8, uno=5.0, resto=9.0, dato=13.5)
    DUR = 20

    def construct(self):
        self.add(self.header('REINO UNIDO', 'sistema mayoritario: un diputado por distrito'))
        import random; random.seed(7)
        grid = VGroup(*[Square(0.62, stroke_color=LINE, stroke_width=2, fill_color=PANEL, fill_opacity=1) for _ in range(40)]).arrange_in_grid(5, 8, buff=0.08).move_to(LEFT * 2.6 + DOWN * 0.4)
        self.go('distritos', 0.2)
        cnt = VGroup(T('650', 110, INK, 'HEAVY'), T('DISTRITOS', 34, MUTE, 'BOLD')).arrange(DOWN, buff=0).move_to(RIGHT * 4.3 + UP * 0.6)
        self.play(LaggedStart(*[FadeIn(s, scale=0.6) for s in grid], lag_ratio=0.02, run_time=1.4), FadeIn(cnt))
        self.go('uno', 0.2)
        z = VGroup()
        for k, v in [('A', 41), ('B', 38), ('C', 21)]:
            row = VGroup(chip(k, PARTY[k], 32, '#0A1424'), bar_h(v, 45, 3.6, PARTY[k], 0.45), T(f'{v} %', 32, INK))
            row[0].move_to(ORIGIN); row[1].move_to(np.array([0.35 + row[1].width / 2, 0, 0])); row[2].next_to(row[1], RIGHT, buff=0.2)
            z.add(row)
        z.arrange(DOWN, aligned_edge=LEFT, buff=0.18).move_to(RIGHT * 3.6 + DOWN * 1.6)
        self.play(FadeOut(cnt), FadeIn(z, shift=UP * 0.2), grid[11].animate.set_fill(GOLD), run_time=0.8)
        win = T('GANA A · 1 escaño', 38, PARTY['A'], 'HEAVY').next_to(z, UP, buff=0.3)
        self.play(FadeIn(win), grid[11].animate.set_fill(PARTY['A']), run_time=0.6)
        self.go('resto', 0.2)
        self.play(z[1].animate.set_opacity(0.25), z[2].animate.set_opacity(0.25), run_time=0.5)
        cols = [PARTY[random.choice('AAABBBC')] for _ in grid]
        self.play(LaggedStart(*[s.animate.set_fill(c) for s, c in zip(grid, cols)], lag_ratio=0.02, run_time=1.4))
        self.go('dato', 0.3)
        self.play(FadeOut(z), FadeOut(win), FadeOut(grid), run_time=0.4)
        lab = T('LABORISTAS · ELECCIONES 2024', 44, INK, 'HEAVY').move_to(UP * 1.6)
        rows = VGroup()
        for name, v, col, txt in [('VOTOS', 33.7, ACC2, '33,7 %'), ('ESCAÑOS', 63.2, ACC, '63 %')]:
            l = T(name, 36, MUTE, 'BOLD'); l.move_to(np.array([-4.3, 0, 0]), aligned_edge=RIGHT)
            b = bar_h(v, 70, 8, col, 0.7); b.move_to(np.array([-4.0 + b.width / 2, 0, 0]))
            n = T(txt, 50, INK, 'HEAVY').next_to(b, RIGHT, buff=0.3)
            rows.add(VGroup(l, b, n))
        rows[0].shift(UP * 0.15); rows[1].shift(DOWN * 0.85)
        self.play(FadeIn(lab), FadeIn(rows[0][0]), GrowFromEdge(rows[0][1], LEFT), FadeIn(rows[0][2]), run_time=0.8)
        self.play(FadeIn(rows[1][0]), GrowFromEdge(rows[1][1], LEFT), FadeIn(rows[1][2]), run_time=0.9)
        self.add(self.source('411 de 650 escaños · House of Commons Library'))
        self.end()


class TresSistemas(DocuScene):
    """Mismos votos, tres sistemas, tres parlamentos distintos (ejemplo ficticio)."""
    DEFAULT = dict(votos=0.5, h1=2.6, h2=4.8, h3=6.8, cambia=4.5)
    DUR = 12
    VOT = dict(A=38, B=30, C=20, D=12)
    RES = [('PROPORCIONAL', 'tipo D\'Hondt', None), ('MAYORITARIO', 'un diputado por distrito', dict(A=61, B=33, C=6, D=0)),
           ('DOS VUELTAS', 'segunda vuelta con pactos', dict(A=46, B=44, C=10, D=0))]

    def construct(self):
        self.add(self.header('MISMOS VOTOS, TRES SISTEMAS', 'ejemplo ficticio · 100 escaños'))
        vb = VGroup(*[VGroup(chip(k, PARTY[k], 28, '#0A1424'), T(f'{v} %', 30, INK)).arrange(RIGHT, buff=0.12) for k, v in self.VOT.items()]).arrange(RIGHT, buff=0.45).move_to(UP * 2.0)
        vt = T('VOTOS', 28, MUTE, 'BOLD').next_to(vb, LEFT, buff=0.35)
        self.go('votos', 0.1)
        self.play(FadeIn(vt), FadeIn(vb, lag_ratio=0.2), run_time=0.7)
        prop = dhondt({k: v * 1000 for k, v in self.VOT.items()}, 100)
        for i, (name, sub, alloc) in enumerate(self.RES):
            alloc = alloc or prop
            hc = hemicycle(100, seat_colors(alloc), r0=0.75, r1=1.85, rows=5).move_to(np.array([-4.6 + i * 4.6, -0.55, 0]))
            lab = VGroup(T(name, 36, INK, 'HEAVY'), T(sub, 24, MUTE, 'SEMIBOLD')).arrange(DOWN, buff=0.04).next_to(hc, DOWN, buff=0.25)
            res = VGroup(*[T(f'{k} {alloc[k]}', 30, PARTY[k], 'HEAVY') for k in 'ABCD']).arrange(RIGHT, buff=0.25).next_to(lab, DOWN, buff=0.15)
            self.go(f'h{i + 1}', 0.2)
            self.play(LaggedStart(*[FadeIn(s, scale=0.4) for s in hc], lag_ratio=0.008, run_time=1.0), FadeIn(lab), FadeIn(res))
        self.end()


US2016_D = set('CA OR WA NV CO NM MN IL VA MD DE NJ NY CT RI MA VT NH ME HI DC'.split())


class ColegioElectoral(DocuScene):
    """EE. UU.: 538 electores, el ganador de cada estado se los lleva (casi siempre). 2016."""
    DEFAULT = dict(electores=3.0, estados=6.0, n270=11.0, votos=15.0, perdio=20.0)
    DUR = 25
    C1 = '#E0A458'; C2 = '#6C9BD2'

    def construct(self):
        feats = [f for f in load_map('eeuu') if f['name'] not in ('Alaska', 'Hawaii')]
        g, by = map_group(feats, (7.2, 4.4), center=LEFT * 3.0 + DOWN * 0.3, keyf=lambda f: f['postal'], sw=0.8)
        self.add(self.header('EL COLEGIO ELECTORAL', 'Estados Unidos · 538 electores'))
        self.play(FadeIn(g, lag_ratio=0.01), run_time=1.0)
        self.go('electores', 0.2)
        big = VGroup(T('538', 120, INK, 'HEAVY'), T('ELECTORES', 34, MUTE, 'BOLD')).arrange(DOWN, buff=0).move_to(RIGHT * 3.9 + UP * 0.6)
        self.play(FadeIn(big, scale=1.2), run_time=0.6)
        self.go('estados', 0.2)
        cands = VGroup(VGroup(Square(0.32, fill_color=self.C2, fill_opacity=1, stroke_width=0), T('Clinton', 34, INK)).arrange(RIGHT, buff=0.15),
                       VGroup(Square(0.32, fill_color=self.C1, fill_opacity=1, stroke_width=0), T('Trump', 34, INK)).arrange(RIGHT, buff=0.15)).arrange(RIGHT, buff=0.5).next_to(g, DOWN, buff=0.3)
        anims = [p.animate.set_fill(self.C2 if k in US2016_D else self.C1) for k, p in by.items()]
        self.play(LaggedStart(*anims, lag_ratio=0.03, run_time=2.4), FadeIn(cands))
        self.go('n270', 0.2)
        self.play(big.animate.scale(0.5).move_to(np.array([6.3, 2.8, 0])), run_time=0.4)
        bw = 4.8; x0 = 1.2
        rows = VGroup()
        for v, col, y in [(227, self.C2, 1.0), (304, self.C1, 0.2)]:
            b = bar_h(v, 538, bw, col, 0.6); b.move_to(np.array([x0 + b.width / 2, y, 0]))
            rows.add(VGroup(b, T(str(v), 40, INK, 'HEAVY').next_to(b, RIGHT, buff=0.2)))
        x270 = x0 + bw * 270 / 538
        l270 = DashedLine(np.array([x270, 1.55, 0]), np.array([x270, -0.3, 0]), color=GOLD, stroke_width=4)
        t270 = T('270 para ganar', 30, GOLD, 'BOLD').move_to(np.array([x270 + 0.12, 1.75, 0]), aligned_edge=LEFT)
        et = T('ELECTORES', 26, MUTE, 'BOLD').move_to(np.array([x0, 1.75, 0]), aligned_edge=LEFT)
        self.play(*[GrowFromEdge(r[0], LEFT) for r in rows], *[FadeIn(r[1]) for r in rows], Create(l270), FadeIn(t270), FadeIn(et), run_time=1.0)
        self.go('votos', 0.3)
        p1 = VGroup(T('VOTO POPULAR', 28, MUTE, 'BOLD'), T('Clinton  +2,9 millones', 44, self.C2, 'HEAVY')).arrange(DOWN, aligned_edge=LEFT, buff=0.05).move_to(np.array([x0, -1.2, 0]), aligned_edge=LEFT)
        self.play(FadeIn(p1, shift=UP * 0.2), run_time=0.7)
        self.go('perdio', 0.2)
        w = chip('GANA TRUMP', self.C1, 42, '#0A1424').next_to(p1, DOWN, buff=0.3, aligned_edge=LEFT)
        self.play(FadeIn(w, scale=1.2), run_time=0.5)
        self.add(self.source('Resultados certificados de 2016'))
        self.end()


class OrganigramaEspana(DocuScene):
    """Quién elige a quién en España; el rey reina pero no gobierna (refrendo)."""
    DEFAULT = dict(rey=2.0, sanciona=5.0, propone=7.5, gobierno=11.0, refrendo=19.0)
    DUR = 24

    def construct(self):
        self.add(self.header('¿QUIÉN ELIGE A QUIÉN?', 'España · monarquía parlamentaria'))
        ciu = card('CIUDADANOS', 'votan', 3.2, 1.25).move_to(np.array([-5.0, -2.3, 0]))
        con = card('CONGRESO', '350 diputados', 3.2, 1.25).move_to(np.array([-5.0, 0.0, 0]))
        pre = card('PRESIDENTE', 'jefe del Gobierno', 3.4, 1.25, edge=ACC).move_to(np.array([0.1, 0.0, 0]))
        rey = card('REY', 'jefe del Estado', 3.0, 1.25, edge=GOLD).move_to(np.array([5.0, 1.9, 0]))
        a1 = Arrow(ciu.get_top(), con.get_bottom(), buff=0.1, color=ACC2, stroke_width=5)
        l1 = T('eligen', 28, ACC2, 'SEMIBOLD').next_to(a1, RIGHT, buff=0.15)
        a2 = Arrow(con.get_right(), pre.get_left(), buff=0.1, color=ACC2, stroke_width=5)
        l2 = T('investidura', 28, ACC2, 'SEMIBOLD').next_to(a2, DOWN, buff=0.12)
        self.play(FadeIn(ciu), FadeIn(con), GrowArrow(a1), FadeIn(l1), FadeIn(pre), GrowArrow(a2), FadeIn(l2), run_time=1.4)
        self.go('rey', 0.2)
        self.play(FadeIn(rey, shift=DOWN * 0.2), run_time=0.6)
        self.go('sanciona', 0.2)
        ley = card('LEYES', 'las sanciona', 2.6, 1.1, edge=GOLD).move_to(np.array([5.0, -0.4, 0]))
        a3 = Arrow(rey.get_bottom(), ley.get_top(), buff=0.1, color=GOLD, stroke_width=5)
        self.play(GrowArrow(a3), FadeIn(ley), run_time=0.6)
        self.go('propone', 0.2)
        a4 = CurvedArrow(rey.get_left() + DOWN * 0.1, pre.get_top() + UP * 0.05, angle=0.5, color=GOLD, stroke_width=5)
        t4 = T('propone candidato', 28, GOLD, 'SEMIBOLD').next_to(a4, UP, buff=0.0).shift(LEFT * 0.2)
        self.play(Create(a4), FadeIn(t4), run_time=0.8)
        self.go('gobierno', 0.2)
        gob = chip('GOBIERNA', ACC, 40).next_to(pre, DOWN, buff=0.35)
        self.play(FadeIn(gob, scale=1.2), Circumscribe(pre, color=ACC), run_time=0.8)
        self.go('refrendo', 0.3)
        ref = VGroup(T('REFRENDO', 52, GOLD, 'HEAVY'), T('sus actos llevan la firma del presidente o de un ministro,\nque es quien responde por ellos', 30, INK, 'SEMIBOLD')).arrange(DOWN, buff=0.08)
        ref.move_to(np.array([2.6, -2.6, 0]))
        lk = DashedLine(pre.get_right(), ley.get_left(), color=GOLD, stroke_width=4)
        self.play(Create(lk), FadeIn(ref, shift=UP * 0.2), run_time=0.9)
        self.add(self.source('Constitución, arts. 56, 62, 64 y 99'))
        self.end()


class Comparativa(DocuScene):
    """Jefe del Estado y jefe del Gobierno en EE. UU., Francia, Alemania y Suiza."""
    DEFAULT = dict(usa=2.0, fra=6.5, ale=13.0, sui=19.0)
    DUR = 27

    def construct(self):
        self.add(self.header('JEFE DEL ESTADO · JEFE DEL GOBIERNO'))
        X = [-3.0, -0.1, 2.8, 5.7]; Y1 = 0.45; Y2 = -1.15; CW = 2.7
        rows = VGroup(T('JEFE DEL\nESTADO', 30, GOLD, 'BOLD').move_to(np.array([-5.65, Y1, 0])), T('JEFE DEL\nGOBIERNO', 30, ACC2, 'BOLD').move_to(np.array([-5.65, Y2, 0])))
        self.add(rows)
        data = [('usa', 'EE. UU.', [('PRESIDENTE', 'elegido por el\nColegio Electoral', 'both')]),
                ('fra', 'FRANCIA', [('PRESIDENTE', 'elegido por los ciudadanos', 'top'), ('PRIMER MINISTRO', None, 'bot')]),
                ('ale', 'ALEMANIA', [('PRESIDENTE', 'papel casi ceremonial', 'top'), ('CANCILLER', 'quien gobierna', 'bot')]),
                ('sui', 'SUIZA', [('CONSEJO\nFEDERAL', '7 miembros', 'both')])]
        for x, (cue, name, items) in zip(X, data):
            self.go(cue, 0.2)
            g = VGroup(T(name, 42, INK, 'HEAVY').move_to(np.array([x, 1.85, 0])))
            for title, body, where in items:
                tl = title.split('\n')
                if where == 'both':
                    c = VGroup(RoundedRectangle(corner_radius=0.16, width=CW, height=2.85, fill_color=PANEL, fill_opacity=1, stroke_color=ACC, stroke_width=2.5).move_to(np.array([x, (Y1 + Y2) / 2, 0])))
                    tx = VGroup(*[T(t, 36, INK, 'BOLD') for t in tl], Paragraph(*body.split('\n'), font=FONT, font_size=24, color=MUTE, alignment='center', line_spacing=0.8)).arrange(DOWN, buff=0.12).move_to(c)
                    c.add(tx)
                else:
                    c = card(title, body, CW, 1.3, edge=GOLD if where == 'top' else ACC, tsize=32, bsize=22).move_to(np.array([x, Y1 if where == 'top' else Y2, 0]))
                g.add(c)
            self.play(FadeIn(g, shift=UP * 0.2, lag_ratio=0.15), run_time=0.9)
        self.end()


REINAN = {'ESP': 'España', 'SWE': 'Suecia', 'GBR': 'Reino Unido'}
REALMS = ['GBR', 'CAN', 'AUS', 'NZL', 'JAM', 'ATG', 'BHS', 'BLZ', 'GRD', 'PNG', 'KNA', 'LCA', 'VCT', 'SLB', 'TUV']


class Monarquias(DocuScene):
    """Reyes que reinan y reyes que gobiernan."""
    DEFAULT = dict(reinan=3.0, ESP=3.8, SWE=4.6, GBR=5.4, gobiernan=7.5, SAU=9.0)
    DUR = 14

    def construct(self):
        g, by = world(center=DOWN * 0.3)
        self.add(self.header('MONARQUÍAS'))
        self.play(FadeIn(g), run_time=0.8)
        self.go('reinan', 0.2)
        k1 = chip('REINAN', GOLD, 36, '#0A1424').to_corner(UR, buff=0.6)
        self.play(FadeIn(k1), run_time=0.4)
        for iso in REINAN:
            self.go(iso, 0.15)
            if iso in by: self.play(by[iso].animate.set_fill(GOLD), run_time=0.35)
        self.go('gobiernan', 0.2)
        k2 = chip('GOBIERNAN', WARN, 36, '#0A1424').next_to(k1, DOWN, buff=0.2).align_to(k1, RIGHT)
        self.play(FadeIn(k2), run_time=0.4)
        self.go('SAU', 0.2)
        self.play(by['SAU'].animate.set_fill(WARN), run_time=0.5)
        c = by['SAU'].get_center()
        self.play(FadeIn(pin('Arabia Saudí', c, WARN, 32, DOWN)), run_time=0.5)
        self.end()


class Reinos(DocuScene):
    """El rey británico es jefe de Estado de 15 países (2026)."""
    DEFAULT = dict(canada=3.5, australia=4.5, nz=5.5, jamaica=6.5, quince=8.5)
    DUR = 13
    LL = {'ATG': (-61.8, 17.1), 'BHS': (-77.4, 25.0), 'BLZ': (-88.5, 17.2), 'GRD': (-61.7, 12.1), 'KNA': (-62.8, 17.3), 'LCA': (-61.0, 13.9),
          'VCT': (-61.2, 13.2), 'TUV': (179.2, -8.5), 'JAM': (-77.3, 18.1), 'SLB': (160.0, -9.6)}

    def construct(self):
        g, by = world(center=DOWN * 0.3)
        P = world_proj(g)
        self.add(self.header('UN REY, QUINCE PAÍSES'))
        self.add(g)
        self.play(by['GBR'].animate.set_fill(GOLD), run_time=0.6)
        for cue, iso in [('canada', 'CAN'), ('australia', 'AUS'), ('nz', 'NZL'), ('jamaica', 'JAM')]:
            self.go(cue, 0.15)
            an = [by[iso].animate.set_fill(GOLD)] if iso in by else []
            if iso == 'JAM': an.append(FadeIn(Dot(P(*self.LL['JAM']), radius=0.07, color=GOLD)))
            self.play(*an, run_time=0.35)
        self.go('quince', 0.3)
        rest = [by[i] for i in REALMS if i in by and i not in ('GBR', 'CAN', 'AUS', 'NZL', 'JAM')]
        dots = VGroup(*[Dot(P(*ll), radius=0.07, color=GOLD) for iso, ll in self.LL.items() if iso != 'JAM'])
        cnt = VGroup(T('15', 130, GOLD, 'HEAVY'), T('PAÍSES INDEPENDIENTES', 32, INK, 'BOLD')).arrange(DOWN, buff=0).to_corner(DL, buff=0.6)
        self.play(*[r.animate.set_fill(GOLD) for r in rest], LaggedStart(*[FadeIn(d, scale=2) for d in dots], lag_ratio=0.1), FadeIn(cnt, scale=1.2), run_time=1.0)
        self.add(self.source('Reinos de la Commonwealth, 2026'))
        self.end()


class Reformas(DocuScene):
    """Constitución de 1978: 169 artículos y solo cuatro reformas."""
    DEFAULT = dict(ref=1.0, art=4.0, cuatro=8.0, ultima=11.0)
    DUR = 15

    def construct(self):
        self.add(self.header('CONSTITUCIÓN DE 1978'))
        Y = -0.9; xs = [-5.6, -2.8, 0.0, 2.8, 5.6]
        ln = Line(np.array([-6.2, Y, 0]), np.array([6.2, Y, 0]), color=DIM, stroke_width=6)
        def mark(i, top, a, b, col, tc):
            return VGroup(Dot(np.array([xs[i], Y, 0]), radius=0.14, color=col), T(top, 40, tc, 'HEAVY').move_to(np.array([xs[i], Y + 0.6, 0])),
                          T(a, 30, INK, 'BOLD').move_to(np.array([xs[i], Y - 0.6, 0])), T(b, 26, MUTE, 'SEMIBOLD').move_to(np.array([xs[i], Y - 1.0, 0])))
        d0 = mark(0, '6-12-1978', 'referéndum', '', GOLD, GOLD)
        self.go('ref', 0.2)
        self.play(Create(ln), FadeIn(d0), run_time=0.9)
        self.go('art', 0.2)
        big = VGroup(T('169', 120, INK, 'HEAVY'), T('ARTÍCULOS', 34, MUTE, 'BOLD')).arrange(DOWN, buff=0).move_to(UP * 1.5 + LEFT * 2.2)
        self.play(FadeIn(big, scale=1.2), run_time=0.6)
        self.go('cuatro', 0.2)
        info = [('1992', 'art. 13.2', 'voto pasivo UE'), ('2011', 'art. 135', 'estabilidad'), ('2024', 'art. 49', 'discapacidad'), ('2026', 'art. 69.3', 'Formentera')]
        ms = [mark(i + 1, y, a, s, ACC, ACC2) for i, (y, a, s) in enumerate(info)]
        c4 = VGroup(T('4', 120, ACC, 'HEAVY'), T('REFORMAS', 34, MUTE, 'BOLD')).arrange(DOWN, buff=0).move_to(UP * 1.5 + RIGHT * 2.2)
        self.play(LaggedStart(*[FadeIn(m, shift=UP * 0.2) for m in ms[:3]], lag_ratio=0.3, run_time=1.4), FadeIn(c4))
        self.go('ultima', 0.2)
        self.play(FadeIn(ms[3], shift=UP * 0.2), Flash(ms[3][0], color=GOLD), run_time=0.8)
        self.add(self.source('BOE · reforma del art. 69.3, 20-5-2026'))
        self.end()


class Tribunales(DocuScene):
    """Tribunal Supremo frente a Tribunal Constitucional."""
    DEFAULT = dict(supremo=3.0, constitucional=8.5, doce=17.0)
    DUR = 26

    def construct(self):
        self.add(self.header('DOS TRIBUNALES QUE SE CONFUNDEN'))
        s = card('TRIBUNAL SUPREMO', 'la cima de los jueces\ndelitos · pleitos · recursos', 5.4, 2.6, edge=ACC2, tsize=46, bsize=30).move_to(LEFT * 3.25 + DOWN * 0.2)
        c = card('TRIBUNAL CONSTITUCIONAL', 'no juzga a personas\n¿choca la ley con la Constitución?\nprotege derechos fundamentales', 5.4, 2.6, edge=GOLD, tsize=46, bsize=30).move_to(RIGHT * 3.25 + DOWN * 0.2)
        self.go('supremo', 0.2); self.play(FadeIn(s, shift=UP * 0.2), run_time=0.7)
        self.go('constitucional', 0.2); self.play(FadeIn(c, shift=UP * 0.2), run_time=0.7)
        self.go('doce', 0.2)
        dots = VGroup(*[Dot(radius=0.13, color=GOLD) for _ in range(12)]).arrange(RIGHT, buff=0.14).next_to(c, DOWN, buff=0.35)
        lbl = T('12 MAGISTRADOS · 4 Congreso · 4 Senado · 2 Gobierno · 2 CGPJ', 26, INK, 'BOLD').next_to(dots, DOWN, buff=0.15)
        if lbl.width > 6.4: lbl.scale_to_fit_width(6.4)
        lbl.set_x(c.get_x())
        cols = [ACC2] * 4 + [ACC] * 4 + [GOLD] * 2 + [WARN] * 2
        for d, col in zip(dots, cols): d.set_color(col)
        self.play(LaggedStart(*[FadeIn(d, scale=0.5) for d in dots], lag_ratio=0.08, run_time=1.2), FadeIn(lbl))
        self.add(self.source('Constitución, art. 159'))
        self.end()


class Mocion(DocuScene):
    """Moción de censura constructiva (España) frente a impeachment (EE. UU.)."""
    DEFAULT = dict(otro=4.0, n176=7.0, ya=10.5, seis=14.5, una=17.0)
    DUR = 21

    def construct(self):
        self.add(self.header('MOCIÓN DE CENSURA', 'España · artículo 113'))
        steps = [('otro', 'CANDIDATO\nALTERNATIVO'), ('n176', '176 VOTOS\nmayoría absoluta'), ('ya', 'NUEVO\nPRESIDENTE')]
        prev = None; xs = [-4.4, 0, 4.4]
        for (cue, txt), x in zip(steps, xs):
            self.go(cue, 0.2)
            t1, *rest = txt.split('\n')
            c = card(t1, rest[0] if rest else None, 3.5, 1.6, edge=ACC).move_to(np.array([x, 0.4, 0]))
            an = [FadeIn(c, shift=UP * 0.2)]
            if prev is not None: an.append(GrowArrow(Arrow(prev.get_right(), c.get_left(), buff=0.1, color=ACC2, stroke_width=6)))
            self.play(*an, run_time=0.6); prev = c
        self.go('seis', 0.2)
        dots = VGroup(*[VGroup(Circle(0.32, color=MUTE, stroke_width=3), T(str(y), 22, MUTE, 'BOLD')) for y in (1980, 1987, 2017, 2018, 2020, 2023)]).arrange(RIGHT, buff=0.5).move_to(DOWN * 2.2)
        for d in dots: d[1].next_to(d[0], DOWN, buff=0.08)
        lab = T('6 MOCIONES', 38, INK, 'HEAVY').next_to(dots, LEFT, buff=0.5)
        self.play(FadeIn(lab), LaggedStart(*[FadeIn(d) for d in dots], lag_ratio=0.15, run_time=1.0))
        self.go('una', 0.2)
        self.play(dots[3][0].animate.set_fill(ACC, 1).set_stroke(ACC), dots[3][1].animate.set_color(ACC), run_time=0.5)
        ok = T('1 APROBADA', 34, ACC, 'HEAVY').next_to(dots, RIGHT, buff=0.5)
        self.play(FadeIn(ok), run_time=0.4)
        self.add(self.source('Congreso de los Diputados'))
        self.end()


class Impeachment(DocuScene):
    """EE. UU.: la Cámara acusa, el Senado juzga, dos tercios para destituir."""
    DEFAULT = dict(camara=2.6, senado=4.0, tercios=6.0, cuatro=9.0, ninguno=11.5)
    DUR = 14

    def construct(self):
        self.add(self.header('IMPEACHMENT', 'Estados Unidos'))
        a = card('CÁMARA DE\nREPRESENTANTES', 'acusa', 3.8, 1.8, edge=ACC2, tsize=34).move_to(np.array([-4.3, 0.5, 0]))
        b = card('SENADO', 'juzga', 3.4, 1.8, edge=ACC2).move_to(np.array([0, 0.5, 0]))
        c = card('2/3', 'de los senadores\npara destituir', 3.4, 1.8, edge=GOLD, tsize=60).move_to(np.array([4.3, 0.5, 0]))
        self.go('camara', 0.2); self.play(FadeIn(a, shift=UP * 0.2), run_time=0.5)
        self.go('senado', 0.2); self.play(GrowArrow(Arrow(a.get_right(), b.get_left(), color=ACC2, stroke_width=6, buff=0.1)), FadeIn(b), run_time=0.5)
        self.go('tercios', 0.2); self.play(GrowArrow(Arrow(b.get_right(), c.get_left(), color=ACC2, stroke_width=6, buff=0.1)), FadeIn(c), run_time=0.5)
        self.go('cuatro', 0.2)
        names = VGroup(*[VGroup(T(n, 28, INK, 'BOLD'), T(y, 24, MUTE, 'SEMIBOLD')).arrange(DOWN, buff=0.04) for n, y in [('A. Johnson', '1868'), ('B. Clinton', '1999'), ('D. Trump', '2020'), ('D. Trump', '2021')]]).arrange(RIGHT, buff=0.9).move_to(DOWN * 1.9)
        lab = T('4 JUICIOS', 38, INK, 'HEAVY').next_to(names, LEFT, buff=0.6)
        self.play(FadeIn(lab), LaggedStart(*[FadeIn(n) for n in names], lag_ratio=0.15, run_time=0.8))
        self.go('ninguno', 0.2)
        z = T('0 DESTITUIDOS', 40, WARN, 'HEAVY').next_to(names, RIGHT, buff=0.5)
        if z.get_right()[0] > 7: VGroup(lab, names, z).arrange(RIGHT, buff=0.5).move_to(DOWN * 1.9).scale_to_fit_width(13)
        self.play(FadeIn(z, scale=1.2), run_time=0.5)
        self.add(self.source('Senado de EE. UU.: juicios de 1868, 1999, 2020 y 2021'))
        self.end()


CCAA_COL = ['#2F6BB3', '#3D8BFF', '#5DA0FF', '#7FB6FF', '#1E4E8C', '#4C7CC2', '#6E9CD8', '#90B8EA', '#2A5C9E', '#3F76C8', '#5C8FD8', '#7DA7E4', '#255394', '#4A82D0', '#689AE0', '#86B0EC', '#3567AE']


class Autonomias(DocuScene):
    """17 comunidades autónomas + Ceuta y Melilla; régimen foral de País Vasco y Navarra."""
    DEFAULT = dict(diecisiete=0.4, servicios=6.0, foral=14.5)
    DUR = 22

    def construct(self):
        feats = load_map('espana_prov')
        g, by = map_group(feats, (7.0, 5.9), center=LEFT * 2.9 + DOWN * 0.4, shift={'Canary Is.': (6.5, 7.5)}, keyf=lambda f: f['region'], sw=0.5)
        self.add(self.header('UN PAÍS DENTRO DE OTRO PAÍS'))
        regs = [r for r in by if r not in ('Ceuta', 'Melilla')]
        self.go('diecisiete', 0.1)
        self.play(FadeIn(g), run_time=0.5)
        self.play(LaggedStart(*[by[r].animate.set_fill(CCAA_COL[i % len(CCAA_COL)]) for i, r in enumerate(regs)], lag_ratio=0.08, run_time=2.2),
                  *[by[c].animate.set_fill(GOLD) for c in ('Ceuta', 'Melilla') if c in by])
        n = VGroup(T('17 + 2', 110, INK, 'HEAVY'), T('comunidades + Ceuta y Melilla', 30, MUTE, 'SEMIBOLD')).arrange(DOWN, buff=0.05).move_to(RIGHT * 4.2 + UP * 1.3)
        self.play(FadeIn(n), run_time=0.5)
        self.go('servicios', 0.2)
        sv = VGroup(*[chip(s, PANEL, 36) for s in ('HOSPITALES', 'COLEGIOS', 'SERVICIOS SOCIALES')]).arrange(DOWN, aligned_edge=LEFT, buff=0.2).move_to(RIGHT * 4.2 + DOWN * 1.0)
        self.play(LaggedStart(*[FadeIn(c, shift=LEFT * 0.2) for c in sv], lag_ratio=0.3, run_time=1.2))
        self.go('foral', 0.2)
        self.play(*[by[r].animate.set_fill(GOLD) for r in ('País Vasco', 'Foral de Navarra') if r in by], *[by[r].animate.set_opacity(0.35) for r in regs if r not in ('País Vasco', 'Foral de Navarra')], FadeOut(sv), run_time=0.7)
        f = VGroup(T('RÉGIMEN FORAL', 44, GOLD, 'HEAVY'), T('País Vasco y Navarra recaudan\ncasi todos sus impuestos y pagan\nal Estado una cantidad pactada', 32, INK, 'SEMIBOLD')).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(RIGHT * 4.2 + DOWN * 1.2)
        self.play(FadeIn(f, shift=UP * 0.2), run_time=0.6)
        self.end()


class Federales(DocuScene):
    """España (17), Alemania (16 länder), EE. UU. (50 estados) y Suiza (26 cantones)."""
    DEFAULT = dict(esp=0.5, ale=5.5, usa=11.0, sui=16.0)
    DUR = 22

    def construct(self):
        self.add(self.header('¿ESPAÑA ES UN PAÍS FEDERAL?'))
        specs = [('esp', 'espana_prov', 'ESPAÑA', '17 comunidades', lambda f: f['region'], {'Canary Is.': (6.5, 7.5)}, 'no federal en la Constitución'),
                 ('ale', 'alemania', 'ALEMANIA', '16 länder', None, {}, 'federal'),
                 ('usa', 'eeuu', 'EE. UU.', '50 estados', None, {}, 'federal'),
                 ('sui', 'suiza', 'SUIZA', '26 cantones', None, {}, 'federal')]
        xs = [-5.0, -1.65, 1.75, 5.1]
        for x, (cue, mp, name, sub, kf, shf, tag) in zip(xs, specs):
            feats = load_map(mp)
            if mp == 'eeuu': feats = [f for f in feats if f['name'] not in ('Alaska', 'Hawaii')]
            g, by = map_group(feats, (2.9, 2.6), center=np.array([x, 0.4, 0]), keyf=kf, shift=shf, sw=0.5)
            for i, v in enumerate(by.values()): v.set_fill(CCAA_COL[i % len(CCAA_COL)])
            lab = VGroup(T(name, 42, INK, 'HEAVY'), T(sub, 32, ACC2, 'BOLD'), T(tag, 26, MUTE if tag != 'federal' else GOLD, 'SEMIBOLD')).arrange(DOWN, buff=0.06)
            lab.move_to(np.array([x, -1.75, 0]), aligned_edge=UP).set_y(-1.7 - lab.height / 2)
            self.go(cue, 0.2)
            self.play(FadeIn(g, lag_ratio=0.02), FadeIn(lab, shift=UP * 0.1), run_time=0.9)
        self.end()


GASTO = [('Protección social', 41, '#3D8BFF'), ('Sanidad', 14, '#2EC4B6'), ('Servicios generales', 13, '#9AA8BD'), ('Asuntos económicos', 11, '#E9C46A'),
         ('Educación', 9, '#7FB6FF'), ('Seguridad y justicia', 4, '#B5838D'), ('Resto', 8, '#5F6B7A')]


class Cien(DocuScene):
    """Tus 100 € de gasto público, por funciones (IGAE, COFOG 2024)."""
    DEFAULT = dict(cien=1.0, ps=8.0, san=14.0, serv=16.0, eco=20.0, edu=25.0, seg=27.0, resto=29.0)
    DUR = 33
    CUES = ['ps', 'san', 'serv', 'eco', 'edu', 'seg', 'resto']
    NOMBRES = ['Protección social (pensiones, paro, ayudas)', 'Sanidad', 'Servicios generales (incl. intereses)', 'Asuntos económicos', 'Educación', 'Seguridad y justicia', 'Cultura, medio ambiente, defensa y vivienda']

    def construct(self):
        self.add(self.header('¿ADÓNDE VAN TUS 100 €?', 'gasto de todas las administraciones públicas · 2024'))
        W = 12.4; y = 1.1; x0 = -W / 2
        frame = Rectangle(width=W, height=1.3, stroke_color=DIM, stroke_width=3).move_to(np.array([0, y, 0]))
        big = T('100 €', 90, INK, 'HEAVY').move_to(frame)
        self.go('cien', 0.2); self.play(Create(frame), FadeIn(big), run_time=0.8)
        acc = x0
        for i, ((_, v, col), cue, name) in enumerate(zip(GASTO, self.CUES, self.NOMBRES)):
            self.go(cue, 0.2)
            seg = Rectangle(width=W * v / 100, height=1.3, fill_color=col, fill_opacity=1, stroke_color=config.background_color, stroke_width=3)
            seg.move_to(np.array([acc + W * v / 200, y, 0]))
            num = T(f'{v}', 44 if v >= 9 else 30, '#0A1424', 'HEAVY').move_to(seg)
            row = VGroup(Square(0.34, fill_color=col, fill_opacity=1, stroke_width=0), T(f'{v} €', 34, col, 'HEAVY'), T(name, 32, INK, 'BOLD')).arrange(RIGHT, buff=0.22)
            row.scale(0.92).move_to(np.array([-6.1, -0.35 - i * 0.5, 0]), aligned_edge=LEFT)
            an = [GrowFromEdge(seg, LEFT), FadeIn(num), FadeIn(row, shift=UP * 0.1)]
            if big in self.mobjects: an.append(FadeOut(big))
            nxt = self.CUES[i + 1] if i + 1 < len(self.CUES) else None
            self.play(*an, run_time=self.avail(nxt, 0.7, 0.25) if nxt else 0.7)
            acc += W * v / 100
        self.add(self.source('IGAE · Clasificación funcional del gasto (COFOG) 2024, provisional').to_corner(UR, buff=0.35))
        self.end()


class Intereses(DocuScene):
    """Intereses de la deuda frente a defensa + medio ambiente (por cada 100 €)."""
    DEFAULT = dict(intereses=1.5, mas=4.5)
    DUR = 8

    def construct(self):
        self.add(self.header('POR CADA 100 € DE GASTO'))
        r1 = VGroup(T('Intereses de la deuda', 38, INK, 'BOLD'), bar_h(5.5, 6.5, 6.5, WARN, 0.8), T('5,5 €', 54, WARN, 'HEAVY'))
        r2 = VGroup(T('Defensa + medio ambiente', 38, INK, 'BOLD'), bar_h(4.1, 6.5, 6.5, MUTE, 0.8), T('4,1 €', 54, MUTE, 'HEAVY'))
        for r in (r1, r2): r.arrange(RIGHT, buff=0.35)
        VGroup(r1, r2).arrange(DOWN, aligned_edge=LEFT, buff=0.5).move_to(DOWN * 0.2)
        r2[1].align_to(r1[1], LEFT); r2[2].next_to(r2[1], RIGHT, buff=0.35)
        r1[0].align_to(r2[0], RIGHT); r1[1].next_to(r1[0], RIGHT, buff=0.35); r1[2].next_to(r1[1], RIGHT, buff=0.35)
        self.go('intereses', 0.2); self.play(FadeIn(r1[0]), GrowFromEdge(r1[1], LEFT), FadeIn(r1[2]), run_time=0.8)
        self.go('mas', 0.2); self.play(FadeIn(r2[0]), GrowFromEdge(r2[1], LEFT), FadeIn(r2[2]), run_time=0.8)
        self.add(self.source('IGAE · COFOG 2024: intereses 39.644 M€ de 725.001 M€'))
        self.end()


class Deuda(DocuScene):
    """Deuda de las AAPP (≈1,75 billones, ≈100 % del PIB) y quién la tiene."""
    DEFAULT = dict(billon=1.0, pib=6.0, quien=8.5, ext=10.0, euro=13.5, resto=18.0)
    DUR = 25

    def construct(self):
        self.add(self.header('LA DEUDA PÚBLICA'))
        vt = ValueTracker(0)
        num = always_redraw(lambda: T(num_es(vt.get_value(), 2) + ' billones €', 90, INK, 'HEAVY').move_to(UP * 1.6))
        self.add(num)
        self.go('billon', 0.2)
        self.play(vt.animate.set_value(1.75), run_time=self.avail('pib', 2.5, 0.3), rate_func=rate_functions.ease_out_cubic)
        self.go('pib', 0.2)
        p = chip('≈ 100 % DEL PIB · todo lo que produce el país en un año', PANEL, 34).next_to(num, DOWN, buff=0.3)
        self.play(FadeIn(p), run_time=0.5)
        self.go('quien', 0.2)
        q = T('¿QUIÉN TIENE LA DEUDA DEL ESTADO?', 40, ACC2, 'HEAVY').move_to(UP * 0.1)
        self.play(FadeOut(p), FadeIn(q), run_time=0.5)
        W = 12; y = -0.9; acc = -6
        segs = [('ext', 49, ACC, 'Inversores extranjeros', '≈ 49 %'), ('euro', 21, GOLD, 'Eurosistema (Banco de España)', '2.º acreedor'), ('resto', 30, MUTE, 'Bancos, aseguradoras, fondos y particulares', 'el resto')]
        for i, (cue, v, col, name, val) in enumerate(segs):
            self.go(cue, 0.2)
            r = Rectangle(width=W * v / 100, height=1.0, fill_color=col, fill_opacity=1, stroke_color=config.background_color, stroke_width=3).move_to(np.array([acc + W * v / 200, y, 0]))
            row = VGroup(Square(0.34, fill_color=col, fill_opacity=1, stroke_width=0), T(val, 34, col, 'HEAVY'), T(name, 32, INK, 'BOLD')).arrange(RIGHT, buff=0.22)
            row.move_to(np.array([-6.0, -1.9 - i * 0.6, 0]), aligned_edge=LEFT)
            self.play(GrowFromEdge(r, LEFT), FadeIn(row, shift=UP * 0.1), run_time=0.7)
            acc += W * v / 100
        self.add(self.source('Banco de España (deuda AAPP, 2026) · Tesoro Público (tenedores, 1T 2026)'))
        self.end()


class PresionFiscal(DocuScene):
    """Impuestos y cotizaciones sobre el PIB: España, media OCDE, Dinamarca (2024) y el Golfo."""
    DEFAULT = dict(esp=3.5, dk=6.5, golfo=10.5)
    DUR = 16

    def construct(self):
        self.add(self.header('IMPUESTOS Y COTIZACIONES', '% de todo lo que produce el país · 2024'))
        data = [('esp', 'ESPAÑA', 36.7, ACC), ('esp', 'MEDIA OCDE', 34.1, MUTE), ('dk', 'DINAMARCA', 45.2, GOLD)]
        rows = VGroup()
        for cue, n, v, col in data:
            rows.add(VGroup(T(n, 38, INK, 'BOLD'), bar_h(v, 50, 8.2, col, 0.75), T(num_es(v, 1) + ' %', 48, col, 'HEAVY')).arrange(RIGHT, buff=0.3))
        rows.arrange(DOWN, aligned_edge=LEFT, buff=0.35).move_to(UP * 0.2 + LEFT * 0.4)
        for r in rows: r[0].align_to(rows[1][0], RIGHT)
        for r in rows: r[1].next_to(rows[1][0], RIGHT, buff=0.3).set_y(r[0].get_y()); r[2].next_to(r[1], RIGHT, buff=0.3)
        shown = set()
        for (cue, *_), r in zip(data, rows):
            self.go(cue, 0.2)
            self.play(FadeIn(r[0]), GrowFromEdge(r[1], LEFT), FadeIn(r[2]), run_time=0.7)
        self.go('golfo', 0.2)
        g = VGroup(T('GOLFO PÉRSICO', 38, INK, 'BOLD'), chip('SIN IMPUESTO SOBRE LA RENTA', WARN, 36, '#0A1424')).arrange(RIGHT, buff=0.35).next_to(rows, DOWN, buff=0.5).align_to(rows, LEFT)
        self.play(FadeIn(g, shift=UP * 0.2), run_time=0.6)
        self.add(self.source('OCDE, Revenue Statistics 2025 (datos provisionales 2024)'))
        self.end()


UE27 = 'AUT BEL BGR HRV CYP CZE DNK EST FIN FRA DEU GRC HUN IRL ITA LVA LTU LUX MLT NLD POL PRT ROU SVK SVN ESP SWE'.split()
EURO21 = 'AUT BEL BGR HRV CYP EST FIN FRA DEU GRC IRL ITA LVA LTU LUX MLT NLD PRT SVK SVN ESP'.split()


def europe(box=(8.6, 6.4), center=ORIGIN):
    feats = load_map('europa')
    clip = lambda r: [[max(-25, min(45, x)), max(33, min(71, y))] for x, y in r]
    sel = []
    for f in feats:
        rs = [r for r in f['rings'] if any(-25 < x < 45 and 33 < y < 71 for x, y in r)]
        if rs: sel.append(dict(iso=f['iso'], name=f['name'], rings=[clip(r) for r in rs]))
    return map_group(sel, box, center, lat0=52, keyf=lambda f: f['iso'], sw=0.4)


class UnionEuropea(DocuScene):
    """UE-27: reglamentos, directivas y primacía del derecho europeo."""
    DEFAULT = dict(ue=0.5, regl=4.5, dir=9.0, prima=14.0)
    DUR = 20

    def construct(self):
        g, by = europe(center=LEFT * 2.6 + DOWN * 0.3)
        self.add(self.header('UNIÓN EUROPEA', '27 países'))
        self.play(FadeIn(g), run_time=0.5)
        self.go('ue', 0.1)
        self.play(LaggedStart(*[by[i].animate.set_fill(ACC) for i in UE27 if i in by], lag_ratio=0.03, run_time=1.6))
        self.play(by['ESP'].animate.set_fill(GOLD), run_time=0.4)
        items = [('regl', 'REGLAMENTOS', 'se aplican directamente\nen toda la Unión'), ('dir', 'DIRECTIVAS', 'fijan un objetivo:\ncada país adapta sus leyes'), ('prima', 'PRIMACÍA', 'en lo que es de la Unión,\nprevalece el derecho europeo')]
        ys = [1.5, -0.2, -1.9]
        for (cue, t, b), y in zip(items, ys):
            self.go(cue, 0.2)
            c = card(t, b, 4.6, 1.5, edge=GOLD if cue == 'prima' else ACC, tsize=38, bsize=26).move_to(np.array([4.2, y, 0]))
            self.play(FadeIn(c, shift=LEFT * 0.3), run_time=0.6)
        self.end()


class Euro(DocuScene):
    """21 países con el euro (Bulgaria, 2026) y el BCE en Fráncfort."""
    DEFAULT = dict(veintiuno=0.6, bulgaria=2.6, bce=6.5)
    DUR = 12

    def construct(self):
        g, by = europe(center=LEFT * 2.6 + DOWN * 0.3)
        self.add(self.header('EL EURO', '21 países · 2026'))
        for i in UE27:
            if i in by: by[i].set_fill(DIM)
        self.add(g)
        self.go('veintiuno', 0.2)
        self.play(LaggedStart(*[by[i].animate.set_fill(GOLD) for i in EURO21 if i in by and i != 'BGR'], lag_ratio=0.03, run_time=1.4))
        n = VGroup(T('21', 130, GOLD, 'HEAVY'), T('PAÍSES CON EL EURO', 32, INK, 'BOLD')).arrange(DOWN, buff=0).move_to(RIGHT * 4.3 + UP * 1.2)
        self.play(FadeIn(n), run_time=0.4)
        self.go('bulgaria', 0.2)
        self.play(by['BGR'].animate.set_fill(GOLD), Flash(by['BGR'].get_center(), color=GOLD, flash_radius=0.4), run_time=0.7)
        self.add(pin('Bulgaria · 1-1-2026', by['BGR'].get_center(), GOLD, 26, DOWN))
        self.go('bce', 0.2)
        fr = by['DEU'].get_center() + np.array([-0.35, -0.15, 0])
        c = card('BANCO CENTRAL EUROPEO', 'Fráncfort · decide los tipos de interés', 4.8, 1.5, edge=ACC, tsize=34, bsize=24).move_to(RIGHT * 4.3 + DOWN * 1.3)
        self.play(FadeIn(Dot(fr, radius=0.09, color=ACC)), FadeIn(c, shift=LEFT * 0.3), run_time=0.7)
        self.end()


class BrexitONU(DocuScene):
    """El Reino Unido sale de la UE (31-1-2020) y los cinco vetos del Consejo de Seguridad."""
    DEFAULT = dict(brexit=3.0, onu=10.0, cinco=14.0, esp=22.0)
    DUR = 25

    def construct(self):
        g, by = europe(box=(6.4, 5.4), center=LEFT * 3.6 + DOWN * 0.3)
        self.add(self.header('SALIR… Y POR ENCIMA DE TODO'))
        for i in UE27:
            if i in by: by[i].set_fill(ACC)
        by['GBR'].set_fill(ACC)
        self.add(g)
        self.go('brexit', 0.2)
        self.play(by['GBR'].animate.set_fill(WARN).shift(LEFT * 0.35 + UP * 0.1), run_time=0.9)
        b = VGroup(T('BREXIT', 54, WARN, 'HEAVY'), T('31 de enero de 2020', 32, INK, 'BOLD')).arrange(DOWN, aligned_edge=LEFT, buff=0.05).move_to(RIGHT * 3.4 + UP * 1.6)
        self.play(FadeIn(b, shift=LEFT * 0.2), run_time=0.5)
        self.go('onu', 0.2)
        self.play(FadeOut(g), FadeOut(b), run_time=0.5)
        t = T('CONSEJO DE SEGURIDAD DE LA ONU', 44, ACC2, 'HEAVY').move_to(UP * 1.9)
        self.play(FadeIn(t), run_time=0.4)
        self.go('cinco', 0.2)
        five = VGroup(*[chip(c, PANEL, 36) for c in ('EE. UU.', 'CHINA', 'RUSIA', 'REINO UNIDO', 'FRANCIA')]).arrange(RIGHT, buff=0.3).move_to(UP * 0.4)
        v = T('DERECHO DE VETO', 48, GOLD, 'HEAVY').next_to(five, DOWN, buff=0.45)
        self.play(LaggedStart(*[FadeIn(c, shift=UP * 0.2) for c in five], lag_ratio=0.12, run_time=1.0), FadeIn(v))
        self.go('esp', 0.2)
        e = VGroup(T('ESPAÑA', 44, INK, 'HEAVY'), chip('SIN VETO', WARN, 36, '#0A1424')).arrange(RIGHT, buff=0.3).next_to(v, DOWN, buff=0.5)
        self.play(FadeIn(e), run_time=0.5)
        self.end()


class Ficha(DocuScene):
    """Ficha de país raro: localizador en el mapa + dato clave. Parámetros en p: iso, nombre, lines, num, numsub."""
    DEFAULT = dict(dato=2.5)
    DUR = 10

    def construct(self):
        p = self.p
        iso = p.get('iso', 'SMR'); lon, lat = p.get('ll', [12.45, 43.94])
        g, by = world(box=(6.6, 3.4), center=LEFT * 3.4 + DOWN * 1.2)
        self.add(self.header(p.get('nombre', 'SAN MARINO').upper(), p.get('sub')))
        self.play(FadeIn(g), run_time=0.5)
        # localizar por lon/lat usando el propio mapa (equirectangular con lat0=25)
        feats = load_map('mundo'); xs = []; ys = []
        for f in feats:
            for r in f['rings']:
                for x, y in r: xs.append(x); ys.append(max(-56, min(78, y)))
        k = math.cos(math.radians(25)); s = g.width / ((max(xs) - min(xs)) * k)
        cx = (max(xs) + min(xs)) / 2; cy = (max(ys) + min(ys)) / 2
        pt = g.get_center() + np.array([(lon - cx) * k * s, (lat - cy) * s, 0])
        if iso in by: by[iso].set_fill(GOLD)
        self.play(FadeIn(pin(p.get('nombre', ''), pt, GOLD, 28)), Flash(pt, color=GOLD, flash_radius=0.35), run_time=0.7)
        if p.get('num'):
            n = VGroup(T(p['num'], 140, GOLD, 'HEAVY'), T(p.get('numsub', ''), 32, INK, 'BOLD')).arrange(DOWN, buff=0).move_to(RIGHT * 3.6 + UP * 0.9)
            self.play(FadeIn(n, scale=1.2), run_time=0.5)
        self.go('dato', 0.2)
        lines = VGroup(*[T(l, 34, INK, 'SEMIBOLD') for l in p.get('lines', [])]).arrange(DOWN, aligned_edge=LEFT, buff=0.12).move_to(RIGHT * 3.6 + DOWN * 1.4)
        if lines.width > 6.6: lines.scale_to_fit_width(6.6)
        self.play(LaggedStart(*[FadeIn(l, shift=UP * 0.1) for l in lines], lag_ratio=0.3, run_time=1.0))
        self.end()


class Repeticion(DocuScene):
    """Dos meses sin investidura → elecciones repetidas (2016 y 2019)."""
    DEFAULT = dict(dos=3.5, r2016=7.5, r2019=9.5)
    DUR = 13

    def construct(self):
        self.add(self.header('SI NADIE CONSIGUE LA INVESTIDURA'))
        c = VGroup(T('2 MESES', 90, GOLD, 'HEAVY'), T('desde la primera votación', 30, MUTE, 'SEMIBOLD')).arrange(DOWN, buff=0).move_to(UP * 1.2)
        a = T('→ NUEVAS ELECCIONES', 54, INK, 'HEAVY').next_to(c, DOWN, buff=0.3)
        self.go('dos', 0.2); self.play(FadeIn(c, scale=1.2), run_time=0.5); self.play(FadeIn(a, shift=RIGHT * 0.3), run_time=0.5)
        r1 = VGroup(T('2015', 46, MUTE, 'HEAVY'), T('→', 46, MUTE), T('2016', 56, ACC, 'HEAVY')).arrange(RIGHT, buff=0.25)
        r2 = VGroup(T('ABRIL 2019', 46, MUTE, 'HEAVY'), T('→', 46, MUTE), T('NOVIEMBRE 2019', 56, ACC, 'HEAVY')).arrange(RIGHT, buff=0.25)
        VGroup(r1, r2).arrange(RIGHT, buff=1.4).move_to(DOWN * 1.9)
        self.go('r2016', 0.2); self.play(FadeIn(r1, shift=UP * 0.2), run_time=0.5)
        self.go('r2019', 0.2); self.play(FadeIn(r2, shift=UP * 0.2), run_time=0.5)
        self.add(self.source('Constitución, art. 99.5'))
        self.end()


class Recap(DocuScene):
    """Cierre: el camino de tu voto."""
    DEFAULT = dict(provincia=4.0, dhondt=5.6, diputados=7.4, rey=9.6, tc=11.4, comunidad=12.8, bruselas=15.0)
    DUR = 19

    def construct(self):
        self.add(self.header('EL CAMINO DE TU VOTO'))
        steps = [('provincia', 'TU PROVINCIA', 'se suma tu voto'), ('dhondt', 'D\'HONDT', 'votos → escaños'), ('diputados', 'DIPUTADOS', 'eligen presidente… o no'),
                 ('rey', 'EL REY', 'sanciona, no decide'), ('tc', 'CONSTITUCIONAL', 'vigila'), ('comunidad', 'TU COMUNIDAD', 'gestiona tu hospital'), ('bruselas', 'BRUSELAS', 'escribe parte de las reglas')]
        pos = [np.array([-4.6, 1.0, 0]), np.array([-1.55, 1.0, 0]), np.array([1.5, 1.0, 0]), np.array([4.6, 1.0, 0]), np.array([-3.1, -1.6, 0]), np.array([0.0, -1.6, 0]), np.array([3.1, -1.6, 0])]
        prev = None
        for (cue, t, b), p in zip(steps, pos):
            self.go(cue, 0.2)
            c = card(t, b, 2.85, 1.55, edge=GOLD if cue in ('rey',) else ACC, tsize=34, bsize=24).move_to(p)
            an = [FadeIn(c, shift=UP * 0.15)]
            if prev is not None and abs(prev.get_y() - c.get_y()) < 0.1: an.append(GrowArrow(Arrow(prev.get_right(), c.get_left(), buff=0.05, color=ACC2, stroke_width=5)))
            self.play(*an, run_time=self.avail(cue, 0.5)); prev = c
        self.end()


class Suma(DocuScene):
    """El más votado no gobierna si otros suman mayoría y se ponen de acuerdo (ejemplo ficticio)."""
    DEFAULT = dict(suma=2.5, acuerdo=4.8, suyo=6.5)
    DUR = 10

    def construct(self):
        self.add(self.header('EJEMPLO FICTICIO', '350 escaños'))
        alloc = dict(A=150, B=120, C=60, D=20)
        hc = hemicycle(350, seat_colors(alloc), r0=1.4, r1=3.4).shift(DOWN * 2.0)
        legend = VGroup(*[VGroup(chip(k, PARTY[k], 30, '#0A1424'), T(str(v), 34, INK)).arrange(RIGHT, buff=0.12) for k, v in alloc.items()]).arrange(RIGHT, buff=0.5).move_to(DOWN * 2.75)
        self.play(LaggedStart(*[FadeIn(s, scale=0.4) for s in hc], lag_ratio=0.003, run_time=1.6), FadeIn(legend))
        top = chip('A, EL MÁS VOTADO', PARTY['A'], 34, '#0A1424').move_to(UP * 1.9 + LEFT * 3.6)
        self.play(FadeIn(top), run_time=0.4)
        self.go('suma', 0.2)
        A_ = VGroup(*hc[:150]); rest = VGroup(*hc[150:330]); D_ = VGroup(*hc[330:])
        self.play(A_.animate.set_opacity(0.25), D_.animate.set_opacity(0.25), run_time=0.6)
        s = VGroup(T('B + C', 60, INK, 'HEAVY'), T('120 + 60 = 180', 44, GOLD, 'HEAVY')).arrange(DOWN, buff=0.05).move_to(UP * 1.75 + RIGHT * 3.3)
        self.play(FadeIn(s, shift=UP * 0.2), run_time=0.6)
        self.go('acuerdo', 0.2)
        m = T('≥ 176', 54, GOLD, 'HEAVY').next_to(s, DOWN, buff=0.2)
        self.play(FadeIn(m), Indicate(rest, color=GOLD, scale_factor=1.0), run_time=0.7)
        self.go('suyo', 0.2)
        g = chip('GOBIERNAN B Y C', ACC, 38).move_to(DOWN * 0.6)
        self.play(FadeIn(g, scale=1.2), run_time=0.5)
        self.end()
