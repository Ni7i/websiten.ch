const { chromium } = require('playwright');
const out = require('path').resolve(__dirname, '../shots') + '/'; require('fs').mkdirSync(out, { recursive: true });
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME_PATH || undefined });
  const pages = process.argv[2].split(',');
  const w = +(process.argv[3] || 1440), h = w < 600 ? 844 : 900;
  for (const f of pages) {
    const p = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1 });
    const errs = [];
    p.on('pageerror', e => errs.push(e.message));
    p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await p.goto('file://' + require('path').resolve(__dirname, '..') + '/' + f, { waitUntil: 'load' });
    await p.evaluate(() => document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager'));
    await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 700) { scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); } scrollTo(0, 0); });
    await p.waitForTimeout(1200);
    const sw = await p.evaluate(() => [document.documentElement.scrollWidth, innerWidth, document.body.scrollHeight]);
    await p.screenshot({ path: out + f.replace('.html', '') + '-' + w + '.png', fullPage: true });
    console.log(f, w, JSON.stringify(sw), errs.join(' | '));
    await p.close();
  }
  await b.close();
})();
