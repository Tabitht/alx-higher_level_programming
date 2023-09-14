#!/usr/bin/python3

""" Defines a function that creates an object from a json file """

import json


def load_from_json_file(filename):
    """ returns the created object """
    with open(filename) as f:
        return json.load(f)
