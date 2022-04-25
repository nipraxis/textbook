# File sizes

## Encourage `@` operator over `np.dot`/`ndarray.dot`

This operator exists in all maintained versions of Python and numpy and produces more readable code.

Introduce in early numpy lesson, and replace `dot()` throughout when there is no reason to keep `dot()`.

## Replace numpy.random with `default_rng`

Move to the [RandomGenerator](https://numpy.org/doc/stable/reference/random/generator.html) API.

## Refactor reshape_and_3d

Merge parts with reshaping section of Numpy intro
