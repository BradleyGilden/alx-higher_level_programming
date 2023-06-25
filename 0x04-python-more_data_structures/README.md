# Sets, Dictionaries and Lambda

**This directory contains tasks that aim in practicing the concepts of set and dictionary data structures as well as how to utilize Lambda with these data structures**

## Directory Files:

* [0-square_matrix_simple.py](0-square_matrix_simple.py) - a function that computes the square value of all integers of a matrix.
* [1-search_replace.py](1-search_replace.py) - a function that replaces all occurrences of an element by another in a new list
* [2-uniq_add.py](2-uniq_add.py) - a function that adds all unique integers in a list (only once for each integer).
* [3-common_elements.py](3-common_elements.py) - a function that returns a set of common elements in two sets.
* [4-only_diff_elements.py](4-only_diff_elements.py) - a function that returns a set of all elements present in only one set.
* [5-number_keys.py](5-number_keys.py) - a function that returns the number of keys in a dictionary.
* [6-print_sorted_dictionary.py](6-print_sorted_dictionary.py) - a function that prints a dictionary by ordered keys.
* [7-update_dictionary.py](7-update_dictionary.py) - a function that replaces or adds key/value in a dictionary.
* [8-simple_delete.py](8-simple_delete.py) - a function that deletes a key in a dictionary.
* [9-multiply_by_2.py](9-multiply_by_2.py) - a function that returns a new dictionary with all values multiplied by 2
* [10-best_score.py](10-best_score.py) - a function that returns a key with the biggest integer value.
* [11-multiply_list_map.py](11-multiply_list_map.py) - a function that returns a list with all values multiplied by a number without using any loops.
* [12-roman_to_int.py](12-roman_to_int.py) - a function that converts a Roman numeral to an integer.
* [101-square_matrix_map.py](101-square_matrix_map.py) - a function that computes the square value of all integers of a matrix using map

## Sets

Sets are unordered and unindexed. They do not contain or tolerate any duplicates. If a duplicate is found, the set will automatically remove it. They are recognised by the `{}` operator. In order to create an empty set you have to use the `set()` class

```Python3
>>> # Creating a set
>>> # my_set = {'dog, 'cat', 'frog', 'mouse'}
>>> fruit = ['banana', 'apple', 'orange', 'apple']
>>> set(fruit)
{'banana', 'apple', 'orange'}
```

There are also some useful set operations:

```Python 3
>>> # Demonstrate set operations on unique letters from two words

>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a                                  # unique letters in a
{'a', 'r', 'b', 'c', 'd'}
>>> a - b                              # letters in a but not in b
{'r', 'd', 'b'}
>>> a | b                              # letters in a or b or both
{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
>>> a & b                              # letters in both a and b
{'a', 'c'}
>>> a ^ b                              # letters in a or b but not both
{'r', 'd', 'b', 'm', 'z', 'l'}
```

```Python3
>>> utensils = {"fork","spoon","knife"}         # create set utensils
>>> dishes = {"bowl","plate","cup","knife"}     # create set dishes

>>> utensils.add("napkin")
{"fork", "spoon", "knife", "napkin"}
>>> utensils.remove("fork")
{"spoon", "knife", "napkin"}
>>> utensils.clear()
{}
>>> utensils = {"fork","spoon","knife"}
>>> #
>>> #
>>> dishes.update(utensils)                         # add untensils items to dishes set
{"fork", "spoon", "knife", "bowl", "plate", "cup"}
dinner_table = utensils.union(dishes)               # combines the 2 sets
{"fork", "spoon", "knife", "bowl", "plate", "cup"}
>>> print(dishes.difference(utensils))              # shows all dish elements that are different from utensils
{"fork", "spoon"}
print(utensils.intersection(dishes))                # shows what is common in both sets
{"knife"}

>>> for x in utensils:
...       print(x)
spoon
fork
knife
>>> # prints unordered because sets are unordered
```

## Dictionaries

* a collection of `{key:value}` pairs
* ordered and changeable. No duplicates

```Python3
>>> capitals = {"USA": "Washington D.C.",
...                 "India": "New Delhi",
...                 "China": "Beijing",
...                 "Russia": "Moscow"}
>>>
>>>
>>> for value in capitals.values():
...    print(f"{value}")
Washington D.C.
New Delhi
Beijing
Moscow
>>>
>>>
>>> for key in capitals.keys():
...    print(f"{key}}")
USA
India
China
Russia
>>>
>>>
>>> for key, value in capitals.items():
...    print(f"{key}: {value}")
USA: Washington D.C.
India: New Delhi
China: Beijing
Russia: Moscow

>>> capitals['China']
beijing
>>> capitals.get('China')  # get is preferred since it's safer to use
beijing

```

## Lambda, Map, Filters and Reduce

### lambda λ

* Function written in 1 line using `lambda` keyword
* accepts any number of arguments, has one expression
* prototype: `lambda` parameters: expression

```Python
>>> def double(x):
...     return x * 2
>>> double(5)
10
>>> exit()

$ python3

>>> double = lambda x: x * 2
>>> double(5)
10
>>> multiply = lambda x, y: x * y
>>> multiply(5, 6)
30
>>> add = lambda x, y, z: x + y + z
>>> add(5, 6, 7)
18
>>> full_name = lambda first_name, last_name: fiirst_name + " " + last_name
>>> full_name("Bradley", "Gilden")
Bradley Gilden
```

### map()

* applies function to each item in iterable (list, tuple, etc)
* prototype: `map(function, sequence)`

```Python
>>> # Currency converter
>>> USD = [22, 32, 13, 2, 5, 302, 94]
>>> RSA = list(map(lambda x: x * 18.47, USD))
>>> print(RSA)
[406.34, 591.04, 240.10999999999999, 36.94, 92.35, 5577.94, 1736.1799999999998]
>>> EUR  = list(map(lambda x: x * 0.05, RSA))
>>> print (EUR)
[20.317, 29.552, 12.0055, 1.847, 4.6175, 278.897, 86.809]
```

### filter()

* provides a way to filter out a sequence
* the sequence is filtered using a boolean return of the functions operation
* prototype: `filter(function, sequence)`

```Python
### print odd numbers from a sequence
nums = [2, 34, 53, 432, 321, 31, 0]
>>> odd = list(filter(lambda x: x % 2 != 0, nums))
>>> print(odd)
[53, 321, 31]
```

### reduce()
* prototype: `reduce (function, sequence)`
* This method has to be imported from the `functools` module since it is not favoured by the creator of Monty Python: Guido Van Rossum
* the reduce process:
  1. It takes the first two items from the iterable and applies the binary function to them, producing a result.
  2. It then takes the result and the next item from the iterable, applying the binary function to them.
  3. This process continues until all items in the iterable have been processed, resulting in a single output value.

```Python
>>> from functools import reduce
>>>
>>>
>>> n = 5
>>> factorial = reduce(lambda x, y: x * y, range(1, n + 1))
>>> print(f"factorial of {n} is {factorial}")
factorial of 5 is 120
```
