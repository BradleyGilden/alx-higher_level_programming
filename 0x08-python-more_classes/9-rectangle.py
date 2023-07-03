#!/usr/bin/python3

"""
module contains an encapsulated class {Rectangle}

Author: Bradley Dillion Gilden
Date: 03-07-2023
"""


class Rectangle:
    """This class contains integer properties {width} and {height}

    Attributes:
        number_of_instances(int): counts the number of Rectangle instances
        print_symbol(any): assigns symbol for rectangular representation
    """
    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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

    def __str__(self):
        """returns string visually representing Rectangle object using #

        Note: returns empty string if width or height = 0
        """
        if self.__width == 0 or self.__height == 0:
            return ""

        s_list = []
        for i in range(self.__height):
            if i == self.__height - 1:
                s_list.append(str(self.print_symbol) * self.__width)
                break
            s_list.append(str(self.print_symbol) * self.__width)
            s_list.append("\n")
        string = "".join(s_list)
        return string

    def __repr__(self):
        """returns string showing the class from which the object instance
        was created

        Example:
            obj = Rectangle(2, 4)
            obj.__repr__
            'Rectangle(2, 4)'
        """
        return f"Rectangle({self.__width:d}, {self.__height:d})"

    def __del__(self):
        """Destructor for an instance of Rectangle when using del keyword"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """a static method that returns the Rectangle object with the biggest
        area

        Args:
            rect1(Rectangle): first object in comparison
            rect2(Rectangle): second object in comparison

        Raises:
            TypeError: if rect_1 or rect_2 are not instances of Rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        """returns a new Rectangle instance with width == height == size"""
        return cls(size, size)
