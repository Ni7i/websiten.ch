const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME_PATH || undefined });
  for (const [u, o] of [['https://kf-bauservice.ch/', 'kf'], ['https://kastrati-trockenbau-innenausbau.de/', 'ka']]) {
    const p = await b.newPage({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1.5 });
    try {
      await p.goto(u, { waitUntil: 'networkidle', timeout: 45000 });
      await p.evaluate(() => document.querySelectorAll('img[loading=lazy]').forEach(i => i.loading = 'eager'));
      await p.evaluate(async () => { for (let y = 0; y < document.body.scrollHeight; y += 300) { scrollTo(0, y); await new Promise(r => setTimeout(r, 250)); } });
      await p.waitForTimeout(2500);
      await p.evaluate(async () => { for (let y = document.body.scrollHeight; y > 0; y -= 600) { scrollTo(0, y); await new Promise(r => setTimeout(r, 80)); } scrollTo(0, 0); });
      await p.waitForTimeout(2500);
      await p.screenshot({ path: require('path').resolve(__dirname, '..') + '/mockups/ref-' + o + '-dfull.png', fullPage: true });
      console.log(o, 'ok', await p.evaluate(() => document.body.scrollHeight));
    } catch (e) { console.log(o, 'ERR', e.message.slice(0, 200)); }
    await p.close();
  }
  await b.close();
})();
