#!/usr/bin/python3

"""
module contains class {Rectangle} with width and height properties

Author: Bradley Dillion Gilden
Date: 03-07-2023
"""


class Rectangle:
    """This class contains integer properties {width} and {height}"""
    def __init__(self, width=0, height=0):
        """constructor for the Rectangle class

            Args:
                width(int): width of Rectangle instance
                height(int): height of Rectangle instance
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter method for the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for the width property

        Args:
            value(int): value set to width property

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter method for the height property"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter method for the height property

        Args:
            value(int): value set to height property

        Raises:
            TypeError: if value is not an integer
            ValueError: if value < 0
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
