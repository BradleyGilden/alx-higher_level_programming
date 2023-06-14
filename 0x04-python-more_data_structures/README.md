# Sets, Dictionaries and Lambda

**This directory contains tasks that aim in practicing the concepts of set and dictionary data structures as well as how to utilize Lambda with these data structures**

## Directory Files:

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
>>>capitals = {"USA": "Washington D.C.",
...                 "India": "New Delhi",
...                 "China": "Beijing",
...                 "Russia": "Moscow"}
>>>for key, value in capitals.items():
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

