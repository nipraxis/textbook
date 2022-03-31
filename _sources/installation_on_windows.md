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

To open Powershell, you can press the Windows key, and type Powershell, then
right click on the Powershell suggestion and select 'Run as administrator'.

## Copy python.exe to python3.exe

### The long-hand way

Type:

```
which python
```

This will show you where Choco installed Python.

In my case, Python was at `c:\Python310\python.exe`

Go to the directory containing Python.  In my case this was `c:\Python310`

```
cd c:\Python310
```

Then copy the `python.exe` file to `python3.exe`, so `python3` will also run the Python command.

```
cp python.exe python3.exe
```

### The short-hand way

If you prefer, you can do this copy step by copy-pasting the code below to the Powershell prompt, and pressing Enter:

```powershell
$py_path = (get-command -CommandType Application python).Source
cp $py_path ((Split-Path $py_path) + '\python3.exe')
```

## To finish

Close the Powershell.  All done.
