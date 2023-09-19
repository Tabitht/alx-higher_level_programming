#!/usr/bin/python3

""" Defines the class rectangle an inheritance of class base """

from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(int, value):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(int, value):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            return self.__x

        @x.setter
        def x(self, value):
            if not isinstance(int, value):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")

            self.__x = value

        @property
        def y(self):
            return self.__y

        @y.setter
        def y(self, value):
            if not isinstance(int, value):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

    def area(self):
        return (self.height * self.width)

    def display(self):
        print("{}".format("\n" * self.x), end="")
        for i in range(self.height):
            print("{} {}".format(" " * self.y, "#" * self.width), end="")
            print()

    def __str__(self):
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        if len(args) == 0:
            for key, value in kwargs.items():
                self.__setattr__(key, value)
            return
        number = 0
        for arg in args:
            if number == 0:
                if arg is None:
                    self.__init__(self.width, self.height, self.x, self.y)
                else:
                    self.id = arg
            if number == 1:
                self.width = arg
            if number == 2:
                self.height = arg
            if number == 3:
                self.x = arg
            if number == 4:
                self.y = arg
            number += 1

    def to_dictionary(self):
        obj_dictionary = {"id": self.id, "width": self.width,
                          "height": self.height, "x": self.x, "y": self.y}
        return obj_dictionary
