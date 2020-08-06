#!/usr/bin/env python3
# Generate a new minimum viable node from the basic node template given a UUID.

# Retrieve user-specified UUID.
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('old_uuid', help='Current UUID of node.')
parser.add_argument('new_uuid', help='New UUID of node.')
args = parser.parse_args()
old_uuid = args.old_uuid
new_uuid = args.new_uuid

# Copy basic template directory over to new directory.
print('Moving node directory from ' + old_uuid + ' to ' + new_uuid + '...',end='')
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
src_path = os.path.join(dir_path,'..','content',old_uuid)
tgt_path = os.path.join(dir_path,'..','content',new_uuid)
os.rename(src_path, tgt_path)
print('done.')

# Replace old UUID with new UUID in`index.md`.
print('Populating moved node UUID...',end='')
with open(os.path.join(tgt_path,'index.md'),'r') as old_index_file:
    old_text = old_index_file.read()
new_text = old_text.replace(old_uuid,new_uuid)
with open(os.path.join(tgt_path,'index.md'),'w') as new_index_file:
    new_index_file.write(new_text)
print('done.')
