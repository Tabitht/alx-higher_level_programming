#!/usr/bin/python3

""" A function that appends to a file """


def append_write(filename="", text=""):
    """ appends a text at the end of the file """
    with open(filename, 'a') as f:
        return f.write(text)
