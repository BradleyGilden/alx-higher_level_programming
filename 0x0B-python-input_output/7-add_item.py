#!/bin/python3

"""
This is a script for dumping and loading objects to and from json files

Author: Bradley Dillion Gilden
Date: 11-07-2023
"""
from sys import argv


if __name__ == '__main__':
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file

    filename = "add_item.json"

    try:
        obj_list = load_from_json_file(filename)
    except FileNotFoundError:
        obj_list = []
    if len(argv) > 1:
        for i in range(1, len(argv)):
            obj_list.append(argv[i])
    save_to_json_file(obj_list, filename)