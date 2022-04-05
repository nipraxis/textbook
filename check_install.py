""" Test installation of packages for psych-214 class

Run with::

    python3 check_install.py

These programs should be installed:

* python 3 version >= 3.8
* git
* pip3 >= 22

See the PACKAGES variables for the packages that should be installed.
"""

PACKAGES = {
    'scipy': 'scipy',
    'matplotlib': 'matplotlib',
    'pandas': 'pandas',
    'scikit-image': 'skimage',
    'nibabel': 'nibabel',
    'jupyter': 'jupyter',
    'ipython': 'IPython',
    'jupytext': 'jupytext',
    'nipraxis': 'nipraxis',
    'okpy': 'client'}

import sys
import platform
import re
from subprocess import check_output
from importlib import import_module

print("Platform:", platform.platform())
print("Python version:", sys.version)

# Python running us is >= 3.8
assert sys.version_info[:2] >= (3, 8), 'Need Python at least version 3.8'

# pip on Python sys path should be >= 8.1
def version_digits(version_str):
    match = re.match('(\d+)\.(\d+)\.', version_str)
    if match:
        return [int(n) for n in match.groups()]

import pip
pip_digits = version_digits(pip.__version__)
assert pip_digits[0] > 20, 'Need pip version at least 20.0'

# Pip on shell path likewise
pip_cmd_out = check_output(['pip3', '--version'],
                           universal_newlines=True,
                          ).split()
assert pip_cmd_out[0] == 'pip'
pip_cmd_digits = version_digits(pip_cmd_out[1])
assert pip_cmd_digits == pip_digits, \
        'Pip version on command line differs from version via import'

for package, import_name in PACKAGES.items():
    try:
        import_module(import_name)
    except ImportError:
        raise RuntimeError('Package {} may not be installed'.format(package))

# git on the command line
assert check_output(['git', '--version'],
                    universal_newlines=True) .startswith('git version'), \
        'Git should return "git version" from "git --version"'

print("\nCongratulations, all checks passed")
