#!/usr/bin/env python3
# Generate a new minimum viable node from the basic node template given a UUID.

# Retrieve user-specified UUID.
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('uuid')
args = parser.parse_args()
if not args.uuid:
    print('Usage:  \n\tnew-node UUID\n\nwhere UUID is the name of the new node.\n\n')
    exit()
uuid = args.uuid

# Copy basic template directory over to new directory.
print('Creating new node directory...',end='')
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
src_path = os.path.join(dir_path,'..','templates/minimal-node')
tgt_path = os.path.join(dir_path,'..','content',uuid)
import shutil
shutil.copytree(src_path,tgt_path)
print('done.')

# Replace JINJA2 variable for UUID in `index.md`.
print('Populating new node UUID...',end='')
import jinja2
with open(os.path.join(tgt_path,'index.md'),'r') as old_index_file:
    old_text = old_index_file.read()
template = jinja2.Template(old_text)
new_text = template.render(uuid=uuid)
with open(os.path.join(tgt_path,'index.md'),'w') as new_index_file:
    new_index_file.write(new_text)
print('done.')
