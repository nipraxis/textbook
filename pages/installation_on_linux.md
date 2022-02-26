# Installation on Linux

## Installing Python 3, git and atom

### On Ubuntu or Debian

Tested on: Ubuntus 14.04, 15.04 through 16.10; Debians Jessie and Sid.

Install git and Python 3:

```bash
sudo apt-get update
sudo apt-get install -y git python3-dev python3-tk
sudo apt-get install -y git
```

Check your Python 3 version with:

```bash
python3 --version
```

This should give you a version >= 3.4.  If not, ask your instructors for help.

Point your web browser at the [atom releases] page and download the latest
`.deb` file for your distribution.  Here's me downloading a recent release
from the command line:

```bash
# Install the wget command for downloading from the command line
sudo apt-get install -y wget
# Download a recent version of Atom for Debian / Ubuntu
wget https://github.com/atom/atom/releases/download/v1.9.9/atom-amd64.deb
```

Install the Atom `.deb` package with:

```bash
# This command may error with unmet dependencies
sudo dpkg --install atom-amd64.deb
# Fix any unmet dependencies with this command
sudo apt-get -f install -y
```

Install the Atom [hydrogen] plugin with:

```bash
# Install dependencies for hydrogen plugin build
sudo apt-get install -y build-essential libzmq3-dev
# Install hydrogen plugin
PYTHON=python2.7 apm install hydrogen
```

### On Fedora

Tested on Fedora 21 through 24.

Install git and Python 3:

```bash
sudo dnf install -y git python3-devel python3-tkinter
```

If you get `bash: dnf: command not found`, run `sudo yum install dnf` and
try again.

Check your Python 3 version with:

```bash
python3 --version
```

This should give you a version >= 3.4.  If not, ask your instructors for help.

Point your web browser at the [atom releases] page and download the latest
`.rpm` file for your distribution.  Here's me downloading a recent release
from the command line:

```bash
# Install the wget command for downloading from the command line
sudo dnf install -y wget
# Download a recent version of Atom for Fedora
wget https://github.com/atom/atom/releases/download/v1.9.9/atom.x86_64.rpm
```

Install the Atom `.rpm` package with:

```bash
sudo dnf install -y ./atom.x86_64.rpm
```

Install the Atom [hydrogen] plugin with:

```bash
# Install dependencies for hydrogen plugin build
sudo dnf install -y python2 gcc-c++ zeromq3-devel
# Install hydrogen plugin
PYTHON=python2.7 apm install hydrogen
```

## Installing Python 3 packages

To get ready for Python user installs, put the user local install `bin`
directory on your system {term}`PATH`.  First find the location of the user
`bin` directory with:

```bash
python3 -c 'import site; print(site.USER_BASE + "/bin")'
```

This will give you a result like `/home/your_username/.local/bin`.

Open the `~/.bashrc` file in your home directory with Atom:

```bash
atom ~/.bashrc
```

Add these lines to end of the file:

```bash
# Put the path to the local bin directory into a variable
py3_local_bin=$(python3 -c 'import site; print(site.USER_BASE + "/bin")')
# Put the directory at the front of the system PATH
export PATH="$py3_local_bin:$PATH"
```

Save the file, and restart your terminal to load the configuration from your
`~/.bashrc` file.  Confirm that you have the `.local/bin` directory in
your PATH now:

```bash
echo $PATH
```

Now install the Python package installer `pip` into your user directories
(see: [install pip with get-pip.py]):

```bash
# Download the get-pip.py installer
wget https://bootstrap.pypa.io/get-pip.py
# Execute the installer for Python 3 and a user install
python3 get-pip.py --user
```

Check you now have the right version of the `pip3` command with:

```bash
which pip3
```

This should give you something like `/home/your_username/.local/bin/pip3`.

Finally, install the packages you need for the class:

```bash
pip3 install --user numpy scipy matplotlib ipython nibabel jupyter
```

% atom commands:
% ctrl-shift-p  command palette
% alt-shift-enter  run in place
% alt-ctrl-enter  run and move down

Don't forget to do the {ref}`installation-check`.
