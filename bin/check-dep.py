#!/usr/bin/env python3
# Check the dependencies of all nodes in the tree, or specific nodes

import argparse
import os

import node_tools

# import pdb


def dirname_matches_uuid(root_dir, node):
    """
    method to check whether or not the `uuid` in the `index.md` file
    matches the name of the directory.

    inputs
    ------
    root_dir : root directory of all nodes
    node : directory name of the node to be tested

    outputs
    -------
    boolean: True if uuid and diretory name match
        False if uuid and directory don't match, or uuid is not in
        metadata, or there is no metadata
    """

    # exception handling will catch multiple failure modes:
    #  - metadata doesn't exist
    #  - meatdata doesn't have `uuid` as a key
    try:
        metadata = node_tools.get_metadata(os.path.join(root_dir,
                                                        node))
        if metadata['uuid'] == node:
            return True
        else:
            return False
    except:
        return False


def find_all_nodes_with_valid_uuid(root_dir):
    """
    method to find all nodes in the root dir and test whether their uuid
    matches their dirname

    inputs
    ------
    root_dir: root directory containing all the nodes


    outputs
    -------
    valid_uuid_set : set of nodes for which the uuid matches the dirname
    invalid_uuid_set : set of dirnames that could be nodes but it doesn't meet
    minimal requirements
    """

    possible_nodes = node_tools.find_all_nodes(root_dir)

    valid_uuid_set = {}
    valid_uuid_set = {node for node in possible_nodes if
                      dirname_matches_uuid(root_dir, node)}

    invalid_uuid_set = possible_nodes.difference(valid_uuid_set)

    return valid_uuid_set, invalid_uuid_set


def check_deps(node_dir, valid_set):
    """
    method to check whether the dependencies of an individual node exist in the
    valid set of nodes

    inputs
    ------
    node_dir : a valid node directory to test
    valid_set : a set of nodes that have valid/matching uuid/dirnames

    output
    ------
    boolean: True if the node has prerequisites and if they exist in the set of
                      minimally valid nodes
             False if the node has no prerequisites, or they don't exist in the
                      set of minimally valid nodes
    """

    metadata = node_tools.get_metadata(node_dir)

    # exception handling will catch multiple failure modes:
    # metadata doesn't exist
    # metadata doesn't have `prerequisites` as a key
    try:
        for prereq in metadata['prerequisites']:
            if prereq not in valid_set:
                return False
    except:
        return False

    return True


def check_all_deps(root_dir, check_nodes, valid_uuid_set):
    """
    method to check a set of possible nodes for their dependencies

    inputs
    ------
    root_dir : root directory of nodes
    check_nodes : set of nodes to check
    valid_uuid_set : set of minimally valid nodes

    outputs
    -------
    missing_prereqs : set of nodes that do not have valid prereqs
    """

    missing_prereqs = set()
    for node in check_nodes:
        if not check_deps(os.path.join(args.root, node), valid_uuid_set):
            missing_prereqs.add(node)

    return missing_prereqs


def parse_input():
    """
    set up and parse cmd line input

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
    parser.add_argument("-n", "--node", nargs='+', type=str,
                        help="node to test if not all nodes")
    parser.add_argument("-d", "--skip_deps", action='store_false',
                        dest='check_deps', default=True,
                        help="avoid checking dependencies")
    parser.add_argument("-s", "--skip_syntax", action='store_false',
                        dest='check_syntax',
                        default=True, help="avoid checking syntax")

    return parser.parse_args()


if __name__ == "__main__":
    args = parse_input()

    valid_uuid_set, invalid_uuid_set = find_all_nodes_with_valid_uuid(args.root)

    check_nodes = set(valid_uuid_set)

    if args.node:
        check_nodes = check_nodes.intersection(args.node)

    print("checking nodes: ", check_nodes)

    missing_prereqs = check_all_deps(args.root, check_nodes, valid_uuid_set)

    check_nodes = check_nodes.difference(missing_prereqs)

    print("valid nodes: ", valid_uuid_set)
    print("invalid nodes: ", invalid_uuid_set)
    print("tested nodes with valid deps: ", check_nodes if check_nodes else
          None)
    print("tested nodes with missing deps: ", missing_prereqs)
