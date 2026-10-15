
(() => {
  const v = document.getElementById('adFilm'), b = document.getElementById('adPlay');
  if (!v || !b) return;
  b.addEventListener('click', () => { v.muted = false; v.controls = true; v.play(); v.parentNode.classList.add('on'); });
  v.addEventListener('ended', () => { v.controls = false; v.currentTime = 0; v.parentNode.classList.remove('on'); });
})();
