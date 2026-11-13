# Jeianne FM (Android APK)

1. I-upload ang **lahat** ng laman ng folder na ito sa GitHub repo (main branch), kasama ang `.github`, `www`, `android-res` at `android-src`.
2. Pumunta sa tab na **Actions** → **Build APK** (kusang tatakbo; puwede ring **Run workflow**).
3. Kapag green na, buksan ang run → **Artifacts** → i-download ang **JeianneFM-APK**.
4. I-unzip, i-install ang `app-debug.apk` sa phone (payagan ang "Install unknown apps").

Para palitan ang stream URL o disenyo, i-edit ang `www/index.html` at mag-commit; kusang magbi-build ulit.

## Mga folder
- `www/` – ang web app (index.html)
- `android-res/` – app icons (lahat ng laki) at kulay ng icon background
- `android-src/` – foreground service para tuloy ang tugtog kapag naka-background / patay ang screen
- `.github/workflows/build.yml` – ang Build APK workflow
