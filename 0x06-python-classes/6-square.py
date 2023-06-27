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
        position(tuple): stores positional co-ordinates of Square
    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__ - constructor
        Args:
            size(int): size of square
            position(tuple): position of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if not isinstance(position, tuple) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(position[0], int)\
                or not isinstance(position[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__size = size
        self.__position = position

    def area(self):
        """Returns current square area"""
        return self.__size**2

    @property
    def size(self):
        """size getter method"""
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

    @property
    def position(self):
        """position getter method"""
        return self.__position

    @position.setter
    def position(self, value):
        """position setter method
        value(tuple): tuple of co-ordinates"""
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """prints square using pound(#) symbol"""
        if self.__size == 0:
            print()
            return
        if self.__position[1] > 0:
            print("\n" * self.__position[1], end="")
        for _ in range(0, self.__size):
            if self.__position[0] > 0:
                print(" " * self.__position[0], end="")
            print("#" * self.__size)
