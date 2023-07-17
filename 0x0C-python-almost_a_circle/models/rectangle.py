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

    def area(self):
        """returns the area (width*height) of a Rectangles instance"""
        return self.__width * self.__height

    def display(self):
        """display area of Rectangle using #"""
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
            print("#" * self.__width)

    def __str__(self):
        """overwriting __str__ method to display:
        [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return f"""[Rectangle] ({self.id:d}) {self.__x:d}/{self.__y:d} - \
{self.__width:d}/{self.__height:d}"""

    def update(self, *args, **kwargs):
        """used to update object instance attributes
        order= (id, width, height, x, y)

        Args:
            args(tuple): variable integer arguments
            kwargs(dict): keyword arguments
        """
        keys = ["id", "width", "height", "x", "y"]
        if args and args != ():
            i = 0
            while i < len(args) and i < 5:
                if i == 0 and args[i] is None:
                    i += 1
                    continue
                setattr(self, keys[i], args[i])
                i += 1
        else:
            for key, value in kwargs.items():
                if key not in keys or (key == "id" and value is None):
                    continue
                setattr(self, key, value)

    def to_dictionary(self):
        """returns a dictionary representaion of Rectangle instance"""
        mylist = ['id', 'width', 'height', 'x', 'y']
        mydict = {}

        for key in mylist:
            mydict[key] = getattr(self, key)

        return mydict
