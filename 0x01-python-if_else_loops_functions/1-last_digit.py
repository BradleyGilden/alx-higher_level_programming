#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# modulo operation changes in python when negative % postive, so use -10
prompt0 = "Last digit of"
prompt1 = "and is greater than 5"
prompt2 = "and is less than 6 and not 0"
if number < 0:
    last = number % -10
else:
    last = number % 10

if last == 0:
    print(prompt0, number, "is 0 and is 0")
elif last > 5:
    print(prompt0, number, "is", last, prompt1)
else:
    print(prompt0, number, "is", last, prompt2)
