#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Team Number: 28
Team Name: MIT Alpha
Author: Maab Mohamedkhair
"""

import unittest
from ..sum_numbers import sum_numbers


class TestSumNumbers(unittest.TestCase):
    """
    This class contains unit tests for the (sum_numbers) function.
    The function takes a positive integer, counts down until it reaches one,
    and returns the sum of all numbers.
    """

    # Standard test cases
    def test_base_case(self):
        """This test checks if the base case (n=1) works correctly."""
        self.assertEqual(sum_numbers(1), 1)

    def test_positive_int(self):
        """This test checks if the function works in the normal case."""
        self.assertEqual(sum_numbers(4), 10)

    def test_two_digit_int(self):
        """This test checks the function efficiency with numbers between 10 and 99."""
        self.assertEqual(sum_numbers(25), 325)

    # Edge cases
    def test_large_number(self):
        """This test checks the function's performance for
        a large number close to the recursion limit."""
        self.assertEqual(sum_numbers(900), 405450)

    # Defensive tests
    def test_zero(self):
        """This test checks if the function raises an AssertionError for zero input."""
        with self.assertRaises(AssertionError):
            sum_numbers(0)

    def test_negative_int(self):
        """This test checks if the function raises an AssertionError for negative input."""
        with self.assertRaises(AssertionError):
            sum_numbers(-3)

    def test_float(self):
        """This test checks if the function raises an AssertionError when n is a float."""
        with self.assertRaises(AssertionError):
            sum_numbers(1.4)

    def test_exceed_recursion_limit(self):
        """This test checks if the function raises
        an AssertionError for numbers greater than or equal 1000."""
        with self.assertRaises(AssertionError):
            sum_numbers(1000)


if __name__ == "__main__":
    unittest.main()
