#!/usr/bin/python3

"""
This module contains the Base class which is the parent class of all the
other classes in the models package.

Date: 13/07/2023
Author: Bradley Dillion Gilden
"""


class Base:
    """Manages id in inheritted classes and to avoid code/bug duplication

    Args->public:
        id(int): if {id} is not None, the public instance attribute {self.id}
        is assigned the value of {id}

    Attribute->private:
        nb_objects(int): A private class attribute that is incremented and
        assigned to the public instance attribute {self.id} if id is None
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method for the Base class, initialized {self.id}"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
