#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test module for count_vowels implementation.

This module contains unit tests for the count_vowels function using the unittest framework.

Created: 29/12/2024
Team Number: 28
Team Name: MIT Alpha
Author: Ghyath Ibrahim
"""

import unittest
from ..count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    """Test cases for count_vowels function.

    Test suite verifies:
    - Input validation
    - Case insensitivity
    - Special characters handling
    - Edge cases
    """

    def test_invalid_type_raises_assertion_error(self):
        """Test that non-string input raises AssertionError."""
        with self.assertRaises(AssertionError):
            count_vowels(123)

    def test_empty_string_returns_zero(self):
        """Test that empty string returns 0."""
        self.assertEqual(count_vowels(""), 0)

    def test_string_no_vowels(self):
        """Test string containing no vowels."""
        self.assertEqual(count_vowels("xyz"), 0)

    def test_string_all_vowels(self):
        """Test string containing only vowels."""
        self.assertEqual(count_vowels("aeiou"), 5)

    def test_case_insensitive(self):
        """Test that function is case insensitive."""
        self.assertEqual(count_vowels("AeIoU"), 5)

    def test_mixed_string(self):
        """Test string with mix of vowels and consonants."""
        self.assertEqual(count_vowels("Hello World"), 3)

    def test_special_characters(self):
        """Test string containing special characters."""
        self.assertEqual(count_vowels("Hello! @#$"), 2)

    def test_spaces_only(self):
        """Test string containing only spaces."""
        self.assertEqual(count_vowels("   "), 0)

    def test_repeated_vowels(self):
        """Test string with repeated vowels."""
        self.assertEqual(count_vowels("book"), 2)
