# NECX: Nuclear Engineering Curriculum eXchange

The Nuclear Engineering Curriculum eXchange (NECX) is a open repository for
nuclear engineering curriculum materials intentionally prepared for reuse,
remixing and rejeuvination.

Materials are bundled in small units called "Nodes", each of which is required
to contain:
* a title
* a unique short title (UID)
* a list of prerequisites based on the UIDs of other nodes
* learning objectives
* a content summary
* at least one assessment object

A node may also contain:
* course notes including equations
* example source code
* citations of other work
* external readings
* instructor guidance
* graphics
* videos (or links to video content)
* audio files (or links to audio content)
* worked example problems
* reference to ABET a-k objectives
* active learning activities, including:
    * demonstrations
    * code completion exercises
    * think pair share questions
    * etc
* additional assessment objects

# Governance

NECX is a community goverened effort according to a set of philosophies and
policies to be fully developed in the near future. ([#20][i20])


## Repository Layout

* exchange: this is the repository of nodes, one per directory, named as the
  UID of the node
* tools: this is a growing set of tools that allow for node data to be
  convert and render the node information in different forms ([#16][i16])
* docs: documentation about preparing a node and using the tools
* ci: configuration files and scripts for managing automated validation of nodes

[i16]: https://github.com/necx-org/necx/issues/16
[i20]: https://github.com/necx-org/necx/issues/20
