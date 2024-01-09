#!/usr/bin/python3

""" A function that returns the json representation of an object """

import json


def to_json_string(my_obj):
    """ It will return the json representation """
    return json.dumps(my_obj)
