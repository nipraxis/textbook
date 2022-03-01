# Comparing floats and floating point error

Requirements:

- {doc}`string_formatting`.

There are an infinite number of real {{ -- }} er {{ -- }} numbers, for example, there
are an infinite number of real numbers between 0 and 1.

The computer stores real numbers as floating point numbers. The typical format
the computer uses for floating point numbers uses 8 bytes (64 bits) of memory
per number. That means the computer can only represent some of the numbers
between 0 and 1 (for example).

One number that standard floating point numbers cannot represent exactly is
0.1. Here we print the value with 20 digits after the decimal point to show
that (see {doc}`string_formatting`):

>>> print('{:.20f}'.format(0.1))
0.10000000000000000555

This means that when we do mathematical operations on floating point numbers,
the exact result of the operation may be a number that the computer cannot
represent. In that case the software implementing the calculation can at best
give us the nearest floating point number that it *can* represent:

>>> print('{:1.20f}'.format(1 / 10))
0.10000000000000000555

For this reason, sometimes the results of doing floating point calculations
are not exactly accurate. This is called [floating point error].  In the case
above the floating point error is very small {{ -- }} 0.00000000000000000555.

Floating point error means that we have to be careful comparing results of
floating point calculations, because the result may be incorrect by some small
amount:

>>> import numpy as np
>>> c = np.cos(1)
>>> # We hope that the inverse cos (np.arccos) should give back the
>>> # original number, but ...
>>> np.arccos(c) == 1
False
>>> np.arccos(c)
0.99999999999999989

In this case, we probably want to check that the result is equal within some
reasonable error due to the limited precision of floating point.  For example,
`np.allclose` checks whether two numbers are almost equal within some
default tolerance levels:

>>> np.allclose(np.arccos(c), 1)
True
