"""converts docx to text"""

import sys
import os
import codecs
import re
from docx import *
import base64
import uuid

sys.stdout = codecs.getwriter('utf-8')(sys.stdout)

IN_DIR = "./docx/"
OUT_DIR = "./docx-to-text/"

for f in os.listdir(IN_DIR):
    fh = opendocx(IN_DIR + f) # get file handle
    text = getdocumenttext(fh) # Office-XML -> text
    uni_file = base64.urlsafe_b64encode(uuid.uuid4().bytes).rstrip('=')
    # universal file name. 22chars long
    # see: http://stackoverflow.com/questions/11089590/django-is-base64-of-md5-hash-of-email-address-under-30-characters
    
    o_fh = codecs.open(OUT_DIR + uni_file, mode="w", encoding="utf-8")
    # Word 2007+ uses utf-8 by default.
    for l in text:
        o_fh.write(l + "\n")
