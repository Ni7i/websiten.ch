const reduce = matchMedia("(prefers-reduced-motion: reduce)").matches;

(function(){
  document.querySelectorAll('.o1').forEach(sec => {
    const fl = sec.querySelector('.o1-float'), im = fl.querySelector('img');
    if(!matchMedia('(hover: hover)').matches) return;
    let x = 0, y = 0, tx = 0, ty = 0, raf = 0;
    const mv = () => { x += (tx - x) * .2; y += (ty - y) * .2; fl.style.left = x + 'px'; fl.style.top = y + 'px'; raf = Math.abs(tx - x) + Math.abs(ty - y) > .5 ? requestAnimationFrame(mv) : 0; };
    sec.querySelectorAll('.o1-list a').forEach(a => {
      a.addEventListener('mouseenter', e => { im.src = a.querySelector('.th').src; if(!fl.classList.contains('on')){ x = tx = e.clientX + 200; y = ty = e.clientY; } fl.classList.add('on'); });
      a.addEventListener('mousemove', e => { tx = e.clientX + 200; ty = e.clientY; if(!raf) raf = requestAnimationFrame(mv); });
      a.addEventListener('mouseleave', () => fl.classList.remove('on'));
    });
  });
})();

(function(){
  document.querySelectorAll('.o2').forEach(sec => {
    const row = sec.querySelector('.o2-row'), w = () => row.querySelector('.o2-c').offsetWidth + 24;
    sec.querySelector('.o2-next').addEventListener('click', () => row.scrollBy({left: w(), behavior: 'smooth'}));
    sec.querySelector('.o2-prev').addEventListener('click', () => row.scrollBy({left: -w(), behavior: 'smooth'}));
  });
})();

(function(){
  document.querySelectorAll('.o3').forEach(sec => {
    const items = [...sec.querySelectorAll('.o3-i')];
    items.forEach(it => it.querySelector('.o3-b').addEventListener('click', () => { const open = !it.classList.contains('open'); items.forEach(o => { o.classList.remove('open'); o.querySelector('.o3-b').setAttribute('aria-expanded', 'false'); }); if(open){ it.classList.add('open'); it.querySelector('.o3-b').setAttribute('aria-expanded', 'true'); } }));
  });
})();
