#!/usr/bin/env python3
""" Make diagnostics repo from template
"""

import os
import os.path as op
from subprocess import run
import shlex
from argparse import ArgumentParser, RawDescriptionHelpFormatter


BASE_URL = 'https://github.com'
TEMPLATE_REPO = f'{BASE_URL}/nipraxis/diagnostics-template'
CLONE_ORG = 'nipraxis-spring-2022'
DATA_LOOKUP = {0: '35098309',
               1: '35098504',
               2: '35098696'}


def replace_data_id(repo_path, data_id):
    readme = op.join(repo_path, 'README.md')
    with open(readme, 'rt') as fobj:
        contents = fobj.read()
    contents = contents.replace('{DATA_ID}', data_id)
    with open(readme, 'wt') as fobj:
        fobj.write(contents)


class GitCmd:

    def __init__(self, repo_path):
        self.repo_path = op.abspath(repo_path)

    def __call__(self, args, **run_args):
        if isinstance(args, str):
            args = shlex.split(args)
        return run(args, check=True, cwd=self.repo_path, **run_args)

    def get_out(self, args, **run_args):
        return self(args, capture_output=True, text=True, **run_args).stdout


def make_repo(repo_suffix, repo_admin, data_no, out_dir=None):
    if out_dir is None:
        out_dir = os.getcwd()
    out_sdir = f'diagnostics-{repo_suffix}'
    GitCmd(out_dir)(['gh', 'repo', 'clone', TEMPLATE_REPO, out_sdir])
    repo_path = op.join(out_dir, out_sdir)
    data_id = DATA_LOOKUP[data_no]
    replace_data_id(repo_path, data_id)
    gitter = GitCmd(repo_path)
    gitter(['git', 'commit', '-a', '-m', 'Set dataset'])
    gitter(['git', 'remote', 'rm', 'origin'])
    out_org_repo = f'{CLONE_ORG}/{out_sdir}'
    gitter(['gh', 'repo', 'create', out_org_repo,
                '--source=.', '--remote=origin',
                '--public'])
    gitter(['git', 'push', 'origin', 'main', '--set-upstream'])
    gitter(
        ['gh', 'api',
         '--method', 'PUT',
         '-H', "Accept: application/vnd.github.v3+json",
         f'repos/{out_org_repo}/collaborators/{repo_admin}',
         '--raw-field', 'permission=admin',
         '--silent',
        ])
    return f'{BASE_URL}/{out_org_repo}'


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('repo_suffix',
                        help='Suffix for repository name')
    parser.add_argument('repo_admin',
                        help='Username to give admin access')
    parser.add_argument('data_version', type=int,
                        help='Data version (0, 1 or 2)')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    url = make_repo(args.repo_suffix, args.repo_admin, args.data_version)
    print(url)


if __name__ == '__main__':
    main()
