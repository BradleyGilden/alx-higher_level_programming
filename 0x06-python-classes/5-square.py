#!/usr/bin/python3

"""
This module contains a Square class

Author: Bradley Dillion Gilden
Date: 27-06-2023
"""


class Square:
    """Square initialises an instance attribute
    Attributes(instance):
        @private
        size(int): stores the size of an object of Square
    """
    def __init__(self, size=0):
        """__init__ - constructor
        Args:
            size(int): size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns current square area"""
        return self.__size ** 2

    @property
    def size(self):
        """size get method"""
        return self.__size

    @size.setter
    def size(self, value):
        """size setter method
        value(int): value to set"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """prints square using pound(#) symbol"""
        if self.__size == 0:
            print()
            return
        for i in range(0, self.__size):
            print('#' * self.__size)
