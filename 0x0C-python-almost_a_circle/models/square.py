#!/usr/bin/python3

"""
This module contains the Square class which inherits from the Rectangle class

Date: 13/07/2023
Author: Bradley Dillion Gilden
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """This class creates a Square object with {size} parameters at position
    {x, y}

    Args:
        size(int): length of all sides of square object
        x(int): x position
        y(int): y position
        id(int): object id
    """
    def __init__(self, size, x=0, y=0, id=None):
        """The constructor method for the Square class"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """overwriting __str__ method to display:
        [Square] (<id>) <x>/<y> - <size>
        """
        return f"""[Square] ({self.id:d}) {self.x:d}/{self.y:d} - \
{self.width:d}"""

    @property
    def size(self):
        """getter method for size property"""
        return self.width

    @size.setter
    def size(self, size):
        """setter method for size property"""
        if type(size) != int:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")

        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """used to update object instance attributes
        order= (id, size, x, y)

        Args:
            args(tuple): variable integer arguments
            kwargs(dict): keyword arguments
        """
        keys = ["id", "size", "x", "y"]
        if args and args != ():
            i = 0
            while i < len(args) and i < 4:
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
        """returns a dictionary representaion of Square instance"""
        mylist = ['id', 'size', 'x', 'y']
        mydict = {}

        for key in mylist:
            mydict[key] = getattr(self, key)

        return mydict
