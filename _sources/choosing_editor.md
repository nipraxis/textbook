---
orphan: true
---

(choosing-editor)=

# Choosing an editor

> *Use a Single Editor Well*
>
> The editor should be an extension of your hand; make sure your editor is
> configurable, extensible, and programmable.
>
> <p class="attribution">-From: "The pragmatic programmer" </p>

Being efficient means being able to use your tools well.  If you are fluent in
using your editor, you will be able think better.  You will do better work more
quickly and you will make fewer mistakes.

This is particularly so for a text file editor.  Bear in mind that you will
likely spend many hundreds of hours using this editor for various parts of
your work over the rest of your career.  Be careful with your choice, and
consider investing time to learn an editor well.

If you do learn your text editor well, you will find yourself using it for
many different tasks, including editing code, documents and configuration
files.

Programmers are a strange bunch of people who are extremely intolerant of
tools that waste their time or energy.  Take their impatience seriously when
you consider choosing your editor.  No programmer would use Windows Notepad
for writing code, and that is for a very good reason.

## Take time to choose

Choosing an editor is an important, even fateful decision.  You choose an
editor in order to invest in it; if you choose wisely, your will find your
investment repaid, handsomely, and daily.  Choose carefully, and choose for the
long haul.

Please be careful that you do not underestimate this task.  It is tempting to
choose an editor "for now", but, whichever editor you choose, there is a good
chance you will still be using it in a few years.  If you choose the wrong
editor, you will find that you have lost a great deal of learning time, when
you have to change later, and you will curse yourself, with reason.  Be free
from future self-recrimination, and choose deliberately, now, for the long
haul.

## What are the options?

There are various surveys on the editors that Python developers use.  Some
recent examples are:

*   [The Jetbrains 2020
    Python developer
    survey](https://www.jetbrains.com/lp/python-developers-survey-2020/)
    (though note, this survey was by the makers of one of the editors,
    PyCharm).
*   [The 2021 StackOverflow developer
    survey](https://insights.stackoverflow.com/survey/2021#section-most-popular-technologies-integrated-development-environment)
    (though note, this is for developers in all languages).
*   [A discussion of recent
    trends](https://asterisk.dynevor.org/editor-dominance.html).

From these, and from our own experience talking to other people with lots of
experience writing Python code, we believe your practical long-term options
are the following.  The editors are in the order from the Jetbrains survey
above, but with the position of PyCharm estimated from the StackOverflow
survey, on the basis that the JetBrains survey results are likely to be biased
to PyCharm users).

* A version of [Visual studio code](https://code.visualstudio.com).  More on
  what we mean by "a version" below.
* [Vim](https://www.vim.org)
* [PyCharm](https://www.jetbrains.com/pycharm)
* [Sublime text](https://www.sublimetext.com)
* [Emacs](https://emacs.org)
* [Spyder](https://www.spyder-ide.org)

## Some version of Visual Studio Code

[Visual studio code](https://code.visualstudio.com) is a code editor and
integrated development environment almost entirely written by programmers at
Microsoft.  It is entirely free to download (free as in free beer).  See below
for more discussion about whether it truly open-source (free as in freedom).

It is very popular as a Python editor, and [increasingly
so](https://asterisk.dynevor.org/editor-dominance.html).

You will find many powerful features for interacting with Python code, and, more recently and experimentally, with Jupyter Notebooks.

It works well and looks good out of the box, but it is highly configurable.
Configuration takes some getting used to, and can be fiddly, but there is a
lot of help from others trying to do the same thing, online.

There are various controversies about Visual Studio Code (or VSCode for short).

Although Microsoft releases the code to build a version of VSCode on your own
computer, the installer you download from their website contains and refers to
to [not-free, not-open-source
components](https://code.visualstudio.com/docs/supporting/faq#_what-does-built-on-open-source-mean),
and it sends telemetry data to Microsoft.  See the [VSCodium
site](https://vscodium.com) for a discussion, and links to download versions
of VSCode without these features, and so, less locked to Microsoft.

Another controversy is the practical extent to which the community can
influence the direction of development of the VSCode editor.  In practice,
Microsoft decides the direction of the project, and drives the changes,
because they pay the programmers that write it.  See [this post for some
discussion](https://eclipse-foundation.blog/2020/05/05/eclipse-theia-and-vs-code-differences-explained).
For those reasons, some people prefer to use a build of the more open [Theia
editor](https://theia-ide.org), that uses much of machinery behind VSCode.

## Vim

The two most well-known and fully-featured cross-platform general text editors
are Emacs and Vim.  These run on any platform.  More about Emacs further down
the page.

Vim is based on a classic Unix editor called
[vi](https://en.wikipedia.org/wiki/Vi).  To quote from the [about
vim](https://www.vim.org/about.php) page:

> Vim isn't an editor designed to hold its users' hands. It is a tool, the use
> of which must be learned.

To use Vim well, you have to practice using its commands, by following any one
of several online tutorials. For example, you might try the [openvim
tutorial](http://www.openvim.com/tutorial.html) or [Vim
adventures](https://vim-adventures.com/).  The trick is to teach your fingers
what to do so you don't think about it any more. This takes a long time,
budget a week of 30 minutes a day to start to feel comfortable.

If you do invest this effort, Vim is an immensely satisfying editor to use,
because you quickly find that your fingers remember what to do.  A
programmer's joke about Vim is that "the cursor follows your eyes", because
your fingers are moving the cursor around the text without any apparent
thought or effort on your part.

It is relatively complicated to configure Vim to its full potential.  Please
ask for help if you are interested to do this.  It is time well spent.

## PyCharm

We have heard good things about PyCharm, from people who know what they are
talking about.  This is a general text editor with features that allow it to
be used as an integrated development environment for Python.  There is a free
"community" version and a £149 initial annual fee for the professional
version.  The free version does have Python editing support, and support for
other languages, but the professional edition supports more languages and
features.  See the [PyCharm web site](https://www.jetbrains.com/pycharm/) and
[PyCharm feature
comparison](https://www.jetbrains.com/products/compare/?product=pycharm&product=pycharm-ce)
for more detail.

### Sublime Text

Some people really like [Sublime text](https://www.sublimetext.com).  It is
free to try, and it appears the trial version does not expire, but if you
continue to use it, the authors ask you to buy a license for \$99.

## Emacs

Emacs is a very powerful classic free, and open-source text editor. The great
[Richard Stallman](https://en.wikipedia.org/wiki/Richard_Stallman) wrote the
original version. It is quicker to learn than vim, probably harder to
configure, and configurable to an extreme degree.  A good place to start is
the [emacs tour](https://www.gnu.org/software/emacs/tour).  About an hour of
research and practice gets you far enough to learn how to start learning
Emacs.

As for Vim, to use it well, it needs practice.  You will need to get used to
the keystrokes, and as for Vim, this practice is amply repaid by very fluent
movement and editing.

Emacs is hard to configure, largely because it is so powerful.  We are very
happy to help with this if you are interested.

## Spyder

[Spyder](https://www.spyder-ide.org) is a code editor and integrated
development environment that is specific to Python.  It is free, and
open-source.  You can install it in the same way you install other Python
packages.  It has a similar interface to, for example, the Matlab graphical
environment, with separate windows for code, plots, variables and so on.

## Another option for Windows

[Notepad++](https://notepad-plus-plus.org) only works on Windows, but seems to be a popular choice.

## Suggestions?

If you have any other suggestions or recommendations, please let us know.
