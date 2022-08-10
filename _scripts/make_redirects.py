#!/usr/bin/env python
""" Write redirects
"""

from pathlib import Path
from argparse import ArgumentParser

import yaml

from oktools.cutils import find_site_config


def write_redirect(source, target, out_dir):
    redirect_pth = Path(out_dir) / f'{source}.html'
    fname_dir = redirect_pth.parent
    if not fname_dir.is_dir():
       fname_dir.mkdir(parents=True)
    redirect_pth.write_text(
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
       site_config = find_site_config(Path(), filenames=('_config.yml',))
    ff = Path(site_config)
    site_dict = yaml.load(ff.read_text(), Loader=yaml.SafeLoader)
    redirection = site_dict.get('redirection', {})
    out_dir = redirection['builddir']
    redirects = redirection['redirects']
    for source, target in redirects.items():
        write_redirect(source, target, out_dir)


if __name__ == '__main__':
    main()
