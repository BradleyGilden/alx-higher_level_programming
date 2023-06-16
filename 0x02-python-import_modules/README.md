# Import and Modules

**This directory tackles with the concept of imports and modules in Python**

## Directory Files:

* [0-add.py ](0-add.py ) - A program that imports the function def add(a, b): from the file add_0.py and prints the result of the addition 1 + 2 = 3
* [1-calculation.py](1-calculation.py) - A program that imports functions from the file calculator_1.py, does some Maths, and prints the result.
* [2-args.py](2-args.py) - A program that prints the number of and the list of its arguments.
* [3-infinite_add.py](3-infinite_add.py) - A program that prints the result of the addition of all arguments
* [4-hidden_discovery.py](4-hidden_discovery.py) - A program that prints all the names defined by the compiled module hidden_4.pyc (please download it locally).
* [5-variable_load.py](5-variable_load.py) - A program that imports the variable a from the file variable_load_5.py and prints its value.
* [100-my_calculator.py](100-my_calculator.py) - A program that imports all functions from the file calculator_1.py and handles basic operations.
* [101-easy_print.py](101-easy_print.py) - A program that prints #pythoniscool, followed by a new line, in the standard output.
* [102-magic_calculation.py](102-magic_calculation.py) - Writing a Python function def magic_calculation(a, b): that does exactly the same as the following Python bytecode:
  ```
  3           0 LOAD_CONST               1 (0)
              3 LOAD_CONST               2 (('add', 'sub'))
              6 IMPORT_NAME              0 (magic_calculation_102)
              9 IMPORT_FROM              1 (add)
             12 STORE_FAST               2 (add)
             15 IMPORT_FROM              2 (sub)
             18 STORE_FAST               3 (sub)
             21 POP_TOP

  4          22 LOAD_FAST                0 (a)
             25 LOAD_FAST                1 (b)
             28 COMPARE_OP               0 (<)
             31 POP_JUMP_IF_FALSE       94

  5          34 LOAD_FAST                2 (add)
             37 LOAD_FAST                0 (a)
             40 LOAD_FAST                1 (b)
             43 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             46 STORE_FAST               4 (c)

  6          49 SETUP_LOOP              38 (to 90)
             52 LOAD_GLOBAL              3 (range)
             55 LOAD_CONST               3 (4)
             58 LOAD_CONST               4 (6)
             61 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             64 GET_ITER
        >>   65 FOR_ITER                21 (to 89)
             68 STORE_FAST               5 (i)

  7          71 LOAD_FAST                2 (add)
             74 LOAD_FAST                4 (c)
             77 LOAD_FAST                5 (i)
             80 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
             83 STORE_FAST               4 (c)
             86 JUMP_ABSOLUTE           65
        >>   89 POP_BLOCK

  8     >>   90 LOAD_FAST                4 (c)
             93 RETURN_VALUE

  10     >>   94 LOAD_FAST                3 (sub)
             97 LOAD_FAST                0 (a)
            100 LOAD_FAST                1 (b)
            103 CALL_FUNCTION            2 (2 positional, 0 keyword pair)
            106 RETURN_VALUE
            107 LOAD_CONST               0 (None)
            110 RETURN_VALUE
  ```
* [103-fast_alphabet.py](103-fast_alphabet.py) - A program that prints the alphabet in uppercase, followed by a new line.

## Important commands to note:

1. `import <module>` - this will import all attribute, method and class definitions in a module. This is not good practice as it is better to import only functionality that you use throughout your program

2. `from <module> import <name>` - this allows you to import specific attributes, functions or classes from the module
e.g. "from functools import reduce"

3. `dir([object])` - the default dir() logic is used and returns:
   * for a module object: the module's attributes.
   * for a class object:  its attributes, and recursively the attributes of its bases. Example:
   ```
   >>> dir(str)
   ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
   ```

4. `help(str)` - this module comes in handy when explaining a functions functionality
   ```
    >>> help(str().join)
    Help on built-in function join:

    join(iterable, /) method of builtins.str instance
    Concatenate any number of strings.
    
    The string whose method is called is inserted in between each given string.
    The result is returned as a new string.
    
    Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
   ```
