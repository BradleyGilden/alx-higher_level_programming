# Object Orientation in Python

OOP is a concept that has objects and classes as it's basis. The purpose of OOP
is to modularize data and functions that work together, and no other part of
the program can access the data.

Python OOP concepts to cover:
* [Class](#classes)
* [Object](#objects)
* [Encapsulation & Data Hiding](#encapsulation--data-hiding)
* [Inheritance](#inheritence)
* [Data Abstraction](#data-abstraction)
* [Polymorphism]()

<br>

## Directory Files

## Classes:

Classes contain a blueprint (data and functions) which serve as the basis from which objects are derived from.

* classes are created with the keyword *class*
* They often have an `__init__(self)` method which acts as a constructor similar to java and C++. It is set to run as soon as an object of the classs is instantiated.
It is used to initialise you class data with either class arguments or predefined values.

<p align=center><img src="resources/class_obj.png" width=350></p>

## Objects:

Objects are an instance of a class and contain all states and behaviours associated with the class. In Python, integers, strings, lists and dictionaries are all objects.
<br>Objects consists of:

* State: It is represented by the attributes of an object. It also reflects the properties of an object
* Behaviour: It is represented by the methods of an object. It also reflects the response of an object to other objects.
* Identity: It gives a unique name to an object and enables one object to interact with other objects.

## Creating a Class and an Object of a Class in python

```Python
class Animal:  # creating class: Animal

    what_are_you = "I am an Animal" # class attributes shared by all instances

    def __init__(self, genus=None, species=None):  # Constructor
        self.genus = genus   # self donates class instance attributes
        self.species = species
        if self.species is None:
            self.species = "Anonymous"

    def makeSound(self):
        genus = self.genus
        if genus is None:
            print("?")
        elif genus == "Canis":
            print("Woof!")
        elif genus == "Felis" or genus == "Lynx":
            print("Meowww :3")
        elif genus == "Panthera":
            print("ROAR!")


if __name__ == '__main__':

    Bobcat = Animal("Lynx", "Bobcat")
    print(Bobcat.species, end="\t")
    Bobcat.makeSound()

    unknown = Animal()
    print(unknown.species, end="\t")
    unknown.makeSound()

    print()
    print(Bobcat.what_are_you, unkown.what_are_you, Animal().what_are_you)

```
```
Bobcat          Meowww :3
Anonymous       ?

I am an Animal, I am an Animal, I am an Animal
```

## Encapsulation & Data Hiding

Encapsulation refers to the bundling of data and the methods that operate on that data into a single unit, known as a class. The class acts as a container that encapsulates the data and provides an interface to interact with that data(getters and setters).

Data Hiding allows you to hide the internal implementation details of an object from the outside world. The internal state of an object can be made private or protected, preventing direct access and modification. Instead, access to the data is provided through methods (getters and setters) defined in the class, which allows for controlled access and manipulation of the data
<br>N.B private attributes can only be accessed within the class, not from the outside

```Python
class Secret:

    def __init__(self):  # Data hiding
        self.__password = "night@lock68" # Use __ for private attributes
        self.__secret = "I am a Secret. Shhhh"

    def unlock_secret(self, password):
        if isinstance(password, str) and password == self.__password:
            print(self.__secret)
        else:
            print("Password incorrect")
    # Encapsulation
    @property  # this allows us to raad data without needing () function notation
    def get_password(self):
        return self.__password

    @set_secret.setter  # this allows us to set date by using = data insteahd of (data)
    def set_secret(self, secret=""):
        self.secret = secret

if __name__ == '__main__':

    mySecret = Secret()
    mySecret.set_secret = "Expelliarmus!"
    # print(mySecret.__secret) will cause an error
    mySecret.unlock_secret(1234)
    mySecret.unlock_secret(mySecret.get_password)
```

```
Password incorrect
Expelliarmus!
```

## Data Abstraction

Data abstraction builds upon encapsulation and data hiding by further abstracting away unnecessary implementation details and exposing a simplified and high-level view of an object or system. It focuses on defining abstract classes and interfaces that specify the behavior expected from a class without concerning themselves with the implementation details.

By combining encapsulation and data hiding, data abstraction allows for the creation of well-structured and modular code. It promotes the separation of concerns, enhances code reusability, simplifies code maintenance, and provides a clear and understandable interface for working with objects.

```Python
from abc import ABC, abstractmethod

class MyAbstractClass(ABC):
    @abstractmethod
    def my_abstract_method(self):
        pass

    @abstractmethod
    def another_abstract_method(self):
        pass

    def my_concrete_method(self):
        print("This is a concrete method.")

# Attempting to instantiate an abstract class will raise an error
# my_object = MyAbstractClass()  # Raises TypeError

# Concrete subclass that inherits from the abstract class
class MyConcreteClass(MyAbstractClass):
    def my_abstract_method(self):
        print("Implementing my_abstract_method.")

    def another_abstract_method(self):
        print("Implementing another_abstract_method.")


# Creating an instance of the concrete subclass
my_object = MyConcreteClass()
my_object.my_abstract_method()  # Output: Implementing my_abstract_method.
my_object.another_abstract_method()  # Output: Implementing another_abstract_method.
my_object.my_concrete_method()  # Output: This is a concrete method.
```

## Inheritence:

<p align=center><img src="resources/inheritence.png" width=350></p>

Allows classes (sub/child class) to inherit properties of another class (parent/super class). This allows us to add features to classes without modifying the original class. In python the builtin `super()` is used to initiate the inherited class.

```Python
class Animal:  # Parent class

    what_are_you = "I am an Animal"

    def __init__(self, genus=None, species=None):
        self.genus = genus
        self.species = species
        if self.species is None:
            self.species = "Anonymous"

    def makeSound(self):
        genus = self.genus
        if genus is None:
            print("?")
        elif genus == "Canis":
            print("Woof!")
        elif genus == "Felis" or genus == "Lynx":
            print("Meowww :3")
        elif genus == "Panthera":
            print("ROAR!")

class Mammal(Animal):

    what_are_you = "I am a Mammal"  # Overrides parents attribute

    def __init__(self, habitat=None, genus=None, species=None):
        super().__init__(genus, species)
        self.__habitat = habitat

    def get_habitat(self):
        if self.__habitat is None:
            return "I dont know where I live!"
        elif self.__habitat == "sea":
            return "I live in the sea"
        elif self.__habitat == "land":
            return "I live in the sea"

if __name__ == '__main__':

    mammal = Mammal("land", "Panthera", "Leopard")
    print(mammal.what_are_you,mammal.get_habitat(), mammal.species, sep=", ")
    mammal.makeSound()
```

```
I am a Mammal, I live in the sea, Leopard
ROAR!
```
