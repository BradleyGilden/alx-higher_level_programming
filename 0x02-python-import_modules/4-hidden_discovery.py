#!/usr/bin/python3
import hidden_4


# This script prints all the methods listed in hidden4.pyc
if __name__ == '__main__':
    m_list = dir(hidden_4)

    for method in m_list:
        if method[0] != '_' and method[1] != '_':
            print(method)
