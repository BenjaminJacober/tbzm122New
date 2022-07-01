import logging
import argparse
import os
import csv
import subprocess

PARSER = argparse.ArgumentParser(description='Logs git repos')

# Required parameters
PARSER.add_argument('--baseDir', help='Where the directories will be cloned to')
PARSER.add_argument('--outputFile', help='The name of the output file you want to ')

parameter = PARSER.parse_args()

baseDirWithSlash = parameter.baseDir
if (parameter.baseDir[len(parameter.baseDir) - 1] != "/"):
    baseDirWithSlash += "/"

directories = os.listdir(baseDirWithSlash)

file = baseDirWithSlash + "output/" + parameter.outputFile

# Checks if output dir exists, if not creates that directory
os.makedirs(os.path.dirname(file), exist_ok=True)

csvHeaderRow = ['Zielverzeichnis', 'Datum', 'Commit-Hash', 'Author']

with open(file, 'w', newline='\n') as csvfile:
    CSV_WRITER = csv.writer(csvfile, delimiter=',')
    CSV_WRITER.writerow(csvHeaderRow)
    for dir in directories:
        if (str(dir) != "output"):
            gitCommand = "cd " + baseDirWithSlash + str(dir) + "&& git log --date=format:%Y%m%" + "d --pretty=format:" + str(dir) + ",%" + "cd,%H,%" + "cn"
            gitOut = subprocess.check_output(gitCommand, shell=True, text=True, universal_newlines=True)

            newLineCharacter = gitOut.split("\n")
            for line in newLineCharacter:
                out = line.split(",")
                CSV_WRITER.writerow(out)
