#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for between_two_sets implementation.
This module contains unit tests for the between_two_sets function using the unittest framework.
The tests verify correct behavior for valid inputs and proper error handling for invalid inputs.
Created: 04/01/2025
Team Name: MIT Alpha
@Author: Hassan Suliman
"""

import unittest
from ..between_two_sets import between_two_sets


class TestGetTotalX(unittest.TestCase):
    """Test cases for the `between_two_sets` function."""

    def test_standard_case(self):
        """Test with standard input values."""
        self.assertEqual(between_two_sets([2, 4], [16, 32, 96]), 3)

    def test_single_element_lists(self):
        """Test with single-element lists."""
        self.assertEqual(between_two_sets([3], [12]), 3)

    def test_no_common_factors(self):
        """Test with lists that have no common factors or multiples."""
        self.assertEqual(between_two_sets([2, 3], [7, 11]), 0)

    def test_large_range(self):
        """Test with larger range of numbers."""
        self.assertEqual(between_two_sets([1], [100]), 9)

    # Edge cases
    def test_empty_a(self):
        """Test with empty `a` list, which should raise a ValueError."""
        with self.assertRaises(ValueError):
            between_two_sets([], [16, 32, 96])

    def test_empty_b(self):
        """Test with empty `b` list, which should raise a ValueError."""
        with self.assertRaises(ValueError):
            between_two_sets([2, 4], [])

    def test_non_integer_elements(self):
        """Test with non-integer elements in input lists, which should raise a TypeError."""
        with self.assertRaises(TypeError):
            between_two_sets([2, "a"], [16, 32])

    def test_non_list_inputs(self):
        """Test with non-list inputs, which should raise a TypeError."""
        with self.assertRaises(TypeError):
            between_two_sets("not a list", [16, 32])


if __name__ == "__main__":
    unittest.main()
