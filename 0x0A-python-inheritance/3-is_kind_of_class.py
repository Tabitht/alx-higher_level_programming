#!/usr/bin/python3

""" module: 2-is_same_class """

def is_kind_of_class(obj, a_class):
    """ checks if an obj is an instance of an inheritance
    args:
        obj - the object to check
        a_class - the inheriatnce or class to check with
    Returns:
        True if it is an instance else false
    """
    return isinstance(obj, a_class)
