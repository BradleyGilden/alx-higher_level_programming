#!/usr/bin/python3

# return a bool list of True/False depending if a number is divisible by 2

def divisible_by_2(my_list=[]):
    bool_list = []

    for num in my_list:
        if num % 2 == 0:
            bool_list.append(True)
        else:
            bool_list.append(False)

    return(bool_list)
