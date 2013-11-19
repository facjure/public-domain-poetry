import boto
import boto.s3
from boto.s3.key import Key
import os
import sys
from datetime import datetime
from dateutil import tz
from tempfile import mkstemp
from shutil import move
from os import remove, close
from glob import glob

AWS_ACCESS_KEY_ID = 'CHANGE-ME'
AWS_SECRET_ACCESS_KEY = 'CHANGE-ME'
BUCKET_NAME = 'CHANGE-ME'
CONN = boto.connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
BUCKET = CONN.create_bucket(BUCKET_NAME, location=boto.s3.connection.Location.DEFAULT)

# Change path accordingly

POEMS_PATH = "/home/priyatam/github/poems"
FROZEN_PIE_PATH = "/home/priyatam/github/frozen-pie/pie"
POETROID_PATH = "/home/priyatam/github/poetroid"
CONFIG = "client" + os.sep + "config.build.yml"
LOG_FILE = "/home/priyatam/github/poetroid/scripts/build.log"
INDEX_HTML = "client" + os.sep + ".build" + os.sep + "index.html"
JS_DIR = "client" + os.sep + "js"

def update_yaml():

    #Create temp file
    fh, abs_path = mkstemp()
    new_file = open(abs_path,'w')
    old_file = open(CONFIG)

    for line in old_file:
        build = re.match(r'build: (\d+)\n$')
        if build:
            no = build.group(1)
            no= str(int(no) + 1)
            line = 'build: %s\n' % no
        new_file.write(line)

    # close temp file
    new_file.flush()
    os.fsync(new_file.fileno())
    new_file.close()
    old_file.close()

    # Atomic Rename
    os.rename(abs_path, CONFIG)

def build():
    utc = datetime.utcnow()
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('America/Los_Angeles')
    utc = utc.replace(tzinfo=from_zone)
    la_time = utc.astimezone(to_zone)

    os.chdir(POETROID_PATH)
    os.system("git pull origin master")
    os.chdir(POEMS_PATH)
    os.system("git pull origin master")
    os.chdir(FROZEN_PIE_PATH)
    os.system("../env/bin/python pie.py --config " + POETROID_PATH + os.sep + CONFIG)
    os.chdir(POETROID_PATH)

    print 'Uploading %s to Amazon S3 bucket %s' % (INDEX_HTML, BUCKET_NAME)

    k = Key(BUCKET)
    k.key = 'index.html'
    k.set_contents_from_filename(INDEX_HTML)

    for jsfile in glob(JS_DIR + os.sep + "*.js"):
        k = Key(BUCKET)
        filename = os.path.basename(jsfile)
        k.key = filename
        k.set_contents_from_filename(jsfile)

    update_yaml()

    deploy_time = 'Deployed at ' + str(la_time) + "\n"
    with open(LOG_FILE, "a") as mylog:
        mylog.write(deploy_time)

    return deploy_time

if __name__ == '__main__':
    build()
