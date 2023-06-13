# Hello World

**This repository deals with formatting the output of Pythons print**

## Directory Files:
* [0-run](0-run) -  A Shell script that runs a Python script. The Python file name will be saved in the environment variable `$PYFILE`
* [1-run_inline](1-run_inline) - A Shell script that runs Python code. The Python code will be saved in the environment variable `$PYCODE`
* [2-print.py](3-print_number.py) -  a Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line.
* [3-print_number.py](3-print_number.py) - Completed this [source code](https://github.com/alx-tools/0x00.py/blob/master/3-print_number.py) in order to print the integer stored in the variable number, followed by Battery street, followed by a new line. Requirements:
  * The output of the script should be:
    * the number, followed by `Battery street`,
    * followed by a new line
  * Not allowed to cast the variable `number` into a string
  * The code must be 3 lines long
  * You have to use f-strings
* [4-print_float.py](4-print_float.py) - Completed the [source code](https://github.com/alx-tools/0x00.py/blob/master/4-print_float.py) in order to print the float stored in the variable number with a precision of 2 digits. Requirements:
  * The output of the program should be:
    * `Float:`, followed by the float with only 2 digits
    * followed by a new line
  * You are not allowed to cast `number` to string
  * You have to use f-strings
* [5-print_string.py](5-print_string.py) - Completed this [source code](https://github.com/alx-tools/0x00.py/blob/master/5-print_string.py) in order to print 3 times a string stored in the variable `str`, followed by its first 9 characters. Requirements
  * The output of the program should be:
    * 3 times the value of `str`
    * followed by a new line
    * followed by the 9 first characters of `str`
    * followed by a new line
  * You are not allowed to use any loops or conditional statement
  * Your program should be maximum 5 lines long
* [6-concat.py](6-concat.py) - Completed this [source code](https://github.com/alx-tools/0x00.py/blob/master/6-concat.py) to print `Welcome to Holberton School!`. Requirements:
  * You are not allowed to use any loops or conditional statements.
  * You have to use the variables `str1` and `str2` in your new line of code
  * Your program should be exactly 5 lines long
* [7-edges.py](7-edges.py) - Complete this [source code](https://github.com/alx-tools/0x00.py/blob/master/7-edges.py). Requirements:
  * You are not allowed to use any loops or conditional statements
  * Your program should be exactly 8 lines long
  * `word_first_3` should contain the first 3 letters of the variable word
  * `word_last_2` should contain the last 2 letters of the variable word
  * `middle_word` should contain the value of the variable word without the first and last letters
* [8-concat_edges.py](8-concat_edges.py) - Completed this [source code](https://github.com/alx-tools/0x00.py/blob/master/8-concat_edges.py) to print `object-oriented programming with Python`, followed by a new line. Requirements:
  * You are not allowed to use any loops or conditional statements
  * The program should be exactly 5 lines long
  * You are not allowed to create new variables
  * You are not allowed to use string literals
* [9-easter_egg.py](9-easter_egg.py) - Write a Python script that prints “The Zen of Python”, by TimPeters, followed by a new line. Requirements:
  * The script should be maximum 98 characters long (please check with `wc -m 9-easter_egg.py`).
* [10-check_cycle.c](10-check_cycle.c) -
Technical interview preparation:
  * You are not allowed to google anything
  * Whiteboard first
Write a function in C that checks if a singly linked list has a cycle in it.

  Prototype: int check_cycle(listint_t *list);<br>
  Return: 0 if there is no cycle, 1 if there is a cycle
  <br>Requirements:
  * Only these functions are allowed: `write`, `printf`, `putchar`, `puts`, `malloc`, `free`
* [100-write.py](100-write.py) - Write a Python script that prints exactly `and that piece of art is useful - Dora Korpar, 2015-10-19`, followed by a new line. Requirements:
  * You have to use the `write` function from `sys` module
  * The script should print to `stderr`
  * exit with status code 1
* [101-compile](101-compile) - A script that compiles a Python script file. The Python file name will be stored in the environment variable `$PYFILE`
* [102-magic_calculation.py](102-magic_calculation.py) - Write the Python function `def magic_calculation(a, b):` that does exactly the same as the following Python bytecode:
  ```
    3         0 LOAD_CONST               1 (98)
              3 LOAD_FAST                0 (a)
              6 LOAD_FAST                1 (b)
              9 BINARY_POWER
             10 BINARY_ADD
             11 RETURN_VALUE
  ```

## Ways to Format Output:

```Python
>>> # The normal way
>>> print("Hello World")
Hello World
>>> # Using format strings
>>> num = 4
>>> print(f"His address was {num} Privet Drive\nLittle Whinging, Surrey")
His addres was 4 Privet Drive
Little Whinging, Surrey
>>> # Using comma seperators
>>> print("Hello", "Agent", 47)
Hello Agent 47
>>> # Using .format method
>>> name = "Harry"
>>> print("You're a wizard {name}".format(name))
You're a wizard Harry
>>> # Using % operator
>>> price = 99.99
>>> print("New best selling game going for only %.2fd"%(price))
```

