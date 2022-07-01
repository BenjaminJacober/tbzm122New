# Projekt Dokumentation

[[_TOC_]]

## Lösungsdesign
Anhand der Analyse wurde folgendes Lösungsdesign entworfen.

### Aufruf der Skripte
1. Skript
Skript kann mit Option -baseDir [PATH] und -inputFile [PATH]  aufgerufen werden, um das Base-Directory festzulegen und das Inputfile einzulesen
CronJobs müssen manuell erstellt werden

2. Skript
Das 2. Skript benötigt 2 Parameter, -outputName [FILE] für das Outputfile und -baseDir [PATH] für das Base-Directory

### Ablauf der Automation

activityDiagram.png

### Konfigurationsdateien

1. Skript
Das Inputfile hat folgendes Format:
<git_repo_url> <directory_name>

2. Skript
Keine Konfiguration

## Abgrenzungen zum Lösungsdesign

TODO: Nachdem das Programm verwirklicht wurde hier die unterschiede von der Implemenatino zum Lösungsdesign beschreiben (was wurde anders gemacht, was wurde nicht gemacht, was wurde zusaetzlich gemacht)
