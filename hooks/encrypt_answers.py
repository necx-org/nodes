#!/usr/bin/env python
"""Encrypt answers"""
import os
import sys
import json

from cryptography.fernet import Fernet, MultiFernet

sys.path.insert(0, os.path.dirname(__file__))
from tools import KEYS_FILE, find_answers, encrypted_answer_filenames



def main(args=None):
    if not os.path.exists(KEYS_FILE):
        print('keys.json does not exist, skipping answer encryption',
              file=sys.stderr)
        return
    with open(KEYS_FILE) as f:
        keys = json.load(f)
    key0 = keys[0]["key"].encode()
    key1 = keys[1]["key"].encode()
    fernets = [Fernet(key0), Fernet(key1)]
    cipher = MultiFernet(fernets)
    # discover which answers need to be (re-)encrypted
    answers = encrypted_answer_filenames(abspath=True)
    sha256s, encs = encrypted_answer_filenames(answers)
    dirty = []
    for answer, sha256sum, enc in zip(answers, sha256s, enc):
        if not os.path.isfile(sha256sum) or not os.path.isfile(enc):
            dirty.append(answer)
             continue
        with open(answer, 'rb') as f:
            contents = f.read()



if __name__ == '__main__':
    main()