#!/usr/bin/python3
for number in range(0, 100):  # print string seperated by a comma,space
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
