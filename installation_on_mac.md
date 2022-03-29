---
orphan: true
---

# Installation on Mac

(terminal-app)=

## Terminal.app

We'll be typing at the "terminal" prompt often during the class.  In macOS, the
program giving the terminal prompt is `Terminal.app`.  It comes installed
with macOS.

Press the Command key and the spacebar at the same time to open the Spotlight
search box.  Type "terminal" and press return to open Terminal.app.  You
should get a terminal window.  Consider pinning Terminal.app to your dock by
right-clicking on the Terminal icon in the dock, chose "Options" and "Keep in
dock".

## Homebrew

[Homebrew](https://brew.sh) is "The missing package manager for macOS".  It is
a system for installing many open-source software packages on macOS.
We recommend Homebrew to any serious Mac user; you will need it for the
instructions on this page.

To install Homebrew, follow the instructions on the [homebrew home page](https://brew.sh/).

## Git

Git comes with the Apple macOS command line tools.

To get these, if you do not have them, open Terminal.app (see above) and type
`git` at the terminal command line.  If Git is not installed already you will
get a dialog box offering to install the command line tools.  See [installing the command line tools](https://www.freecodecamp.org/news/install-xcode-command-line-tools/) for an illustration.

Click 'install' to install the macOS developer command line tools, including
Git.

## Python

In {ref}`terminal.app`, type:

```
brew install python
```
