#!/usr/bin/python3
""" Defines a class student """

class Student:
    """ Represent a class student """
    def __init__(self, first_name, last_name, age):
        """ method initialization.
        Args:
            first_name: The first name of the student
            last_name: The last name of the student.
            age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Gets a dictionary representation of the student.
        if attrs is a list of string, represent only those attribute present in the list.
        Args:
            attrs: (optional) the attribute to represent
        """
        if (type(attrs) == list and all(type(ele)
                == str for ele in attrs)):
            return {k: getattr(self, k)for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ replace all attribute of the student
        Args:
        json: The key/value pair to replace attribute with
        """
        for k, v in json.items():
            setattr(self, k, v)

