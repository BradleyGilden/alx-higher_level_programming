#!/usr/bin/python3

# for every 'search' value, replace it with variabe: replace
def search_replace(my_list, search, replace):
    if my_list == [] or search not in my_list:
        return my_list
    new_list = my_list[:]

    for i in range(0, len(new_list)):
        new_list[i] = replace if new_list[i] == search else new_list[i]

    return new_list
