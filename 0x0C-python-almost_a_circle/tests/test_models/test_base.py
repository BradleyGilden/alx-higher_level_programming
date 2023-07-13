#!/usr/bin/python3

"""
This module is for testing the base module

              Index:
+------++-------------------------+
| Line ||       Class             |
+======++=========================+
| 25   || Test_Base_Documentation |
+------++-------------------------+
| 38   || Test_Base_Instantiation |
+------++-------------------------+

Date: 13/07/2023
Author: Bradley Dillion Gilden
"""


import unittest
import models.base
from models.base import Base


class Test_Base_Documentation(unittest.TestCase):
    """Unit test to test for correct documentation"""

    def test_module_doc(self):
        """test modules documentation"""
        self.assertGreater(len(models.base.__doc__), 1)

    def test_class_doc(self):
        """tests class' documentation"""
        self.assertGreater(len(Base.__doc__), 1)

    def test_init_doc(self):
        """tests init method documentation"""
        self.assertGreater(len(Base.__init__.__doc__), 1)


class Test_Base_Instantiation(unittest.TestCase):
    """Unit test for testing a Base object instantiation"""

    def test_no_arg(self):
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

    def test_none_arg(self):
        """test for None argument input"""
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_int_arg(self):
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

    def test_negative_arg(self):
        """tests negative value for id"""
        self.assertEqual(Base(-1).id, -1)

    def test_float_arg(self):
        """tests float id argument input"""
        self.assertEqual(Base(1.4).id, 1.4)

    def test_string_arg(self):
        """tests string id argument"""
        self.assertEqual(Base('Petrificus Totalus').id, 'Petrificus Totalus')

    def test_tuple_arg(self):
        """tests tuple id argument"""
        self.assertEqual(Base((1, )).id, (1, ))

    def test_list_arg(self):
        """tests list id argument"""
        self.assertEqual(Base([1, 2, 3]).id, [1, 2, 3])

    def test_dict_arg(self):
        """tests dictionary id arguments"""
        self.assertEqual(Base({'ola': 1, 'hey': 2}).id, {'ola': 1, 'hey': 2})

    def test_set_arg(self):
        """tests set id arguments"""
        self.assertEqual(Base({1, 2, 3}).id, {1, 2, 3})

    def test_bool_arg(self):
        """test boolean id argumetns"""
        self.assertEqual(Base(True).id, True)

    def test_private_directly(self):
        """attempt access private attribute directly"""
        b1 = Base()
        with self.assertRaises(AttributeError):
            b1.__nb_objects

    def test_two_args(self):
        """attempt to use two arguments"""
        with self.assertRaises(TypeError):
            Base(1, 2)


if __name__ == "__main__":
    unittest.main()
