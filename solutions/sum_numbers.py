#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sum Numbers

sum_numbers is a recursive function that returns the sum of countdown numbers.

Created: 25/12/2024
Team Number: 28
Team Name: MIT Alpha
Author: Maab Mohamedkhair
"""


def sum_numbers(n):
    """
    sum_numbers is a function that returns the sum of numbers from n -> 1.

    Base case:
        n == 1
        return 1

    Recursive case:
        For n > 1:
        smaller_result of n + the value of sum_numbers(n - 1)

    Parameters:
        n (int): Any positive integer less than 1000 due to Python's recursion limitation.

    Returns:
        int: The sum of all numbers from n down to 1 (inclusive).

    Raises:
        AssertionError: If n is not a positive integer less than 1000.

    Examples:
    >>> sum_numbers(4)
    10

    >>> sum_numbers(5)
    15

    >>> sum_numbers(0)
    Traceback (most recent call last):
    ...
    AssertionError: Input must be greater than 0.

    """
    # Ensure n is a positive integer and within the recursion limit
    assert isinstance(n, int), "Input must be an integer greater than 0."
    assert n > 0, "Input must be greater than 0."
    assert n < 1000, "Input must be less than 1000."

    # Base case
    if n == 1:
        return 1

    # Recursive case
    smaller_result = n + sum_numbers(n - 1)
    return smaller_result
