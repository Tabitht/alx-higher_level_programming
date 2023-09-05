#!/usr/bin/python3
""" Defines a function that prints a string """


def say_my_name(first_name, last_name=""):
    """ prints My name is <first name> <last name>
    args:
        firts_name - first name to be printed
        last_name - last name to be printed
    Error to raise:
        TypeError - if first and second parameter are not strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
