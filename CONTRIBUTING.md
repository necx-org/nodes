# Making Contributions to the Nuclear Engineering Curriculum eXchange

Contributions by all are welcome - complete documentation is forthcoming ....

## Requirements of a valid node

There are two types of valid nodes in the graph of nuclear engineering
curriculum data, with the following requirements.

An internal node must have the following fields defined:
* prerequisites
* learning objective
* assessment (at least one)

A boundary node may NOT define any of the required elements of an internal
node.

## Prerequisites in pull requests

All prerequisites that are referred to in a given pull request must be
available in the graph once the pull request has been merged.  Therefore, all
modifications to prerequisites - whether changing preexisting prerequisities
or introducing new ones - must be either be already defined in the graph or
introduced as part of the same pull request.  A new prerequisite may be
introduced as a boundary node.
