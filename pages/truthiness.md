(equivalent-to-true)=

# Kind-of True

See: [truthiness in Python] and Python [truth value testing].

There are several places where you will find Python applying a test of True
that is more general than simply `val == True`.

One example is in `if` statements:

```Python
>>> val = 'a string'  # A not-empty string is True for truth testing
>>> if val:
...     print('Truth testing of "val" returned True')
Truth testing of "val" returned True
```

Here the `if val:` clause applies Python [truth value testing] to `'a
string'`, and returns True. This is because the truth value testing
algorithm returns True from an not-empty string, and False from an empty
string:

```Python
>>> another_val = ''
>>> if another_val:
...     print('No need for a message, we will not get here')
```

You can see the results of truth value testing using `bool()` in Python.
For example:

```Python
>>> bool(True)
True
>>> bool(False)
False
>>> bool(['some', 'elements'])  # not-empty list tests as True
True
>>> bool([])  # an empty list tests as False
False
>>> bool(10)  # any number other than zero evaluates as True
True
>>> bool(1)
True
>>> bool(0)
False
>>> bool(None)  # None tests as False
False
```

Examples of situations in which Python uses truth value testing are `if`
statements; `while statements` and {doc}`assert statements <assert>`.
