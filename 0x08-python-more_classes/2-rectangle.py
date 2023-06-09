#!/usr/bin/python3

"""
module contains an encapsulated class {Rectangle}

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

            Raises:
                TypeError: if width or height is not an integer
                ValueError: if (width or height) < 0
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter method for the width property"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter method for the width property

        Args:
            value(int): value set to width property
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
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns area of Rectange object: width * height"""
        return self.__width * self.__height

    def perimeter(self):
        """returns perimeter of rectangle: 2*width + 2*height

        Note: if width or height is 0, perimeter returned will also be 0
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.__height)
