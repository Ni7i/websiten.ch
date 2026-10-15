// Rendert Geräte-Szenen als PNG mit transparentem Hintergrund
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME_PATH || undefined, args: ['--use-gl=swiftshader', '--enable-unsafe-swiftshader'] });
  const dir = __dirname;
  const jobs = JSON.parse(process.argv[2]);
  for (const j of jobs) {
    const p = await b.newPage({ viewport: { width: j.w || 1200, height: j.h || 760 }, deviceScaleFactor: 2 });
    const url = 'file://' + path.join(dir, j.page) + '?' + new URLSearchParams(j.q).toString();
    await p.goto(url);
    await p.waitForFunction(() => [...document.images].every(i => i.complete));
    await p.waitForTimeout(400);
    await p.screenshot({ path: path.join(dir, j.out), omitBackground: true });
    if (j.rect) {
      const r = await p.evaluate(sel => { const e = document.querySelector(sel).getBoundingClientRect(); return { x: e.left, y: e.top, w: e.width, h: e.height, W: innerWidth, H: innerHeight }; }, j.rect);
      console.log(j.out, JSON.stringify(r));
    } else console.log(j.out);
    await p.close();
  }
  await b.close();
})();
