#!/usr/bin/python3

""" a function that returns the list """

def lookup(obj):
    """ returns all attributes and methods of a class
    Returns:
        a list object
    """
    return dir(obj)
