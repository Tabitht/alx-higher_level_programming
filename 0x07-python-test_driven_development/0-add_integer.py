#!/usr/bin/python3
""" defines the addition of two numbers """


def add_integer(a, b=98):
    """ Returns the addition of a and b.
    a and b must first be casted into integers if they are float.
    Error to raise:
      TypeError if a and b is not an integer.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if (not isinstance(b, int) and not isinstance(b, float)):
        raise TypeError("b must be an integer")
    return a + b
