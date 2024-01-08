#!/usr/bin/python3

""" a function that checks for inheritance """


def inherits_from(obj, a_class):
    """ checks if an object inherited from specified class
    args:
        obj - the object to check
        a_class - the class to check with
    Returns:
        True if inherited else False
    """
    return type(obj) != a_class and isinstance(obj, a_class)
