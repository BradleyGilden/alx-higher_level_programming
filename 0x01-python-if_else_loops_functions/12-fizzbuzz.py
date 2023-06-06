#!/usr/bin/python3

# print Fizz for multiples of 3
# print Buzz for multiples of 5
# print FizzBuzz for multiples of both 3 and 5
# do this for a rang of 1 -> 100
def fizzbuzz():
    for i in range(1, 101):
        if (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
