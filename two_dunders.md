# Two double underscore variables

Python often uses variable and function and method names with double
underscores on each end.

For example, as Python sets up to import a module, it defines a variable for
itself called `__file__`.

Experienced Python people often call these variables "dunder" variables,
because they have double underscores on each side.

When you see a *dunder* variable or function or method, it is almost
invariably a variable or function or method that Python has defined, or that
Python is using in a special way.

(file-variable)=

## The "\_\_file\_\_" variable

The `__file__` variable contains the path to the file that Python is
currently importing.  You can use this variable inside a module to find the
path of the module.  For example, let's say you have a module like this:

```{eval-rst}
.. runblock::
    :hide:

    rm -rf example_module.py* another_example.py*
```

```{eval-rst}
.. writefile:: example_module.py

    # An example Python module
    print("Type of __file__ variable is:", type(__file__))
    print("__file__ is:", __file__)
```

If you run this module as a script, `__file__` is set:

```{eval-rst}
.. runblock::

    python3 example_module.py
```

If you `import` the module, `__file__` is also set:

```{eval-rst}
.. runblock::

    # Run Python code with "-c" flag
    python3 -c "import example_module"
```

(name-variable)=

## The "\_\_name\_\_" variable

When Python imports a module, it sets the `__name__` variable to be a string
containing the name of the module it is importing:

```{eval-rst}
.. writefile:: another_example.py

    # Another example Python module
    print("Type of __name__ variable is:", type(__name__))
    print("__name__ is:", __name__)
```

```{eval-rst}
.. runblock::

    python3 -c "import another_example"
```

If you run the same module as a script, Python is not importing when it runs
the code, and `__name__` contains the string `"__main__"`:

```{eval-rst}
.. runblock::

    python3 another_example.py
```

```{eval-rst}
.. runblock::
    :hide:

    rm -rf example_module.py* another_example.py*
```
