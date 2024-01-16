#!/usr/bin/python3

""" Defines the class rectangle an inheritance of class base """

from models.base import Base


class Rectangle(Base):
    """ creates a class called Rextangle """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes the class Rectangle
        Args:
            width: the width of the new rectangle
            height: the height of the new rectangle
            x: the new coordinate
            y: the new coordinate
            id: the identity of the rectangle
            Raises:
                TypeError: if either width or height are not integers
                ValueError: if either width or height <= 0
                TypeError: if either x or y is not an integer
                ValueError: if either x or y is <= 0"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """ gets the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        """ validates and set the value of width """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ gets the value of height """
        return self.__height

    @height.setter
    def height(self, value):
        """ validates and sets the value of height """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ gets the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ validates and sets the value of x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")

        self.__x = value

    @property
    def y(self):
        """ gets the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ validates and sets the value of y """
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ it calculates the area of a rectangle """
        return (self.height * self.width)

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        if self.width == 0 or self.height == 0:
            print("")
            return
        [print("") for y in range(self.y)]
        for h in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print("#", end="") for w in range(self.width)]
            print("")

    def __str__(self):
        """ returns the __str__ method of the string """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x,
                                                        self.y, self.width,
                                                        self.height))

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute and also its
        key/value arguments """
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
        """ returns the dictionary representation of a Rectangle """
        obj_dictionary = {"id": self.id, "width": self.width,
                          "height": self.height, "x": self.x, "y": self.y}
        return obj_dictionary
