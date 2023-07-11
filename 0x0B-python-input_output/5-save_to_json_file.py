#!/usr/bin/python3

"""
This module utlizes json module to implement save_to_json_string()

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""
import json


def save_to_json_file(my_obj, filename):

    """writes object to file using JSON representation

    Args;
        my_obj(any): object to be converted
        filename(str): file to be written to
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
