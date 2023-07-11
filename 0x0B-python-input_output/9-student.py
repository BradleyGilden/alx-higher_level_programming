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

    def to_json(self):
        """returns dictonary representation of Student object"""
        return self.__dict__
