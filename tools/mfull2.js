const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME_PATH || undefined });
  for (const [u, o] of [['https://kastrati-trockenbau-innenausbau.de/', 'ka'], ['https://kf-bauservice.ch/', 'kf']]) {
    const p = await b.newPage({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, isMobile: true, hasTouch: true });
    await p.goto(u, { waitUntil: 'networkidle', timeout: 45000 });
    await p.evaluate(() => document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager'));
    await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 250) { scrollTo(0, y); await new Promise(r => setTimeout(r, 220)); } });
    await p.waitForTimeout(2500);
    await p.evaluate(async () => { for (let y = document.body.scrollHeight; y > 0; y -= 500) { scrollTo(0, y); await new Promise(r => setTimeout(r, 60)); } scrollTo(0, 0); });
    await p.waitForTimeout(2500);
    await p.screenshot({ path: require('path').resolve(__dirname, '..') + '/mockups/ref-' + o + '-mfull2.png', fullPage: true });
    console.log(o, await p.evaluate(() => document.body.scrollHeight));
    await p.close();
  }
  await b.close();
})();
