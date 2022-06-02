# File sizes

## Encourage `@` operator over `np.dot`/`ndarray.dot`

Introduce in early numpy lesson.

## Refactor reshape_and_3d

Merge parts with reshaping section of Numpy intro

## Change image in slice timing page

Consider using `sub-01 func sub-01_task-Emotionregulation_run-01_bold.nii.gz`
from <https://openneuro.org/datasets/ds000108>.  Tor says:

> I'm pretty sure we were using ascending interleaved, first the odd slices
bottom to top up to TR/2, then the even slices bottom to top.

Find a scan with a lot of motion, look for comb artefact to confirm.  Find
good run and put into nipraxis-data.  Use that, redo graphic.
