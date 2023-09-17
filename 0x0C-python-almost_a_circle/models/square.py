#!/usr/bin/python3
""" Defines a class square """

from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
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
        obj_dictionary = {"id": self.id,
                          "size": self.size, "x": self.x, "y": self.y}
        return obj_dictionary
