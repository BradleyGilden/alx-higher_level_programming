#!/usr/bin/python3

"""
This module is for testing the rectangel module

              Index:
+------++------------------------------+
| Line ||           Class              |
+======++==============================+
| 40   || Test_Rectangle_Documentation |
+------++------------------------------+
| 65   || Test_Rectangle_Instantiation |
+------++------------------------------+
| 116  || Test_Width_Values            |
+------++------------------------------+
| 181  || Test_Height_Values           |
+------++------------------------------+
| 246  || Test_X_Values                |
+------++------------------------------+
| 313  || Test_Y_Values                |
+------++------------------------------+
| 380  || Test_Rectangle_Functions     |
+------++------------------------------+
| 416  || Test_Rect_Out                |
+------++------------------------------+

Date: 13/07/2023
Author: Bradley Dillion Gilden
"""

import unittest
import models.square
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class Test_Rectangle_Documentation(unittest.TestCase):
    """Unit test for correct documentation of imports"""

    def test_module_doc(self):
        """test square module documentation"""
        self.assertGreater(len(models.square.__doc__), 1)

    def test_class_doc(self):
        """test Square class documentation"""
        self.assertGreater(len(Square.__doc__), 1)

    def test_method_docs(self):
        """test the methods of rectangle class"""
        self.assertGreater(len(Square.__init__.__doc__), 1)
        self.assertGreater(len(Square.size.__doc__), 1)
        self.assertGreater(len(Square.__str__.__doc__), 1)
        self.assertGreater(len(Square.update.__doc__), 1)
        self.assertGreater(len(Square.to_dictionary.__doc__), 1)


class Test_Square_Instantiation(unittest.TestCase):
    """Tests Square objects behaviour during instantiation"""

    def test_base_rect_instance(self):
        """Tests if Square is an instance of Base"""
        self.assertTrue(isinstance(Square(22), Base) and
                        isinstance(Square(22), Rectangle))

    def test_no_args(self):
        """Test Square with no arguments"""
        with self.assertRaises(TypeError):
            Square()

    def test_too_many_args(self):
        """Test Square with too many arguments"""
        with self.assertRaises(TypeError):
            Square(1, 1, 1, 1, 1, 1)

    def test_one_arg(self):
        """Test Square with one argument"""
        r = Square(33)
        self.assertEqual(r.size, 33)

    def test_two_args(self):
        """Test Square with two arguments"""
        rect1 = Square(22, 33)
        rect2 = Square(44, 66)
        self.assertEqual(rect1.size, 22)
        self.assertEqual(rect1.x, 33)
        self.assertEqual(rect1.y, 0)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_all_args(self):
        """Test Square with all it's arguments"""
        r = Square(22, 33, 1, 3077)

        self.assertEqual(r.size, 22)
        self.assertEqual(r.x, 33)
        self.assertEqual(r.y, 1)
        self.assertEqual(r.id, 3077)

    def test_base_Square(self):
        """Ensures base and Square id's correlate"""
        b = Base()
        r = Square(1)
        self.assertEqual(1, r.id - b.id)


class Test_Size_Values(unittest.TestCase):
    """this class deals with testing size argument types and operations"""

    def test_isint_arg_setter(self):
        """this class tests for instances that size arg and setter is an int
        """
        r = Square(12)
        self.assertEqual(r.size, 12)
        r.size = 19
        self.assertEqual(r.size, 19)

    def test_not_int_arg(self):
        """attempt to assign a non int to Square argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square("size")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square([1, 2, 3])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square((1, 2, 3))
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(1.4, 22)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(True, 22)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({1, 2, 3})
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square({'one': 1, 'two': 2, 'three': 3})

    def test_not_int_setter(self):
        """attempt to set non int to Square object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(33, 22)
            r.size = "width"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(33, 22)
            r.size = [1, 2, 3]
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(33, 22)
            r.size = (1, 2, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(33, 22)
            r.size = 1.4
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(33, 22)
            r.size = True
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(33, 22)
            r.size = {1, 2, 3}
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Square(33, 22)
            r.size = {'one': 1, 'two': 2, 'three': 3}

    def test_not_negative(self):
        """test if size is negative"""
        r = Square(22, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.size = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.size = -5
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-5, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0, 33)


class Test_X_Values(unittest.TestCase):
    """this class deals with testing x argument types and operations"""

    def test_isint_arg_setter(self):
        """this class tests for instances that x arg and setter is an int
        """
        r1 = Square(1)
        r2 = Square(1, 20, 1)

        self.assertEqual(r1.x, 0)
        r1.x = 0
        self.assertEqual(r1.x, 0)

        self.assertEqual(r2.x, 20)
        r2.x = 40
        self.assertEqual(r2.x, 40)

    def test_not_int_arg(self):
        """attempt to assign a non int to Square argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, "x", 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, [1, 2, 3], 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, (1, 2, 3), 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, 1.4, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, True, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {1, 2, 3}, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(1, {'one': 1, 'two': 2, 'three': 3}, 1)

    def test_not_int_setter(self):
        """attempt to set non int to Square object"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1)
            r.x = "x"
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1)
            r.x = [1, 2, 3]
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1)
            r.x = (1, 2, 3)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1)
            r.x = 1.4
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1)
            r.x = True
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1)
            r.x = {1, 2, 3}
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Square(1)
            r.x = {'one': 1, 'two': 2, 'three': 3}

    def test_not_negative(self):
        """test if x is negative"""
        r = Square(1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.x = -5
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -5, 1)


class Test_Y_Values(unittest.TestCase):
    """this class deals with testing y argument types and operations"""

    def test_isint_arg_setter(self):
        """this class tests for instances that y arg and setter is an int
        """
        r1 = Square(1)
        r2 = Square(1, 1, 20)

        self.assertEqual(r1.y, 0)
        r1.y = 0
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.y, 20)
        r2.y = 40
        self.assertEqual(r2.y, 40)

    def test_not_int_arg(self):
        """attempt to assign a non int to Square argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, "y")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, (1, 2, 3))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, 1.4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(1, 1, {'one': 1, 'two': 2, 'three': 3})

    def test_not_int_setter(self):
        """attempt to set non int to Square object"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1)
            r.y = "y"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1)
            r.y = [1, 2, 3]
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1)
            r.y = (1, 2, 3)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1)
            r.y = 1.4
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1)
            r.y = True
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1)
            r.y = {1, 2, 3}
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Square(1)
            r.y = {'one': 1, 'two': 2, 'three': 3}

    def test_not_negative(self):
        """test if y is negative"""
        r = Square(1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.y = -5
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 1, -5)


class Test_Square_Functions(unittest.TestCase):
    """test outcome of functions of Square"""

    def test_area_args(self):
        """this function tests area with arguments"""
        r = Square(2, 2)
        with self.assertRaises(TypeError):
            r.area(22)

    def test_area(self):
        """test area of Square instance"""
        r = Square(12, 11)
        self.assertEqual(r.area(), 144)
        r.size = 5
        self.assertEqual(r.area(), 25)
        self.assertEqual(Square(3, 0, 0, 99).area(), 9)

    def test_to_dictionary_args(self):
        """tests to dictionary function with arguments"""
        r = Square(2, 11)
        with self.assertRaises(TypeError):
            r.to_dictionary(300)

    def test_to_dictionary(self):
        """tests a Square objects to dictionary function"""
        r1 = Square(1, 3, 4, 5)
        r2 = Square(1, 3, 4)
        r3 = Square(1)
        dict1 = {"size": 1, "x": 3, "y": 4, "id": 5}
        dict2 = {"size": 1, "x": 3, "y": 4, "id": r2.id}
        dict3 = {"size": 1, "x": 0, "y": 0, "id": r2.id + 1}
        self.assertEqual(r1.to_dictionary(), dict1)
        self.assertEqual(r2.to_dictionary(), dict2)
        self.assertEqual(r3.to_dictionary(), dict3)
