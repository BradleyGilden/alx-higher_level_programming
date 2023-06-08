#!/usr/bin/python3
from add_0 import add


if __name__ == '__main__':
    a = 1
    b = 2
    # imports method "add" from file "add_0" to be run in py script
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
