
const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
/* Fragen: Drüberfahren oder Antippen zeigt die Antwort */
(function(){
  const qs = [...document.querySelectorAll('.fq')]; if(!qs.length) return;
  const show = i => qs.forEach((q, j) => { q.setAttribute('aria-expanded', i === j); document.getElementById('fa' + j).classList.toggle('on', i === j); });
  const desk = matchMedia('(hover: hover) and (min-width: 861px)');
  qs.forEach((q, i) => {
    q.addEventListener('mouseenter', () => { if(desk.matches) show(i); });
    q.addEventListener('focus', () => { if(desk.matches) show(i); });
    q.addEventListener('click', () => { if(!desk.matches && q.getAttribute('aria-expanded') === 'true') q.setAttribute('aria-expanded', 'false'); else show(i); });
  });
})();

