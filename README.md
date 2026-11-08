# Agentic Coding Schule – Staffel 1

In diesem Repo liegen die Hausaufgaben der Staffel 1. Zu jedem Schulungstermin gehört ein Trail, und zu jedem Trail gibt es einen Ordner mit der Hausaufgabe:

```
trail-1/index.html
trail-2/index.html
…
```

> [!WARNING]
> **Pushe nie in dieses Repo.** Als eingeladene Person hast du hier Schreibrechte, weil das Repo einem persönlichen Konto gehört. Deine Antworten gehören ausschließlich in **deinen eigenen Fork**.

## Ablauf für Teilnehmer

### 1. Forken und den eigenen Fork klonen

Einmalig zu Beginn der Staffel:

1. Oben rechts auf **Fork** klicken und den Fork unter deinem Konto anlegen.
2. **Deinen Fork** klonen, nicht dieses Repo:

   ```sh
   gh repo clone <dein-konto>/agentic-coding-schule-staffel-1
   ```

3. Prüfen, dass `origin` auf deinen Fork zeigt:

   ```sh
   git remote -v
   ```

   Dort muss `<dein-konto>/agentic-coding-schule-staffel-1` stehen, nicht `BoP-haeger/…`.

### 2. Die Hausaufgabe öffnen

Öffne `trail-N/index.html` lokal im Browser, zum Beispiel per Doppelklick im Dateimanager oder mit:

```sh
open trail-1/index.html        # macOS
xdg-open trail-1/index.html    # Linux
start trail-1/index.html       # Windows
```

### 3. Antworten abgeben

1. Auf der Seite `antworten.json` herunterladen.
2. Die Datei als `trail-N/antworten.json` in deinen Fork legen.
3. Committen und in **deinen Fork** pushen:

   ```sh
   git add trail-1/antworten.json
   git commit -m "Antworten Trail 1"
   git push
   ```

Du kannst die Datei bis zum Einsammeln beliebig oft überschreiben und neu pushen.

### 4. Neue Hausaufgaben holen

Nach jedem Schulungstermin kommt hier ein neuer `trail-N/`-Ordner dazu. So holst du ihn in deinen Fork:

1. Auf GitHub in deinem Fork auf **Sync fork** → **Update branch** klicken.
2. Lokal `git pull` ausführen.

Alternativ auf der Kommandozeile: `gh repo sync <dein-konto>/agentic-coding-schule-staffel-1`, danach `git pull`.

Lösche deinen Fork nicht, solange die Staffel läuft. Dort sammeln wir deine Antworten ein.

## Hinweis für Schulungsleiter und Trainer

Wer einen Teilnehmer aus diesem Repo entfernt, löscht damit auch dessen Fork. Teilnehmer also erst entfernen, wenn alle Antworten eingesammelt sind.
