---
orphan: true
---

# Installation on Windows

## Git version control

Go to <http://git-scm.com/>

Click on the Downloads for Windows link at the bottom right.

Download the file they propose, with a filename something like
`Git-2.35.1.2-32-bit.exe`.

Run the file to start the installation.

We suggest you accept the defaults, except the screen called "Adjusting your
PATH environment", where we suggest you choose the option "Use git from the
Windows Command Prompt".

## Python

We suggest you use [Chocolatey](https://chocolatey.org/) to install Python.

Go to the [Choclately install page](https://chocolatey.org/install) and follow the instructions there.  Choose the 'individual' install.

Install.  Then, in a Powershell terminal with Administrator privileges, type:

```
choco install python
```

Close the Powershell, and open it again, again with Administrator privileges.

Type:

```
which python
```

This will show you where Choco installed Python.

Go to the directory containing Python.  In my case this was `c:\Python310`

```
cd c:\Python310
```

Then copy the `python.exe` file to `python3.exe`, so `python3` will also run the Python command.

```
cp python.exe python3.exe
```

Close the Powershell.  All done.
