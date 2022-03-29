---
orphan: true
---

# Installation on Linux

## Installing Python 3, git and atom

### On Ubuntu or Debian

Tested on: Ubuntus 14.04, 15.04 through 16.10; Debians Jessie and Sid.

Install git and Python 3:

```bash
sudo apt-get update
sudo apt-get install -y git python3-dev python3-tk python3-pip
sudo apt-get install -y git
```

Check your Python 3 version with:

```bash
python3 --version
```

This should give you a version >= 3.8.  If not, ask your instructors for help.

### On Fedora

Tested on Fedora 21 through 24.

Install git and Python 3:

```bash
sudo dnf install -y git python3-devel python3-tkinter python3-pip
```

If you get `bash: dnf: command not found`, run `sudo yum install dnf` and
try again.

Check your Python 3 version with:

```bash
python3 --version
```

This should give you a version >= 3.8.  If not, ask your instructors for help.
