#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Test module for is_palindrome implementation.

This module contains unit tests for the is_palindrome function using the unittest framework.
The tests verify correct behavior for valid inputs and proper error handling for invalid inputs.

Created: 31/12/2024
Team Name: MIT Alpha
@Author: Nada Hamza

"""

import unittest
from ..is_palindrome import is_palindrome


class TestIsPalindrome(unittest.TestCase):
    """Test cases for the `is_palindrome` function."""

    # Standard test cases
    def test_simple_palindrome(self):
        """Test a simple palindrome with only lowercase letters."""
        self.assertTrue(is_palindrome("racecar"))

    def test_mixed_case_palindrome(self):
        """Test a palindrome with both uppercase and lowercase letters."""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_numeric_palindrome(self):
        """Test a palindrome consisting of numbers."""
        self.assertTrue(is_palindrome("12321"))

    def test_non_palindrome(self):
        """Test a string that is not a palindrome."""
        self.assertFalse(is_palindrome("hello"))

    # Edge cases
    def test_empty_string(self):
        """Test an empty string, which is considered a palindrome."""
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        """Test a string with a single character."""
        self.assertTrue(is_palindrome("a"))

    def test_spaces_and_punctuation(self):
        """Test a palindrome with punctuation and spaces."""
        self.assertTrue(is_palindrome("Madam, in Eden, I'm Adam"))

    # Defensive tests
    def test_non_string_input(self):
        """Test that the function raises a TypeError for non-string inputs."""
        with self.assertRaises(TypeError):
            is_palindrome(12345)

    def test_boolean_input(self):
        """It should raise a TypeError for boolean input."""
        with self.assertRaises(TypeError):
            is_palindrome(True)


if __name__ == "__main__":
    unittest.main()
