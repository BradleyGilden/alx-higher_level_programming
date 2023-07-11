#!/usr/bin/python3

"""
This module utlizes json module to implement to_json_string()

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""
import json


def to_json_string(my_obj):
    """converts object into JSON string representation

    Args;
        obj(any): object to be converted

    Returns:
        JSON string
    """
    return json.dumps(my_obj)
