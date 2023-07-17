#!/usr/bin/python3

"""
This module contains the Base class which is the parent class of all the
other classes in the models package.

Date: 13/07/2023
Author: Bradley Dillion Gilden
"""


import json
import csv
import turtle


class Base:
    """Manages id in inheritted classes and to avoid code/bug duplication

    Args->public:
        id(int): if {id} is not None, the public instance attribute {self.id}
        is assigned the value of {id}

    Attribute->private:
        nb_objects(int): A private class attribute that is incremented and
        assigned to the public instance attribute {self.id} if id is None
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Constructor method for the Base class, initialized {self.id}"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns JSON string representation of list_dictionaries

        Args:
            list_dictionaries([{}]): a list of dictionaires
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes json string representation of {list_objs} to {Class.json}

        Args:
            list_objs(Rectangle or Square): list of objects
        """
        filename = cls.__name__ + ".json"

        if list_objs is None:
            with open(filename, "w", encoding="utf-8") as file:
                file.write("[]")
        else:
            expand_list = [obj.to_dictionary() for obj in list_objs]
            json_list = cls.to_json_string(expand_list)
            with open(filename, "w", encoding="utf-8") as file:
                file.write(json_list)

    @staticmethod
    def from_json_string(json_string):
        """converts JSON string to a list of dictionaries

        Args:
        json_string(str): JSON string
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create a new instance of Square or Rectangle with all it's
        attributes set to values in dictionary

        Args:
        dictionary(dict): variable keyword arguments
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                dummy = cls(1, 1)
            else:
                dummy = cls(1)
            dummy.update(**dictionary)
            return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances from json file"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r") as file:
                json_string = file.read()

        except FileNotFoundError:
            return []

        json_list = cls.from_json_string(json_string)
        obj_list = [cls.create(**dictionary) for dictionary in json_list]
        return obj_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """save python object to csv file format"""
        filename = cls.__name__ + ".csv"
        if cls.__name__ == "Rectangle":
            fieldnames = ["id", "width", "height", "x", "y"]
        else:
            fieldnames = ["id", "size", "x", "y"]

        with open(filename, "w", newline="") as file:
            if list_objs is None or list_objs == []:
                file.write("[]")
            else:
                expand_list = [obj.to_dictionary() for obj in list_objs]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                for row in expand_list:
                    writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """load a list of objects from csv file"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """this static method will draw a list of squares and rectangles
        using tkinters turtle module

        Args:
        list_rectangles([Rectangle]): a list of rectangle objects
        list_squares([Square]): a list of square objects
        """
        t = turtle.Turtle()
        # setup drawing area
        drawing_area = turtle.Screen()
        drawing_area.setup(width=800, height=600)
        drawing_area.bgcolor("green")
        t.pensize(3)
        t.shape("turtle")
        t.color("yellow")
        t.pencolor("yellow")
        t.up()
        t.goto(-350, 250)
        t.down()
        t.write("Rectangles", font=("Arial", 20, "normal"))
        t.up()

        for r in list_rectangles:
            t.showturtle()
            t.goto(r.x, r.y)
            t.down()
            for _ in range(2):
                t.forward(r.width)
                t.left(90)
                t.forward(r.height)
                t.left(90)
            t.hideturtle()
            t.up()

        t.color("green")
        t.pencolor("green")
        drawing_area.bgcolor("yellow")
        t.up()
        t.goto(-350, 250)
        t.down()
        t.write("Squares", font=("Arial", 20, "normal"))
        t.up()

        for s in list_squares:
            t.showturtle()
            t.goto(s.x, s.y)
            t.down()
            for _ in range(2):
                t.forward(s.width)
                t.left(90)
                t.forward(s.height)
                t.left(90)
            t.hideturtle()
            t.up()

        turtle.done()
