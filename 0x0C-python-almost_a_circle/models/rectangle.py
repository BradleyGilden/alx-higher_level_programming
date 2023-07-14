#!/usr/bin/python3

"""
This module contains the Rectangle class which inherits from the Base class

Date: 13/07/2023
Author: Bradley Dillion Gilden
"""


from models.base import Base


class Rectangle(Base):
    """A class that creates an object with width and height paramters

    Args:
        width(int): width of rectangle
        height(int): height of rectangle
        x(int): x postion
        y(int): y position
        id(int): object id
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """the constructor method for Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width property for Rectangle object"""
        return self.__width

    @property
    def height(self):
        """height property for Rectangle object"""
        return self.__height

    @property
    def x(self):
        """x co-ordinate property for Rectangle object"""
        return self.__x

    @property
    def y(self):
        """y co-ordinate property for Rectangle object"""
        return self.__y

    @width.setter
    def width(self, width):
        """setter method for width property"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

        self.__width = width

    @height.setter
    def height(self, height):
        """setter method for height property"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")

        self.__height = height

    @x.setter
    def x(self, x):
        """setter method for x co-ordinate property"""
        if type(x) != int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")

        self.__x = x

    @y.setter
    def y(self, y):
        """setter method for y co-ordinate property"""
        if type(y) != int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")

        self.__y = y
