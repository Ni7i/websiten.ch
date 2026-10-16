
(function(){
  const $ = id => document.getElementById(id), fmt = n => String(n).replace(/\B(?=(\d{3})+(?!\d))/g, '’');
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const PROD = [['up to 30', 0], ['bis 150', 490], ['bis 500', 990], ['over 500', 1890]];
  const S = {type:'web', pages:4, prod:0, lang:1, texts:0, x:{}};
  const LIM = {cfPages:[1, 30], cfProd:[0, 3], cfLang:[1, 4]};
  let shown = 590, anim = 0, last = '';
  const count = to => { cancelAnimationFrame(anim); if (reduce) { $('cfTotal').textContent = fmt(to); shown = to; return; } const from = shown, t0 = performance.now(); const step = t => { const k = Math.min(1, (t - t0) / 420), e = 1 - Math.pow(1 - k, 3); shown = Math.round(from + (to - from) * e); $('cfTotal').textContent = fmt(shown); if (k < 1) anim = requestAnimationFrame(step); }; anim = requestAnimationFrame(step); };
  function calc(){
    const shop = S.type === 'shop', L = [];
    $('cfPages').textContent = S.pages; $('cfPagesW').textContent = S.pages === 1 ? 'page' : 'pages';
    $('cfProd').textContent = PROD[S.prod][0]; $('cfProdW').hidden = !shop;
    $('cfLang').textContent = S.lang; $('cfLangW').textContent = S.lang === 1 ? 'language' : 'languages';
    L.push([shop ? 'Shop with 4 pages and 30 products' : 'Website with 4 pages', shop ? 1890 : 590]);
    if (S.pages > 4) L.push([(S.pages - 4) + '  more page' + (S.pages > 5 ? 's' : ''), (S.pages - 4) * 150]);
    if (shop && PROD[S.prod][1]) L.push(['Produkte ' + PROD[S.prod][0], PROD[S.prod][1]]);
    if (S.lang > 1) L.push([(S.lang - 1) + '  more language' + (S.lang > 2 ? 's' : ''), (S.lang - 1) * 50]);
    if (S.texts) L.push(['Copy for  ' + S.pages + '  pages', S.pages * 45]);
    document.querySelectorAll('.cf-x').forEach(b => { if (S.x[b.dataset.x]) L.push([b.textContent, +b.dataset.p]); });
    const total = L.reduce((a, l) => a + l[1], 0);
    count(total);
    $('cfMonth').textContent = shop ? 'Plus the Shopify subscription, which you pay directly to Shopify.' : 'Plus hosting and domain for CHF 25 a month.';
    $('cfLines').innerHTML = L.map(l => `<li><span>${l[0]}</span><b>CHF ${fmt(l[1])}</b></li>`).join('');
    last = 'Preisrechner: ' + L.map(l => l[0] + ' (CHF ' + fmt(l[1]) + ')').join(', ') + '. Total CHF ' + fmt(total) + '.';
  }
  document.querySelectorAll('[data-t]').forEach(b => b.onclick = () => { document.querySelectorAll('[data-t]').forEach(o => o.setAttribute('aria-pressed', o === b)); S.type = b.dataset.t; calc(); });
  document.querySelectorAll('[data-tx]').forEach(b => b.onclick = () => { document.querySelectorAll('[data-tx]').forEach(o => o.setAttribute('aria-pressed', o === b)); S.texts = +b.dataset.tx; calc(); });
  document.querySelectorAll('.cf-x').forEach(b => b.onclick = () => { S.x[b.dataset.x] = !S.x[b.dataset.x]; b.setAttribute('aria-pressed', !!S.x[b.dataset.x]); calc(); });
  const key = {cfPages:'pages', cfProd:'prod', cfLang:'lang'};
  document.querySelectorAll('[data-step]').forEach(b => b.onclick = () => { const id = b.dataset.step, k = key[id], [lo, hi] = LIM[id]; S[k] = Math.min(hi, Math.max(lo, S[k] + +b.dataset.d)); calc(); });
  $('cfGo').addEventListener('click', () => { try { localStorage.setItem('websiten-anfrage', last); } catch(e){} });
  calc();
})();
