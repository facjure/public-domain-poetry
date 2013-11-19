import sys
import re
import os
import string
import yaml
import StringIO
from glob import glob
from codecs import open
from pipes import quote
import random
import hashlib

poems_path = "/Users/harsha/yuti/poems-test"
success_path = poems_path + "/success/"
errors_path = poems_path + "/errors/"
dups_path = poems_path + "/dups/"

path = sys.argv[1]

def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) -1
    return random.randint(range_start, range_end)


def split_file(poem_text):
    match = re.split(u"\n---[ ]*\n", poem_text, flags=re.U | re.S)
    yaml_text = match[0]
    poem = match[1]
    return yaml_text, poem

def clean_name(name):
    punctuation_rx = re.compile('[%s]' % re.escape(string.punctuation))
    name = re.sub(punctuation_rx," ", name) # substiture punctuation with " "
    name = re.sub(" ", "-", name) # substitute spaces with
    name = re.sub("-+", "-", name) # replace multiple hyphens with single
    return name


def generate_name(title, author):
    final_author = clean_name(author)
    title_words = re.split(r'\s+', title)
    required_title = u" ".join(title_words[0:6])
    final_title = clean_name(required_title)
    final_name = final_author + "-" + final_title
    final_name = re.sub("-+", "-", final_name)
    final_name = re.sub("-$", "", final_name)
    return final_name


def move(frm, to):
    print to
    if os.path.isfile(success_path + to) or os.path.isfile(poems_path + "/" + to):
        to = errors_path + to + str(random_with_N_digits(6))
    else:
        to = success_path + to
    cmd = "mv " + quote(frm) + " " +  quote(to)
    print "#Cmd: " + cmd
#    os.system(cmd)

def rename():
    for txtfile in glob(path + os.sep + "*.txt"):
        try:
            txtfile_name = os.path.basename(txtfile)
            text = open(txtfile, "r", "utf-8").read()
            yaml_text, poem = split_file(text)
            ds = yaml.load(StringIO.StringIO(yaml_text))
            author = ds['author']
            title = ds['title']
            name = generate_name(title, author)
            final_file_name = name + ".txt"
            move(txtfile, final_file_name)

        except Exception, error:
            print "#Error: " + txtfile + " (" + str(error) + ")"
            cmd = "mv " + quote(txtfile) + " " +  quote(errors_path + txtfile_name) + str(random_with_N_digits(6))
            print "#Cmd: " + cmd
            os.system(cmd)
            continue

def duplicates():
    for txtfile in glob(errors_path + "*" ):
        try:
            txtfile_name = os.path.basename(txtfile)
            text = open(txtfile, "r", "utf-8").read()
            yaml_text, poem = split_file(text)
            ds = yaml.load(StringIO.StringIO(yaml_text))
            author = ds['author']
            title = ds['title']
            name = generate_name(title, author)
            final_file_name = name + ".txt"

            if os.path.isfile(poems_path + "/" + final_file_name):
                to = dups_path + txtfile_name
                print "#Moving To: " + to
                cmd = "mv " + quote(txtfile) + " " +  quote(to)
                print "#Cmd: " + cmd
                os.system(cmd)

        except Exception, error:
            continue

def yaml_errors():
    for txtfile in glob(errors_path + "*" ):
        try:
            txtfile_name = os.path.basename(txtfile)
            text = open(txtfile, "r", "utf-8").read()
            yaml_text, poem = split_file(text)
            ds = yaml.load(StringIO.StringIO(yaml_text))

        except Exception, error:
            print "#Error: " + txtfile + " (" + str(error) + ")"
            continue

def rename2():
    for txtfile in glob(dups_path + "*" ):
        try:
            txtfile_name = os.path.basename(txtfile)
            text = open(txtfile, "r", "utf-8").read()
            yaml_text, poem = split_file(text)
            ds = yaml.load(StringIO.StringIO(yaml_text))
            author = ds.get('author', None)
            if not author:
                author = ds.get('translator', None)
                if not author:
                    raise Exception("author")
            title = ds.get('title', None)
            if not title:
                lines = poem.split('\n')
                for line in lines:
                    if not re.match(r'^\s*$', line):
                        title = line
                        break
            name = generate_name(title, author)
            final_file_name = name + ".txt"
            move(txtfile, final_file_name)

        except Exception, error:
            print "#Error: " + txtfile + " (" + str(error) + ")"
            cmd = "mv " + quote(txtfile) + " " +  quote(errors_path + txtfile_name) + str(random_with_N_digits(6))
            print "#Cmd: " + cmd
#        os.system(cmd)
            continue

def move_success():
    for txtfile in glob(success_path + "*" ):
        txtfile_name = os.path.basename(txtfile)
        to = poems_path + "/" + txtfile_name
        if not os.path.isfile(to):
           cmd = "mv " + quote(txtfile) + " " +  quote(to)
           print "#Cmd: " + cmd
           os.system(cmd)
        else:
            print "#Dup: " + txtfile

def move_dups():
    for txtfile in glob(success_path + "*" ):
        txtfile_name = os.path.basename(txtfile)
        to = poems_path + "/" + txtfile_name
        if not os.path.isfile(to):
           cmd = "mv " + quote(txtfile) + " " +  quote(to)
           print "#Cmd: " + cmd
           os.system(cmd)
        else:
            print "#Dup: " + txtfile

def get_first_line(poem):
    lines = poem.split('\n')
    for line in lines:
        if not re.match(r'^\s*$', line):
            title = line
            break
    return title


def get_basename_yaml_and_poem(txtfile):
    txtfile_name = os.path.basename(txtfile)
    text = open(txtfile, "r", "utf-8").read()
    yaml_text, poem = split_file(text)
    ds = yaml.load(StringIO.StringIO(yaml_text))
    return (txtfile_name, ds, poem)

def rename3():
    for txtfile in glob(dups_path + "*" ):
        try:
            txtfile_name, ds, poem = get_basename_yaml_and_poem(txtfile)
            author = ds.get('author', None)
            if not author:
                author = ds.get('translator', None)
                if not author:
                    raise Exception("author")
            title = ds.get('title', None)
            if not title:
                title = get_first_line(poem)

            name = generate_name(title, author)
            final_file_name = name + ".txt"
            original_file = poems_path + "/" + final_file_name

            if os.path.isfile(original_file):
                orig_txtfile_name, orig_ds, orig_poem = get_basename_yaml_and_poem(original_file)
                orig_first_line = get_first_line(orig_poem)

                first_line = get_first_line(poem)

                if orig_first_line != first_line:
                    print "#NOT REALLY A DUPLICATE"
                    title = first_line
                    name = generate_name(title, author)
                    final_file_name = name + ".txt"
                    to = poems_path + "/" + final_file_name
                    if os.path.isfile(to):
                        print "##HUGE DUP"
                        continue
                else:
                    print "##Duplicate" + txtfile
                    continue

            else:
                print "##NOT REALLY DUP" + txtfile
            cmd = "mv " + quote(txtfile) + " " +  quote(to)
            print "#Cmd: " + cmd
            os.system(cmd)

        except Exception, error:
            print "#Error: " + txtfile + " (" + str(error) + ")"
#            cmd = "mv " + quote(txtfile) + " " +  quote(errors_path + txtfile_name) + str(random_with_N_digits(6))
#            print "#Cmd: " + cmd
#        os.system(cmd)
            continue

def md5_check():
    md5s = []
    md5s_dups = []
    for txtfile in glob(poems_path + "/*.txt" ):
        md5s.append(hashlib.md5(open(txtfile).read()).hexdigest())
    for txtfile in glob(dups_path + "*"):
        md5s_dups.append(hashlib.md5(open(txtfile).read()).hexdigest())
        md5s.append(hashlib.md5(open(txtfile).read()).hexdigest())
    print md5s + md5s_dups
    for md5 in md5s_dups:
        if md5 not in md5s:
            print "Hmmm"

md5_check()

print "Done"
