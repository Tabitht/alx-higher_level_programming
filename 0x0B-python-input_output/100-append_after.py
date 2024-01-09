#!/usr/bin/python3
""" defines a function that inserts text to a file """

def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file after each line containing a specific string.
    Args:
    filename: name of the file.
    search_string: The string you are searching for within the file.
    new_string: The string to insert.
    """
    text = ""
    with open(filename) as f:
        for lines in f:
            text += lines
            if search_string in lines:
                text += new_string
    with open(filename, "w") as n:
        n.write(text)


