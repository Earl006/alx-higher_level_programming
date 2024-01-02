#!/usr/bin/python3
"""

This module has one function that adds up 2 integers

"""
def add_integer(a, b=98):
      """Return the sum of two integers or floats as integers

    Args:
        a: first argument
        b: second argument

    Returns:
        Sum of the two arguments

    Raises:
        TypeError: If either of the arguments not an integer or a float
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return (int(a) + int(b))
