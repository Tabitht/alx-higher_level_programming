#!/usr/bin/python3

""" Defines a class named base """

import json


class Base:
    """ creates a class Base, a base for all other classes """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes the class Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the json representation of a list
        @list_dictionaries - list to convert
        Returns:
            the json representation
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)
