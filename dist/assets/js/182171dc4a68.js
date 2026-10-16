/* websiten.ch – gemeinsame Skripte */
(function(){
  const body = document.body;
  /* Seitenname ohne .html und Schrägstrich: /websites, websites.html und / (index) zählen gleich */
  const pg = h => (h || '').split('#')[0].split('/').pop().replace(/\.html$/, '') || 'index';

  /* Logo: Schriftzug beim Scrollen ausblenden.
     Die Farbe richtet sich nach der Fläche direkt unter dem Logo:
     dunkel = Originalfarben, mittel/grün = dunkles Logo, hell = dunkles Logo,
     farbig und dunkel (z.B. Blau, Rot) = weisses Logo. */
  const logo = document.querySelector('.logo');
  const parse = c => { const m = c && c.match(/[\d.]+/g); return m ? m.map(Number) : null; };
  const bgAt = (x, y) => {
    const els = document.elementsFromPoint(x, y);
    for (const el of els) {
      if (el.closest('.logo,.menu-btn,#menu,.stk')) continue;
      let n = el;
      while (n && n.nodeType === 1) {
        const cs = getComputedStyle(n), c = parse(cs.backgroundColor);
        if (c && (c.length < 4 || c[3] > 0.5)) return c;
        if (cs.backgroundImage && cs.backgroundImage !== 'none' && n !== document.body) {
          const g = parse((cs.backgroundImage.match(/rgba?\([^)]*\)/) || [])[0]);
          if (g) return g;
        }
        n = n.parentElement;
      }
    }
    return parse(getComputedStyle(body).backgroundColor) || [21, 21, 21];
  };
  const lin = v => { v /= 255; return v <= .03928 ? v / 12.92 : Math.pow((v + .055) / 1.055, 2.4); };
  const toneOf = ([r, g, b]) => {
    const L = .2126 * lin(r) + .7152 * lin(g) + .0722 * lin(b);
    const mx = Math.max(r, g, b) / 255, mn = Math.min(r, g, b) / 255, l = (mx + mn) / 2;
    const sat = mx === mn ? 0 : (mx - mn) / (1 - Math.abs(2 * l - 1));
    if (L > .5) return 'light';
    if (L > .2) return 'mid';
    return sat > .35 && mx > .25 ? 'color' : 'dark';
  };
  let ticking = false;
  const upd = () => {
    ticking = false;
    body.classList.toggle('scrolled', scrollY > 40);
    let tone = 'dark';
    if (body.classList.contains('menu-open')) tone = 'mid';
    else if (logo) {
      const m = logo.querySelector('.logo-mark').getBoundingClientRect();
      tone = toneOf(bgAt(m.left + m.width / 2, m.top + m.height / 2));
    }
    if (body.dataset.tone !== tone) body.dataset.tone = tone;
    body.classList.toggle('over-sage', tone === 'mid');
  };
  const req = () => { if (!ticking) { ticking = true; requestAnimationFrame(upd); } };
  addEventListener('scroll', req, {passive:true}); addEventListener('resize', req); upd();
  /* Beim Scrollen tritt der Menü-Knopf zurück, nach dem Anhalten ist er wieder voll da */
  let stopT;
  addEventListener('scroll', () => { body.classList.add('is-scrolling'); clearTimeout(stopT); stopT = setTimeout(() => body.classList.remove('is-scrolling'), 260); }, {passive:true});
  window.__logoTone = req;

  /* Menü: Panel von rechts */
  const btn = document.getElementById('menuBtn'), menu = document.getElementById('menu'), dim = document.getElementById('menuDim');
  if(btn && menu){
    const set = open => {
      menu.classList.toggle('open', open); body.classList.toggle('menu-open', open);
      btn.setAttribute('aria-expanded', open); btn.setAttribute('aria-label', open ? 'Menü schliessen' : 'Menü öffnen');
      req();
    };
    btn.addEventListener('click', () => set(!menu.classList.contains('open')));
    if(dim) dim.addEventListener('click', () => set(false));
    menu.addEventListener('click', e => { if(e.target.closest('a')) set(false); });
    addEventListener('keydown', e => { if(e.key === 'Escape' && menu.classList.contains('open')){ set(false); btn.focus(); } });
    /* Leistung rechts: das MacBook in der Mitte zeigt sie, darunter Titel und Kurztext */
    const prev = menu.querySelector('.menu-prev');
    if (prev) {
      const mds = [...prev.querySelectorAll('.md')], shots = [...prev.querySelectorAll('.mp-scr img')], links = [...menu.querySelectorAll('.menu-cols a[data-k]')];
      const page = links.find(a => pg(a.getAttribute('href')) === pg(location.pathname));
      const base = page ? page.dataset.k : 'websites';
      const show = k => { k = k || base; mds.forEach(d => d.classList.toggle('on', d.dataset.k === k)); shots.forEach(i => i.classList.toggle('on', i.dataset.k === k)); links.forEach(a => a.classList.toggle('on', a.dataset.k === k)); };
      links.forEach(a => { a.addEventListener('mouseenter', () => show(a.dataset.k)); a.addEventListener('focus', () => show(a.dataset.k)); });
      const col = menu.querySelector('.menu-cols'); if (col) col.addEventListener('mouseleave', () => show(null));
      /* Bilder erst laden, wenn jemand zum Menü greift (Zeigen, Fokus oder Klick), nur wenn die Vorschau sichtbar ist */
      const load = () => { if (getComputedStyle(prev).display === 'none') return; prev.querySelectorAll('img[data-src]').forEach(i => { i.src = i.dataset.src; i.removeAttribute('data-src'); }); };
      ['pointerenter', 'focus', 'click'].forEach(ev => btn.addEventListener(ev, load));
      show(null);
    }
    const here = pg(location.pathname);
    menu.querySelectorAll('.menu-big a').forEach(a => { if(pg(a.getAttribute('href')) === here) a.setAttribute('aria-current', 'page'); });
  }

  /* Footer: Schriftzug aus Pixeln, steigt aus dem Boden und pixelt leise weiter */
  const ground = document.querySelector('.ground'), cv = ground && ground.querySelector('.giant-px');
  const src = ground && ground.querySelector('.giant-src path');
  if (cv && src && cv.getContext) {
    const ctx = cv.getContext('2d'), still = matchMedia('(prefers-reduced-motion: reduce)').matches;
    const VB = {x: 205, y: 50, w: 840, h: 118};
    const BASE = [35, 35, 35], LIFT = [50, 58, 52], SPARK = [143, 174, 150];
    let cells = [], cs = 8, W = 0, H = 0, dpr = 1, t0 = 0, seen = false, running = false;
    const path = new Path2D(src.getAttribute('d'));
    function build() {
      dpr = Math.min(2, devicePixelRatio || 1);
      W = ground.clientWidth; H = Math.round(W * VB.h / VB.w);
      cv.style.height = H + 'px'; cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr);
      cs = Math.max(4, Math.round(W / 150));
      const cols = Math.ceil(W / cs), rows = Math.ceil(H / cs);
      const off = document.createElement('canvas'); off.width = cols; off.height = rows;
      const o = off.getContext('2d'), k = cols / VB.w;
      o.setTransform(k, 0, 0, rows / VB.h, -VB.x * k, -VB.y * rows / VB.h); o.fill(path);
      const px = o.getImageData(0, 0, cols, rows).data;
      cells = [];
      for (let y = 0; y < rows; y++) for (let x = 0; x < cols; x++) {
        if (px[(y * cols + x) * 4 + 3] > 110) cells.push({x: x * cs, y: y * cs, d: (x / cols) * 900 + (rows - y) * 18 + Math.random() * 500, s: Math.random() * 1e4, f: 0});
      }
    }
    const ease = t => 1 - Math.pow(1 - t, 3);
    function frame(now) {
      if (!t0) t0 = now;
      const t = now - t0, g = cs - 1;
      ctx.setTransform(dpr, 0, 0, dpr, 0, 0); ctx.clearRect(0, 0, W, H);
      let busy = false;
      for (const c of cells) {
        const p = still ? 1 : Math.min(1, Math.max(0, (t - c.d) / 700));
        if (p < 1) busy = true;
        if (p <= 0) continue;
        const rise = (1 - ease(p)) * (H - c.y + cs * 2);
        // leises Pixeln: einzelne Zellen leuchten kurz auf
        if (!still && p === 1 && c.f <= 0 && Math.random() < 0.00018) c.f = 1;
        let mix = 0;
        if (c.f > 0) { mix = Math.sin(c.f * Math.PI) * 0.9; c.f -= 0.008; }
        const wave = still ? 0 : Math.max(0, Math.sin((c.x / W) * 4 - t / 5200 + Math.sin(c.s) * 0.3)) * 0.12;
        const a = Math.min(1, wave);
        const col = mix > 0.05 ? SPARK : LIFT, m = Math.max(a, mix);
        const r = BASE[0] + (col[0] - BASE[0]) * m, gg = BASE[1] + (col[1] - BASE[1]) * m, b = BASE[2] + (col[2] - BASE[2]) * m;
        ctx.fillStyle = `rgb(${r | 0},${gg | 0},${b | 0})`;
        ctx.fillRect(c.x, c.y + rise, g, g);
      }
      if (running) requestAnimationFrame(frame);
      return busy;
    }
    build(); ground.classList.add('live');
    if (still) { frame(performance.now()); }
    else {
      const io = new IntersectionObserver(es => es.forEach(e => {
        if (e.isIntersecting) { if (!seen) { seen = true; t0 = 0; } if (!running) { running = true; requestAnimationFrame(frame); } }
        else running = false;
      }), {threshold: 0.15});
      io.observe(ground);
    }
    let rt; addEventListener('resize', () => { clearTimeout(rt); rt = setTimeout(() => { if (ground.clientWidth !== W) { build(); if (still) frame(performance.now()); } }, 200); });
  }

  /* Footer: Leistungen zum Durchblättern */
  const fx = document.querySelector('.fx');
  if (fx) {
    const tabs = [...fx.querySelectorAll('[role=tab]')];
    const show = t => tabs.forEach(b => { const on = b === t; b.setAttribute('aria-selected', on); document.getElementById(b.getAttribute('aria-controls')).hidden = !on; });
    tabs.forEach((b, i) => {
      b.addEventListener('click', () => show(b));
      if (matchMedia('(hover: hover)').matches) b.addEventListener('mouseenter', () => { if (b.getAttribute('aria-selected') !== 'true') show(b); });
      b.addEventListener('keydown', e => { const d = e.key === 'ArrowDown' || e.key === 'ArrowRight' ? 1 : e.key === 'ArrowUp' || e.key === 'ArrowLeft' ? -1 : 0; if (d) { e.preventDefault(); const n = tabs[(i + d + tabs.length) % tabs.length]; show(n); n.focus(); } });
    });
  }

  /* Aufklappbare Fragen */
  document.querySelectorAll('.qa button').forEach(b => b.addEventListener('click', () => b.setAttribute('aria-expanded', b.getAttribute('aria-expanded') !== 'true')));

  /* Kopieren-Knöpfe */
  document.querySelectorAll('[data-copy]').forEach(b => b.addEventListener('click', () => {
    const txt = b.getAttribute('data-copy'), old = b.textContent;
    const done = () => { b.textContent = 'Kopiert'; setTimeout(() => b.textContent = old, 1600); };
    try { navigator.clipboard.writeText(txt).then(done, () => { b.textContent = txt; }); } catch(e){ b.textContent = txt; }
  }));
  /* Nächste Seite vorladen, sobald der Zeiger auf einem Link ruht (Chrome erledigt das über speculation.json) */
  if (!(HTMLScriptElement.supports && HTMLScriptElement.supports('speculationrules'))) {
    const got = new Set();
    const pre = e => {
      const a = e.target.closest && e.target.closest('a[href^="/"]');
      if (!a || a.origin !== location.origin || a.pathname.startsWith('/assets/') || a.pathname === location.pathname || got.has(a.href)) return;
      got.add(a.href);
      const l = document.createElement('link'); l.rel = 'prefetch'; l.href = a.href; document.head.appendChild(l);
    };
    document.addEventListener('pointerover', pre, { passive: true });
    document.addEventListener('touchstart', pre, { passive: true });
  }
})();
