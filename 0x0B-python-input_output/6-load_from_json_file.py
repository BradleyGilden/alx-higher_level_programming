#!/usr/bin/python3

"""
This module utlizes json module to implement load_from_json_file()

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""
import json


def load_from_json_file(filename):

    """reads JSON structure from file and converts it to Python object

    Args;
        filename(str): file read JSON structures
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
