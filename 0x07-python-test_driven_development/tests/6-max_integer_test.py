#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
from 6-max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function"""

    def test_max_integer(self):
        """Test with various cases"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)  # Normal case
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)  # Normal case
        self.assertEqual(max_integer([5, 1, 2, 3]), 5)  # Max at the start
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)  # All negative numbers
        self.assertEqual(max_integer([1]), 1)  # Single element
        self.assertIsNone(max_integer([]))  # Empty list

    def test_max_integer_with_floats(self):
        """Test with lists containing floats"""
        self.assertEqual(max_integer([1.1, 2.2, 3.3, 4.4]), 4.4)
        self.assertEqual(max_integer([1.0, 2.0, 3.0]), 3.0)
        self.assertEqual(max_integer([-1.1, -2.2, -3.3]), -1.1)

    def test_max_integer_with_mixed_types(self):
        """Test with lists containing integers and floats"""
        self.assertEqual(max_integer([1, 2.2, 3]), 3)
        self.assertEqual(max_integer([1.1, 2, 3.0]), 3.0)

    def test_max_integer_exceptions(self):
        """Test for invalid input"""
        with self.assertRaises(TypeError):
            max_integer("string")
        with self.assertRaises(TypeError):
            max_integer(None)
        with self.assertRaises(TypeError):
            max_integer([1, 'string', 3])

if __name__ == '__main__':
    unittest.main()

