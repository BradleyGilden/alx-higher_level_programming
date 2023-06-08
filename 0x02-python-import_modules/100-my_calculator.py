#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv


# perfecting calculator program with error messages from 1_calculator
# if arg_count != 3, print Usage: ./100-my_calculator.py <a> <operator> <b>
# if operator is unknown, print:
# Unknown operator. Available operators: +, -, * and /
def my_switch(sign, a, b):
    if sign == '+':
        print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
    elif sign == '-':
        print("{:d} - {:d} = {:d}".format(a, b, sub(a, b)))
    elif sign == '*':
        print("{:d} * {:d} = {:d}".format(a, b, mul(a, b)))
    elif sign == '/':
        print("{:d} / {:d} = {:d}".format(a, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == '__main__':

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(argv[1])
        sign = argv[2]
        b = int(argv[3])
        my_switch(sign, a, b)
