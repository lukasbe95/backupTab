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
def optionParser():

    # name of the file is still to upgrade :)
    editFile("/home/lukas/dupa")

if __name__ == '__main__':
    optionParser()
