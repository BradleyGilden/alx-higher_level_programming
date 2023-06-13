# Conditionals, Loops and Functions in Python

**This repository tackles pythons unique way of handling conditional statements, loops and functions**

## Files in Directory:

* [0-positive_or_negative.py](0-positive_or_negative.py) - A program will assign a random signed number to the variable number each time it is executed. Requirements:
  * The variable `number` will store a different value every time you will run this program
  * The output of the program should be:
    * the number, followed by
      * if the number is greater than 0: `is positive`
      * if the number is 0: `is zero`
      * if the number is less than 0: `is negative`
    * followed by a new line
* [1-last_digit.py](1-last_digit.py) - A program will assign a random signed number to the variable `number` each time it is executed. Requirements:
  * The output of the program should be:
    * The string Last digit of, followed by
    * the number, followed by
    * the string is, followed by the last digit of number, followed by
      * if the last digit is greater than 5: `the string and is greater than 5`
      * if the last digit is 0: `the string and is 0`
      * if the last digit is less than 6 and not 0: `the string and is less than 6 and not 0`
    * followed by a new line
* [2-print_alphabet.py](2-print_alphabet.py) - A program that prints the ASCII alphabet, in lowercase, not followed by a new line. Requirements:
  * You can only use one `print` function with string format
  * You can only use one loop
* [3-print_alphabt.py](3-print_alphabt.py) - A program that prints the ASCII alphabet, in lowercase, not followed by a new line. Requirements:
  * You can only use one `print` function with string format
  * You can only use one loop
  * you have exclude letters `q` and `e`
* [4-print_hexa.py](4-print_hexa.py) - A program that counts from `0` to `98` in hexidecimal
* [5-print_comb2.py](5-print_comb2.py) - A program that prints numbers from 0 to 99.
  * Numbers must be separated by `, `
  * Numbers should be printed in ascending order, with two digits
  * The last number should be followed by a new line
  * You can only use no more than 2 `print` functions with string format
  * You can only use one loop in your code
  * You are not allowed to store numbers or strings in a variable
  * You are not allowed to import any module
* [6-print_comb3.py](6-print_comb3.py) -  A program that prints all possible different combinations of two digits. Requirements:
  * Numbers must be separated by `, `
  * The two digits must be different
  * `01` and `10` are considered the same combination of the two digits 0 and 1
  * Print only the smallest combination of two digits
  * Numbers should be printed in ascending order, with two digits
  * The last number should be followed by a new line
  * You can only use no more than 3 `print` functions with string format
  * You can only use no more than 2 loops in your code
  * You are not allowed to store numbers or strings in a variable
  *You are not allowed to import any module
* [7-islower.py](7-islower.py) - A function that checks for lowercase character. Requirements:
  * You are not allowed to import any module
  * You can't use `str.upper()` and `str.isupper()`
* [8-uppercase.py8-uppercase.py](8-uppercase.py) -  a function that prints a string in uppercase followed by a new line. Requirements:
  * You can only use one loop
  * You can't use `str.upper()` and `str.isupper()`
* [9-print_last_digit.py](9-print_last_digit.py) - A function that prints the last digit of a number. 
* [10-add.py](10-add.py) - Write a function that adds two integers and returns the result.
  * Prototype: `def add(a, b):`
  * Returns the value of `a + b`
* [11-pow.py](11-pow.py) - Write a function that computes `a` to the power of `b` and return the value. Requirements:
  * Prototype: `def pow(a, b):`
  * Returns the value of `a ^ b`
  * You are not allowed to import any module
* [12-fizzbuzz.py](12-fizzbuzz.py) - Write a function that prints the numbers from 1 to 100 separated by a space. Requirements:
  * For multiples of three print Fizz instead of the number and for multiples of five print `Buzz`.
  * For numbers which are multiples of both three and five print `FizzBuzz`.
  * Prototype: `def fizzbuzz():`
  * Each element should be followed by a space
  * You are not allowed to import any module
* [13-insert_number.c](13-insert_number.c) - Write a function in C that inserts a number into a sorted singly linked list.
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
