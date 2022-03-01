# Using `assert` for testing

The Python `assert` statement means - "raise an error unles the following
expression is equivalent to True".

By "equivalent to True", I mean the expression returns True from Python
{doc}`truth value testing <truthiness>`.

`assert` raises an `AssertionError` if the statement is equivalent to
False.  It does nothing if the statement is equivalent to True.

So, if you `assert an_expression` and there is no error, then the result of
`an_expression` was equivalent to True.  The following expressions evaluate
to True, and therefore the asserts do not raise an error:

```Python
>>> assert True
>>> assert 10 == 10
>>> assert 10 % 2 == 0
```

These expressions are equivalent to False, and the asserts do raise errors:

```Python
>>> assert False
Traceback (most recent call last):
   ...
AssertionError
>>> assert 10 == 11
Traceback (most recent call last):
   ...
AssertionError
```

Although `assert` does work with expression values of True and False, the test
that assert uses is more general than `expr_result == True`.  In fact,
assert uses {doc}`truth value testing <truthiness>` to decide whether to raise
an `AssertionError` or not:

```Python
>>> assert ['some', 'elements']  # not-empty list tests as True
>>> assert []  # an empty list tests as False
Traceback (most recent call last):
   ...
AssertionError
>>> assert 10  # any number other than zero evaluates as True
>>> assert 1
>>> assert 0
Traceback (most recent call last):
   ...
AssertionError
>>> assert None
Traceback (most recent call last):
   ...
AssertionError
```
