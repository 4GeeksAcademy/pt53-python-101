"""
We can either use multiline strings for comments,
or the pound sign/octothorpe (#) for them.
"""
import math
from itertools import chain
from fractions import Fraction

# let someVariable = "some value"
some_variable = "some value"

# Strings:
some_string = "Any string between double or single quotes."
some_other_string = 'Just like this!'
some_ml_sting = """
These strings can have break returns in them, and as long as you don't put 3
of the "quote marks" that surround the string in a row in them, they
will remain open!  These work with the half-quote as well, e.g.: '''Some multiline string'''
"""

some_fstring = f"This string can have variables inside it! {math.pi}"
# print(some_fstring)

# Numbers
some_int = 0
some_big_int = 1_000_000_000
some_float = 0.0
some_int_div = 10 // 3
some_float_div = 10 / 3
# print(some_int_div, some_float_div)

# Python is respectable, it doesn't claim that this is infinity:
# 1/0

# Booleans (this will trip you up, it still gets me)
some_bool = True
some_bool = False

# Arrays?  Nope, we get Lists.
some_list = [
    "This is pretty much just an array, a la JS.",
    "They work much the same as well, with some diffs.",
    "e.g.: there is no length property on a list.",
    "Instead use the len() function.",
]
some_tuple = (1, 2, 3, 4, 5, 6)

# some_list[0] = "new value!"
# print(some_list)

# This is an error, because tuples are nonmutable (can't be changed.)
# some_tuple[0] = 90210

# Objects?  Nope, we get dictionaries.
some_dict = {
    "key": "value",
}

# You can't use dot notation!  Use square braces instead!
# print(some_dict["key"])

# On the flip side, merging dicts is pretty straightforward.
# print({**{"a": 1, "b": 2}, **{"b": 3, "c": 4}})

# Null?  Nope, we get None.
some_none = None

some_iterable = ["Un", "Deux", "Trois", "Cat", "Sank", "Oiseaux"]

# Iteration!
# for word in some_iterable:
#     print(word)

# some_exit_val = True

# while some_exit_val:
#     print("This loop should eventually end!")
#     some_exit_val = False

# Control flow!

# for word in some_iterable:
#     if len(word) < 5:
#         print(word.lower())
#     elif len(word) < 7:
#         print(word.capitalize())
#     else:
#         print(word.upper())

def some_function(*args, **kwargs):
    """
    This function accepts arbitrary args and
    kwargs, and prints them to the command line
    """
    print(args)
    print(kwargs)

# some_function(4, 5, 6, a=1, b=2, c=3)

"""
What about anonymous functions?
const someFunc = () => {
    // do stuff
}

Nope, we get lambdas.
"""

some_lambda = lambda x: print(x)

def some_other_func(x):
    print(x)

a = {"a": 1}
b = {"a": 1}

if a == b:
    print("These are equal")

if a is b:
    print("But these are not identical")

print(id(a))
print(id(b))
