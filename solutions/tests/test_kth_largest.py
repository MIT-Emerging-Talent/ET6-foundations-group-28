#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for kth largest in a list function.

This module contains unit tests for the kth largest in a list
function using the unittest framework.

Created: 04/01/2025
Team Number: 28
Team Name: MIT Alpha
Author: Ahd AbdelRahim
"""

import unittest

from ..kth_largest import kth_largest


class TestKthLargest(unittest.TestCase):
    """Test kth largest Function"""

    # BASE CASES
    def test_normal_case(self):
        """It should return the correct kth largest element"""
        actual = kth_largest(["3", "2", "1", "5", "6", "4"], 2)
        expected = "5"
        self.assertEqual(actual, expected)

    def test_duplicate_elements(self):
        """It should return the correct kth largest element"""
        actual = kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], 4)
        expected = "4"
        self.assertEqual(actual, expected)

    def test_k_is_one(self):
        """It should return the largest element in the list"""
        actual = kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], 1)
        expected = "6"
        self.assertEqual(actual, expected)

    # EDGE CASES
    def test_k_equal_list_length(self):
        """It should return the smallest element in the list"""
        actual = kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], 9)
        expected = "1"
        self.assertEqual(actual, expected)

    def test_single_element(self):
        """It should return the only element when the list has one element"""
        actual = kth_largest(["42"], 1)
        expected = "42"
        self.assertEqual(actual, expected)

    def test_sorted_list_k_is_1(self):
        """It should return the largest element when the list is sorted"""
        actual = kth_largest(["1", "2", "3", "4", "5"], 1)
        expected = "5"
        self.assertEqual(actual, expected)

    def test_identical_elements(self):
        """It should return the correct kth largest element when all elements are identical"""
        actual = kth_largest(["7", "7", "7", "7"], 3)
        expected = "7"
        self.assertEqual(actual, expected)

    def test_large_number(self):
        """It should return the correct kth largest element when the numbers are large"""
        actual = kth_largest(["1000000", "1", "5000"], 2)
        expected = "5000"
        self.assertEqual(actual, expected)

    # DEFENSIVE CASES
    def test_empty_list(self):
        """It should raise an AssertionError for an empty list"""
        with self.assertRaises(AssertionError):
            kth_largest([], 1)

    def test_non_numeric_strings(self):
        """It should raise an AssertionError if non-numeric strings are included"""
        with self.assertRaises(AssertionError):
            kth_largest(["apple", "banana", "cherry"], 2)

    def test_k_is_negative(self):
        """It should raise a AssertionError if k is negative"""
        with self.assertRaises(AssertionError):
            kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], -1)

    def test_k_is_zero(self):
        """It should raise a AssertionError if k is zero"""
        with self.assertRaises(AssertionError):
            kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], 0)

    def test_not_a_list(self):
        """It should raise an AssertionError if the input is not a list"""
        with self.assertRaises(AssertionError):
            kth_largest("3, 2, 1, 5", 2)

    def test_list_items_not_strings(self):
        """It should raise an AssertionError if the list items are not strings"""
        with self.assertRaises(AssertionError):
            kth_largest([3, 2, 1, 5], 2)

    def test_strings_not_integers(self):
        """It should raise an AssertionError if the strings are not integers"""
        with self.assertRaises(AssertionError):
            kth_largest(["3", "2", "a", "5"], 2)

    def test_leading_zeros(self):
        """It should raise an AssertionError if the strings have leading zeros"""
        with self.assertRaises(AssertionError):
            kth_largest(["03", "2", "1", "5"], 2)

    def test_k_not_integer(self):
        """It should raise an AssertionError if k is not an integer"""
        with self.assertRaises(AssertionError):
            kth_largest(["3", "2", "1", "5"], "2")

    def test_k_out_of_range(self):
        """It should raise an AssertionError if k is out of range"""
        with self.assertRaises(AssertionError):
            kth_largest(["3", "2", "1", "5"], 5)
