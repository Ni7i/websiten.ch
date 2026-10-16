# websiten.ch: eigene Agentur-Website von Loli

Statische Website, erzeugt mit Python. Live-Vorschau auf Vercel: https://beispiel13241324.vercel.app (Projekt "beispiel13241324", NICHT websiten.ch).

## Regeln für Texte und Gestaltung (vom Kunden festgelegt, nicht verhandelbar)

- Sprache: Deutsch (Schweiz, "ss" statt "ß"), Kunden werden gesiezt. Ehrlich, konkret, keine Werbefloskeln.
- Keine Gedankenstriche (—) und keine Halbgeviertstriche (–). Preise schreiben wir als "CHF 590", nicht "590.–".
- Loli arbeitet allein, die Texte sprechen trotzdem von "wir". Nie "kleine Agentur" schreiben.
- Keine Telefonnummer, kein WhatsApp, kein "rufen Sie an". Kontakt nur per E-Mail (hallo@websiten.ch) und Terminbuchung per Video (Google Meet).
- Keine Frauen auf Bildern. Keine Stockfotos, die nach Stock aussehen.
- Kein KI-Look: keine Trennlinien (auch keine Linien zwischen Abschnitten, Listeneinträgen, im Abschluss, Footer oder Menü, keine Unterstriche unter Pfeil-Links), keine Punktlinien, keine "01 02 03"-Nummern (ausser bei echten Abläufen), keine Breadcrumbs, kein Glas, keine Verläufe, kein Mint, kein Orange.
- Farben: dunkel #151515, Akzent gedämpftes Salbeigrün (--acc-s #A3C2AA, Fläche --sage #8FAE96). Ein paar Wörter pro Überschrift in Salbei (class="hl") sind erwünscht.
- Server und Hosting: Infomaniak in Genf. Loli selbst arbeitet mit Microsoft 365.
- Geräte-Grafiken (MacBook, schräges iPhone) gefallen dem Kunden sehr. Weiter so.

## Preise (verbindlich)

- Website: CHF 590 für 4 Seiten, CHF 890 bis 6, CHF 1’190 bis 8, CHF 1’490 bis 10, jede weitere Seite CHF 150
- Online-Shop: ab CHF 1’890 (4 Seiten, bis 30 Produkte), bis 150 Produkte + CHF 490, bis 500 + CHF 990, über 500 mit Import + CHF 1’890. Shopify-Abo zahlt der Kunde direkt.
- Extras: Texte CHF 90 pro Seite, weitere Sprache CHF 50 pro Sprache (fester Betrag, unabhängig von der Seitenzahl), Terminbuchung CHF 290, News/Blog CHF 190, Google-Profil CHF 150, Google Ads einrichten CHF 390
- Hosting und Domain: CHF 25 im Monat. Das alte Angebot "3 Monate für CHF 10" gibt es nicht mehr.
- Microsoft 365 und KI-Chatbots: kein fester Preis, Offerte nach Gespräch.
- Bezahlung: Hälfte bei Auftrag, Rest bei Livegang.

## Aufbau

- `build/build.py` erzeugt alle HTML-Seiten im Hauptordner. Ausführen: `cd build && python3 build.py` (braucht Pillow: `pip install pillow`).
- `build/parts.py`: gemeinsames Gerüst `page()`, Logo, Menü, Abschluss ("Reden wir über Ihre Website."), Footer.
- `build/home9.py`: Startseite (Reihenfolge: Einstieg mit Film, "Wir bauen Ihre Website", Schweizer Karte/Ablauf, "Was wir machen" mit MacBook-Umschalter, Referenzen, Preise, Abschluss). Ältere Fassungen home*.py werden noch importiert, nicht löschen ohne build.py anzupassen.
- `build/pages3.py`: alle Unterseiten (aktuelle Fassung). Jede Leistung hat eine eigene Seite mit einer Live-Demo:
  - websites.html: echte Websites von KF Bauservice und Kastrati in MacBook und iPhone (Bilder assets/img/live-*.jpg). Am Computer scrollen sie beim Scrollen mit (web_scrub, Klasse pc-only). Auf dem Handy (bis 860 px) kein Mitscrollen, stattdessen beide ruhig untereinander (web_work, Klasse m-only). So will es der Kunde.
  - online-shops.html: Einkauf im iPhone (Rösterei Linde, erfunden, so gekennzeichnet)
  - google-seo.html: helle Google-Suche im MacBook (seo_demo), Suchbegriff tippt sich, Vorher/Nachher-Schalter darunter (Keller Sanitär, erfunden, so gekennzeichnet)
  - hosting.html: Schweizer Karte, Linien nach Genf, Statusanzeige (Kartendaten build/swissmap.json)
  - microsoft-365.html: Konto für neuen Mitarbeiter wird Schritt für Schritt eingerichtet
  - ki-chatbots.html: Chat mit vorbereiteten Fragen
  - ueber-uns.html: Werbefilm "Websiten Ad v3" direkt unter dem Einstieg (FILM, FILM_CSS, FILM_JS in pages3.py). Abspielen nur per Klick, dann mit Ton. Die Startseite bleibt ohne diesen Film.
  - leistungen.html, preise.html (Satz zum Ausfüllen als Preisrechner), ueber-uns.html, kontakt.html, fragen.html, impressum.html, datenschutz.html
- Leistungsseiten kompakt halten (Kunde: sonst zu unübersichtlich): "Das bekommen Sie" (gets) nur als Häkchen-Liste mit Titeln in 2 Spalten, "So läuft es" (steps) eine Zeile pro Schritt (Woche, Titel, ein Satz), ohne grosse Zahlen und ohne Linien.
- Preise auf den Leistungsseiten (price in pages3.py): keine Riesenzahlen, sondern eine ruhige Liste "Leistung links, Preis rechts" unter "Was es kostet". Der Kunde fand die grosse Zahl ohne Zusammenhang unübersichtlich.
- Google-Suche auf google-seo.html: Browserfenster in 1280 x 800 gebaut und ins MacBook verkleinert, damit es wie ein echter Bildschirm wirkt (nicht wie ein generiertes Bild).
- MacBook-Grafiken: immer ohne Notch, nur Kamerapunkt im Rand (`macbook()` in pages3.py, `assets/img/mac-frame.webp`).
- Menü (MENU in parts.py, Logik in site.js): fährt man über eine Leistung, zeigt ein MacBook in der Mitte echte Inhalte (assets/img/mp-*.jpg: echte Websites von KF Bauservice und Kastrati, sonst echte Fotos ohne Personen, keine nachgebauten Bildschirme), darunter Titel und Kurztext. Die Bilder laden erst beim ersten Öffnen. Unter 1100 px und auf Touch-Geräten ausgeblendet.
- `build/pages2.py` und `build/pages.py`: ältere Fassungen, liefern noch Daten und die Terminbuchung (KONTAKT_JS) an pages3.
- `assets/site.css`, `assets/site.js`: gemeinsame Gestaltung und Skripte (Logo-Farbe je nach Hintergrund, Menü, Pixel-Schriftzug im Footer).
- `assets/websiten-ad.mp4` (1080p mit Ton) und `assets/websiten-ad-poster.jpg`: Werbefilm für ueber-uns.html. Quelle ist der Ordner `web/` im Design-Repo (Claude Design Export "Websiten Ad v3"), gerendert mit `node render/render.mjs`. Dort liegt auch die 4K-Fassung.
- `assets/websiten-hero.mp4` (Computer, 2560x1440) und `assets/websiten-hero-m.mp4` (Handy bis 860 px, Ausschnitt ums Logo): Hintergrundfilm im Logo-Fenster der Startseite. Erzeugt aus `video/bg.html` (8 Fotos in 4K aus `assets/img/hero4k/`, alle ohne Gesichter) mit `node tools/bgrender.js`, gerendert in 4K. Das Poster `video/bg-poster.jpg` ist das erste Bild des Films.
- `mockups/`: Erzeuger für Geräte-Grafiken (scene.html, render.js) und Bildschirm-Bilder (screens.html).
- `tools/`: Playwright-Skripte für Screenshots (shots.js, vp.js), Aufnahmen der Referenz-Websites (dfull.js, mfull2.js), Hintergrundfilm (bgrender.js). Ausführen mit `node tools/shots.js websites.html,preise.html 1440`. Optional `CHROME_PATH` setzen.

## Veröffentlichen

Jeder Push auf `main` von GitHub-Repo Ni7i/websiten.ch geht automatisch live: GitHub Actions (`.github/workflows/vercel.yml`) lädt mit der Vercel-CLI ins Projekt beispiel13241324 hoch. Dafür braucht das Repo das Actions-Secret `VERCEL_TOKEN`. `.vercelignore` sorgt dafür, dass nur `dist/` und `vercel.json` hochgeladen werden. Nach jedem Deploy prüft der Ablauf die Live-Seite (4 Seiten erreichbar, neue Fassung, CSP und HSTS aktiv) und öffnet danach 10 Seiten in einem echten Chrome (`tools/livecheck.mjs`: keine Script-Fehler, keine fehlenden Dateien, Menü-Vorschau sofort sichtbar). Ergebnis und Fehler stehen als Hinweise im Actions-Lauf auf GitHub. Vercel baut dabei nichts, sondern liefert den fertigen Ordner `dist/` aus (`outputDirectory` in `vercel.json` im Hauptordner). Deshalb gehört `dist/` ins Repo.

1. `cd build && python3 build.py` (erzeugt die Seiten, `fast.py` optimiert jede Seite)
2. `python3 dist.py` (stellt `dist/` neu zusammen: alle Seiten und genau die Dateien, auf die sie verweisen)
3. Alles committen, auch `dist/`, und auf `main` pushen. Vercel übernimmt den Rest.

Die Sicherheits- und Cache-Header stehen in `vercel.json` im Hauptordner (gilt für Vercel) und in `_headers` (für Cloudflare Pages oder Netlify, falls einmal gewechselt wird).

Vor jedem Deploy prüfen: keine "–" und "—" in den HTML-Dateien (dist.py warnt), keine Telefonnummer, kein horizontales Scrollen bei 390 px Breite.

## Tempo und Sicherheit (nicht verschlechtern)

- `build/fast.py` läuft auf jeder Seite: eingebettete Bilder (data:) und fest verlinkte JPG/PNG werden zu WebP-Dateien in `assets/img/x/` (Name = Hash). Bilder nach dem ersten Abschnitt bekommen `loading="lazy"`. CSS (auch site.css) steht direkt im HTML. Seiten-JS kommt nach `assets/js/` (Name = Hash), site.js bekommt `?v=Hash`.
- Schriften liegen selbst gehostet in `assets/fonts/` (Hanken Grotesk variabel, Fraunces, Newsreader). Kein Google Fonts mehr, keine Verbindung zu Google beim Laden.
- `vercel.json` und `_headers` setzen eine strenge Content-Security-Policy und weitere Sicherheits-Header. Deshalb: kein Inline-JavaScript im Seiten-HTML (kein `onclick=`, kein `<script>` in MAIN), keine externen Skripte, Schriften oder Bilder. Wer so etwas braucht, muss die CSP in beiden Dateien anpassen. Die Terminbuchung darf script.google.com erreichen.
- Dateien mit Hash im Namen bleiben ein Jahr im Browser-Cache. Andere Dateien in assets einen Tag.
- Die Vorschau beispiel13241324 ist laut Kunde nicht kommerziell und darf auf Vercel Hobby (gratis) laufen. Für das echte websiten.ch: Cloudflare Pages (gratis, kommerziell erlaubt) oder eigenes Hosting bei Infomaniak.

## Offen

- PLATZHALTER: Impressum, Datenschutz und Footer enthalten erfundene Angaben (Inhaber Leandro Tschanzer, Postfach, 8021 Zürich). Vor dem echten Livegang von websiten.ch durch echte Angaben ersetzen (IMPRESSUM_MAIN und DATENSCHUTZ_MAIN in build/pages.py, FOOTER in build/parts.py).
- LinkedIn-Link fehlt (`LINKEDIN` in build/parts.py). Datenschutz vor dem Livegang juristisch prüfen lassen.
- `BOOKING_API` in build/build.py ist leer: Terminbuchung läuft im Vorschau-Modus, bis das Google Apps Script bereitgestellt ist.
- Shop-Beispiel im MacBook (Rösterei Linde) ist erfunden. Durch einen echten Kunden-Shop ersetzen, sobald einer genannt wird.
