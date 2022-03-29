# Installation

We are going to be using the following major software for the class:

- [Python] 3 (see {ref}`why-python-3`);
- [numpy] (the Python array package);
- [matplotlib] (Python plotting package);
- [scipy] (Python scientific library);
- [nibabel] (read / write of neuroimaging file formats in Python);

For the class and homework we will use:

- a text editor of your choice - see {doc}`choosing_editor`.  Choosing an
  editor is an important and personal decision, and one we recommend you invest
  some time in.
- the [git](https://git-scm.com/) version control system.

## Installation

:::{note}
It's common to run into problems with installation - don't worry, we're
expecting that.  One of the things we are teaching in this class is how to
solve problems like installing and using scientific software.  So, if you
run into trouble - great - that will be a good opportunity for us to work
together on a not-trivial problem.
:::

Here are the instructions for installing Git and Python:

- {doc}`installation_on_mac`;
- {doc}`installation_on_linux`;
- {doc}`installation_on_windows`.

Next, open Terminal (Mac) or Powershell (Windows) or a terminal of your choice on Linux:

Check you have Python installed:

```
which python3
```

Check you have the Python package manager installed:

```
which pip3
```

Now finish the install with:

```
pip3 install --user scipy matplotlib scikit-image nibabel jupyter ipython jupytext
```

Finally, to git a copy of the textbook files:

```
git clone https://github.com/nipraxis/textbook
```

Now you can open the textbook notebooks with:

```
cd textbook
python3 -m jupyter notebook
```

This will open your web browser in the Jupyter interface.  Select the file you
are interested in.

## Why Python

Python is well-suited to scientific computing for [many
reasons](https://github.com/nipy/nipy/blob/master/doc/faq/why.rst#why-python).

Python code is famously easy to read, and Python has become a common choice
for introductions to programming {{ -- }} see for example the [Berkeley CS61A
course](http://cs61a.org) and the [MIT introduction to computer science and
programming](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-00sc-introduction-to-computer-science-and-programming-spring-2011/).

The CS61A course notes have a good introduction to the [benefits of
Python](http://composingprograms.com/pages/11-getting-started.html#programming-in-python).
You may want to read [10 reasons Python rocks for
research](https://blog.fanplastic.org/2010/11/03/10-reasons-python-rocks-for-research/)
for a comparison between Python and MATLAB.

Berkeley teaches its new data science courses using Python.

For the class, you will need a version of Python >= 3.8.
