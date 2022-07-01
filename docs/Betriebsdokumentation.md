# Betriebsdokumentation
[[_TOC_]]
## Einführungstext 

1. Skript: Klonen und Updaten (falls schon vorhanden) von Repos
2. Logfile (csv) erstellen von einem User-definierten Base-Verzeichnis (enthält Repos) von Commits

## Installationsanleitung für Administratoren

### Installation

Klonen von Repo und ausführen der .py dateien per python3 SKRIPTNAME.py

### Konfiguration

coneGit.config muss im gleichen Verzeichnis wie das Skript sein und die URL des Repos und den Branch beeinhalten
Falls config nicht gefunden wird ein Error geworfen.

Cronjob kann wie bei LB1 erstellt werden indem dort das Skript angepasst wird

Keine User-Home-Templates

....

## Bediensanleitung Benutzer

Keine Input files nötig ausser der Config

Skriptaufruf durch navigieren zum Skriptverzeichnis per Konsole und ausführen wie bei "Installation" beschrieben

Erzeugte Files: Logfile

Logfile wird im gleichen Verzeichnis wie das Skript gespeichert

