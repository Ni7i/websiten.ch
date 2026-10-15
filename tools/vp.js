// Viewport-Aufnahmen an bestimmten Stellen: node vp.js page.html width "sel:frac,sel:frac" 
const { chromium } = require('playwright');
const out = require('path').resolve(__dirname, '../shots') + '/'; require('fs').mkdirSync(out, { recursive: true });
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME_PATH || undefined });
  const [f, w, spec] = process.argv.slice(2);
  const W = +w, Hh = W < 600 ? 844 : 900;
  const p = await b.newPage({ viewport: { width: W, height: Hh }, deviceScaleFactor: 1 });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + require('path').resolve(__dirname, '..') + '/' + f, { waitUntil: 'load' });
  await p.waitForTimeout(600);
  let n = 0;
  for (const s of spec.split(',')) {
    const [sel, fr, wait] = s.split(':');
    const y = await p.evaluate(([sel, fr]) => { const el = document.querySelector(sel); const r = el.getBoundingClientRect(); const top = r.top + scrollY; const span = Math.max(0, r.height - innerHeight); return top + span * +fr; }, [sel, fr]);
    await p.evaluate(y => scrollTo(0, y), y);
    await p.waitForTimeout(+(wait || 900));
    const name = out + f.replace('.html', '') + '-vp' + W + '-' + (n++) + '.png';
    await p.screenshot({ path: name });
    console.log(name);
  }
  console.log('errors:', errs.join(' | ') || 'none');
  await b.close();
})();
