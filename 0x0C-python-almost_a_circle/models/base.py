#!/usr/bin/python3

"""
This module contains the Base class which is the parent class of all the
other classes in the models package.

Date: 13/07/2023
Author: Bradley Dillion Gilden
"""


import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries

        Args:
            list_dictionaries([{}]): a list of dictionaires
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string representation of {list_objs} to {Class.json}

        Args:
            list_objs(Rectangle or Square): list of objects
        """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            with open(filename, "w", encoding="utf-8") as file:
                file.write("[]")
        else:
            expand_list = [obj.to_dictionary() for obj in list_objs]
            json_list = cls.to_json_string(expand_list)
            with open(filename, "w", encoding="utf-8") as file:
                file.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """converts JSON string to a list of dictionaries

        Args:
        json_string(str): JSON string
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a new instance of Square or Rectangle with all it's
        attributes set to values in dictionary

        Args:
        dictionary(dict): variable keyword arguments
        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy
