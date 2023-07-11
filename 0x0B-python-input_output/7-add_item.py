#!/bin/python3

"""
This module adds items to python list to save them to a file

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""
import sys


if __name__ == '__main__':
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"

    try:
        obj_list = load_from_json_file(filename)
    except FileNotFoundError:
        obj_list = []
    if len(sys.argv) > 1:
        for i in range(1, len(sys.argv)):
            obj_list.append(sys.argv[i])
    save_to_json_file(obj_list, filename)
