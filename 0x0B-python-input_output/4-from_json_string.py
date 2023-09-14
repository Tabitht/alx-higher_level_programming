#!/usr/bin/python3

""" A function that returns an object represented by JSON string """

import json


def from_json_string(my_str):
    """ it returns the json string representation of the object """

    return json.loads(my_str)
