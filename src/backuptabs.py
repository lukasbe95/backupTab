#!/usr/bin/python3

import os
import tempfile
import sys
import argparse
from subprocess import call
from pathlib import Path

def editFile(path):
    EDITOR = os.environ.get('EDITOR','vim')
    file = Path(path)
    if not file.exists():
        r = open(path, mode='w+')
        r.close()
    f = open(path, mode='r+', encoding="utf-8")
    initial_message = f.read()

    with tempfile.NamedTemporaryFile(suffix=".tmp") as tf:
        tf.write(initial_message.encode('ascii'))
        tf.flush()
        call([EDITOR, tf.name])
        tf.seek(0)
        edited_message = tf.read()
        f.write(edited_message.decode("utf-8"))
        f.close()
        print ("File has been updated!")
def listFile(path):
    f = open(path, mode='r')
    for line in f.readlines():
        print(line,end='')
    f.close()
def clearFile(path):
    f = open(path, mode='w')
    f.close()
    print("File is clear now.", sep=' ', end='\n', file=sys.stdout, flush=False)
def optionParser():
    parser = argparse.ArgumentParser(description='This is daemon\'s help. All options listed below!')
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-e','--edit', help='Edit tab in vim',action='store_true')
    group.add_argument('-l','--list', help='List whole tab (config file)',action='store_true')
    group.add_argument('-c','--clear', help='Delete whole tab (clear config file)',action='store_true')
    # name of the file is still to upgrade :)
    # editFile("/home/lukas/dupa")
    args = parser.parse_args()
    if args.edit:
        editFile("/home/lukas/dupa")
    elif args.list:
        listFile("/home/lukas/dupa")
    else:
        clearFile("/home/lukas/dupa")
if __name__ == '__main__':
    optionParser()
