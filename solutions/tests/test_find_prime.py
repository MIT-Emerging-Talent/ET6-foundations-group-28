#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Team Number: 28
Team Name: MIT Alpha
Author: Maab Mohamedkhair
"""

import unittest
from ..find_prime import find_prime


class TestIsPrime(unittest.TestCase):
    """
    This class contains unit tests for the (find_prime) function.
    The function takes a positive integer greater than one,
    and returns a boolean value representing if it's a prime number or not.
    """

    # Standard test cases
    def test_prime_numbers(self):
        """This test checks the function's performance with prime numbers."""
        self.assertEqual(find_prime(3), True)

    def test_non_prime_numbers(self):
        """This test checks the function's performance with non-prime numbers."""
        self.assertEqual(find_prime(27), False)

    def test_large_numbers(self):
        """This test checks if the function works with large numbers."""
        self.assertEqual(find_prime(131), True)

    def test_even_numbers(self):
        """This test checks if the function works with even numbers."""
        self.assertEqual(find_prime(24), False)

    # Edge cases
    def test_number_two(self):
        """This test checks if the function considers two as a prime number."""
        self.assertEqual(find_prime(2), True)  # 2 is the only even prime

    def test_number_one(self):
        """This test checks the function behavior with the smallest value."""
        self.assertEqual(find_prime(1), False)  # 1 is the common factor for all numbers

    # Defensive tests
    def test_float_numbers(self):
        """This test checks the function behavior with non-integer values."""
        with self.assertRaises(AssertionError):
            find_prime(2.4)

    def test_negative_numbers(self):
        """This test checks the function behavior with negative numbers."""
        with self.assertRaises(AssertionError):
            find_prime(-3)

    def test_zero(self):
        """This test checks the function behavior with zero."""
        with self.assertRaises(AssertionError):
            find_prime(0)
