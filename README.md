# NECX: Nuclear Engineering Curriculum eXchange

The Nuclear Engineering Curriculum eXchange (NECX) is an open repository for
nuclear engineering curriculum materials intentionally prepared for reuse,
remixing and rejeuvination.

This repository contains only the nodes and their content.  For more
information, please see [the full documentation](http://necx-org.github.io/).

Contributions by all are welcomed!  In addition to detailed guidance, you can
also review this [brief guide](CONTRIBUTING.md).

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
* reference to [ABET General Criterion 3. Student Outcomes - a-k objectives](http://www.abet.org/accreditation/accreditation-criteria/criteria-for-accrediting-engineering-programs-2016-2017/#outcomes)
* active learning activities, including:
    * demonstrations
    * code completion exercises
    * think pair share questions
    * etc
* additional assessment objects

## Rendering nodes

Experimental support for rendering nodes exists as part of the NEC-X website rendering repository, github.com/necx-org/necx-org.github.io.

These instructions are a rough guide and your mileage may vary:

1. clone your own copy of [the website repo](https://github.com/necx-org/necx-org.github.io)
1. change to the top-level directory for that repo
1. initialize the `_nodes` submodule with `git submodule init`
1. update the `_nodes` submodule with `git submodule update`
1. run a `jekyll serve` instance and look at http://localhost:4000/nodes/

To review changes to nodes

1. go to the `_nodes` directory
1. checkout a branch that has the changes you are interested in reviewing
  * you may want/need to add another git remote to fetch those changes
1. restart the jekyll server and look at http://localhost:4000/nodes/


