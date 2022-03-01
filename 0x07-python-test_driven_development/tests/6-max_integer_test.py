#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_empty_list(self):
        """Checks if list is empty"""
        x = []
        self.assertIsNone(max_integer(x))

    def test_no_arguments(self):
        """checks no arguments passed"""
        self.assertIsNone(max_integer())

    def test_none(self):
        """Checks when none is passed"""
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_one_item(self):
        """Tests for only one number in the list"""
        one = [1]
        self.assertEqual(max_integer(one), 1)

    def test_all_neg(self):
        """Tests for list with all negative nbrs"""
        neg = [-7, -42, -68, -3, -240]
        self.assertEqual(max_integer(neg), -3)

    def test_positive_beginning(self):
        """Tests for max at beginning"""
        beg = [187, 23, 21, 57, 27, 63]
        self.assertEqual(max_integer(beg), 187)

    def test_positive_end(self):
        """Tests for max int in end"""
        end = [15, 25, 21, 49, 27, 63]
        self.assertEqual(max_integer(end), 63)

    def test_positive_middle(self):
        """Tests for all positive with max in middle"""
        mid = [1, 17, 25, 412, 2, 67]
        self.assertEqual(max_integer(mid), 412)

    def test_non_int(self):
        """Tests for a non-int type in list"""
        string = [1, 2, "Python", 4, 5]
        with self.assertRaises(TypeError):
            max_integer(string)

if __name__ == "__main__":
    unittest.main()
