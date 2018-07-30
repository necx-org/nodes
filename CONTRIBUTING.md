# Making Contributions to the Nuclear Engineering Curriculum eXchange

Contributions by all are welcome. We are thrilled that you've found yourself here.

- [Types of Contributions](#types-of-contributions)
- [Issues](#issues)
- [Making a Change](#making-a-change)
- [Creating a Node](#creating-a-node)
- [Contributor Workflow](#contributor-workflow) 
- [Review Criteria](#review-criteria)
- [Asking for Help](#asking-for-help)


## Types of Contributions

Just as contributors come in many forms (student, faculty, interested
programmer), so too do contributions. Some of the most valuable contributions
include reporting issues and requesting new features. Improvements to the
project can also take the form of minor or major fixes to existing content,
contributions to process documentation, or creating brand new nodes. 

### Issues

When you notice something wrong or a desirable feature that is missing, you can
help us by reporting it as an [issue](https://github.com/necx-org/nodes/issues) in this
repository. Perhaps you've noticed bad grammar, formatting, or malformed
content. Alternatively, perhaps you have had an idea for a nice potential
whiz-bang feature and you'd like to suggest it. Either way, the process is the
same:

1. Search the issues to determine whether an existing issue addresses your
   bug/feature already. If one appears, comment within that issue to add to the
   conversation. 
2. If no existing issue matches your needs, create one.
3. Include as many details as possible to describe the bug or desired feature. 

### Meta Changes

The NECX project relies on many processes and the documentation explaining
them. Contribution to documentation and procedures are welcome.  Lively review
and discussion of such changes can be expected, and consensus will enable
community adoption. 

In any case, the process will follow the [contributor workflow.](#contributor-workflow)

### Making a Change to a Node

Perhaps an existing node could use improvement, corrections, or new features.
Ideally, the original author of the node should be available and open for
discussion (in an issue or pull request) about how best to integrate your
changes into the node, but their permission is not necessary. Your changes will
undergo community review in the [contributor workflow](#contributor-workflow)
process. Accordingly, the node author is free to engage in the review of your
changes, but may choose not to -- and that's ok!  

In any case, the process will follow the [contributor workflow.](#contributor-workflow)

### Creating a Node 

A major effort in this project is the development of nuclear engineering
curriculum content in the form of 'nodes'. A node template appears in the
repository and the review criteria for node contributions can be found
in the [node criteria section below](#node-criteria). 


Start by copying the template node directory and work from there. Beyond that,
the process will follow the [contributor workflow.](#contributor-workflow)

## Contributor Workflow

- The terminology we use is based on the [Integrator Workflow](http://en.wikipedia.org/wiki/Integrator_workflow).
- The first step is to create your own [fork](https://help.github.com/articles/fork-a-repo/) of the project.
- Use a branching workflow similar to the one described in the [pro-git book](https://git-scm.com/book/en/v2/Git-Branching-Branching-Workflows).
- Keep your own "master" branch in sync with the mainline repository's "master"
  branch. Specifically, do not push your own commits directly to your "master"
  branch.
- Any commit should pass all tests (though no tests currently exist).
- In addition to a review of the content changes in your contribution, it will
  be reviewed on a variety of levels including such things as style,
  documentation, tests, etc. While such review can appear tedious, these aspects
  are important for the long term success of the project.
- When you are ready to move changes from one of your topic branches into the
  "master" branch, it must be reviewed and accepted by another developer.
- You may want to review [this tutorial](https://help.github.com/articles/using-pull-requests/) 
  before you make a pull request to the master branch.
- Consider [assigning a reviewer.](https://help.github.com/articles/about-pull-request-reviews/)
- Engage in the ensuing discussion and iterations while the reviewers review
  your pull request.

## Asking for Help

- The best way to ask for help is by creating an [issue](#issues). 
- However, for more dynamic discussion, join us in our Slack workspace
  [necx-org.slack.com](https://necx-org.slack.com).

# Reviews

For all reviews, the reviewer is expected to:

- Look over the contribution.
- Check that it meets our style and content guidelines.
- Make inline review comments concerning improvements.
- Wait for the Continuous Integration service to show full test passage
- When satisfied, click the green "Merge Pull Request" button

For nodes, requirements can be found in the [node 
criteria](#required-node-elements) section below.

## Required Node Elements

The following are required elements of a valid node. There are two types 
of valid nodes in the graph of nuclear engineering curriculum data, with the 
following requirements.

An internal node must have the following fields defined:
* title
* uuid
* prerequisites: list of uuids
* learning objective(s)
* assessment (at least one)

A boundary node should only define a `title` and `uuid` and may NOT define any
of the other required elements of an internal node, but may include a brief
description of what is within the scope of that node.

### Requirements for Prerequisite

Prerequisites should be specified by providing a list of correctly formed
UUIDs that refer to those prerequisites.

All prerequisites that are referred to in a given pull request must be
available in the graph once the pull request has been merged.  Therefore, all
modifications to prerequisites - whether changing preexisting prerequisites
or introducing new ones - must be either be already defined in the graph or
introduced as part of the same pull request.  A new prerequisite may be
introduced as a boundary node.

A prerequisite should be as specific as possible, though very general boundary 
nodes may be proposed as needed and will be addressed on a case-by-case basis 
during the review process until a community norm is established.

### Learning Objectives

Each of the nodes should satisfy at least one learning objective.

In order to develop learning goals, contributors should answer the question, “What
do I want my students to know or be able to do by the end of this course?”

Each objective should be specific, actionable, and observable (meaning you can 
somehow see it and record the event).
This can be done by focusing on the verbs and nouns: verbs from Blooms and nouns from your discipline. Any student who takes your 
class or learns this "thing" should know how to VERB NOUN and if they can VERB 
NOUN then they know it. For example:

"Students will be able to derive Fick's Law."

For relationships between Blooms Taxonomy and appropriate verbs, see [Blooms verbs](http://www.fresnostate.edu/academics/oie/documents/assesments/Blooms%20Level.pdf).

Three good resources on learning outcomes appear here:

- [learning outcomes assessment](https://provost.illinois.edu/assessment/learning-outcomes-assessment/what-is-learning-outcomes-assessment/)
- [course-level learning outcomes](http://teaching.berkeley.edu/resources/design/course-level-learning-goalsoutcomes)

[Bloom's taxonomy actino verbs](https://www.apu.edu/live_data/files/333/blooms_taxonomy_action_verbs.pdf)

### Formatting Assessments

Assessments may take many forms: markdown files, data, images, LaTeX
documents, standard question format files, etc, and a single unit of
assessment may include multiple related files.

Each unit of assessment should be placed in a separated subdirectory of the
node, named using a uuid-like directory name.

## Recommended Node Elements

In addition to the required node elements, many elements are recommended and
should be incorporated into the `index.md` file as links, references, or
otherwise.
 
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
- Homework problems
- Exam problems
- Quiz questions
- Other learning outcomes

