# "Was wir machen" im Stil von zumostudios.ch: grosse dunkle Karten, Titel oben, darunter eine Oberfläche, runder Knopf
from parts import ARROW

def badge(uid):
    return f'''<span class="zb" aria-hidden="true"><svg class="zb-ring" viewBox="0 0 120 120"><defs><path id="{uid}" d="M60,60 m-44,0 a44,44 0 1,1 88,0 a44,44 0 1,1 -88,0"/></defs><text><textPath href="#{uid}" textLength="276">MEHR ANZEIGEN · MEHR ANZEIGEN · </textPath></text></svg><span class="zb-c"><svg viewBox="0 0 22 14" aria-hidden="true"><path d="M1 7h19M14 1l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8"/></svg></span></span>'''

V_WEB = '''<div class="zv zv-web">
  <div class="ed-side"><i></i><i></i><i></i><i></i></div>
  <div class="ed-main">
    <div class="ed-top"><span class="ed-tab">Startseite</span><span class="ed-tab o">Leistungen</span><span class="ed-tab o">Kontakt</span><span class="ed-pub">Veröffentlichen</span></div>
    <div class="ed-canvas">
      <div class="ws-nav"><b>Keller Sanitär</b><span></span><span></span><span></span><em>Anfrage</em></div>
      <div class="ws-hero"><div><small>Sanitär in Baden</small><h5>Badumbau aus einer Hand.</h5><p></p><p class="s"></p><em>Besichtigung vereinbaren</em></div><div class="ws-img"></div></div>
      <div class="ws-row"><span></span><span></span><span></span></div>
    </div>
  </div>
</div>'''

V_SHOP = '''<div class="zv zv-shop">
  <div class="sh-l"><small>Ihr Warenkorb</small><div class="sh-p"><i></i><span><b>Duschset Rondo</b>Chrom, 1 Stück</span><em>189.00</em></div><div class="sh-p"><i class="b"></i><span><b>Thermostat Linea</b>Weiss, 1 Stück</span><em>124.00</em></div></div>
  <div class="sh-r"><h5>Bestellung</h5><div class="sh-l2"><span>Zwischensumme</span><span>313.00</span></div><div class="sh-l2"><span>Versand Post</span><span>9.00</span></div><div class="sh-l2 t"><span>Total CHF</span><span>322.00</span></div><div class="sh-pay"><em class="tw">TWINT</em><em>Karte</em><em>Rechnung</em></div></div>
</div>'''

V_SEO = '''<div class="zv zv-seo">
  <div class="se-k"><div><small>Klicks</small><b>1’284</b></div><div><small>Impressionen</small><b>48’930</b></div><div><small>Ø Position</small><b>6.2</b></div></div>
  <svg class="se-c" viewBox="0 0 600 220" preserveAspectRatio="none" aria-hidden="true"><g stroke="#2C2C2C" stroke-width="1"><line x1="0" y1="55" x2="600" y2="55"/><line x1="0" y1="110" x2="600" y2="110"/><line x1="0" y1="165" x2="600" y2="165"/></g><path d="M0 190 C40 185 70 170 110 172 S180 150 220 140 S290 150 330 118 S400 90 440 96 S520 60 600 38" fill="none" stroke="#E6E6E6" stroke-width="2.4"/><path d="M0 205 C50 200 90 196 130 190 S210 184 250 176 S330 170 370 156 S460 150 500 132 S560 120 600 112" fill="none" stroke="#6A6A6A" stroke-width="2"/></svg>
  <div class="se-q"><span>Suchbegriff</span><span>Position</span><b>badsanierung baden</b><b>3</b><b>sanitär wettingen</b><b>5</b></div>
</div>'''

V_HOST = '''<div class="zv zv-host">
  <div class="ho-t"><b>ihre-firma.ch</b><span><i></i>Online</span></div>
  <div class="ho-bars">''' + ''.join(f'<i style="height:{h}%"></i>' for h in (62, 70, 66, 80, 74, 88, 79, 92, 85, 90, 96, 88, 94, 99, 91, 97, 93, 100)) + '''</div>
  <div class="ho-r"><span>Server</span><b>Infomaniak, Genf</b></div>
  <div class="ho-r"><span>Letztes Backup</span><b>Heute, 03:00</b></div>
  <div class="ho-r"><span>SSL-Zertifikat</span><b>gültig bis 09/2027</b></div>
  <div class="ho-r"><span>Updates</span><b>alle installiert</b></div>
</div>'''

V_M365 = '''<div class="zv zv-m365">
  <div class="ms-side"><i class="on"></i><i></i><i></i><i></i></div>
  <div class="ms-main"><div class="ms-t">Posteingang <span>info@ihre-firma.ch</span></div>
    <div class="ms-m"><i>MB</i><div><b>Offerte Badsanierung</b><span>Guten Tag, anbei die Masse unseres Badezimmers</span></div><em>09:12</em></div>
    <div class="ms-m"><i>RS</i><div><b>Lieferung am Dienstag</b><span>Die Platten kommen um 7 Uhr auf die Baustelle</span></div><em>08:40</em></div>
    <div class="ms-m"><i>TK</i><div><b>Teams: Besprechung</b><span>Morgen 10 Uhr, Planung Projekt Wettingen</span></div><em>Gestern</em></div>
    <div class="ms-m"><i>NL</i><div><b>Neues Konto eingerichtet</b><span>Willkommen im Team, Ihr Zugang ist bereit</span></div><em>Mo</em></div>
  </div>
</div>'''

V_KI = '''<div class="zv zv-ki">
  <div class="ki-h"><i></i><b>Fragen an Keller Sanitär</b><span>antwortet sofort</span></div>
  <div class="ki-b in">Haben Sie am Samstag offen?</div>
  <div class="ki-b out">Ja, am Samstag von 9 bis 14 Uhr. Soll ich Ihnen einen Termin für eine Besichtigung vorschlagen?</div>
  <div class="ki-b in">Gerne, am Vormittag.</div>
  <div class="ki-in"><span>Nachricht schreiben</span><i></i></div>
</div>'''

CARDS = [
    ('websites', 'Websites', 'Für Ihren Betrieb gestaltet, fürs Handy gebaut.', V_WEB),
    ('shops', 'Online-Shops', 'Mit TWINT, Karte, Rechnung und Versand.', V_SHOP),
    ('seo', 'Google und SEO', 'Gefunden werden, wo Ihre Kunden suchen.', V_SEO),
    ('hosting', 'Domains und Hosting', 'Bei Infomaniak in Genf, mit Backups und Updates.', V_HOST),
    ('m365', 'Microsoft 365', 'E-Mail, Teams und Dateien für Ihr Team.', V_M365),
    ('ki', 'KI-Chatbots', 'Beantwortet häufige Fragen auf Ihrer Website.', V_KI),
]

def section():
    cards = ''.join(f'<a class="zc" href="leistungen.html#{i}"><div class="zc-h"><h3>{t}</h3><p>{d}</p></div><div class="zc-v">{v}{badge("zb" + str(k))}</div></a>' for k, (i, t, d, v) in enumerate(CARDS))
    return '''<section class="zs pad" id="leistungen" aria-labelledby="zsT">
    <div class="zs-top"><span>Unsere Leistungen</span><span>02</span></div>
    <h2 id="zsT">Was wir für Ihren Betrieb <span>machen.</span></h2>
    <div class="zs-grid">''' + cards + '''</div>
    <a class="sv-all zs-all" href="leistungen.html">Alle Leistungen ''' + ARROW + '''</a>
  </section>'''

CSS = r'''
.zs{padding-top:clamp(70px,8vw,120px);padding-bottom:clamp(90px,10vw,160px)}
.zs-top{display:flex;justify-content:space-between;font-size:13px;letter-spacing:.06em;text-transform:uppercase;color:#BDBDBD;padding-bottom:clamp(56px,7vw,110px)}
.zs h2{font-size:clamp(34px,3.6vw,62px);line-height:1.12;font-weight:600;letter-spacing:-.035em;max-width:18ch}
.zs h2 span{color:#7A7A7A}
.zs-grid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:clamp(24px,5vw,96px);margin-top:clamp(56px,7vw,110px);align-items:start}
.zs-grid .zc:nth-child(2n){transform:translateY(clamp(40px,6vw,100px))}
.zc{display:block;background:#1E1E1E;border-radius:28px;overflow:hidden;margin-bottom:clamp(28px,4vw,64px);transition:background .3s}
.zc:hover{background:#222}
.zc-h{padding:clamp(32px,3.6vw,60px) clamp(28px,3.6vw,60px) clamp(28px,3vw,44px)}
.zc h3{font-size:clamp(34px,3.6vw,60px);line-height:1;font-weight:600;letter-spacing:-.04em}
.zc-h p{font-size:16px;color:var(--muted);margin-top:14px}
.zc-v{position:relative;height:clamp(300px,30vw,440px);border-radius:28px 28px 0 0;overflow:hidden;background:#0F0F0F}
.zv{position:absolute;inset:0;font-family:var(--sans);color:#D9D9D9;transition:transform .7s var(--ease)}
.zc:hover .zv{transform:translateY(-8px)}
.zb{position:absolute;left:clamp(24px,3vw,44px);bottom:clamp(24px,3vw,40px);width:112px;height:112px;display:grid;place-items:center;z-index:3}
.zb-ring{position:absolute;inset:0;width:100%;height:100%;animation:zspin 16s linear infinite}
.zb-ring text{font-size:11.5px;font-weight:600;letter-spacing:.08em;fill:#EDEDED}
.zb-c{width:58px;height:58px;border-radius:50%;background:#3A3A3A;color:#F2F2F2;display:grid;place-items:center;transition:transform .4s var(--ease),background .3s}
.zb-c svg{width:20px;height:13px}
.zc:hover .zb-c{transform:rotate(-45deg);background:#EDEDED;color:#151515}
.zc:hover .zb-ring{animation-duration:6s}
@keyframes zspin{to{transform:rotate(360deg)}}
.zs-all{margin-top:clamp(60px,8vw,120px)}

/* Oberflächen in den Karten */
.zv-web{display:flex;left:22%;top:28px;right:-8%;bottom:-6%;background:#151515;border:1px solid #2C2C2C;border-radius:16px 0 0 0}
.ed-side{width:46px;border-right:1px solid #262626;display:flex;flex-direction:column;align-items:center;gap:16px;padding-top:18px}
.ed-side i{width:16px;height:16px;border-radius:4px;border:1.5px solid #555}
.ed-main{flex:1;display:flex;flex-direction:column;min-width:0}
.ed-top{display:flex;align-items:center;gap:8px;padding:10px 14px;border-bottom:1px solid #262626;font-size:12px}
.ed-tab{background:#262626;padding:5px 10px;border-radius:6px}
.ed-tab.o{background:none;color:#777}
.ed-pub{margin-left:auto;background:#E6E6E6;color:#151515;font-weight:600;padding:5px 12px;border-radius:6px}
.ed-canvas{margin:18px;flex:1;background:#E4E4E4;border-radius:8px;color:#1A1A1A;padding:14px 18px;display:flex;flex-direction:column;gap:14px}
.ws-nav{display:flex;align-items:center;gap:14px;font-size:11px}
.ws-nav b{margin-right:auto}
.ws-nav span{width:34px;height:5px;border-radius:3px;background:#C8C8C8}
.ws-nav em{font-style:normal;font-size:10px;border:1px solid #1A1A1A;padding:3px 8px;border-radius:4px}
.ws-hero{display:grid;grid-template-columns:1fr 1fr;gap:16px;flex:1;min-height:0}
.ws-hero small{font-size:9px;color:#777}
.ws-hero h5{font-size:22px;line-height:1.05;letter-spacing:-.03em;margin:6px 0 10px}
.ws-hero p{height:5px;background:#CFCFCF;border-radius:3px;margin-top:6px}
.ws-hero p.s{width:70%}
.ws-hero em{display:inline-block;font-style:normal;font-size:10px;background:#1A1A1A;color:#fff;padding:6px 10px;border-radius:4px;margin-top:14px}
.ws-img{border-radius:6px;background:linear-gradient(160deg,#BDBDBD,#8A8A8A 60%,#6E6E6E)}
.ws-row{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}
.ws-row span{height:36px;border-radius:5px;background:#E0E0E0}

.zv-shop{display:grid;grid-template-columns:1fr 1fr;left:22%;right:-10%;top:26px;bottom:-4%;background:#151515;border:1px solid #2C2C2C;border-radius:16px 0 0 0}
.sh-l{padding:24px;border-right:1px solid #262626}
.sh-l small,.ho-r span,.se-k small,.se-q span{font-size:12px;color:#7A7A7A}
.sh-p{display:grid;grid-template-columns:46px 1fr auto;gap:12px;align-items:center;margin-top:18px;font-size:12px;color:#8A8A8A}
.sh-p i{width:46px;height:46px;border-radius:10px;background:linear-gradient(150deg,#5A5A5A,#2A2A2A)}
.sh-p i.b{background:linear-gradient(150deg,#D0D0D0,#8A8A8A)}
.sh-p b{display:block;color:#E6E6E6;font-size:13px;font-weight:600}
.sh-p em{font-style:normal;color:#E6E6E6;font-size:13px}
.sh-r{padding:24px;background:#0C0C0C}
.sh-r h5{font-family:Fraunces,Georgia,serif;font-weight:400;font-size:28px;margin-bottom:16px}
.sh-l2{display:flex;justify-content:space-between;font-size:12.5px;padding:9px 0;border-bottom:1px solid #222;color:#9A9A9A}
.sh-l2.t{color:#F2F2F2;font-weight:700;font-size:14px}
.sh-pay{display:flex;gap:8px;margin-top:18px}
.sh-pay em{font-style:normal;font-size:11px;padding:7px 11px;border-radius:7px;border:1px solid #333;color:#BDBDBD}
.sh-pay em.tw{background:#F2F2F2;color:#0C0C0C;border-color:#F2F2F2;font-weight:800;letter-spacing:.04em}

.zv-seo{left:22%;right:-6%;top:26px;bottom:-4%;background:#151515;border:1px solid #2C2C2C;border-radius:16px 0 0 0;padding:26px 28px}
.se-k{display:flex;gap:44px}
.se-k b{display:block;font-size:30px;font-weight:600;letter-spacing:-.03em;margin-top:4px;color:#F2F2F2}
.se-c{display:block;width:100%;height:42%;margin-top:22px}
.se-q{display:grid;grid-template-columns:1fr auto;gap:10px 30px;margin-top:20px;font-size:13px;max-width:360px}
.se-q b{font-weight:500;color:#D9D9D9}

.zv-host{left:24%;right:-4%;top:30px;bottom:-4%;background:#151515;border:1px solid #2C2C2C;border-radius:16px 0 0 0;padding:24px 26px}
.ho-t{display:flex;justify-content:space-between;align-items:center;font-size:15px}
.ho-t span{display:flex;align-items:center;gap:8px;font-size:12px;color:#BDBDBD}
.ho-t span i{width:8px;height:8px;border-radius:50%;background:#E6E6E6;box-shadow:0 0 0 4px rgba(230,230,230,.12)}
.ho-bars{display:flex;align-items:flex-end;gap:5px;height:70px;margin:22px 0 14px;border-bottom:1px solid #262626}
.ho-bars i{flex:1;background:#3A3A3A;border-radius:3px 3px 0 0}
.ho-bars i:last-child{background:#E6E6E6}
.ho-r{display:flex;justify-content:space-between;padding:10px 0;border-bottom:1px solid #222;font-size:13px}
.ho-r b{font-weight:500}

.zv-m365{display:flex;left:22%;right:-8%;top:26px;bottom:-4%;background:#151515;border:1px solid #2C2C2C;border-radius:16px 0 0 0}
.ms-side{width:54px;border-right:1px solid #262626;display:flex;flex-direction:column;align-items:center;gap:14px;padding-top:20px}
.ms-side i{width:22px;height:22px;border-radius:6px;background:#2A2A2A}
.ms-side i.on{background:#E6E6E6}
.ms-main{flex:1;padding:18px 20px;min-width:0}
.ms-t{font-size:15px;font-weight:600;margin-bottom:10px}
.ms-t span{font-weight:400;font-size:12px;color:#7A7A7A;margin-left:8px}
.ms-m{display:grid;grid-template-columns:34px minmax(0,1fr) auto;gap:12px;align-items:center;padding:11px 0;border-bottom:1px solid #222}
.ms-m i{width:34px;height:34px;border-radius:50%;background:#2E2E2E;display:grid;place-items:center;font-style:normal;font-size:11px;color:#BDBDBD}
.ms-m b{display:block;font-size:13px;font-weight:600}
.ms-m span{display:block;font-size:12px;color:#7A7A7A;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ms-m em{font-style:normal;font-size:11px;color:#7A7A7A}

.zv-ki{left:30%;right:6%;top:30px;bottom:-4%;background:#151515;border:1px solid #2C2C2C;border-radius:20px 20px 0 0;padding:18px;display:flex;flex-direction:column;gap:12px}
.ki-h{display:flex;align-items:center;gap:10px;padding-bottom:12px;border-bottom:1px solid #262626;font-size:13px}
.ki-h i{width:28px;height:28px;border-radius:50%;background:#E6E6E6}
.ki-h span{margin-left:auto;font-size:11px;color:#7A7A7A}
.ki-b{max-width:80%;font-size:13px;line-height:1.45;padding:10px 13px;border-radius:14px}
.ki-b.in{align-self:flex-end;background:#E6E6E6;color:#151515;border-bottom-right-radius:4px}
.ki-b.out{align-self:flex-start;background:#262626;border-bottom-left-radius:4px}
.ki-in{margin-top:auto;display:flex;justify-content:space-between;align-items:center;border:1px solid #2C2C2C;border-radius:99px;padding:9px 10px 9px 16px;font-size:12px;color:#6A6A6A}
.ki-in i{width:26px;height:26px;border-radius:50%;background:#3A3A3A}

@media (max-width: 860px){
  .zs-grid{grid-template-columns:1fr}
  .zs-grid .zc:nth-child(2n){transform:none}
  .zc-v{height:320px}
  .zb{width:92px;height:92px}
  .zb-c{width:48px;height:48px}
  .zv-shop{grid-template-columns:1fr;left:26%}
  .sh-l{display:none}
  .zv-web,.zv-seo,.zv-host,.zv-m365{left:26%}
  .zv-ki{left:28%;right:-10%}
  .se-k{gap:24px}
  .se-k b{font-size:22px}
}
@media (prefers-reduced-motion: reduce){ .zb-ring{animation:none} }
'''
