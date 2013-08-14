"""
Converts docx to text

Usage: python parse.py docx "./"
"""

import sys
import os
import codecs
import re
import zipfile
import random
import markdown
import urllib

import pprint

from StringIO import StringIO
from lxml import etree

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)
pp = pprint.PrettyPrinter(indent=4)

IN_DIR = sys.argv[1]
OUT_DIR = sys.argv[2]

def opendocx(file_name):
    mydoc = zipfile.ZipFile(file_name)
    xmlcontent = mydoc.read('word/document.xml')
    return xmlcontent

def getdocumenttext(xmlcontent):
    context = etree.iterparse(StringIO(xmlcontent), events=("start","end"))
    single_file = []

    grab_next_t = False

    for action, elem in context:
        if action == "end" and re.search(r'\}p$', elem.tag):
            grab_next_t = False
            single_file.append("\n")
        if action == "end" and re.search(r'\}b$', elem.tag):
            grab_next_t = True
            continue
        if action == "end" and grab_next_t == True and re.search(r'\}t$', elem.tag):
            single_file.append("title: " + elem.text + "\n")
            grab_next_t = False
            continue
        if action == "end" and re.search(r'\}t$', elem.tag):
            single_file.append(elem.text)

    return single_file

for file_name in os.listdir(IN_DIR):
    xmlcontent = opendocx(IN_DIR + "/" + file_name)
    text_lines = getdocumenttext(xmlcontent)

    text = ""
    first_iteration = True

    idx = 0

    while idx < len(text_lines):
        print idx
        line = text_lines[idx]
        if re.search(r'^title:', line):
            if first_iteration:
                text += line
                first_iteration = False
                idx += 1
                continue
            else:
                text = re.sub(ur'\u2028', "\n",text)
                text = re.sub(ur'\u2019', "'",text)
                uni_id = random_with_N_digits(6)
                md = markdown.Markdown(extensions=['meta', 'nl2br'], output_format="html5")
                md.convert(text)
                title = md.Meta["title"][0]
                title = urllib.quote(re.sub(r' ','-', title.lower()))
                uni_file = str(uni_id) + "-" + title
                print uni_file
                o_fh = codecs.open(OUT_DIR + uni_file, mode="w", encoding="utf-8")
                o_fh.write(text)
                text = line
                ixs = [0]
                for ix in range(1,5):
                    next_header_line = text_lines[idx + ix]
                    if re.search(r'##', next_header_line):
                        text += next_header_line
                        ixs.append(ix)
                idx += max(ixs) + 1
        else:
            text += line
            idx += 1

