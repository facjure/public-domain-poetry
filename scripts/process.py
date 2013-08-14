#!/usr/bin/env python
"""
Usage:
    ./process_poems.py <dropbox folder>

YAML Problems:

-> -<space>
-> \t\n
-> \s*---(.+?)---\s*\n

Poem Problems:
-> title
-> \t\n
"""
import yaml
import re
import StringIO
from glob import glob
import os
import sys
from pipes import quote
from codecs import open


def yaml_and_poem(poem_text):
    match = re.search(u"\s*---(.+?)---[ ]*\n", poem_text, flags=re.U | re.S)
    yaml = match.group(1)
    match_len = len(match.group(0))
    poem_text = poem_text[match_len:]
    return yaml, poem_text


def clean_yaml(yaml_text):
    yaml_text = re.sub(r'[ \t]+\n', "\n", yaml_text)
    yaml_text = re.sub(r'\*', "", yaml_text)
    yaml_text = re.sub(r'-(.)', r'- \1', yaml_text)
    return yaml_text


def clean_poem(text):
    text = re.sub(r'[ \t]+\n', "\n", text)
    text = re.sub(r'\r\n?|\n', "\n", text)  # \r is Mac OSX line ending
    text = re.sub(r'\n{2,}', "\n\n", text)
    text = re.sub(r'^\s*?(.+?)\n\n', "", text)  # remove title if any
    return text


def clean_name(txtfile):
    new_txtfile_name = txtfile[len('raw/'):]  # Get rid of "raw/"filename
    new_txtfile_name = re.sub(r'[\'",]', "-", new_txtfile_name)
    new_txtfile_name = re.sub(" ", "-", new_txtfile_name)
    new_txtfile_name = re.sub("-+", "-", new_txtfile_name)
    return new_txtfile_name

os.system("rm -rf raw")
os.system("cp -R " + quote(sys.argv[1]) + " raw")

os.system("rm except.log")
log = open("except.log", "a")

for txtfile in glob("raw/*"):
    print txtfile
    try:
        text = open(txtfile, "r", "utf-8").read()
        yaml_text, poem = yaml_and_poem(text)
        yaml_cleaned = clean_yaml(yaml_text)
        yaml.load(StringIO.StringIO(yaml_cleaned))
        cleaned_poem = clean_poem(poem)
        final_filename = clean_name(txtfile)
        ffh = open("processed/" + final_filename, "w", "utf-8")
        ffh.write(u"---" + yaml_cleaned + u"---\n" + cleaned_poem)
        ffh.close()
    except Exception, error:
        log.write("Error in \"" + txtfile + "\": " + str(error) + "\n")
        cmd = "cp " + quote(txtfile) + " errors/"
        print cmd
        os.system(cmd)
        continue

log.close()
