#!/usr/bin/python3

"""
This module contains say_my_name() that prints a persons full name

Author: Bradley Dillion Gilden
Date: 29-06-2023
"""


def say_my_name(first_name, last_name=""):
    """This function prints: My name is <first_name> <last_name>

    Args:
        first_name(str): persons first name
        last_name(str): persons last name (not mandatory)

    Raises:
        TypeError: if first_name or last_name is not of type str
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
