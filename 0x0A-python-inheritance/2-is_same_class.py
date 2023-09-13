#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ to check whether an object is an instance of a specified class
    args:
        obj - the object to check
        a_class - the class to check with
    Returns:
        True if object is an insance else returns  False
    """
    if type(obj) == a_class:
        return True
    else:
        return False
