#!/usr/bin/python3
"""Unittest for max_integer([..])
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unit Test class for the 6-max_integer function
    6-max_integer accepts a list of integers and returns the maximum value
    """

    def test_empty_list(self):
        """Tests an empty list to see if it returns None"""
        self.assertEqual(max_integer([]), None)

    def test_ordered_int(self):
        """Tests an ordered list of integers"""
        self.assertEqual(max_integer([4, 5, 6, 7, 8]), 8)

    def test_unordered_int(self):
        """Tests an unordered list of integers"""
        self.assertEqual(max_integer([5, 90, 34, 21]), 90)

    def test_floats(self):
        """Tests for any ordered list of floating point numbers"""
        self.assertEqual(max_integer([2.3, 6.9, 39.3, 2.2]), 39.3)

    def test_single_digit(self):
        """Tests a single digit input"""
        self.assertEqual(max_integer([3]), 3)

    def test_float_and_int(self):
        """Tests a list of both floats and ints"""
        self.assertEqual(max_integer([2.3, 2, 90.1, 90, 4]), 90.1)

    def test_empty_tuple(self):
        """Tests an empty tuple, should return None"""
        self.assertEqual(max_integer(()), None)

    def test_empty_string(self):
        """Tests an empty string, should return None"""
        self.assertEqual(max_integer(""), None)

    def test_list_of_strings(self):
        """Tests a list of strings based on lexicographical order"""
        s_list = ["fear", "is", "the", "mind", "killer"]
        self.assertEqual(max_integer(s_list), "the")
