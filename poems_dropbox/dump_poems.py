"""
Problems
yaml
-> -<space>
-> \t
-> \s*---(.+?)---\s*\n

Poem
-> title
-> \t
"""
import yaml
import random
import re
import StringIO
from glob import glob
import os
import sys
from pipes import quote
from codecs import open

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

def yaml_and_poem(poem_text):
    match  = re.search(u"\s*---(.+?)---[ ]*\n", poem_text, flags=re.U | re.S)
    yaml = match.group(1)
    match_len = len(match.group(0))
    poem_text = poem_text[match_len:]
    return yaml, poem_text

def clean_yaml(yaml_text):
    yaml_text = re.sub(r'[ \t]+\n', "\n", yaml_text)
    yaml_text = re.sub(r'\*', "", yaml_text)
    yaml_text = re.sub(r'"', " ", yaml_text)
    yaml_text = re.sub(r'-(.)', r'- \1', yaml_text)
    return yaml_text


def clean_poem(text):
    text = re.sub(r'[ \t]+\n', "\n", text)
    text = re.sub(r'\r\n?|\n', "\n", text)  # \r is Mac OSX line ending
    text = re.sub(r'\n{2,}', "\n\n", text)
    text = re.sub(r'^\s*?(.+?)\n\n', "", text)  # remove title if any
    return text

def clean_name(txtfile):
    new_txtfile_name = txtfile[len('raw/'):] # Get rid of "raw/"filename
    new_txtfile_name = re.sub(r'[\'",]', "-", new_txtfile_name)
    new_txtfile_name = re.sub(" ", "-", new_txtfile_name)
    new_txtfile_name = re.sub("-+", "-", new_txtfile_name)
    new_txtfile_name = str(random_with_N_digits(6)) + "-" + new_txtfile_name
    return new_txtfile_name

os.system("rm -rf raw")
os.system("cp -R \'" + sys.argv[1] + "\' raw")

log = open("except.log","a")

for txtfile in glob("raw/*"):
    print txtfile
    try:
        text = open(txtfile,"r", "utf-8").read()
        yaml_text, poem = yaml_and_poem(text)
        yaml_cleaned = clean_yaml(yaml_text)
        yaml.load(StringIO.StringIO(yaml_cleaned))
        cleaned_poem = clean_poem(poem)
        final_filename = clean_name(txtfile)
        ffh = open("done/" + final_filename,"w", "utf-8")
        ffh.write(u"---" + yaml_cleaned + u"---\n" + cleaned_poem)
        ffh.close()
    except Exception, error:
        log.write("Error in \"" + txtfile + "\": " + str(error) + "\n")
        cmd = "mv " + quote(txtfile) + " except/"
        print cmd
        os.system(cmd)
        continue

log.close()

