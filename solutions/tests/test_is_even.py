#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Team Number: 28
Team Name: MIT Alpha
Author: Duha Mohammed
"""

import unittest
from ..is_even import is_even


class TestIsEven(unittest.TestCase):
    """Unit test class to test the `is_even` function."""

    def test_even(self):
        """Test that the function returns True for even numbers."""
        self.assertTrue(is_even(4))

    def test_odd(self):
        """Test that the function returns False for odd numbers."""
        self.assertFalse(is_even(5))

    def test_non_integer(self):
        """Test that an assertion error is raised for non-integer inputs."""
        with self.assertRaises(AssertionError):
            is_even("string")

    def test_zero(self):
        """Test that the function returns True for zero (an even number)."""
        self.assertTrue(is_even(0))


if __name__ == "__main__":
    unittest.main()
