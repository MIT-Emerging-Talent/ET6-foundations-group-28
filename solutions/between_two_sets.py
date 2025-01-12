#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
between_two_sets: Count integers satisfying divisibility conditions.
This module provides a function to calculate the number of integers that are factors
of all elements in `b` and divisible by all elements in `a`.
Created: 04/01/2025
Team Name: MIT Alpha
@Author: Hassan Suliman
"""


def between_two_sets(a: list[int], b: list[int]) -> int:
    """Calculate the count of integers satisfying specific divisibility conditions.

    This function finds integers between the maximum of `a` and the minimum of `b` (inclusive)
    that are divisible by all elements in `a` and are factors of all elements in `b`.

    Args:
        a (List[int]): A list of integers to act as divisors.
        b (List[int]): A list of integers to act as multiples.

    Returns:
        int: The count of integers meeting the criteria.

    Raises:
        ValueError: If either list is empty.
        TypeError: If inputs are not lists of integers.

    Examples:
        >>> between_two_sets([2, 4], [16, 32, 96])
        3
        >>> between_two_sets([1], [100])
        9
        >>> between_two_sets([3], [12])
        3
        >>> between_two_sets([], [16, 32, 96])
        Traceback (most recent call last):
        ...
        ValueError: Both lists must be non-empty.
        >>> between_two_sets([2, "a"], [16, 32])
        Traceback (most recent call last):
        ...
        TypeError: All elements in both lists must be integers.
    """
    # Defensive assertions
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("Both inputs must be lists.")
    if not a or not b:
        raise ValueError("Both lists must be non-empty.")
    if not all(isinstance(x, int) for x in a + b):
        raise TypeError("All elements in both lists must be integers.")

    a_max = max(a)
    b_min = min(b)
    counter = 0

    for i in range(a_max, b_min + 1):
        is_factor_multiple = True

        for element in a:
            if i % element != 0:
                is_factor_multiple = False
                break
        for element in b:
            if element % i != 0:
                is_factor_multiple = False
                break

        if is_factor_multiple:
            counter += 1

    return counter
