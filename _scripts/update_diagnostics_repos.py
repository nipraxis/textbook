#!/usr/bin/env python3
""" Make diagnostics repo from template
"""

from subprocess import CalledProcessError
from argparse import ArgumentParser, RawDescriptionHelpFormatter


import make_diagnostics_repo as mdr



def pr_to_repo(repo_path, template_branch):
    # Assert that we have a main branch.
    gitter = mdr.GitCmd(repo_path)
    gitter('git checkout main')
    # Add template repository as remote, if not present.
    remotes = gitter.get_out('git remote').splitlines()
    if 'template' in remotes:
        gitter('git remote rm template')
    gitter(f'git remote add template {mdr.TEMPLATE_REPO}')
    # Add nipraxis fork
    gitter(f'gh repo fork '
           '--org nipraxis-spring-2022-forks '
           '--remote --remote-name nipraxis-forked')
    # Fetch upstream remotes.
    gitter('git fetch --all')
    # Delete target branch, if present
    gitter('git checkout main')
    branches = [b.strip() for b in gitter.get_out('git branch').splitlines()]
    if template_branch in branches:
        gitter(f'git branch -D {template_branch}')
    # Rebase PR branch on top of main
    gitter(f'git checkout -t template/{template_branch}')
    try:
        gitter('git rebase origin/main')
    except CalledProcessError:
        gitter('git rebase --abort')
        gitter('git checkout main')
        gitter(f'git branch -D {template_branch}')
        raise
    # Make PR
    gitter(f'git push nipraxis-forked {template_branch} --force --set-upstream')
    gitter('gh pr create --fill')


def get_parser():
    parser = ArgumentParser(description=__doc__,  # Usage from docstring
                            formatter_class=RawDescriptionHelpFormatter)
    parser.add_argument('repo_path',
                        help='Path to local repo')
    parser.add_argument('pr_branch',
                        help='Branch from which to make PR')
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args()
    pr_to_repo(args.repo_path, args.pr_branch)


if __name__ == '__main__':
    main()
