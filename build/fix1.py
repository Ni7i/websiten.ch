s=open('pages.py').read()
pairs=[
('''    <h1>Arbeiten. <span class="quiet">Drei Branchen, drei Handschriften.</span></h1>
    <p>Diese drei Entwürfe zeigen, wie verschieden eine Website von uns aussehen kann. Jede hat eigene Farben, eine eigene Schrift und einen eigenen Weg zur Anfrage.</p>''',
'''    <h1>Arbeiten</h1>
    <p>Drei Beispiel-Entwürfe für drei Branchen. Jeder hat eigene Farben, eine eigene Schrift und einen eigenen Weg zur Anfrage, weil ein Café andere Besucher hat als eine Arztpraxis.</p>'''),
("'Kunden suchen im Notfall schnell eine Nummer und planen sonst ein neues Bad. Die Seite bedient beides: Notfall-Service ganz oben, Offerte mit wenigen Klicks.'",
 "'Wer einen Rohrbruch hat, sucht eine Telefonnummer. Wer ein neues Bad plant, will Beispiele sehen und eine Offerte. Darum steht der Notfall-Service oben, und das Offertformular ist zwei Klicks entfernt.'"),
("'Ruhig, klar und vertrauenswürdig. Öffnungszeiten und Notfallnummer sind sofort sichtbar, Termine lassen sich online buchen.'",
 "'Patientinnen und Patienten wollen vor allem drei Dinge wissen: wann offen ist, wie sie einen Termin bekommen und wen sie im Notfall anrufen. Genau das steht auf der Startseite.'"),
("'Warm und appetitlich. Die Tagesvitrine steht auf der Startseite, Torten lassen sich online bestellen und abholen.'",
 "'Die Vitrine von heute steht gleich auf der Startseite. Geburtstagstorten lassen sich online bestellen und zu einer gewählten Zeit abholen. Das spart Anrufe mitten im Morgenbetrieb.'"),
('.ex-info h2{font-size:clamp(32px,3.4vw,56px);line-height:1.02;font-weight:500;letter-spacing:-.04em;margin-top:10px}','.ex-info h2{font-size:clamp(32px,3.4vw,58px);line-height:1;font-weight:700;letter-spacing:-.05em;margin-top:10px}'),
('''    <h1>Preise. <span class="quiet">Rechnen Sie selbst.</span></h1>
    <p>Beantworten Sie den Satz unten, und Sie sehen sofort einen Richtpreis. Der genaue Preis steht danach in der Offerte, und der gilt.</p>''',
'''    <h1>Was kostet Ihre Website?</h1>
    <p>Füllen Sie den Satz unten aus. Rechts sehen Sie sofort einen Richtpreis. Den genauen Preis bekommen Sie nach einem kurzen Gespräch als Offerte.</p>'''),
('''  <section class="fine pad">
    <div><b>Was immer dabei ist</b><p>Design nach Mass, Handy-Version, SSL, Kontaktformular, Einrichtung bei Infomaniak und eine Einführung.</p></div>
    <div><b>Was extra kostet</b><p>Bilder von Fotografen, Bildlizenzen, das Shopify-Abo und Gebühren der Zahlungsanbieter. Das sagen wir Ihnen vorher.</p></div>
    <div><b>Wie bezahlt wird</b><p>Die Hälfte bei Auftrag, die andere Hälfte beim Livegang. Betreuung monatlich, jederzeit kündbar.</p></div>
  </section>''',
'''  <section class="fine">
    <h2>Gut zu wissen</h2>
    <p>In jedem Preis sind die Gestaltung, die Version fürs Handy, das SSL-Zertifikat, ein Kontaktformular, die Einrichtung bei Infomaniak und eine Einführung enthalten. Nicht enthalten sind Fotografen, gekaufte Bilder, das Shopify-Abo und die Gebühren der Zahlungsanbieter. Wenn so etwas dazukommt, steht es in der Offerte. Bezahlt wird die Hälfte bei Auftrag und der Rest beim Livegang. Die Betreuung läuft monatlich und ist jederzeit kündbar.</p>
  </section>'''),
('.fine{padding-bottom:clamp(100px,12vw,160px);display:grid;grid-template-columns:repeat(3,1fr);gap:clamp(24px,3vw,48px)}\n.fine div{border-top:1px solid var(--line);padding-top:20px}\n.fine b{display:block;font-size:19px;font-weight:500}\n.fine p{color:var(--muted);font-size:16px;margin-top:8px;max-width:36ch}',
 '.fine{margin:0 var(--pad) clamp(100px,12vw,160px);padding-top:40px;border-top:1px solid var(--line);display:grid;grid-template-columns:minmax(0,1fr) minmax(0,2fr);gap:clamp(24px,5vw,96px)}\n.fine h2{font-size:22px;font-weight:600}\n.fine p{color:#C7D0CA;font-size:18px;line-height:1.75;max-width:62ch}'),
('<span class="pick" role="group" aria-label="Sprachen"><button type="button" data-k="lang" data-v="1" aria-pressed="true">Deutsch</button><button type="button" data-k="lang" data-v="2" aria-pressed="false">2 Sprachen</button><button type="button" data-k="lang" data-v="3" aria-pressed="false">3 Sprachen</button></span>.',
 '<span class="nw"><span class="pick" role="group" aria-label="Sprachen"><button type="button" data-k="lang" data-v="1" aria-pressed="true">Deutsch</button><button type="button" data-k="lang" data-v="2" aria-pressed="false">2 Sprachen</button><button type="button" data-k="lang" data-v="3" aria-pressed="false">3 Sprachen</button></span>.</span>'),
('<span class="pick" role="group" aria-label="Texte"><button type="button" data-k="texts" data-v="1" aria-pressed="true">schreibt ihr</button><button type="button" data-k="texts" data-v="0" aria-pressed="false">liefern wir</button></span>.',
 '<span class="nw"><span class="pick" role="group" aria-label="Texte"><button type="button" data-k="texts" data-v="1" aria-pressed="true">schreibt ihr</button><button type="button" data-k="texts" data-v="0" aria-pressed="false">liefern wir</button></span>.</span>'),
('<button type="button" class="chk" data-x="bot" aria-pressed="false"><i></i>einen KI-Chatbot</button>\n      <span class="shop-only" hidden><button type="button" class="chk" data-x="invoice" aria-pressed="false"><i></i>Kauf auf Rechnung</button></span>.',
 '<span class="shop-only" hidden><button type="button" class="chk" data-x="invoice" aria-pressed="false"><i></i>Kauf auf Rechnung</button></span>\n      <span class="nw"><button type="button" class="chk" data-x="bot" aria-pressed="false"><i></i>einen KI-Chatbot</button>.</span>'),
('<span class="pick" role="group" aria-label="Betreuung"><button type="button" data-k="care" data-v="0" aria-pressed="false">kümmern wir uns selbst</button><button type="button" data-k="care" data-v="29" aria-pressed="false">kümmert ihr euch</button><button type="button" data-k="care" data-v="79" aria-pressed="true">kümmert ihr euch, mit kleinen Änderungen</button></span>.',
 '<span class="pick wrapok" role="group" aria-label="Betreuung"><button type="button" data-k="care" data-v="0" aria-pressed="false">kümmern wir uns selbst</button><button type="button" data-k="care" data-v="29" aria-pressed="false">kümmert ihr euch</button><button type="button" data-k="care" data-v="79" aria-pressed="true">kümmert ihr euch, inklusive kleiner Änderungen</button></span>'),
('.sentence .w{color:var(--text)}','.sentence .w{color:var(--text)}\n.nw{white-space:nowrap}\n.pick.wrapok{flex-wrap:wrap;border-radius:26px}\n.sentence{font-weight:600;letter-spacing:-.035em}'),
('''    <h1>Gute Websites. <span class="quiet">Ohne Umwege.</span></h1>
    <p>websiten.ch baut Websites, Online-Shops und alles, was dazugehört, für Betriebe in der ganzen Schweiz. Wir reden Klartext, halten Termine und machen Dinge, die funktionieren.</p>''',
'''    <h1>Über uns</h1>
    <p class="letter">websiten.ch baut Websites, Online-Shops und alles, was dazugehört, für Betriebe in der ganzen Schweiz. Für Handwerker, Praxen, Restaurants und Läden, die online gefunden werden wollen, ohne sich selbst um die Technik zu kümmern. Wir reden Klartext, halten Termine und machen Dinge, die funktionieren.</p>'''),
('.beliefs{padding-bottom','.page-hero .letter{font-size:clamp(24px,2.6vw,42px);line-height:1.35;color:var(--text);max-width:34ch;font-weight:500;letter-spacing:-.025em}\n.beliefs{padding-bottom'),
('<div class="belief"><h2>Sie verstehen, was wir tun.</h2><p>Kein Fachchinesisch und keine Abkürzungen, die niemand kennt. Wir erklären, was wir vorschlagen und warum. Wenn etwas für Ihren Betrieb keinen Sinn ergibt, sagen wir es.</p></div>',
 '<div class="belief"><h2>Sie verstehen, was wir tun.</h2><p>Wir erklären, was wir vorschlagen und warum, ohne Abkürzungen, die niemand kennt. Und wenn etwas für Ihren Betrieb keinen Sinn ergibt, sagen wir das, auch wenn wir daran verdienen könnten.</p></div>'),
('<div class="belief"><h2>Ihre Website gehört Ihnen.</h2><p>Domain, Inhalte und Zugänge laufen auf Ihren Namen. Sie sind nie an uns gebunden. Wer gut arbeitet, braucht keine Kunden, die nicht gehen können.</p></div>',
 '<div class="belief"><h2>Ihre Website gehört Ihnen.</h2><p>Domain, Inhalte und Zugänge laufen auf Ihren Namen. Wenn Sie einmal wechseln möchten, bekommen Sie alles, was Sie dafür brauchen.</p></div>'),
('<div><h2>Ein Ansprechpartner für alles, was online ist.</h2><p style="margin-top:28px">Website, Shop, Google, Domains, E-Mail und Microsoft 365. Sie müssen nicht fünf Firmen koordinieren, die sich gegenseitig die Schuld geben. Sie rufen eine Nummer an, und die Sache wird erledigt.</p></div>',
 '<div><h2>Eine Nummer für alles, was online ist.</h2><p style="margin-top:28px">Website, Shop, Google, Domains, E-Mail und Microsoft 365. Sie müssen nicht fünf Firmen koordinieren, die sich bei einem Problem gegenseitig die Schuld geben. Sie rufen an, und die Sache wird erledigt.</p></div>'),
('''    <h2 class="h-sec">Womit wir arbeiten.</h2>
    <div class="tools-grid">
      <div><b>Infomaniak</b><p>Domains, Hosting und E-Mail. Schweizer Anbieter aus Genf.</p></div>
      <div><b>WordPress</b><p>Für Websites, die Sie danach selbst pflegen können.</p></div>
      <div><b>Shopify</b><p>Für Online-Shops, die einfach laufen sollen.</p></div>
      <div><b>WooCommerce</b><p>Für Shops direkt in der eigenen WordPress-Website.</p></div>
      <div><b>Microsoft 365</b><p>E-Mail, Teams und OneDrive für Ihr Büro.</p></div>
      <div><b>Google</b><p>Unternehmensprofil, Search Console und Google Ads.</p></div>
    </div>''',
'''    <h2 class="h-sec">Womit wir arbeiten</h2>
    <table class="tools-t">
      <tr><th>Infomaniak</th><td>Domains, Hosting und E-Mail bei einem Schweizer Anbieter aus Genf</td></tr>
      <tr><th>WordPress</th><td>Für Websites, die Sie danach selbst pflegen können</td></tr>
      <tr><th>Shopify</th><td>Für Online-Shops, die ohne Bastelei laufen sollen</td></tr>
      <tr><th>WooCommerce</th><td>Für einen Shop direkt in der bestehenden WordPress-Website</td></tr>
      <tr><th>Microsoft 365</th><td>E-Mail, Teams und OneDrive fürs Büro</td></tr>
      <tr><th>Google</th><td>Unternehmensprofil, Search Console und Google Ads</td></tr>
    </table>'''),
('.tools-grid{margin-top','.tools-t{margin-top:clamp(40px,5vw,64px);width:100%;border-collapse:collapse}\n.tools-t th,.tools-t td{text-align:left;padding:22px 0;border-top:1px solid var(--line);vertical-align:baseline}\n.tools-t tr:last-child th,.tools-t tr:last-child td{border-bottom:1px solid var(--line)}\n.tools-t th{width:34%;font-size:clamp(22px,2vw,32px);font-weight:600;letter-spacing:-.03em}\n.tools-t td{color:#C7D0CA;font-size:17px}\n.tools-grid{margin-top'),
('.belief h2{font-size:clamp(30px,3.6vw,64px);line-height:1.04;font-weight:500;letter-spacing:-.04em}','.belief h2{font-size:clamp(30px,3.4vw,60px);line-height:1;font-weight:700;letter-spacing:-.05em}'),
('.band h2{font-size:clamp(36px,4.6vw,80px);line-height:1.02;font-weight:500;letter-spacing:-.045em}','.band h2{font-size:clamp(36px,4.4vw,78px);line-height:.98;font-weight:700;letter-spacing:-.05em}'),
('  .tools-grid{grid-template-columns:1fr}','  .tools-t th{display:block;width:auto;padding-bottom:4px}\n  .tools-t td{display:block;border-top:0;padding-top:0}'),
('<h1>Erzählen Sie uns von Ihrem Projekt.</h1>\n    <p>Ein paar Sätze reichen. Wir melden uns meistens am gleichen oder nächsten Arbeitstag und vereinbaren ein kurzes Gespräch.</p>',
 '<h1>Kontakt</h1>\n    <p>Ein paar Sätze zu Ihrem Projekt reichen. Wir melden uns meistens am gleichen oder nächsten Arbeitstag.</p>'),
]
for a,b in pairs:
    assert a in s, a[:80]; s=s.replace(a,b,1)
open('pages.py','w').write(s)

c=open('../assets/site.css').read()
pairs=[
('.h-sec{font-size:clamp(36px,4.6vw,76px);line-height:1.04;font-weight:500;letter-spacing:-.035em}','.h-sec{font-size:clamp(36px,4.4vw,74px);line-height:1;font-weight:700;letter-spacing:-.05em}'),
('.page-hero h1{font-size:clamp(48px,8vw,150px);line-height:.96;font-weight:500;letter-spacing:-.055em;max-width:14ch}','.page-hero h1{font-size:clamp(56px,10vw,190px);line-height:.9;font-weight:700;letter-spacing:-.06em;max-width:14ch}'),
('.closing h2{font-size:clamp(52px,9vw,184px);line-height:.92;font-weight:500;letter-spacing:-.055em}','.closing h2{font-size:clamp(52px,8.6vw,176px);line-height:.9;font-weight:700;letter-spacing:-.06em;max-width:12ch}'),
('.menu-big a{display:inline-block;font-size:clamp(44px,6.6vw,116px);line-height:1.03;font-weight:500;','.menu-big a{display:inline-block;font-size:clamp(44px,6.6vw,116px);line-height:1.03;font-weight:700;'),
('.giant{margin-top:clamp(64px,8vw,120px);font-size:clamp(72px,17vw,360px);line-height:.78;font-weight:500;letter-spacing:-.065em;color:#19211D;white-space:nowrap;user-select:none}\n.giant span{color:#26332C}',
 '.giant{display:block;width:100%;height:auto;margin-top:clamp(64px,8vw,120px);margin-bottom:-1px;fill:#1B2420}'),
('  --muted:#8E9A93;','  --muted:#97A39C;'),
('.page-hero p{font-size:clamp(18px,1.5vw,22px);line-height:1.6;color:#BAC5BE;','.page-hero p{font-size:clamp(18px,1.5vw,22px);line-height:1.6;color:#C7D0CA;'),
]
for a,b in pairs:
    assert a in c, a[:70]; c=c.replace(a,b,1)
open('../assets/site.css','w').write(c)
print('ok')
