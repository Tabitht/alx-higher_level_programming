#!/usr/bin/python3

""" Defines the class rectangle an inheritance of class base """

from models.base import base


class rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

        @widthgetter
        def width(self):
            return self.width
        @widthsetter
        def width(self):
            if 

