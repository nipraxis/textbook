# Installing on your computer

We are going to be using the following major software for the class:

- [Python](https://python.org)
- [numpy](https://numpy.org) (the Python array package);
- [matplotlib](https://matplotlib.org) (Python plotting package);
- [scipy](https://scipy.org) (Python scientific library);
- [nibabel](https://nipy.org/nibabel) (read / write of neuroimaging file
  formats in Python);

For the class and homework we will use:

- a text editor of your choice - see {doc}`choosing_editor`.  Choosing an
  editor is an important and personal decision, and one we recommend you invest
  some time in.
- the [git](https://git-scm.com/) version control system.

## Installation

:::{note}

It is common to run into problems with installation - don't worry, we're
expecting that.  One of the things we are teaching in this class is how to
solve problems like installing and using scientific software.  So, if you run
into trouble - great - that will be a good opportunity for us to work together
on a not-trivial problem.

:::

Here are the instructions for installing Git and Python:

- {doc}`installation_on_mac`;
- {doc}`installation_on_linux`;
- {doc}`installation_on_windows`.

Next, open Terminal (Mac) or Powershell (Windows) or a terminal of your choice
on Linux.

We suggest you start the steps below in the `Documents` directory in your home
(user) directory.  To make sure you are working in that directory, run this
command in the terminal.

```
cd $HOME/Documents
```

```{warning}
If you get `The system cannot find the path specified`, and you are on Windows,
make sure you are running a **Powershell** shell, not the much older Windows `cmd` shell.
```

Make a new directory to store your work:

```
mkdir nipraxis-work
```

Change your shell to that directory:

```
cd nipraxis-work
```

Confirm you are in the right directory with:

```
pwd
```

This Prints the Working Directory (pwd).  You should see something like the following:

::::{tab-set}

:::{tab-item} Windows Powershell
```
Path
----
C:\Users\your-user\Documents\nipraxis-work
```
:::

:::{tab-item} Mac
```
/Users/your-user/Documents/nipraxis-work
```
:::

:::{tab-item} Linux
```
/home/your-user/Documents/nipraxis-work
```
:::

::::

Now, in the terminal, check you have Python installed:

```
python3 --version
```

This should show you the Python 3 version report, something like this:

```
Python 3.10.4
```

Check you have the Python package manager installed:

```
pip3 --version
```

This should show you something like this:

```
pip 22.0.4 from <some-directory/site-packages/pip (python 3.10)
```

Now finish the install with:

```
pip3 install --user scipy matplotlib pandas scikit-image sympy nibabel jupyter ipython jupytext nipraxis okpy
```

:::{note}

Don't worry about warnings like this:

```
WARNING: The script <some-program> is installed in 'C:\Users\scipy\AppData\Roaming\Python\Python310\Scripts' which is not on PATH.
```

:::

Keep the terminal open.

Check your install by downloading {download}`check_install.py` to your
computer.   Note where the file went.  For example, you might have downloaded the file to your `Downloads` directory.

Move the file to your `Documents/nipraxis-work` directory.  You can use the terminal for this.  For example, if the file did appear in your default `Downloads` folder:

```
mv $HOME/Downloads/check_install.py .
```

Check you do have the file in the `nipraxis-work` directory with:

```
ls check_install.py
```

from your terminal.  You should see something like:

::::{tab-set}

:::{tab-item} Windows Powershell
```
    Directory: C:\Users\your-user\Documents\nipraxis-work


Mode                 LastWriteTime         Length Name
----                 -------------         ------ ----
-a----          4/6/2022   5:04 AM           1937 check_install.py
```
:::

:::{tab-item} Mac or Linux
```
check_install.py
```
:::

::::

Now check your installation has succeeded with:

```
python3 check_install.py
```

You should see something like:

```
Platform: macOS-12.3.1-x86_64-i386-64bit
Python version: 3.8.13 (default, Mar 16 2022, 20:38:07) 
[Clang 13.0.0 (clang-1300.0.29.30)]

Congratulations, all checks passed
```

where the details in the first three lines will depend on your system.

Finally, to get a copy of the textbook files:

```
git clone https://github.com/nipraxis/textbook
```

Now you can open the textbook notebooks with:

```
cd textbook
python3 -m notebook
```

This will open your web browser in the Jupyter interface.  Select the file you
are interested in.
