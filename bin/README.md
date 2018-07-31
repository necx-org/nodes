# Tools for Managing Curriculum Exchange Nodes

This directory contains a number of useful tools for use in the management of
nodes.

## node_tools.py

This is a module of useful functions for accessing and nodes and their
metadata.  It is intended to be imported into other scripts.

## new-node.py

This is a tool for generating a new node in the correct location, with a
`uuid` of the users choosing.  All necessary metadata that is derived from
that `uuid` will be correctly set.

## check-dep.py

This is a tool for testing which nodes have all of their dependencies defined
within the curriculum exchange.

## gen_dot_file.py

This is a tool to scan the full curriculum exchange and generate an input file
for the Graphvis DOT tool, that can then be used to generate a network graph
of the exchange.

```
%> python bin/gen_dot_file.py -r content > necx.dot

%> dot -Tpng necx.dot
```

