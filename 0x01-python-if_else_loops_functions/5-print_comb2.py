#!/usr/bin/python3
for number in range(0, 100): # print combination seperated by a comma ,
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
