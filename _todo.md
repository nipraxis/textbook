# File sizes

Before too many people have cloned, we should consider ways of reducing the
data size.

<https://github.com/nipraxis/tutorial-files> is one direction - considering processing the files.

We could also think of Pooch or similar, maybe with a shared repository for the student JupyterHub.

# Encourage `@` operator over `np.dot`/`ndarray.dot`

This operator exists in all maintained versions of Python and numpy and produces more readable code.

Introduce in early numpy lesson, and replace `dot()` throughout when there is no reason to keep `dot()`.

# Replace numpy.random with `default_rng`

Move to the [RandomGenerator](https://numpy.org/doc/stable/reference/random/generator.html) API.
