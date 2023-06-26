# Exceptions in Python

Errors detected during execution of a program are called *exceptions* and are not always a result of an incorrect expression. In order for the program to not exit with failure as soon as an exception is thrown, we then handle exceptions.

## Directory Files:



## Basic Exception Handling

In basic exception handling we have the `try` and `except` block in Python. In the `try` block lies the code that could "raise" a potential exception, in the `except` block is where the exception that was raised is caught and handled.

```Python
values = [10, 2, 3, 5, 0, 9]

for num in values:
    try:
        print(f"{10//num}")  # will raise exception when num=0
    except:
        print("Exception raised") # we could use `pass` if we did not want to print anything
```
```
1
5
3
2
Exception raised
1
```

## Explicit exception handling

It's not good practice to use just `except` as it is very broad in which exceptions it is catching. It is better to know what error is being thrown using explicit exceptions such as  *ZeroDivisionError*, *ValueError* and many more.

```Python
values = [10, 2, "Hey", 5, 0, 9]

for num in values:
    try:
        print(f"{10//num}")  # will raise exception when num=0 and num="Hey"
    except ZeroDivisonError:  # catches division error exception
        print("Cannot divide by 0")
    except TypeError as e:  # e is where the default error message is stored
        print(str(e))
    except Exception as e:  # catches any exception that was not explicitely checked
        print("Exception Thrown")
```
```
1
5
unsupported operand type(s) for //: 'int' and 'str'
2
Cannot divide by 0
1
```

It is also possible to handle multiple errors the same way e.g:

```Python
values = [10, 2, "Hey", 5, 0, 9]

for num in values:
    try:
        print(f"{10//num}")
    except (ZeroDivisionError, TypeError):
        pass
```
```
1
5
2
1
```
We can also use an `else` block like in `if` conditionals to execute code if no exceptions are caught

```Python
values = [10, 2, 1, 5, 1, 9]

for num in values:
    try:
        print(f"{10//num}", end="\t")
    except (ZeroDivisionError, TypeError):
        pass
    except Exception:
        pass
    else:
        print("No Errors")
```
```
1       No Errors
5       No Errors
10      No Errors
2       No Errors
10      No Errors
1       No Errors
```

## Raising Exceptions

It is also possible to raise your own exceptions during a program to fit your own specific needs

```Python
even = [2, 4, 6, 8, 9, 10]
divisor = [2, 2, 2, 0, 2, 2]
value = 0
for num, div in zip(even, divisor):
    try:
        value = num % div
        if value != 0:  # raising my own custom exception for odd nums
            raise ZeroDivisionError(f"{num} is odd")
        print(f"{num} is even")
    except ZeroDivisionError as e:
        print(str(e))
```
```
2 is even
4 is even
6 is even
integer division or modulo by zero
9 is odd
10 is even
```
