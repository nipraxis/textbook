#!/usr/bin/env python
""" Write redirects
"""

import os
import os.path as op
import sys
from argparse import ArgumentParser

import yaml

HERE = op.dirname(op.realpath(__file__))
SITE_ROOT = op.realpath(op.join(HERE, '..'))
sys.path.append(HERE)

from cutils import find_site_config


def write_redirect(source, target, out_dir):
    redirect_fname = op.join(out_dir, f'{source}.html')
    fname_dir = op.dirname(redirect_fname)
    if not op.isdir(fname_dir):
        os.makedirs(fname_dir)
    with open(redirect_fname, 'wt') as fobj:
        fobj.write(
            """<meta http-equiv="Refresh" content="0; """
            f"""url='{target}.html'" />""")


def main():
    parser = ArgumentParser()
    parser.add_argument('--site-config',
                        help='Path to configuration file for course '
                        '(default finds _config.yml, in dir, parents)'
                       )
    args = parser.parse_args()
    site_config = args.site_config
    if site_config is None:
       site_config = find_site_config(os.getcwd(), filenames=('_config.yml',))
    with open(site_config, 'r') as ff:
        site_dict = yaml.load(ff.read(), Loader=yaml.SafeLoader)
    redirection = site_dict.get('redirection', {})
    out_dir = redirection['builddir']
    redirects = redirection['redirects']
    for source, target in redirects.items():
        write_redirect(source, target, out_dir)


if __name__ == '__main__':
    main()
