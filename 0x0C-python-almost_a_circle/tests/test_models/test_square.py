#!/usr/bin/python3

"""
This module is for testing the rectangel module

              Index:
+------++------------------------------+
| Line ||           Class              |
+======++==============================+
| 40   || Test_Square_Documentation    |
+------++------------------------------+
| 65   || Test_Square_Instantiation    |
+------++------------------------------+
| 116  || Test_Size_Values             |
+------++------------------------------+
| 246  || Test_X_Values                |
+------++------------------------------+
| 313  || Test_Y_Values                |
+------++------------------------------+
| 380  || Test_Square_Functions        |
+------++------------------------------+
| 416  || Test_Square_Out              |
+------++------------------------------+

Date: 13/07/2023
Author: Bradley Dillion Gilden
"""

import unittest
from io import StringIO
from unittest.mock import patch
import models.square
from models.square import Square
from models.rectangle import Rectangle
from models.base import Base


class Test_Square_Documentation(unittest.TestCase):
    """Unit test for correct documentation of imports"""

    def test_module_doc(self):
        """test square module documentation"""
        self.assertGreaterEqual(len(models.square.__doc__), 1)

    def test_class_doc(self):
        """test Square class documentation"""
        self.assertGreaterEqual(len(Square.__doc__), 1)

    def test_method_docs(self):
        """test the methods of rectangle class"""
        self.assertGreaterEqual(len(Square.__init__.__doc__), 1)
        self.assertGreaterEqual(len(Square.size.__doc__), 1)
        self.assertGreaterEqual(len(Square.__str__.__doc__), 1)
        self.assertGreaterEqual(len(Square.update.__doc__), 1)
        self.assertGreaterEqual(len(Square.to_dictionary.__doc__), 1)


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


class Test_Square_Out(unittest.TestCase):
    """tests Square method outputs on stdout"""

    @staticmethod
    def capture(rect):
        """captures output from stdout and returns it as a string

        Args:
            rect(Square): Square object
            method(str): display method for Rectanlge object
        """
        output = StringIO()
        with patch('sys.stdout', new=output):
            rect.display()

        return output.getvalue()

    def test_display_no_xy(self):
        """test display function with just size and height"""
        expected = "###\n###\n###\n"
        output = Test_Square_Out.capture(Square(3))
        self.assertEqual(expected, output)

    def test_display_with_x(self):
        """test display function with just x"""
        expected = "    ##\n    ##\n"
        output = Test_Square_Out.capture(Square(2, 4))
        self.assertEqual(expected, output)

    def test_display_with_y(self):
        """test display function with just y"""
        expected = "\n\n\n\n##\n##\n"
        output = Test_Square_Out.capture(Square(2, 0, 4))
        self.assertEqual(expected, output)

    def test_display_with_xy(self):
        """test display function with all parameters except id"""
        expected = "\n\n ###\n ###\n ###\n"
        output = Test_Square_Out.capture(Square(3, 1, 2))
        self.assertEqual(expected, output)

    def test_display_with_xy_id(self):
        """test display function with all parameters"""
        expected = "\n\n ###\n ###\n ###\n"
        s = Square(3, 1, 2, 2022)
        output = Test_Square_Out.capture(s)
        self.assertEqual(expected, output)
        self.assertEqual(s.id, 2022)

    def test_print_size_height(self):
        """print object with size and height"""
        r = Square(3)
        expected = f"[Square] ({r.id:d}) 0/0 - 3"
        self.assertEqual(expected, str(r))

    def test_print_id(self):
        """print object with id"""
        r = Square(3, 0, 0, 818)
        expected = "[Square] (818) 0/0 - 3"
        self.assertEqual(expected, str(r))

    def test_print_all(self):
        """print object with all parameters"""
        r = Square(2, 1, 1, 310)
        expected = "[Square] (310) 1/1 - 2"
        self.assertEqual(expected, str(r))

    def test_update_args_none_id(self):
        r = Square(10, 10, 10, 10)
        r.update(None)
        correct = f"[Square] ({r.id}) 10/10 - 10"
        self.assertEqual(correct, str(r))

    def test_update_nothing(self):
        """test no parameter update"""
        r = Square(23)
        r.update()
        expected = f"[Square] ({r.id:d}) 0/0 - 23"
        self.assertEqual(expected, str(r))

    def test_update_id(self):
        """test update function with id"""
        r1 = Square(33)
        r2 = Square(33, 0, 0, 420)
        r1.update(240)
        r2.update(720)
        expected1 = "[Square] (240) 0/0 - 33"
        expected2 = "[Square] (720) 0/0 - 33"
        self.assertEqual(expected1, str(r1))
        self.assertEqual(expected2, str(r2))

    def test_update_all(self):
        """test update function with all arguments"""
        r = Square(9)
        r.update(890, 3)
        expected = "[Square] (890) 0/0 - 3"
        self.assertEqual(expected, str(r))

        r.update(891, 3, 21)
        expected = "[Square] (891) 21/0 - 3"
        self.assertEqual(expected, str(r))

        r.update(892, 3, 21, 40)
        expected = "[Square] (892) 21/40 - 3"
        self.assertEqual(expected, str(r))

    def test_update_full(self):
        """test update function with already filled arguments"""
        r = Square(1, 3, 4, 12345)
        r.update(54321, 4, 3, 1)
        expected = "[Square] (54321) 3/1 - 4"
        self.assertEqual(expected, str(r))

    def test_update_many_args(self):
        """test update function with more than maximum arguments"""
        r = Square(9, 5)
        r.update(232, 2, 21, 9, 8, 3, 5)
        expected = "[Square] (232) 21/9 - 2"
        self.assertEqual(expected, str(r))

    def test_update_kwargs_None_id(self):
        r = Square(10, 10, 10, 10)
        r.update(id=None)
        correct = f"[Square] ({r.id}) 10/10 - 10"
        self.assertEqual(correct, str(r))

    def test_update_keyword_args(self):
        """this function tests updates ability to handle keyword args"""
        r = Square(3)
        r.update(height=3)
        expected = f"[Square] ({r.id}) 0/0 - 3"
        self.assertEqual(str(r), expected)

    def test_update_3keyword_args(self):
        """this function tests update with 3 keyword arguments"""
        r = Square(3, 5)
        r.update(x=2, size=45)
        expected = f"[Square] ({r.id}) 2/0 - 45"
        self.assertEqual(str(r), expected)

    def test_update_4keyword_args(self):
        """this function tests update with 4 keyword arguments"""
        r = Square(32, 21, 84)
        r.update(y=20, size=35, x=88)
        expected = f"[Square] ({r.id}) 88/20 - 35"
        self.assertEqual(str(r), expected)

    def test_update_5keyword_args(self):
        """this function tests update with 5 keyword arguments"""
        r = Square(32, 21, 84, 1020)
        r.update(id=208, x=35, y=77, size=1)
        expected = f"[Square] ({208}) 35/77 - 1"
        self.assertEqual(str(r), expected)

    def test_update_multiple_keyword_args(self):
        """this function tests update function with multiple arguments"""
        r = Square(22)
        r.update(x=33, id=99, size=22, y=55, edges=433)
        expected = f"[Square] ({99}) 33/55 - 22"
        self.assertEqual(expected, str(r))

    def test_update_args_kwargs(self):
        """this function tests update function with args and kwargs"""
        r = Square(22)
        r.update(21, 234, x=220, y=5)
        expected = f"[Square] ({21}) 0/0 - 234"
        self.assertEqual(expected, str(r))

    def test_update_err1_int(self):
        """this function tests for update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(r.id, "22", "33", "2")

    def test_update_err3_int(self):
        """this function tests for update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(r.id, r.size, "2", "1")

    def test_update_err4_int(self):
        """this function tests for update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(r.id, r.size, r.x, "3")

    def test_update_err1_negative(self):
        """this function tests for update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(r.id, -22, -33, -3)

    def test_update_err3_negative(self):
        """this function tests for update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(r.id, r.size, -2, -1)

    def test_update_err4_negative(self):
        """this function tests for update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(r.id, r.size, r.x, -3)

    def test_update_err1_zero(self):
        """this function tests for update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(r.id, 0, -33, -3)

    def test_update_kwerr1_int(self):
        """this function tests for keyword update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(size="big")

    def test_update_kwerr3_int(self):
        """this function tests for keyword update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(y=r.x, id=33, x="WEEE")

    def test_update_kwerr4_int(self):
        """this function tests for keyword update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(id=r.id, size=r.size, y="why")

    def test_update_kwerr1_negative(self):
        """this function tests for keyword update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(id=r.id, size=-22, y=-3, x=-1)

    def test_update_kwerr3_negative(self):
        """this function tests for keyword update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(id=r.id, size=r.size, y=2, x=-1)

    def test_update_kwerr4_negative(self):
        """this function tests for keyword update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(id=r.id, x=2, size=3, y=-3)

    def test_update_kwerr1_zero(self):
        """this function tests for keyword update errors"""
        r = Square(22, 33)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(id=r.id, y=0, size=-3, x=-1)


if __name__ == "__main__":
    unittest.main()
