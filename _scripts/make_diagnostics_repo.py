#!/usr/bin/env python3
""" Make diagnostics repo from template
"""

import os
import os.path as op
from subprocess import check_call
from argparse import ArgumentParser, RawDescriptionHelpFormatter


BASE_URL = 'https://github.com'
TEMPLATE_REPO = f'{BASE_URL}/nipraxis/diagnostics-template'
CLONE_ORG = 'nipraxis-spring-2022'


def make_repo(repo_suffix, repo_admin, out_dir=None):
    if out_dir is None:
        out_dir = os.getcwd()
    out_sdir = f'diagnostics-{repo_suffix}'
    check_call(['gh', 'repo', 'clone', TEMPLATE_REPO, out_sdir],
                cwd=out_dir)
    repo_path = op.join(out_dir, out_sdir)
    check_call(['git', 'remote', 'rm', 'origin'], cwd=repo_path)
    out_org_repo = f'{CLONE_ORG}/{out_sdir}'
    check_call(['gh', 'repo', 'create', out_org_repo,
                '--source=.', '--remote=origin',
                '--public'],
               cwd=repo_path)
    check_call(['git', 'push', 'origin', 'main', '--set-upstream'],
               cwd=repo_path)
    check_call(
        ['gh', 'api',
         '--method', 'PUT',
         '-H', "Accept: application/vnd.github.v3+json",
         f'repos/{out_org_repo}/collaborators/{repo_admin}',
         '--raw-field', 'permission=admin',
         '--silent',
        ],
        cwd=repo_path)


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('repo_suffix',
                        help='Suffix for repository name')
    parser.add_argument('repo_admin',
                        help='Username to give admin access')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    make_repo(args.repo_suffix, args.repo_admin)


if __name__ == '__main__':
    main()
