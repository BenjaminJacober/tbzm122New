# Betriebsdokumentation
[[_TOC_]]
## Einführungstext 

1. Skript: Klonen und Updaten (falls schon vorhanden) von Repos
2. Logfile (csv) erstellen von einem User-definierten Base-Verzeichnis (enthält Repos) von Commits

## Installationsanleitung für Administratoren

### Installation

Klonen von Repo und ausführen der .py dateien per python3 SKRIPTNAME.py

```git clone git@github.com:BenjaminJacober/tbzm122New.git```

```python3 clone_repos.py```

```python3 log_repos.py```

Install at least python 3.8

```sudo apt-get install python3.8```

### Konfiguration



## Bediensanleitung Benutzer

1. Repo klonen

```https://github.com/BenjaminJacober/tbzm122New```

2. Input File anpassen (```inputFile.csv```)

3. Skripte nach belieben ausführen


```python3 log_repos.py --baseDir TestFolder --outputFile outputFile.csv```

```python3 clone_repos.py --baseDir TestFolder --inputFile inputfile.csv```
