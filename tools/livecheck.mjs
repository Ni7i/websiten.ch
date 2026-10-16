// Prüft die Live-Seite in einem echten Chrome (läuft nach jedem Deploy in GitHub Actions).
//   node tools/livecheck.mjs https://websiten.ch
// Meldet Fehler als GitHub-Annotation und endet dann mit Code 1.
import { chromium } from 'playwright-core';

const BASE = process.argv[2] || 'https://beispiel13241324.vercel.app';
const PAGES = ['index.html', 'websites.html', 'online-shops.html', 'google-seo.html', 'hosting.html', 'microsoft-365.html', 'ki-chatbots.html', 'preise.html', 'ueber-uns.html', 'kontakt.html'];
const browser = await chromium.launch({ executablePath: process.env.CHROME_PATH || '/usr/bin/google-chrome' });
const problems = [];

for (const name of PAGES) {
  const page = await browser.newPage({ viewport: { width: 1440, height: 900 } });
  page.on('pageerror', e => problems.push(`${name}: JS-Fehler ${e.message.slice(0, 120)}`));
  page.on('console', m => { if (m.type() === 'error') problems.push(`${name}: ${m.text().slice(0, 140)}`); });
  page.on('response', r => { if (r.status() >= 400) problems.push(`${name}: ${r.status()} ${r.url().replace(BASE, '')}`); });
  // Saubere Adressen: /websites statt websites.html, / statt index.html
  const path = name === 'index.html' ? '' : name.replace(/\.html$/, '');
  await page.goto(`${BASE}/${path}`, { waitUntil: 'load' });
  if (/\.html/.test(page.url())) problems.push(`${name}: Adresse zeigt .html (${page.url()})`);
  const bad = await page.evaluate(() => [...document.querySelectorAll('a[href]')].map(a => a.getAttribute('href')).filter(h => /\.html/.test(h)).slice(0, 3));
  if (bad.length) problems.push(`${name}: Links mit .html ${bad.join(' ')}`);
  await page.waitForTimeout(400);
  if (name === 'index.html' || name === 'hosting.html') {
    // Menü öffnen: MacBook-Vorschau muss sofort Bild und Text zeigen, ohne Zeigen auf eine Leistung
    await page.click('#menuBtn');
    await page.waitForTimeout(1500);
    const m = await page.evaluate(() => {
      const p = document.querySelector('.menu-prev');
      const img = p && p.querySelector('.mp-scr img.on'), fr = p && p.querySelector('.mp-fr');
      return { visible: !!p && getComputedStyle(p).opacity === '1', text: !!(p && p.querySelector('.md.on')), shot: !!img && img.naturalWidth > 0, frame: !!fr && fr.naturalWidth > 0 };
    });
    if (!m.visible || !m.text || !m.shot || !m.frame) problems.push(`${name}: Menü-Vorschau unvollständig ${JSON.stringify(m)}`);
  }
  await page.close();
}
await browser.close();

if (problems.length) {
  console.log(problems.join('\n'));
  console.log(`::error::Live-Test im Browser: ${problems.slice(0, 6).join(' | ')}`);
  process.exit(1);
}
console.log(`::notice::Live-Test im Browser ok: ${PAGES.length} Seiten ohne Fehler, Menü-Vorschau sofort sichtbar`);
