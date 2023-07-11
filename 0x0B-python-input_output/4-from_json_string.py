#!/usr/bin/python3

"""
This module utlizes json module to implement from_json_string()

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""
import json


def from_json_string(my_str):
    """converts JSON string to Python object

    Args;
        my_str(str): JSON string

    Returns:
        Python Object
    """
    return json.loads(my_str)
