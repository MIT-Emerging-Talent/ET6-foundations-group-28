"""
Test module for find_smallest implementation.
This module contains unit tests for the find_smallest function using the unittest framework.
The tests verify correct behavior for valid inputs and proper error handling for invalid inputs.
Created: 31/12/2024
Team Name: MIT Alpha
@Author: Hassan Suliman
"""

import unittest
from ..find_smallest import find_smallest


class TestFindSmallest(unittest.TestCase):
    """Test cases for the `find_smallest` function."""

    # Standard test cases
    def test_single_element_list(self):
        """Test a list with a single element."""
        self.assertEqual(find_smallest([42]), 42)

    def test_multiple_elements(self):
        """Test a list with multiple elements."""
        self.assertEqual(find_smallest([3, 1, 2]), 1)

    def test_negative_numbers(self):
        """Test a list with negative numbers."""
        self.assertEqual(find_smallest([-5, -2, -10]), -10)

    def test_mixed_numbers(self):
        """Test a list with mixed positive and negative numbers."""
        self.assertEqual(find_smallest([10.5, -2.5, 0.0]), -2.5)

    # Edge cases
    def test_empty_list(self):
        """Test an empty list, which should raise a ValueError."""
        with self.assertRaises(ValueError):
            find_smallest([])

    def test_non_numeric_elements(self):
        """Test a list with non-numeric elements, which should raise a TypeError."""
        with self.assertRaises(TypeError):
            find_smallest(["a", 1])

    def test_non_list_input(self):
        """Test that the function raises a TypeError for non-list inputs."""
        with self.assertRaises(TypeError):
            find_smallest("not a list")

    def test_boolean_input(self):
        """Test that the function raises a TypeError for a list containing booleans."""
        with self.assertRaises(TypeError):
            find_smallest([True, 1])


if __name__ == "__main__":
    unittest.main()
