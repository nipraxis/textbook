# Projects

We designed this class to teach you:

- the ideas and practice of functional MRI analysis;
- how to work efficiently with your computer;
- how to collaborate with code and analysis;
- making your work reproducible.

During the class you'll see us put a constant emphasis on collaboration for
learning and for increasing the quality of your work.

The best way to learn this, is with a substantial shared project.  So, a major
part of this class is the final project.

## A group project

Because we want you to learn how to share work, the projects should be in
groups of 2 or 3.  Please agree your projects and mentors in discussion with
the others in the class.

## Choosing a project

The project should be an open-ended exploration and analysis of functional MRI
data on multiple subjects.

A typical example would be to for you to explore a dataset, replicate a
previous analysis, and extend the previous analysis. For example, you might:

- take an [OpenFMRI] dataset;
- investigate the data for outliers and sources of noise;
- attempt to replicate the original analysis of the data;
- explore the assumptions of the original analysis and whether these
  assumptions and met;
- explore other analyses of the data to test new hypotheses.

(project-examples)=

## Examples

For examples of projects in a previous class, please see
<https://github.com/berkeley-stat159>, in particular:

- <https://github.com/berkeley-stat159/project-alpha>
- <https://github.com/berkeley-stat159/project-beta>
- <https://github.com/berkeley-stat159/project-epsilon>

You'll notice that these analysis are fully reproducible {{ -- }} the students had
to provide instructions that their graders could follow to reproduce their
whole analysis, including their project figures.

## Project data

Your project must be reproducible.  That means, that we, your graders, must be
able to get the raw data for your project onto our own computers, and run your
analysis on this data.

We strongly prefer that the data that you use be available to anyone who
agrees to license for the data.  For example, all the [OpenFMRI] datasets have
a liberal license ([PDDL 1.0]) allowing re-use and redistribution of the
data.

## Submission

As for the {ref}`project-examples`, you should submit the final version of
your project as a [github] [git] repository.

The project should have a `README` file that gives an introduction to the
project, and lists the steps that your readers should follow in order to get
the data, and run your analysis.

Your repository should also contain the information necessary to build your
final project report, including the figures.

## Recommended datasets

You will get the most benefit if you are working on data that you and your
mentor find interesting.  Here are some datasets selected from the OpenFMRI
catalogue that you might consider exploring:

- [ds005]: The neural basis of loss aversion in decision making under risk;
- [ds009]: The generality of self-control;
- [ds105]: Distributed and overlapping representations of faces and objects in
  ventral temporal cortex.  This is a very well-studied dataset from a famous
  2001 paper by Haxby *et al*.  The advantage to you is there are several
  tutorials for analyzing this dataset on the web.  The disadvantage is that
  you will have to do more on this dataset to uncover new information;
- [ds113]: A high-resolution 7-Tesla fMRI dataset from complex natural
  stimulation with an audio movie;
- [ds115]: Working memory in healthy and schizophrenic individuals.

## Mentors

A major part of collaboration is learning to learn from your more experienced
peers.  We are expecting that they, like us, will learn from you.

Each project will have a mentor with experience of functional FMRI analysis.
See {doc}`mentors` for the instructions we give to the project mentors.

Of most use to you will be to find a mentor that you will work with later in
your Berkeley career.  If you have an idea which lab you will be working with
after this course, please try and find a mentor from that lab.  Please point
potential mentors at the {doc}`mentors` page and tell them to get in contact
with us as soon as possible.

(project-timing)=

## Timing

We'll ask you to start thinking about your project in the first class.

- September 30 : deadline for choosing a mentor;

- October 17 : project pitches to the class.  Each group makes a 10 minute
  presentation describing:

  - the dataset;
  - any exploration you have already done;
  - your initial plan of investigation.

- December 5 : project presentation;

- December 17 : final project submission.

## Grading

See {doc}`project_grading`.

See also {doc}`participate`.
