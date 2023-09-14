#!/usr/bin/python3

""" a function that writes a text """


def write_file(filename="", text=""):
    """ wites a text and return the number written """
    with open(filename, 'w') as f:
        return f.write(text)
