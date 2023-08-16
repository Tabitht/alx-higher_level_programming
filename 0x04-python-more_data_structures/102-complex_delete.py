#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for keys in a_dictionary:
        if a_dictionary[keys] == value:
            del keys
        else:
            return a_dictionary
    return a_dictionary
