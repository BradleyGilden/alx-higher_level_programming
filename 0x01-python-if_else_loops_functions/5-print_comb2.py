#!/usr/bin/python3

for i in range(0, 100):  # displays a number combination seprated by ", "
    if i != 99:
        print("{:02d}".format(i), end=", ")
    else:
        print("{}".format(i))
