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
from io import StringIO
from unittest.mock import patch
from models.base import Base
import models.rectangle
from models.rectangle import Rectangle


class Test_Rectangle_Documentation(unittest.TestCase):
    """Unit test for correct documentation of imports"""

    def test_module_doc(self):
        """test rectangle module documentation"""
        self.assertGreaterEqual(len(models.rectangle.__doc__), 1)

    def test_class_doc(self):
        """test Rectangle class documentation"""
        self.assertGreaterEqual(len(Rectangle.__doc__), 1)

    def test_method_docs(self):
        """test the methods of rectangle class"""
        self.assertGreaterEqual(len(Rectangle.__init__.__doc__), 1)
        self.assertGreaterEqual(len(Rectangle.width.__doc__), 1)
        self.assertGreaterEqual(len(Rectangle.height.__doc__), 1)
        self.assertGreaterEqual(len(Rectangle.x.__doc__), 1)
        self.assertGreaterEqual(len(Rectangle.y.__doc__), 1)
        self.assertGreaterEqual(len(Rectangle.area.__doc__), 1)
        self.assertGreaterEqual(len(Rectangle.display.__doc__), 1)
        self.assertGreaterEqual(len(Rectangle.__str__.__doc__), 1)
        self.assertGreaterEqual(len(Rectangle.update.__doc__), 1)
        self.assertGreaterEqual(len(Rectangle.to_dictionary.__doc__), 1)


class Test_Rectangle_Instantiation(unittest.TestCase):
    """Tests Rectangle objects behaviour during instantiation"""

    def test_base_instance(self):
        """Tests if Rectangle is an instance of Base"""
        self.assertTrue(isinstance(Rectangle(22, 33), Base))

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

    def test_base_rectangle(self):
        """Ensures base and rectangle id's correlate"""
        b = Base()
        r = Rectangle(1, 1)
        self.assertEqual(1, r.id - b.id)


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


class Test_Rectangle_Functions(unittest.TestCase):
    """test outcome of functions of Rectangle"""

    def test_area_args(self):
        """this function tests area with arguments"""
        r = Rectangle(2, 2)
        with self.assertRaises(TypeError):
            r.area(22)

    def test_area(self):
        """test area of Rectangle instance"""
        r = Rectangle(2, 11)
        self.assertEqual(r.area(), 22)
        r.width = 1
        self.assertEqual(r.area(), 11)
        self.assertEqual(Rectangle(3, 22, 0, 0, 99).area(), 66)

    def test_to_dictionary_args(self):
        """tests to dictionary function with arguments"""
        r = Rectangle(2, 11)
        with self.assertRaises(TypeError):
            r.to_dictionary(300)

    def test_to_dictionary(self):
        """tests a Rectangle objects to dictionary function"""
        r1 = Rectangle(1, 2, 3, 4, 5)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(1, 2)
        dict1 = {"width": 1, "height": 2, "x": 3, "y": 4, "id": 5}
        dict2 = {"width": 1, "height": 2, "x": 3, "y": 4, "id": r2.id}
        dict3 = {"width": 1, "height": 2, "x": 0, "y": 0, "id": r2.id + 1}
        self.assertEqual(r1.to_dictionary(), dict1)
        self.assertEqual(r2.to_dictionary(), dict2)
        self.assertEqual(r3.to_dictionary(), dict3)


class Test_Rect_Out(unittest.TestCase):
    """tests Rectangle method outputs on stdout"""

    @staticmethod
    def capture(rect):
        """captures output from stdout and returns it as a string

        Args:
            rect(Rectangle): Rectangle object
            method(str): display method for Rectanlge object
        """
        output = StringIO()
        with patch('sys.stdout', new=output):
            rect.display()

        return output.getvalue()

    def test_display_no_xy(self):
        """test display function with just width and height"""
        expected = "###\n###\n###\n###\n"
        output = Test_Rect_Out.capture(Rectangle(3, 4))
        self.assertEqual(expected, output)

    def test_display_with_x(self):
        """test display function with just x"""
        expected = "    ##\n    ##\n"
        output = Test_Rect_Out.capture(Rectangle(2, 2, 4))
        self.assertEqual(expected, output)

    def test_display_with_y(self):
        """test display function with just y"""
        expected = "\n\n\n\n##\n##\n"
        output = Test_Rect_Out.capture(Rectangle(2, 2, 0, 4))
        self.assertEqual(expected, output)

    def test_display_with_xy(self):
        """test display function with all parameters except id"""
        expected = "\n\n ###\n ###\n"
        output = Test_Rect_Out.capture(Rectangle(3, 2, 1, 2))
        self.assertEqual(expected, output)

    def test_display_with_xy_id(self):
        """test display function with all parameters"""
        expected = "\n\n ###\n ###\n"
        r = Rectangle(3, 2, 1, 2, 2022)
        output = Test_Rect_Out.capture(r)
        self.assertEqual(expected, output)
        self.assertEqual(r.id, 2022)

    def test_print_width_height(self):
        """print object with width and height"""
        r = Rectangle(3, 4)
        expected = f"[Rectangle] ({r.id:d}) 0/0 - 3/4"
        self.assertEqual(expected, str(r))

    def test_print_id(self):
        """print object with id"""
        r = Rectangle(3, 4, 0, 0, 818)
        expected = "[Rectangle] (818) 0/0 - 3/4"
        self.assertEqual(expected, str(r))

    def test_print_all(self):
        """print object with all parameters"""
        r = Rectangle(2, 2, 1, 1, 310)
        expected = "[Rectangle] (310) 1/1 - 2/2"
        self.assertEqual(expected, str(r))

    def test_update_args_none_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(None)
        correct = f"[Rectangle] ({r.id}) 10/10 - 10/10"
        self.assertEqual(correct, str(r))

    def test_update_nothing(self):
        """test no parameter update"""
        r = Rectangle(23, 32)
        r.update()
        expected = f"[Rectangle] ({r.id:d}) 0/0 - 23/32"
        self.assertEqual(expected, str(r))

    def test_update_id(self):
        """test update function with id"""
        r1 = Rectangle(33, 22)
        r2 = Rectangle(33, 22, 0, 0, 420)
        r1.update(240)
        r2.update(720)
        expected1 = "[Rectangle] (240) 0/0 - 33/22"
        expected2 = "[Rectangle] (720) 0/0 - 33/22"
        self.assertEqual(expected1, str(r1))
        self.assertEqual(expected2, str(r2))

    def test_update_all(self):
        """test update function with all arguments"""
        r = Rectangle(9, 5)
        r.update(890, 3)
        expected = "[Rectangle] (890) 0/0 - 3/5"
        self.assertEqual(expected, str(r))

        r.update(891, 3, 21)
        expected = "[Rectangle] (891) 0/0 - 3/21"
        self.assertEqual(expected, str(r))

        r.update(892, 3, 21, 40)
        expected = "[Rectangle] (892) 40/0 - 3/21"
        self.assertEqual(expected, str(r))

        r.update(893, 3, 21, 40, 100)
        expected = "[Rectangle] (893) 40/100 - 3/21"
        self.assertEqual(expected, str(r))

    def test_update_full(self):
        """test update function with already filled arguments"""
        r = Rectangle(1, 2, 3, 4, 12345)
        r.update(54321, 4, 3, 2, 1)
        expected = "[Rectangle] (54321) 2/1 - 4/3"
        self.assertEqual(expected, str(r))

    def test_update_many_args(self):
        """test update function with more than maximum arguments"""
        r = Rectangle(9, 5)
        r.update(232, 2, 32, 21, 9, 8, 3, 5)
        expected = "[Rectangle] (232) 21/9 - 2/32"
        self.assertEqual(expected, str(r))

    def test_update_kwargs_None_id(self):
        r = Rectangle(10, 10, 10, 10, 10)
        r.update(id=None)
        correct = f"[Rectangle] ({r.id}) 10/10 - 10/10"
        self.assertEqual(correct, str(r))

    def test_update_keyword_args(self):
        """this function tests updates ability to handle keyword args"""
        r = Rectangle(3, 5)
        r.update(height=3)
        expected = f"[Rectangle] ({r.id}) 0/0 - 3/3"
        self.assertEqual(str(r), expected)

    def test_update_3keyword_args(self):
        """this function tests update with 3 keyword arguments"""
        r = Rectangle(3, 5, 9)
        r.update(x=2, width=45)
        expected = f"[Rectangle] ({r.id}) 2/0 - 45/5"
        self.assertEqual(str(r), expected)

    def test_update_4keyword_args(self):
        """this function tests update with 4 keyword arguments"""
        r = Rectangle(32, 21, 43, 84)
        r.update(y=20, width=35, x=88, height=1)
        expected = f"[Rectangle] ({r.id}) 88/20 - 35/1"
        self.assertEqual(str(r), expected)

    def test_update_5keyword_args(self):
        """this function tests update with 5 keyword arguments"""
        r = Rectangle(32, 21, 43, 84, 1020)
        r.update(id=208, x=35, height=88, y=77, width=1)
        expected = f"[Rectangle] ({208}) 35/77 - 1/88"
        self.assertEqual(str(r), expected)

    def test_update_multiple_keyword_args(self):
        """this function tests update function with multiple arguments"""
        r = Rectangle(22, 2)
        r.update(x=33, id=99, height=77, width=22, y=55, edges=433)
        expected = f"[Rectangle] ({99}) 33/55 - 22/77"
        self.assertEqual(expected, str(r))

    def test_update_args_kwargs(self):
        """this function tests update function with args and kwargs"""
        r = Rectangle(22, 2)
        r.update(21, 234, x=220, y=5)
        expected = f"[Rectangle] ({21}) 0/0 - 234/2"
        self.assertEqual(expected, str(r))

    def test_update_err1_int(self):
        """this function tests for update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(r.id, "22", "33", "2", "1")

    def test_update_err2_int(self):
        """this function tests for update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(r.id, r.width, "1", "2", "3")

    def test_update_err3_int(self):
        """this function tests for update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(r.id, r.width, r.height, "2", "1")

    def test_update_err4_int(self):
        """this function tests for update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(r.id, r.width, r.height, r.x, "3")

    def test_update_err1_negative(self):
        """this function tests for update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(r.id, -22, -33, -3, -1)

    def test_update_err2_negative(self):
        """this function tests for update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(r.id, r.width, -1, -2, -3)

    def test_update_err3_negative(self):
        """this function tests for update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(r.id, r.width, r.height, -2, -1)

    def test_update_err4_negative(self):
        """this function tests for update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(r.id, r.width, r.height, r.x, -3)

    def test_update_err1_zero(self):
        """this function tests for update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(r.id, 0, -33, -3, -1)

    def test_update_err2_zero(self):
        """this function tests for update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(r.id, r.width, 0, -2, -3)

    def test_update_kwerr1_int(self):
        """this function tests for keyword update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(width="big")

    def test_update_kwerr2_int(self):
        """this function tests for keyword update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(id=r.id, width=r.height, x=r.y, height="low", y=4)

    def test_update_kwerr3_int(self):
        """this function tests for keyword update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(y=r.x, id=33, x="WEEE")

    def test_update_kwerr4_int(self):
        """this function tests for keyword update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(id=r.id, width=r.width, y="why")

    def test_update_kwerr1_negative(self):
        """this function tests for keyword update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(id=r.id, width=-22, height=-33, y=-3, x=-1)

    def test_update_kwerr2_negative(self):
        """this function tests for keyword update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(id=r.id, height=-22, width=-33, y=-3, x=-1)

    def test_update_kwerr3_negative(self):
        """this function tests for keyword update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(id=r.id, height=r.width, width=r.height, y=2, x=-1)

    def test_update_kwerr4_negative(self):
        """this function tests for keyword update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(id=r.id, height=3, x=2, width=3, y=-3)

    def test_update_kwerr1_zero(self):
        """this function tests for keyword update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(id=r.id, y=0, height=5, width=-3, x=-1)

    def test_update_kwerr2_zero(self):
        """this function tests for keyword update errors"""
        r = Rectangle(22, 33)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(id=r.id, width=r.width, x=0, height=0, y=-2)


if __name__ == '__main__':
    unittest.main()
