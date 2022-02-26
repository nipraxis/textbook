# Formats for floating point values in text files

```{eval-rst}
.. testsetup::

    import numpy as np
    # Set print options for doctests below
    np.set_printoptions(precision=6)
```

Let's say we have a floating point numbers like this:

>>> a_number = 314.15926
>>> a_number
314.15926

We can also represent these numbers in exponential format.  Exponential format
breaks the number into a two parts: the *significand*; and the *exponent*.

The significand is a floating point number with one digit before a decimal
point.  The exponent is an integer.  For example:

>>> exp_number = 3.1415926E2
>>> exp_number
314.15926

Here the significand is `3.1415926`, and the exponent is `2`, the value
after the `E`.  The number is given by `s * 10 ** e` where `s` is the
significand and `e` is the exponent.  In this case: `314.15926 = 3.1415926
\* 10 ** 2`.

This exponential format is the default format that `np.savetxt` uses to
represent floating point numbers when writing to text files.  For example:

>>> import numpy as np
>>> an_array = np.array(\[a_number, 1.0, 2.0\])
>>> an_array
array(\[ 314.15926,    1.     ,    2.     \])
>>> np.savetxt('some_numbers.txt', an_array)
>>> with open('some_numbers.txt', 'rt') as fobj:
...     contents = fobj.read()
>>> print(contents)
3.141592600000000175e+02
1.000000000000000000e+00
2.000000000000000000e+00
\<BLANKLINE>

```{eval-rst}
.. testcleanup::

    import os
    os.unlink('some_numbers.txt')
```
