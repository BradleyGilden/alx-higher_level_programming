#!/usr/bin/python3

"""
This module contains class Student

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""


class Student:
    """this class contains Student descriptions

    Args:
        first_name(str): students first name
        last_name(str): students last name
        age(int): students age
    """

    def __init__(self, first_name, last_name, age):
        """constructor for student class"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """returns dictonary representation of Student object

        Args;
            attrs(list): list of attributes represented as strings"""
        if (attrs is None or type(attrs) != list or
                not all(type(strings) == str for strings in attrs)):
            return self.__dict__

        custom_dict = {}

        for attributes in attrs:
            # checks if attribute exists before assigning
            if attributes in self.__dict__:
                custom_dict[attributes] = getattr(self, attributes)

        return custom_dict

    def reload_from_json(self, json):
        """reloads Student object with attributes from json

        Args:
            json(dict): dictionary of python object
        """
        for attributes in json:
            if (attributes in self.__dict__ and not attributes.startswith("_")
                    and not attributes.startswith("__")):
                self.__dict__[attributes] = json[attributes]
