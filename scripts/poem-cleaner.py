"""
YAML Problems:

-> -<space>
-> \t\n
-> \s*---(.+?)---\s*\n
-> :, * in data

Poem Problems:
-> title
-> \t\n
"""
import re
import os

def clean_yaml(yaml_text):
    yaml_text = re.sub(r'[ \t]+\n', "\n", yaml_text)  # No Tabs or spaces before \n 
    yaml_text = re.sub(r'\*', "", yaml_text) # some poems have '*' in meta data
    yaml_text = re.sub(r'-([^ ])', r'- \1', yaml_text) # yaml spec for lists, space before -
    return yaml_text


def clean_poem(text):
    text = re.sub(r'[ \t]+\n', "\n", text)  # No Tabs or spaces before \n
    text = re.sub(r'\r\n?|\n', "\n", text)  # \r is Mac OSX line ending
    text = re.sub(r'\n{2,}', "\n\n", text)  # At max 2 new lines
    text = re.sub(r'^\s*?(.+?)\n\n', "", text)  # remove title if any
    return text


def is_clean_name(txtfile_name):
    if re.search(r'[\'", ]', txtfile_name):
        return False
    else:
        return True

def clean_name(txtfile):
    new_txtfile_name = os.path.basename(txtfile)
    new_txtfile_name = re.sub(r'[\'",]', "-", new_txtfile_name) # substiture quotes with -
    new_txtfile_name = re.sub(" ", "-", new_txtfile_name) # substitute spaces with -
    new_txtfile_name = re.sub("-+", "-", new_txtfile_name) # replace multiple hyphens with single -
    return new_txtfile_name
