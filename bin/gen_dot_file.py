#!/usr/bin/env python3

import os
import argparse

import node_tools

def dirname_matches_uuid(root_dir,node):
    """
    method to check whether or not the `uuid` in the `index.md` file
    matches the name of the directory.

    inputs
    ------
    root_dir : root directory of all nodes
    node : directory name of the node to be tested

    outputs
    -------
    boolean: 
        True if uuid and diretory name match
        False if uuid and directory don't match, or uuid is not in metadata, or there is no metadata
    """

    # exception handling will catch multiple failure modes:
    #  - metadata doesn't exist
    #  - meatdata doesn't have `uuid` as a key
    try:
        metadata = node_tools.get_metadata(os.path.join(root_dir,node))
        if metadata['uuid'] == node:
            return True
        else:
            return False
    except:
        return False

def find_all_nodes_with_valid_uuid(root_dir):
    """
    metehod to find all nodes in the root dir and test whether their uuid
    matches their dirname

    inputs
    ------
    root_dir: root directory containing all the nodes


    outputs
    -------
    valid_uuid_set : set of nodes for which the uuid matches the dirname
    invalid_uuid_set : set of dirnames that could be nodes but it doesn't meet minimal requirements
    """
    
    possible_nodes = node_tools.find_all_nodes(root_dir)

    valid_uuid_set = {}
    valid_uuid_set = {node for node in possible_nodes if dirname_matches_uuid(root_dir,node) }

    invalid_uuid_set = possible_nodes.difference(valid_uuid_set)
    
    return valid_uuid_set, invalid_uuid_set






def parse_input():
    """
    setup and parse cmd line input

    inputs
    ------
    none

    outputs
    -------
    argparse object
    """
    
    parser = argparse.ArgumentParser()

    parser.add_argument("-r", "--root", type=str, default=os.getcwd(),
                        help="root directory for node list")

    return parser.parse_args()

# define some colors and formatting
bgcolor = "#bbbbbb"      # light gray
node_default = "#000000" # black
edge_default = "#009900" # medium green
missing_dep = {'bg': "#aa0000",  # deep red
               'fontcolor' : "#ffffff"} # white

header = 'digraph necx {{\n bgcolor="{0}" node [ color="{1}" ] edge [ color="{2}" ] \n\n'.format(bgcolor,node_default,edge_default)


if __name__ == "__main__":

    args = parse_input()

    valid_uuid_set, invalid_uuid_set = find_all_nodes_with_valid_uuid(args.root)

    nodelist = ""
    edgelist = ""
    for node in valid_uuid_set:
        children = node_tools.get_metadata(os.path.join(args.root,node))['prerequisites']
        for child in children:
            if child not in valid_uuid_set:
                nodelist += '"{0}" [ color="{1}" style=filled fontcolor="{2}" ]\n'.format(child,missing_dep['bg'],missing_dep['fontcolor'])
            edgelist += '"{0}" -> "{1}" ;\n'.format(child,node)

            
    print(header,nodelist,"\n",edgelist,"}")
    
            

    


