#!/usr/bin/python3

""" a function that opens a file """


def read_file(filename=""):
    """ It opens a file and prints it to stdout
    Return:
        None
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
