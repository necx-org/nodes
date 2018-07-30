# node-tools: a set of functions useful for manipulating and querying nodes

import os
import yaml


def find_all_nodes(root_dir):

    ignore_dir_list = {'template-node','style-guide','.git', 'bin'}

    possible_nodes = {name for name in os.listdir(root_dir)
                      if os.path.isdir(os.path.join(root_dir,name))}

    possible_nodes = possible_nodes.difference(ignore_dir_list)

    return possible_nodes

def get_metadata(node_dir):

    idx_md = os.path.join(node_dir,"index.md")

    try:
        with open(idx_md, 'r') as node_file:
            return next(yaml.load_all(node_file))
    except FileNotFoundError:
        return None
    


