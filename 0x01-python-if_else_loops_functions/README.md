# Conditionals, Loops and Functions in Python

**This repository tackles pythons unique way of handling conditional statements, loops and functions**

## Files in Directory:

* [0-positive_or_negative.py](0-positive_or_negative.py) -
* [1-last_digit.py](1-last_digit.py) -
* [2-print_alphabet.py](2-print_alphabet.py) -
* [3-print_alphabt.py](3-print_alphabt.py) -
* [4-print_hexa.py](4-print_hexa.py) -
* [5-print_comb2.py](5-print_comb2.py) -
* [6-print_comb3.py](6-print_comb3.py) -
* [7-islower.py](7-islower.py) -
* [8-uppercase.py8-uppercase.py](8-uppercase.py) -
* [9-print_last_digit.py](9-print_last_digit.py) -
* [10-add.py](10-add.py) - Write a function that adds two integers and returns the result.
  * Prototype: `def add(a, b):`
  * Returns the value of `a + b`
* [11-pow.py](11* -pow.py) - Write a function that computes `a` to the power of `b` and return the value. Requirements:
  * Prototype: `def pow(a, b):`
  * Returns the value of `a ^ b`
  * You are not allowed to import any module
* [12-fizzbuzz.py](12-fizzbuzz.py) - Write a function that prints the numbers from 1 to 100 separated by a space. Requirements:
  * For multiples of three print Fizz instead of the number and for multiples of five print `Buzz`.
  * For numbers which are multiples of both three and five print `FizzBuzz`.
  * Prototype: `def fizzbuzz():`
  * Each element should be followed by a space
  * You are not allowed to import any module
* [13-insert_number.c, lists.h](13-insert_number.c, lists.h) - Write a function in C that inserts a number into a sorted singly linked list.
* [100-print_tebahpla.py](100-print_tebahpla.py) - A program that prints the `ASCII` alphabet, in reverse order, alternating lowercase and uppercase (`z` in lowercase and `Y` in uppercase) , not followed by a new line.
* [101-remove_char_at.py](101-remove_char_at.py) - A function that creates a copy of the string, removing the character at the position `n` (not the Python way, the “C array index”).
* [102-magic_calculation.py](102-magic_calculation.py) - Write the Python function def `magic_calculation(a, b, c):` that does exactly the same as the following Python bytecode:
  ```
  3           0 LOAD_FAST                0 (a)
              3 LOAD_FAST                1 (b)
              6 COMPARE_OP               0 (<)
              9 POP_JUMP_IF_FALSE       16

  4          12 LOAD_FAST                2 (c)
             15 RETURN_VALUE

  5     >>   16 LOAD_FAST                2 (c)
             19 LOAD_FAST                1 (b)
             22 COMPARE_OP               4 (>)
             25 POP_JUMP_IF_FALSE       36

  6          28 LOAD_FAST                0 (a)
             31 LOAD_FAST                1 (b)
             34 BINARY_ADD
             35 RETURN_VALUE

  7     >>   36 LOAD_FAST                0 (a)
             39 LOAD_FAST                1 (b)
             42 BINARY_MULTIPLY
             43 LOAD_FAST                2 (c)
             46 BINARY_SUBTRACT
             47 RETURN_VALUE
  ```

## Keywords to note in Python:

*and* - similar to logical '&&' operator <br>
*or* - logical '||' operator<br>
*not* - logical '!' operator<br>
*pass* - do nothing
*in* - used to check if a value is present in a sequence or collection.<br>Example:
```Python
fruit = ["banana", "apple", "pear", "grape"]
greeting = "Hello World"

if "banana" in fruit:
    print("banana is a fruit!")  # prints banana is a fruit
if 'W' in greeting:
    print("True")  # prints True

# it is also possible to use it when iterating a for loop

for item in fruit:
    print(item)
# output:
# banana
# apple
# pear
# grape
```
*is* - compares if objects are identical. Different from the '==' comparison operatory which compares equality.Example:
```Python
str1 = "Hello"
str2 = "World"
str1_cp = str1

if str1 == str2:
    print("equal")  # prints equal

if str1 is str2:  # behaviour undefined since they are different objects
    print("equal")

if str1 is str1_cp:  # prints equal since they point to the same object
    print("equal")

# Becuase of Pythons 'object interning, it's possible to compare small integers (-5, 256)...
# using the 'is' keyword.

x = 5
y = 5

if x == y:
    print("equal")  # prints equal
if x is y:
    print("equal")  # prints equal
```

## Defining functions in python:

functions are defined using the 'def' keyword. Example
```Python
def sum(n1 , n2):
    return n1 + n2

print(sum(2, 3)) # prints 5

# you can also hint what the function returns but it does not change runtime execution

def sum(n1, n2) -> int:
    return n1 + n2

# void functions have no return. You can also pass in arguments out of order using '='

def greeting(hello, world):
    print(hello, world)

greeting(world="World!", hello="Hello")
# output:
# Hello World!
```
