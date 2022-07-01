import argparse
import logging
import os
import shutil
from csv import reader

PARSER = argparse.ArgumentParser(description='Clones git repos')

# Required parameters
PARSER.add_argument('basedir', help='Where the directories will be cloned to')
PARSER.add_argument('inputfile', help='input csv file that contains the git repos')

parameter = PARSER.parse_args()

baseDirWithSlash = parameter.basedir

if (parameter.basedir[len(parameter.basedir) - 1] != "/"):
    baseDirWithSlash += "/"

directories = os.listdir(parameter.basedir)

inputFile = open(parameter.inputfile, newline='')
csv = reader(inputFile, delimiter=',')

# Clone and pull directories
for line in csv:
    if (len(line) == 2):
        repoName = line[1]
        repoSSH = line[0]
        repoDirectory = parameter.basedir + str(repoName)
        # Clone
        if (repoName not in directories):
            logging.info("Cloning repository")
            gitcommand = "git clone " + str(repoSSH) + " " + repoDirectory
        # Pull
        else:
            logging.info("Pulling repository")
            gitcommand = "cd " + repoDirectory + " && git pull"
        os.system(gitcommand)
        # subprocess.run(gitcommand, shell=True, check=True)
    else:
        logging.warning(
            "CSV doesn't have all fields, check documentation to see how to properly format the input file.")

# Remove directories that aren't in inputFile anymore
for dir in directories:
    for line in csv:
        if (dir not in line):
            # os.system("rm -r " + baseDirWithSlash + str(dir))
            shutil.rmtree(parameter.basedir + str(dir))
