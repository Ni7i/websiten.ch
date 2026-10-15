// Hintergrundfilm der Startseite aus video/bg.html rendern.
//   node tools/bgrender.js            -> assets/websiten-hero.mp4 (Computer, 2560x1440) und assets/websiten-hero-m.mp4 (Handy, Ausschnitt ums Logo)
// Optionen: --fps 30 --workers 4 --crf 20 --crf-m 23
// Gerendert wird in 2688x1512 (Faktor 1.4), dann für beide Fassungen sauber verkleinert. Optional CHROME_PATH setzen.
const { chromium } = require('playwright');
const { spawn } = require('child_process');
const path = require('path');

const arg = (n, d) => { const i = process.argv.indexOf('--' + n); return i < 0 ? d : process.argv[i + 1]; };
const FPS = +arg('fps', 30), WORKERS = +arg('workers', 4), CRF = arg('crf', '20'), CRF_M = arg('crf-m', '23'), SCALE = 1.4;
const ROOT = path.resolve(__dirname, '..');
const OUT = path.join(ROOT, 'assets/websiten-hero.mp4'), OUT_M = path.join(ROOT, 'assets/websiten-hero-m.mp4');
// Handy: Ausschnitt rund ums Logo (x 865 bis 1905 von 1920, volle Höhe), in gerenderten Pixeln
const CROP = `crop=${Math.round(1040 * SCALE)}:${Math.round(1080 * SCALE)}:${Math.round(865 * SCALE)}:0`;

(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROME_PATH || undefined });
  const open = async () => {
    const p = await b.newPage({ viewport: { width: 1920, height: 1080 }, deviceScaleFactor: SCALE });
    await p.goto('file://' + path.join(ROOT, 'video/bg.html'));
    await p.evaluate(() => window.ready);
    return p;
  };
  const pages = await Promise.all(Array.from({ length: WORKERS }, open));
  const DUR = await pages[0].evaluate(() => window.DUR), N = Math.round(FPS * DUR);
  const enc = (crf) => ['-c:v', 'libx264', '-preset', 'medium', '-crf', crf, '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-movflags', '+faststart', '-an'];
  const ff = spawn('ffmpeg', ['-v', 'error', '-y', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'png', '-i', '-',
    '-filter_complex', `[0:v]split=2[a][b];[a]scale=2560:1440:flags=lanczos[d];[b]${CROP},scale=1248:1296:flags=lanczos[m]`,
    '-map', '[d]', ...enc(CRF), OUT, '-map', '[m]', ...enc(CRF_M), OUT_M], { stdio: ['pipe', 'inherit', 'inherit'] });

  // mehrere Seiten rendern parallel, ffmpeg bekommt die Bilder streng der Reihe nach
  const done = new Map(); let next = 0, claimed = 0; const t0 = Date.now();
  let chain = Promise.resolve();
  const flush = async () => {
    while (done.has(next)) {
      const buf = done.get(next); done.delete(next); next++;
      if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
      if (next % 60 === 0) console.log(next, '/', N, ((Date.now() - t0) / 1000).toFixed(0) + 's');
    }
  };
  await Promise.all(pages.map(async (p) => {
    while (claimed < N) {
      const i = claimed++;
      while (i - next > WORKERS * 4) await new Promise(r => setTimeout(r, 20));
      await p.evaluate(t => render(t), i / FPS);
      done.set(i, await p.screenshot({ type: 'png' }));
      chain = chain.then(flush);
    }
  }));
  await chain;
  ff.stdin.end();
  const code = await new Promise(r => ff.on('close', r));
  await b.close();
  console.log(code === 0 ? 'done ' + ((Date.now() - t0) / 1000).toFixed(0) + 's' : 'ffmpeg failed ' + code);
})();
