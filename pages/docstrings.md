# Docstrings

Quoting from the [Python glossary], a docstring is a "A string literal which
appears as the first expression in a class, function or module.".

A {doc}`string literal <string_literals>` is a string contained within quotes
or triple quotes.

Here is a docstring in a function:

>>> def func(arg1):
...     "This is the function docstring"
...     return arg1 * 4

It is useful to write docstrings for several reasons:

- the process of writing the docstring forces you to explain the function to
  yourself, and therefore write clearer code with better design;
- you and others using your function can read the docstring to see how to use
  your function;
- Python (via "help()") and [IPython] (via "func?") can read the docstring and
  return it to you, when you are working interactively;
- there are good tools, such as [Sphinx], that can process the docstrings to
  make attractive documentation. See {ref}`documentation-guidelines`.

## Using docstrings

You can use docstrings at your interactive Python or IPython prompt:

>>> help(func)
Help on function func:
\<BLANKLINE>
func(arg1)
    This is the function docstring
\<BLANKLINE>

In fact Python puts the docstring into the `__doc__` attribute of the
function:

>>> print(func.\_\_doc\_\_)
This is the function docstring

One of the most useful features of [IPython] is its ability to return
docstrings when you add a question mark and press return after the name of the
function you are interested in:

```ipython
In [1]: def func(arg1):
   ...:     "This is the function docstring"
   ...:     return arg1 * 4
   ...:

In [2]: func?
Signature: func(arg1)
Docstring: This is the function docstring
File:      ~/<ipython-input-2-0233609cddfb>
Type:      function
```
