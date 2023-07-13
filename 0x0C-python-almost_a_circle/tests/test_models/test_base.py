#!/usr/bin/python3

"""
This module is for testing the base module

              Index:
+------++-------------------------+
| Line ||       Class             |
+======++=========================+
| 21   || Test_Base_Documentation |
+------++-------------------------+
| 32   || Test_Base_Instantiation |
+------++-------------------------+

Date: 13/07/2023
Author: Bradley Dillion Gilden
"""


import unittest
from models.base import Base


class Test_Base_Documentation(unittest.TestCase):
    """Unit test to test for correct documentation"""

    def test_class_doc(self):
        self.assertGreater(len(Base.__doc__), 1)

    def test_init_doc(self):
        self.assertGreater(len(Base.__init__.__doc__), 1)


class Test_Base_Instantiation(unittest.TestCase):
    """Unit test for testing a Base object instantiation"""

    def test_no_arguments(self):
        """test instantiation with no arguments"""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_more_than_two(self):
        """test for more than two instantiations"""
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)
        self.assertEqual(b2.id, b3.id - 1)
        self.assertEqual(b3.id, b1.id + 2)

    def test_none_arguments(self):
        """test for None argument input"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_int_argument(self):
        """test for a single integer input"""
        b1 = Base(None)
        b2 = Base(700)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)
        self.assertEqual(b2.id, 700)

    def test_id_assignment(self):
        """test for public attribute id assignment"""
        b1 = Base()
        b2 = Base()
        b2.id = 117
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)
        self.assertEqual(b2.id, 117)


if __name__ == "__main__":
    unittest.main()
