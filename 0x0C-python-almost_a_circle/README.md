# Python Almost A Circle

This project is designed to review the following Python concpets:

* Import
* Exceptions
* Class
* Private attribute
* Getter/Setter
* Class method
* Static method
* Inheritance
* Unittest
* Read/Write file
* JSON and CSV formatting

<br>

## Folder Layout:

|Directory|Info|
| ------- | -- |
[models/](models/) | A package containing classes and subclasses|
[tests/test_models](tests/test_models/) | directory of test files using unittest for testing all the classes in [models/](models/) |

## List of files:

* ### [models/](models/)
  * [base.py](models/base.py) - Contains the Base class that sets up the id for the square and rectangle class and also handles loading and saving Square/Rectangle objects to and from JSON/CSV formatted files

  * [rectangle.py](models/rectangle.py) - Contains the Rectangle module which creates a rectangle object of *width* and *height*

  * [square.py](models/square.py) - Contains the Square module which creates a Square object of all equal dimension of length *size*

* ### [tests/test_models/](tests/test_models)
  * [test_base.py](tests/test_models/test_base.py) - contains multiple test classes for testing module [base.py](models/base.py)

  * [test_rectangle.py](tests/test_models/test_rectangle.py) - contains multiple test classes for testing module [rectangle.py](models/rectangle.py)

  * [test_square.py](tests/test_models/test_square.py) - contains multiple test classes for testing module [square.py](models/square.py)
