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
