#!/usr/bin/python3

""" It that writes an Object to a text file, using a JSON representation """

import json


def save_to_json_file(my_obj, filename):
    """ accepts python object and saves json representation of the file """

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
