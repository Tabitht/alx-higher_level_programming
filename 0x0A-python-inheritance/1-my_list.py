#!/usr/bin/python3

""" module - my list """


class MyList(list):
    """ A class that inherits from another class
    prints:
        it prints the list in a sorted form
    """
    def print_sorted(self):
        print(sorted(self))
