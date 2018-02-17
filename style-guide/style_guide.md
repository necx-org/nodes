# Node Syntax Reference and Style Guide

This document serves as the official reference for the structure of a node as
well as a style guide for filling that structure.

## Node

The fundamental unit of the Nuclear Engineering Curriculum Exchange is a
"Node".  Two types of nodes are defined:

* Interior nodes contain the bulk of the contained in the exchange
* Boundary nodes define prerequisite material that is not included in the exchnage

The two node types are distinguished by which metadata (see below) appears in
the file.

### Node Syntax

Each node is in its own directory with a name identical to its uuid (see
below).  That directory must contain a file called `index.md` .  All interior
nodes must also contain a sub-directory called `assessments`.

#### Syntax of `index.md` file

The `index.md` file is a markdown file with YAML-formatted metadata at the
top, delimited with `---`, followed by content to be rendered as part of the
fundamental definition of the node.

##### Metadata

For a complete description of YAML formatting for metadata, see
[the YAML specification](http://www.yaml.org/spec/1.2/spec.html).  This
section defines specific metadata and its meaning.

**Required Metadata**

Everynode is required to have the following metadata:

* _title_: A human readable title for the node

  e.g. `title: A NECX Node Template`

* _uuid_ : A unique universal identifier formatted as words joined with
  hyphens, and often similar to the title

  e.g. `uuid: necx-node-template`

**Required Metadata for Internal Nodes**

The following metadata are required for all internal nodes, and its presence
identifies the node as an internal node rather than a boundary node.

* _prerequisites_: A list of node uuids that are considered prerequisite
  knowledge for this node.

e.g.
```
prerequisites:
    - other-content
    - another-node
```

* _learning objective_: A phrase indicating the learning objective of the
node.  Each node is expected to have a single learning objective.

e.g.
```
learning objective:
   construct a node with the correct syntax and contents
```

* _assessments_: A list of assessment activities that allow a student to
  demonstrate their compitency with the learning objective.  Each assessment
  is stored in a separate subdirectory within he `assessments` subdirectory.
  The name of that subdirectory should be a uid, but only unique within this
  node.  The entries in the metadata list are the uid subdirector names.

e.g.
```
assessments:
  - a-multiple-choice-question
  - a-notebook-problem
  - write-an-essay
```

#### Content
Content files for each node contain the lecture material for the subject matter. See the documentation for node requirements. The content file should be named 'content.md' and be a pure markdown file, so that it can be rendered into different formats. 

Syntax for the file should adhere to the following guidelines:
1. No html tags
2. Use latex tags for equations; i.e., $e^{-\lambda t}$ or $$e^{-\lambda t}$$
3. Images should be stored in an img subdirectory within the parent node directory

#### Exercises

