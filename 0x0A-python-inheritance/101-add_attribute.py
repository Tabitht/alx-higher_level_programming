#!/usr/bin/python3

""" Defines a function add_attribute """


def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.
    Args:
        obj: The object to add an attribute to.
        att: The name of the attribute to add to obj.
        value: The value of the attribute.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
