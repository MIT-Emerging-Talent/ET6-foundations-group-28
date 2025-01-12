#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Team Number: 28
Team Name: MIT Alpha
Author: Duha Mohammed
"""

import unittest
from solutions.add_2_numbers import add_2_numbers


class TestAdd2Numbers(unittest.TestCase):
    """Test cases for add_2_numbers function."""

    def test_add_integers(self):
        """Test adding two integers."""
        self.assertEqual(add_2_numbers(3, 5), 8)

    def test_add_floats(self):
        """Test adding two float numbers."""
        self.assertAlmostEqual(add_2_numbers(2.5, 4.5), 7.0)

    def test_invalid_input(self):
        """Test that the function raises an AssertionError for invalid inputs."""
        with self.assertRaises(AssertionError):
            add_2_numbers("3", 5)

    def test_add_zero(self):
        """Test adding zero with another number."""
        self.assertEqual(add_2_numbers(0, 0), 0)
        self.assertEqual(add_2_numbers(0, 5), 5)
        self.assertEqual(add_2_numbers(-5, 0), -5)

    def test_large_numbers(self):
        """Test adding very large numbers."""
        self.assertEqual(
            add_2_numbers(1e308, 1e308), float("inf")
        )  # Exceeds float limit

    def test_small_numbers(self):
        """Test adding very small numbers (close to zero)."""
        self.assertAlmostEqual(add_2_numbers(1e-308, 1e-308), 2e-308)

    def test_positive_negative_boundary(self):
        """Test adding a positive and negative number resulting in zero."""
        self.assertEqual(add_2_numbers(1e308, -1e308), 0.0)
