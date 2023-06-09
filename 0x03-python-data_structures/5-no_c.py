#!/usr/bin/python3

# removes all occurences of C and c in string
def no_c(my_string):

    my_list = list(my_string)

    for i in range(len(my_list)):
        if my_list[i] == 'C' or my_list[i] == 'c':
            my_list[i] = ''

    return("".join(my_list))
