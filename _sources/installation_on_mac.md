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
search box.  (You can also click on the magnifier glass icon in menu bar
towards the right). Type "terminal" and press return to open Terminal.app.
You should get a terminal window.  Consider pinning Terminal.app to your dock
by right-clicking on the Terminal icon in the dock, chose "Options" and "Keep
in dock".

## Git

Git comes with the Apple macOS command line tools.

Install these by typing:

```bash
xcode-select --install
```

in Terminal.app.   If you don't have the command line tools, you will get a dialog box like this:

![](image/xcode_cli_dialog.png)

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

## Python

In {ref}`terminal.app`, type:

```bash
brew install python
```
