# Array reduction operations

Operations like `sum` and `mean` are array reduction operations.

We call these "reduction operations" because operations like sum have the
effect of slicing out 1D arrays from the input array, and reducing these 1D
arrays to scalars.

For example, if we have a 2D array, we might take the sum over the first axis:

>>> import numpy as np
>>> a = np.arange(6).reshape((2, 3))
>>> a
array(\[\[0, 1, 2\],
       \[3, 4, 5\]\])
>>> np.sum(a, axis=0)
array(\[3, 5, 7\])

What has happened here is that numpy takes each column (slice over the first
axis), then reduces the column to a scalar (that is the sum of the column):

>>> np.sum(a\[:, 0\])
3
>>> np.sum(a\[:, 1\])
5
>>> np.sum(a\[:, 2\])
7

Notice that the new summed array has one fewer dimension than the input array.  The dimension over which we have done the sum has gone (numpy "reduced" it):

>>> np.sum(a, axis=0).shape
(3,)

Similarly, when we sum across the second axis, we reduce that second axis:

>>> np.sum(a, axis=1)
array(\[ 3, 12\])
>>> np.sum(a\[0, :\])
3
>>> np.sum(a\[1, :\])
12

Now imagine a 3D array:

>>> b = np.arange(24).reshape(2, 3, 4)
>>> b
array(\[\[\[ 0,  1,  2,  3\],
        \[ 4,  5,  6,  7\],
        \[ 8,  9, 10, 11\]\],
\<BLANKLINE>
       \[\[12, 13, 14, 15\],
        \[16, 17, 18, 19\],
        \[20, 21, 22, 23\]\]\])

Let's say we want to sum across axis 0 (the first axis).  How do we get 1D
arrays from this first axis?

>>> b\[:, 0, 0\]
array(\[ 0, 12\])
>>> b\[:, 0, 1\]
array(\[ 1, 13\])

So, we can think of this 3D array as a 2D array shape (3, 4) where each element
is a 1D array length 2.

Sum then operates over this array of 1D arrays to reduce the first axis:

>>> np.sum(b, axis=0)
array(\[\[12, 14, 16, 18\],
       \[20, 22, 24, 26\],
       \[28, 30, 32, 34\]\])
>>> np.sum(b\[:, 0, 0\])
12
>>> np.sum(b\[:, 0, 1\])
14

You could imagine doing what numpy does with something like this:

>>> sum_over_axis_0 = np.zeros((b.shape\[1:\]))
>>> for j in range(b.shape\[1\]):
...     for k in range(b.shape\[2\]):
...         arr_1d = b\[:, j, k\]
...         sum_over_axis_0\[j, k\] = np.sum(arr_1d)
>>> sum_over_axis_0
array(\[\[ 12.,  14.,  16.,  18.\],
       \[ 20.,  22.,  24.,  26.\],
       \[ 28.,  30.,  32.,  34.\]\])

It is the same for reducing over the second axis. Now the 1D arrays are slices
over the second axis.

>>> b\[0, :, 0\]
array(\[0, 4, 8\])
>>> b\[0, :, 1\]
array(\[1, 5, 9\])
>>> np.sum(b, axis=1)
array(\[\[12, 15, 18, 21\],
       \[48, 51, 54, 57\]\])
>>> np.sum(b\[0, :, 0\])
12
>>> np.sum(b\[0, :, 1\])
15

It is the same idea over the third axis (axis=2):

>>> b\[0, 0, :\]
array(\[0, 1, 2, 3\])
>>> b\[0, 1, :\]
array(\[4, 5, 6, 7\])
>>> np.sum(b, axis=2)
array(\[\[ 6, 22, 38\],
       \[54, 70, 86\]\])
>>> np.sum(b\[0, 0, :\])
6
>>> np.sum(b\[0, 1, :\])
22
