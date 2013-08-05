import yaml
import random
import re
import StringIO
# from redis import Redis
from glob import glob
import os
import sys
from pipes import quote

if not len(sys.argv) > 1:
    print """Usage:
python sync.py <dropbox-folder>
"""

os.system("rm -rf raw")
# Copy all dropbox content
os.system("cp -R \'" + sys.argv[1] + "\' raw")

log = open("except.log","a")


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return random.randint(range_start, range_end)


def yaml_extract(poem_text):
    yaml_data = re.search(u"---(.+?)---\n", poem_text, flags=re.U | re.S).group(1)
    return yaml.load(StringIO.StringIO(yaml_data))

# poem:<id> -- String
# poem:<id>:props -- pickle

# REDIS_URL = "redis://localhost:6379"
# redis_handle = Redis.from_url(REDIS_URL)

for txtfile in glob("raw/*"):
    print txtfile
    try:
        new_txtfile_name = txtfile[len('raw/'):] # Get rid of "raw/"filename
        new_txtfile_name = re.sub(r'[\'",]', "-", new_txtfile_name)
        new_txtfile_name = re.sub(" ", "-", new_txtfile_name)
        new_txtfile_name = re.sub("-+", "-", new_txtfile_name)
        new_txtfile_name = str(random_with_N_digits(6)) + "-" + new_txtfile_name
        text = open(txtfile).read().decode('utf-8')
        metadata = yaml_extract(text)
#        metadata['fname'] = new_txtfile_name
#        for key in metadata:
#            redis_handle.hset("poem:props", key, metadata[key])
#        redis_handle.set("poem:" + new_txtfile_name,  text)
    except Exception, error:
        log.write("Error in " + txtfile + ": " + str(error) + "\n")
        cmd = "mv " + quote(txtfile) + " except/"
        print cmd
        os.system(cmd)
        continue
    cmd = "mv " + quote(txtfile) + " " + quote("done/" + new_txtfile_name)
    print cmd
    os.system(cmd)

log.close()
