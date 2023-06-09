#!/usr/bin/python3

# returns key with biggest score
def best_score(a_dictionary):

    if a_dictionary is None or len(a_dictionary) == 0:
        return None

    large_name = list(a_dictionary.keys())[0]
    large_value = a_dictionary[large_name]

    for key, value in a_dictionary.items():
        if value > large_value:
            large_value = value
            large_name = key

    return large_name
