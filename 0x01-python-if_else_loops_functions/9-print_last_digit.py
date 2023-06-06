#!/usr/bin/python3
def print_last_digit(number):  # return and print last digit
    n = 0
    if number == 0:
        print(n, end="")
        return n
    elif number < 0:
        n = (-number) % 10
        print(n, end="")
        return (n)
    else:
        n = number % 10
        print(n, end="")
        return (n)
