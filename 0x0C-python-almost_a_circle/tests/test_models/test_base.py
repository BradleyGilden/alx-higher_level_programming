#!/usr/bin/python3

"""
This module is for testing the base module

Date: 13/07/2023
Author: Bradley Dillion Gilden
"""


import unittest
from models.base import Base


class Test_Base_Instantiation(unittest.TestCase):
    """Unit test for testing a Base object instantiation"""

    def Test_with_no_arguments(self):
        """test instantiation with no arguments"""
        b1 = Base()
        b2 = Base()
        b3 = Base(None)
        b4 = Base(None)
        self.assertEqual(b1.id, 1), self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3), self.assertEqual(b4.id, 4)


if __name__ == "__main__":
    unittest.main()
