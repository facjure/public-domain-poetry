"""
Converts docx to text

Usage: python parse.py docx "./"
"""

import sys
import os
import codecs
import re
import zipfile
import base64
import uuid

import pprint

from StringIO import StringIO
from lxml import etree

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
            single_file.append("## " + elem.text + "\n")
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
        line = text_lines[idx]
        if re.search(r'##', line):
            if first_iteration:
                text += line
                first_iteration = False
                idx += 1
                continue
            else:
                uni_file = base64.urlsafe_b64encode(uuid.uuid4().bytes).rstrip('=')
# universal file name. 22chars long
# see: http://stackoverflow.com/questions/11089590/django-is-base64-of-md5-hash-of-email-address-under-30-characters
                o_fh = codecs.open(OUT_DIR + uni_file, mode="w", encoding="utf-8")
                text = re.sub(r'\n{2,}',"\n\n",text)
                text = re.sub(ur'\u2028',"\n",text)
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

