# Node Review Criteria

For all reviews, the reviewer is expected to:

- Look over the contribution.
- Check that it meets our style and content guidelines.
- Make inline review comments concerning improvements.
- Wait for the Continuous Integration service to show full test passage
- When satisfied, click the green "Merge Pull Request" button

For nodes, requirements can be found in the [node criteria](#node-criteria) 
section below.

## Required Node Elements

The following are required elements of a valid node. There are two types 
of valid nodes in the graph of nuclear engineering curriculum data, with the 
following requirements.

An internal node must have the following fields defined:
* title
* uuid
* prerequisites
* learning objective(s)
* assessment (at least one)

A boundary node may NOT define any of the required elements of an internal
node.

### Title requirements

The title should be:

- unique
- descriptive
- short
- uppercase

### UUID requirements

The uuid should be:

- unique
- descriptive
- short
- lowercase
- hyphenated where necessary


### Prerequisites in pull requests

All prerequisites that are referred to in a given pull request must be
available in the graph once the pull request has been merged.  Therefore, all
modifications to prerequisites - whether changing preexisting prerequisites
or introducing new ones - must be either be already defined in the graph or
introduced as part of the same pull request.  A new prerequisite may be
introduced as a boundary node.

### Learning Objectives

Each of the nodes should satisfy at least one learning objective.

In order to develop learning goals, faculty should answer the question, “What
do I want my students to know or be able to do by the end of this course?”

http://teaching.berkeley.edu/resources/design/course-level-learning-goalsoutcomes

Each objective should be specific, actionable, and observable (meaning you can 
somehow see it and record the event).
I teach this quite often and explain it as focusing on the verbs and nouns, 
verbs from Blooms and nouns from your discipline. Any student who takes your 
class or learns this "thing" should know how to VERB NOUN and if they can VERB 
NOUN then they know it. I.e. Student will be able to derive Fick's Law.
Blooms verbs: 
http://www.fresnostate.edu/academics/oie/documents/assesments/Blooms%20Level.pdf
This is a good resource: 
https://provost.illinois.edu/assessment/learning-outcomes-assessment/what-is-learning-outcomes-assessment/


## Recommended Node Elements

In addition to the required node elements, many elements are recommended and
should be incorporated into the content.md file as links, references, or
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

