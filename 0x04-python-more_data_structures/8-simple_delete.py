#!/usr/bin/python3

# deletes entry in dictionary

def simple_delete(a_dictionary, key=""):
    if key in a_dictionary.keys():
        a_dictionary.pop(key)
        return a_dictionary
    else:
        return a_dictionary
