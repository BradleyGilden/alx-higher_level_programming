#!/usr/bin/python3

"""
This is the Geometry module containing class: Rectangle

Author: Bradley Dillion Gilden
Date: 10-07-2023
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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

    def area(self):
        """calculates the area of a Rectangle object"""
        return self.__width * self.__height

    def __str__(self):
        """shows string representation of Rectangle object"""
        return f"[Rectangle] {self.__width}/{self.__height}"
