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
    parser.add_argument("-n", "--node", type=str,
                        help="node to test if not all nodes")
    parser.add_argument("-d", "--skip_deps", action='store_false', dest='check_deps',
                        default=True, help="avoid checking dependencies")
    parser.add_argument("-s", "--skip_syntax", action='store_false', dest='check_syntax',
                        default=True, help="avoid checking syntax")

    return parser.parse_args()


if __name__ == "__main__":

    args = parse_input()

    valid_uuid_set, invalid_uuid_set = find_all_nodes_with_valid_uuid(args.root)

    children = {}
    parents = {}
    for node in valid_uuid_set:
        print(node)
        chilrden[node] = node_tools.get_metadata(os.path.join(root_dir,node))['prerequisites']
        print(children[node])
        for child in children[node]:
            parents.setdefault(child,[]).append(node)
        

    print(parents)
    print(children)
            

    


