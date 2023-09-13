#!/usr/bin/python3
def inherits_from(obj, a_class):
    """ checks if an object inherited directly or indirectly from the soecified class
    args:
        obj - the object to check
        a_class - the class to check with
    Returns:
        True if inherited else False
    """
    return type(obj) != a_class and isinstance(obj, a_class)
