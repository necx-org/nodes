#!/usr/bin/env python
"""Rotates keys in the keys.json file. If no file exists, it is populated."""
import os
import sys
import time
import json

from cryptography.fernet import Fernet

sys.path.insert(0, os.path.dirname(__file__))
from tools import KEYS_FILE


def make_new_entry():
    return {"key": Fernet.generate_key().decode(), "timestamp": time.time()}


def main(args=None):
    if os.path.exists(KEYS_FILE):
        with open(KEYS_FILE) as f:
            keys = json.load(f)
        while len(keys) < 3:
            keys.insert(0, make_new_entry())
        keys.sort(reverse=True, key=lambda x: x['timestamp'])
        keys = keys[:2]
    else:
        keys = [make_new_entry()]
        keys.insert(0, make_new_entry())
    with open(KEYS_FILE, 'w') as f:
        json.dump(keys, f)


if __name__ == '__main__':
    main()