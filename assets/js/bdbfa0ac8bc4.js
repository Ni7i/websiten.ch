
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
    const tick = () => { raf = 0; scrubs.forEach(s => { const r = s.getBoundingClientRect(), span = r.height - innerHeight; const p = Math.min(1, Math.max(0, -r.top / (span || 1))); if (s._p !== p) { s._p = p; H[s.dataset.scrub](s, p); } }); };
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
