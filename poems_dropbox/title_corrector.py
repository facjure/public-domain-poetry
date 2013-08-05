from glob import glob
import re
from codecs import open


def _read_yaml(fname):
    """Splits subdir/fname into a tuple of YAML and raw content"""
    with open(fname, "r", "utf-8") as fin:
        yaml_and_raw = fin.read().split('\n---\n')
        if len(yaml_and_raw) == 1:
            return {}, yaml_and_raw[0]
        else:
            return yaml_and_raw[0] + "\n---\n", yaml_and_raw[1]


def clean_poem(textfile):
    yaml_data, text = _read_yaml(textfile)
    text = re.sub(r'\r\n?|\n', "\n", text)  # \r is Mac OSX line ending
    text = re.sub(r'\n{2,}', "\n\n", text)
    text = re.sub(r'^\s*?(.+?)\n\n', "", text)  # remove title if any
    return yaml_data + text


for txtfile in glob("done/*"):
    print txtfile
    text = clean_poem(txtfile)
    open("cleaned/" + txtfile,"w", "utf-8").write(text)

