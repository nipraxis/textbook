# Inserting values into strings

Use the string methd `format` method to create new strings with inserted
values. Here we insert a string into another string:

>>> shepherd = "Mary"
>>> print("Shepherd {} is on duty.".format(shepherd))
Shepherd Mary is on duty.

The curly braces show where the inserted value should go.

You can insert more than one value.  The values do not have to be strings,
they can be numbers and other Python objects.

>>> shepherd = "Mary"
>>> age = 32
>>> print("Shepherd {} is {} years old.".format(shepherd, age))
Shepherd Mary is 32 years old.

>>> 'Here is a {} floating point number'.format(3.33333)
'Here is a 3.33333 floating point number'

You can do more complex formatting of numbers and strings using formatting
options within the curly brackets {{ -- }} see the documentation on [curly brace
string formatting][string formatting].

This system allows us to give formatting instructions for things like numbers,
by using a `:` inside the curly braces, followed by the formatting
instructions.  Here we ask to print in integer (`d`) where the number should
be prepended with `0` to fill up the field width of `3`:

>>> print("Number \{:03d} is here.".format(11))
Number 011 is here.

This prints a floating point value (`f`) with exactly `4` digits after the
decimal point:

>>> 'A formatted number - {:.4f}'.format(.2)
'A formatted number - 0.2000'

See the Python [string formatting] documentation for more details and
examples.
