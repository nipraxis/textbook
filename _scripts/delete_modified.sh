#!/bin/sh
# Delete modified ipynb files.
MODIFIED=$(git diff-index --name-only HEAD -- */*.ipynb)
if [ "$MODIFIED" != "" ]; then
    echo Modified are $MODIFIED
    rm $MODIFIED
fi
