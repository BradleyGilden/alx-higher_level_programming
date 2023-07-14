#!/usr/bin/python3

"""
This module is for testing the rectangel module

              Index:
+------++------------------------------+
| Line ||           Class              |
+======++==============================+
| 25   || Test_Rectangle_Documentation |
+------++------------------------------+
| 46   || Test_Rectangle_Instantiation |
+------++------------------------------+

Date: 13/07/2023
Author: Bradley Dillion Gilden
"""


import unittest
from models.base import Base
import models.rectangle
from models.rectangle import Rectangle


class Test_Rectangle_Documentation(unittest.TestCase):
    """Unit test for correct documentation of imports"""

    def test_module_doc(self):
        """test rectangle module documentation"""
        self.assertGreater(len(models.rectangle.__doc__), 1)

    def test_class_doc(self):
        """test Rectangle class documentation"""
        self.assertGreater(len(Rectangle.__doc__), 1)

    def test_method_docs(self):
        """test the methods of rectangle class"""
        self.assertGreater(len(Rectangle.__init__.__doc__), 1)
        self.assertGreater(len(Rectangle.width.__doc__), 1)
        self.assertGreater(len(Rectangle.height.__doc__), 1)
        self.assertGreater(len(Rectangle.x.__doc__), 1)
        self.assertGreater(len(Rectangle.y.__doc__), 1)


class Test_Rectangle_Instantiation(unittest.TestCase):
    """Tests Rectangle objects behaviour during instantiation"""

    def test_no_args(self):
        """Test Rectangle with no arguments"""
        with self.assertRaises(TypeError):
            Rectangle()

    def test_too_many_args(self):
        """Test Rectangle with too many arguments"""
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 1, 1, 1)

    def test_one_arg(self):
        """Test Rectangle with one argument"""
        with self.assertRaises(TypeError):
            Rectangle(33)
        with self.assertRaises(TypeError):
            Rectangle(None)

    def test_two_args(self):
        """Test Rectangle with two arguments"""
        rect1 = Rectangle(22, 33)
        rect2 = Rectangle(44, 66)
        self.assertEqual(rect1.width, 22)
        self.assertEqual(rect1.height, 33)
        self.assertEqual(rect1.x, 0)
        self.assertEqual(rect1.y, 0)
        self.assertEqual(rect1.id, rect2.id - 1)

    def test_all_args(self):
        """Test Rectangle with all it's arguments"""
        r = Rectangle(22, 33, 1, 2, 3077)

        self.assertEqual(r.width, 22)
        self.assertEqual(r.height, 33)
        self.assertEqual(r.x, 1)
        self.assertEqual(r.y, 2)
        self.assertEqual(r.id, 3077)

    def test_base_instance(self):
        """Tests if Rectangle is an instance of Base"""
        self.assertTrue(isinstance(Rectangle(22, 33), Base))


class Test_Width_Values(unittest.TestCase):
    """this class deals with testing width argument types and operations"""

    def test_isint_arg_setter(self):
        """this class tests for instances that width arg and setter is an int
        """
        r = Rectangle(12, 13)
        self.assertEqual(r.width, 12)
        r.width = 19
        self.assertEqual(r.width, 19)

    def test_not_int_arg(self):
        """attempt to assign a non int to Rectangle argument"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("width", 22)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle([1, 2, 3], 22)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle((1, 2, 3), 22)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(1.4, 22)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(True, 22)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({1, 2, 3}, 22)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({'one': 1, 'two': 2, 'three': 3}, 22)

    def test_not_int_setter(self):
        """attempt to set non int to Rectangle object"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(33, 22)
            r.width = "width"
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(33, 22)
            r.width = [1, 2, 3]
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(33, 22)
            r.width = (1, 2, 3)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(33, 22)
            r.width = 1.4
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(33, 22)
            r.width = True
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(33, 22)
            r.width = {1, 2, 3}
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(33, 22)
            r.width = {'one': 1, 'two': 2, 'three': 3}

    def test_not_negative(self):
        """test if width is negative"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.width = -5
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-5, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 33)


class Test_Height_Values(unittest.TestCase):
    """this class deals with testing height argument types and operations"""

    def test_isint_arg_setter(self):
        """this class tests for instances that height arg and setter is an int
        """
        r = Rectangle(12, 13)
        self.assertEqual(r.height, 13)
        r.height = 19
        self.assertEqual(r.height, 19)

    def test_not_int_arg(self):
        """attempt to assign a non int to Rectangle argument"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(22, "height")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(22, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(22, (1, 2, 3))
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(22, 1.4)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(22, True)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(22, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(22, {'one': 1, 'two': 2, 'three': 3})

    def test_not_int_setter(self):
        """attempt to set non int to Rectangle object"""
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(33, 22)
            r.height = "height"
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(33, 22)
            r.height = [1, 2, 3]
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(33, 22)
            r.height = (1, 2, 3)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(33, 22)
            r.height = 1.4
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(33, 22)
            r.height = True
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(33, 22)
            r.height = {1, 2, 3}
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(33, 22)
            r.height = {'one': 1, 'two': 2, 'three': 3}

    def test_not_negative(self):
        """test if height is negative"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = 0
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.height = -5
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(33, -5)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(33, 0)


class Test_X_Values(unittest.TestCase):
    """this class deals with testing x argument types and operations"""

    def test_isint_arg_setter(self):
        """this class tests for instances that x arg and setter is an int
        """
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1, 20, 1)

        self.assertEqual(r1.x, 0)
        r1.x = 0
        self.assertEqual(r1.x, 0)

        self.assertEqual(r2.x, 20)
        r2.x = 40
        self.assertEqual(r2.x, 40)

    def test_not_int_arg(self):
        """attempt to assign a non int to Rectangle argument"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, "x", 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, [1, 2, 3], 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, (1, 2, 3), 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, 1.4, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, True, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, {1, 2, 3}, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(1, 1, {'one': 1, 'two': 2, 'three': 3}, 1)

    def test_not_int_setter(self):
        """attempt to set non int to Rectangle object"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1)
            r.x = "x"
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1)
            r.x = [1, 2, 3]
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1)
            r.x = (1, 2, 3)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1)
            r.x = 1.4
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1)
            r.x = True
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1)
            r.x = {1, 2, 3}
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1)
            r.x = {'one': 1, 'two': 2, 'three': 3}

    def test_not_negative(self):
        """test if x is negative"""
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.x = -5
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(1, 1, -5, 1)


class Test_Y_Values(unittest.TestCase):
    """this class deals with testing y argument types and operations"""

    def test_isint_arg_setter(self):
        """this class tests for instances that y arg and setter is an int
        """
        r1 = Rectangle(1, 1)
        r2 = Rectangle(1, 1, 1, 20)

        self.assertEqual(r1.y, 0)
        r1.y = 0
        self.assertEqual(r1.y, 0)

        self.assertEqual(r2.y, 20)
        r2.y = 40
        self.assertEqual(r2.y, 40)

    def test_not_int_arg(self):
        """attempt to assign a non int to Rectangle argument"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, "y")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, [1, 2, 3])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, (1, 2, 3))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, 1.4)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, {1, 2, 3})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(1, 1, 1, {'one': 1, 'two': 2, 'three': 3})

    def test_not_int_setter(self):
        """attempt to set non int to Rectangle object"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1)
            r.y = "y"
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1)
            r.y = [1, 2, 3]
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1)
            r.y = (1, 2, 3)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1)
            r.y = 1.4
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1)
            r.y = True
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1)
            r.y = {1, 2, 3}
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1)
            r.y = {'one': 1, 'two': 2, 'three': 3}

    def test_not_negative(self):
        """test if y is negative"""
        r = Rectangle(1, 1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.y = -5
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(1, 1, 1, -5)


if __name__ == '__main__':
    unittest.main()
