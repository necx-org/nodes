# node-tools: a set of functions useful for manipulating and querying nodes

import os
import yaml


def find_all_nodes(root_dir):
    """
    method to collect all directories in the `root_dir` and exclude a specific list

    inputs
    ------
    root_dir : root directory to walk looking for nodes

    output
    ------
    possible_nodes : set of directory names that could be nodes
    """

    ignore_dir_list = {'template-node','template-node-full'}

    possible_nodes = {name for name in os.listdir(root_dir)
                      if os.path.isdir(os.path.join(root_dir,name))}

    possible_nodes = possible_nodes.difference(ignore_dir_list)

    return possible_nodes

def get_metadata(node_dir):
    """
    method to get the metadata dictionary from an individual node

    input
    -----
    node_dir : string with adequately resolved directory name of a node

    output
    ------
    dictionary of data contained in YAML header of node `index.md` file

    OR

    None if the file doesn't exist.
    """
    
    idx_md = os.path.join(node_dir,"index.md")

    try:
        with open(idx_md, 'r') as node_file:
            return next(yaml.load_all(node_file))
    except FileNotFoundError:
        return None
    


