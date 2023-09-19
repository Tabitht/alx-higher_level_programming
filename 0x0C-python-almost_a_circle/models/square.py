#!/usr/bin/python3
""" Defines a class square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ creates the class square """
    def __init__(self, size, x=0, y=0, id=None):
        """ initializes the class with the attributes of class rectangle """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ prints the __str__ representation of the string """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.width)

    @property
    def size(self):
        """ gets the value of size """
        return self.width

    @size.setter
    def size(self, value):
        """ sets the value of size """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns the key/value and arguments to its attributes """
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        number = 0
        for arg in args:
            if number == 0:
                if arg is None:
                    self.__init__(self.size, self.size, self.x, self.y)
                else:
                    self.id = arg
            if number == 1:
                self.width = arg
            if number == 2:
                self.x = arg
            if number == 3:
                self.y = arg
            number += 1

    def to_dictionary(self):
        """ returns the dictionary representation of rectangle """
        obj_dictionary = {"id": self.id,
                          "size": self.size, "x": self.x, "y": self.y}
        return obj_dictionary
