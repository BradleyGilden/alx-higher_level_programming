#!/usr/bin/python3

"""
This is the Geometry module containing class: BaseGeometry

Author: Bradley Dillion Gilden
Date: 10-07-2023
"""


class BaseGeometry:
    """This class contains functions that raise exceptions

    Raises:
        Exception: when area() is called
        TypeError: if value is not an integer
        ValueError: if value <= 0
    """

    def area(self):
        """raises an Exception always"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if value is a correct type of integer

        Args:
            name(str): is always a string
            value(int): a non-zero positive integer value
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """The rectangle class is a subclass of BaseGeometry

    Args:
        width(int): width of Rectangle object
        height(int): height of Retangle object
    """
    def __init__(self, width, height):
        """The constructor method for initializing width and height of a
        Rectangle object
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
