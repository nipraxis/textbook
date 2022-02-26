# Installation on Windows

## Git version control

Go to <http://git-scm.com/>

Click on the Downloads for Windows link at the bottom right.

Download the file they propose, with a filename something like
`Git-2.9.3.2-32-bit.exe`.

Run the file to start the installation.

We suggest you accept the defaults, except the sceen called "Adjusting your
PATH environment", where we suggest you choose the option "Use git from the
Windows Command Prompt".

## The Atom text editor

Go to <https://atom.io/>

Download the Windows installer, run.

## The Hydrogen plugin for Atom

Installing this plugin is complicated, because you will need:

- Atom to be running with Python version 2 as the default Python version.
  That is inconvenient, because later on we'll need Python 3 for the class;
- an installation of a particular Microsoft Windows compiler program. A
  compiler is software that takes programs written in human-readable format
  and "compiles" them into instructions for the computer cental processing
  unit (CPU).

See <https://atom.io/packages/hydrogen> for more information.  What follows is a
recipe:

1. Python 2.7: go to: <https://www.continuum.io/downloads>.  Click on the
   Windows symbol for Windows downloads.  Select the 64-bit installer *for
   Python 2.7*, download, and install.  Choose to install for "Just me", and
   leave the defaults as they are for the rest of the installation dialog
   boxes.  Now you have a version of Python 2.7;
2. You are going to install Microsoft Visual Studio 2013 Express.  This is a
   free compiler from Microsoft.  You need the 2013 version, so be careful not
   to install a later version, such as the 2015 edition. Go to:
   <https://www.microsoft.com/en-US/download/details.aspx?id=44914>. Choose
   `wdexpress.exe` to download.  Run this installer.  Accept all the
   defaults.  Reboot when the Visual Studio 2013 install has finished.  You
   now have the compiler you need;
3. You can now install the Hydrogen plugin.  Start the Atom editor.  Go to the
   File menu, Settings, select +Install, type "hydrogen" in the search box,
   and click the Packages button to search.  When hydrogen comes up, click the
   Install button.  Wait a few minutes.  If there is an error, please come and
   find us for help.  Close Atom.
4. Now install Python 3. Go back to: <https://www.continuum.io/downloads>.
   Click on the Windows symbol for Windows downloads.  Select the 64-bit
   installer *for Python 3.5*, download, and install.  Choose to install for
   "Just me", and leave the defaults as they are for the rest of the
   installation dialog boxes.  Now you have a version of Python 3.5;

Test the Hydrogen plugin by starting Atom as you normally would. Make a new
text file and save it somewhere as `test.py`.  Type `a = 10` and press
Alt-Shift-Enter to run this line in Hydrogen.  After a few seconds, you should
see that Hydrogen started a new Python 3 kernel, and there will be a tick
after the `a = 10` line.  Or you may have got a small menu asking if you
want a Python 2 or a Python 3 menu.  If so, all is probably well.  Otherwise,
come and ask your instructors.

## Python and packages

You install Python 3 and many of the packages you need in the last step, when
you installed Anaconda3 (the version of Anaconda with Python 3.5).

The last package you need is [nibabel].

Open git bash (this should have been installed with git).

Type `which python` (and return) to see the version of Python that bash is
finding.  It should be something like `/c/Users/your_user/Anaconda3/python`
(note the `Anaconda3`).

Now type:

```
pip install nibabel
```

Check the installation worked with:

```
ipython
```

then, from the IPython `In [1]` prompt:

```
import nibabel
```

That should return without an error.  Congratulations, you're ready for the
classes.
