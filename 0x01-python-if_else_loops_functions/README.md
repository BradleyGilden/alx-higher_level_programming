# Conditionals, Loops and Functions in Python

**This repository tackles pythons unique way of handling conditional statements, loops and functions**

## Files in Directory:

## Keywords to note in Python:

*and* - similar to logical '&&' operator <br>
*or* - logical '||' operator<br>
*not* - logical '!' operator<br>
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
