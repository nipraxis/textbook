#!/bin/bash
# Check if current branch contents has been pushed
if [ -n "$(git status --porcelain)" ]; then
    echo "Check git status; needs commit"
    exit 1
fi
upstream_diff=$(git diff @{u} --stat)
if [ "$upstream_diff" != "" ]; then
    echo "HEAD differs from upstream; please review git status"
    exit 2
fi
