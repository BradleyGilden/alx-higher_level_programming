#!/usr/bin/python3

for i in range(0, 100):  # prints numbers in decimal seperated by comma
    if i != 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{:d}".format(i))
