# Node Syntax Reference and Style Guide

This document serves as the official reference for the structure of a node as
well as a style guide for filling that structure.

## Node

The fundamental unit of the Nuclear Engineering Curriculum Exchange is a
"Node".  Two types of nodes are defined:

* Interior nodes contain the bulk of the contained in the exchange
* Boundary nodes define prerequisite material that is not included in the exchnage

The two node types are distinguished by which [metadata][#metadata] appears in
the file.

Each node is in its own directory with a name identical to its uuid (see
below).  That directory must contain a file called `index.md`.  All interior
nodes must also contain a sub-directory called
[`assessments`](assessment-formats.md).

Each node may contain [other elements](#additional-elements), either as
optional metadata or additional files linked from the `index.md` file.

## Syntax of `index.md` file

The `index.md` file is a markdown file with YAML-formatted metadata at the
top, delimited with `---`, followed by [content](#content) that serves as
instructor notes for the node.

### Metadata

For a complete description of YAML formatting for metadata, see
[the YAML specification](http://www.yaml.org/spec/1.2/spec.html).  This
section defines specific metadata and its meaning.  The metadata components
may appear in any order.

#### Required Metadata

Everynode is required to have the following metadata:

* _title_: A human readable title for the node.  Titles should be unique,
  descriptive, short, and capitalized.

  e.g. `title: A NECX Node Template`

* _uuid_ : A unique universal identifier formatted as words joined with
  hyphens, and often similar to the title.  UUIDs should be unique,
  descriptive, short, and lowercase.

  e.g. `uuid: necx-node-template`

#### Required Metadata for Internal Nodes

The following metadata are required for all internal nodes, and its presence
identifies the node as an internal node rather than a boundary node.

* _learning objective_: A phrase indicating the learning objective of the
  node.  Each node is expected to have a single learning objective.

  e.g.
```
learning objective:
   construct a node with the correct syntax and contents
```

* _prerequisites_: A list of node uuids that are considered prerequisite
  knowledge for this node.  All prerequisites must be present in the exchange,
  whether as other interior nodes or as boundary nodes.

  e.g.
```
prerequisites:
    - other-content
    - another-node
```

* _assessments_: A list of assessment activities that allow a student to
  demonstrate their compitency with the learning objective.  Each assessment
  is stored in a separate subdirectory within he `assessments` subdirectory.
  The name of that subdirectory should be a uid, but only unique within this
  node.  The entries in the metadata list are the uid subdirector names.
  There must be at least one assessment.  Individual assessments may take on
  [many formats](assessement-formats.md).

  e.g.
```
assessments:
  - a-multiple-choice-question
  - a-notebook-problem
  - write-an-essay
```

### Content

Markdown formatted content files for each node contain the lecture
material/instructor notes for the subject matter.

Syntax for the file should adhere to the following guidelines:
1. No html tags
2. Use latex tags for equations; i.e., $e^{-\lambda t}$ or $$e^{-\lambda t}$$
3. Images should be stored in an `img` subdirectory within the parent node directory


## Additional Elements

In addition to the required node elements, many elements are recommended and
should be incorporated into the `index.md` file as metadata, links,
references, or otherwise.

- Text, equations
- Example code
- References
- External readings
- Instructor guidance
- Graphics
- Videos
- Audio files
- Worked Examples
- List of ABET a-k objectives supported
- Active Learning activities
- Demonstration
- Code completion exercises
- Think pair share questions
- Other learning outcomes
