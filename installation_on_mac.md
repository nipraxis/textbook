---
orphan: true
---

# Installation on Mac

(terminal-app)=

## Terminal.app

We'll be typing at the "terminal" prompt often during the class.  In macOS, the
program giving the terminal prompt is `Terminal.app`.  It comes installed
with macOS.

You'll find it in the Utilities sub-folder of your Applications folder, but
the easiest way to start it is via Spotlight.

Start spotlight by either:

*   Clicking on the magnifying glass icon at the right of your menu bar at the
    top of your screen

    ![](images/spotlight_on_menu.png)

    or (the better option):
*   Press the command key (the key with the ⌘ symbol) and then (at the same
    time) the spacebar.

In either case, a mini-window like this will come up:

![](images/spotlight_mini_window.png)

Type `terminal` in this window.  The first option that comes up is almost
invariably the Terminal application:

![](images/spotlight_terminal.png)

Select this by pressing Enter, and you should see the Terminal application window, as above.

Consider pinning Terminal.app to your dock by right-clicking on the Terminal
icon in the dock, chose "Options" and "Keep in dock".

## Git

Git comes with the Apple macOS command line tools.

Install these by typing:

```bash
xcode-select --install
```

in Terminal.app.   If you don't have the command line tools, you will get a dialog box like this:

![](images/xcode_cli_dialog.png)

Select "Install".  You may need to wait a while for that to complete.

When it has run, check you can run the `git` command with this, in Terminal.app:

```bash
git
```

It should show you the Git help message.

## Homebrew

[Homebrew](https://brew.sh) is "The missing package manager for macOS".  It is
a system for installing many open-source software packages on macOS.
We recommend Homebrew to any serious Mac user; you will need it for the
instructions on this page.

To install Homebrew, follow the instructions on the [homebrew home page](https://brew.sh/).

## Install Python

Mac actually comes with a version of Python for its own use, but it's nearly always better to install your own version, for your use.

First, install with Homebrew.

In {ref}`terminal-app`, type:

```bash
brew install python
```

**Check carefully for any error messages about failure, like this**:

```
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /usr/local
Could not symlink bin/2to3
Target /usr/local/bin/2to3
already exists. You may want to remove it:
  rm '/usr/local/bin/2to3'
```

The `2to3` command above is just one command that Python installs to your
system.

If you see a message like that, it means you had another, presumably older,
copy of Python and its associated commands installed in your `/usr/local/bin`
folder.  Fix the problem by forcing Homebrew to overwrite the old copy, with
the instructions you will see further down that message:

```
brew link --overwrite python
```

## Set up Python for your Terminal

Next, open the file `~/.bash_profile` with a text editor, for example, like this:

```
touch ~/.bash_profile
open -a TextEdit ~/.bash_profile
```

Scroll to the end of the file, and add this line:

```
export PATH=/usr/local/bin:$PATH
```

Be very careful that TextEdit doesn't automatically capitalize `export` above
to `Export`.  Correct it again to lower case if it does.

* Save, and close the text editor.
* Close Terminal.app.
* Start Terminal.app again, and

— confirm you are looking at the right Python:

```bash
which python3
```

You should see:

```
/usr/local/bin/python3
```
