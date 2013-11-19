#!/usr/bin/env python
"""
Usage:
    process scripts/process.py

Assumptions
1) Always run from poetics directory
2) virtual env for frozen-pie in in the same folder as frozen pie
3) paths are hardcoded
"""

poetics_path = "/Users/harsha/yuti/poetics"
frozen_pie_path = "/Users/harsha/yuti/frozen-pie-latest"
poems_path = "/Users/harsha/yuti/poems"
errors_path = poems_path + "/errors"
github_url = "git@github.com:Facjure/poetics.git"

# get latest poems if any
import os
cmd = "cd " + poems_path + "; git pull origin master"
os.system(cmd)

os.system("rm except.log.md")
log = open("except.log.md", "a")

import sys
import re
import yaml
import StringIO
from glob import glob
from pipes import quote
from codecs import open
from datetime import datetime
from dateutil import tz

import cleaners

def split_file(poem_text):
    match = re.split(u"\n---[ ]*\n", poem_text, flags=re.U | re.S)
    yaml_text = match[0]
    poem = match[1]
    return yaml_text, poem

print """Processing poems"""

for txtfile in glob(poems_path + os.sep + "*.txt"):
    try:
        txtfile_name = os.path.basename(txtfile)
        if not cleaners.is_clean_name(txtfile_name):
            raise Exception("Filenames should have hyphens only. \"<authorLastName>-<first-five-words-of-title>.txt\". Use - for all special characters.")
        text = open(txtfile, "r", "utf-8").read()
        yaml_text, poem = split_file(text)
        if len(poem) < 10:
            raise Exception("Fault in process.py or Poem is too small")
        yaml.load(StringIO.StringIO(yaml_text))
    except Exception, error:
        log.write("#### Error in \"" + txtfile + "\"\n" + str(error) + "\n\n")
        cmd = "mv " + quote(txtfile) + " " +  quote(errors_path)
        print "    " + cmd
        os.system(cmd)
        continue

print "Done"


log.close()
log = open("except.log.md", "r")
if len(log.readlines()) > 2:
    log.close()

    utc = datetime.utcnow()
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/New_York')
    utc = utc.replace(tzinfo=from_zone)
    boston_time = utc.astimezone(to_zone)
    print str(boston_time)

    cmd = "mv except.log.md " + quote(errors_path + os.sep + "except.log.BostonTime." + str(boston_time) + ".md")
    print "    " + cmd
    os.system(cmd)

    os.chdir(poems_path)
    os.system("git add -A; git commit -m 'BuildBot " + str(boston_time) + "'")
    os.system("git push origin master")
    os.chdir(frozen_pie_path)
    os.system("./env/bin/python bake.py --config " + poetics_path + os.sep + "config.yml")
    os.chdir(poetics_path)
    os.system("mkdir deploy")
    os.system("mv .build/index.html deploy/")
    os.system("rm -rf .build")
    os.system("git clone -b gh-pages " + github_url + " .build")
    os.system("cp deploy/index.html .build/")
    os.system("cd .build; git add index.html; git commit -m 'new deploy " + str(boston_time) + "'; git push --force origin gh-pages")



