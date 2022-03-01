# Subtracting the mean from a vector

We have a vector \$vec\{x}\$ with \$n\$ elements: \$\[x_1, x_2, ..., x_n\]\$.

The mean is:

$$
\bar{x} = \frac{1}{n} \sum_{i=1}^n x_i
$$

From here I will abbreviate \$sum\_{i=1}^n x_i\$ as \$sum\{x_i}\$.

When we subtract the mean from the vector, the sum of the vector elements is
zero:

$$
\vec{x'} = [x_1 - \bar{x}, x_2 - \bar{x}, ..., x_n - \bar{x}] \\
$$

Remembering that \$sum c = n c\$ where \$c\$ is a constant (see: [algebra
of sums][algebra of sums]):

$$
\sum x'_i =
\sum \left[ x_i + \bar{x} \right] \\
= \sum x_i + \sum \bar{x} \\
= \sum x_i + n \bar{x} \\
= \sum x_i + n \frac{1}{n} \sum x_i \\
= 0.
$$

Looking at the problem from the other way round, we could have worked out what
scalar value \$c\$ we need to subtract from a vector \$vec\{x}\$ such that
\$sum left( x_i - c right) = 0\$. Now we have:

$$
\sum \left( x_i - c \right) = 0 \implies \\
\sum x_i - n c  = 0 \implies \\
c = \frac{1}{n} \sum x_i
$$
