#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains a function to add two numbers.

It defines a function called `add_2_numbers` which takes two numbers as input
and returns their sum.
Created: [04/01/25]
Team Number: 28
Team Name: MIT Alpha
Author: Duha Mohammed
"""


def add_2_numbers(a: int | float, b: int | float) -> int | float:
    """
    This function takes two numbers as input and returns their sum.

    Args:
        a (int or float): The first number.
        b (int or float): The second number.

    Returns:
        int or float: The sum of a and b.

    Raises:
        AssertionError: If a or b are not int or float.

    Examples:
        >>> add_2_numbers(2, 3)
        5
        >>> add_2_numbers(-1, 5)
        4
        >>> add_2_numbers(4.5, 5.5)
        10.0
        >>> add_2_numbers(0, 0)
        0
    """
    assert isinstance(a, (int, float)), "First argument must be an int or float"
    assert isinstance(b, (int, float)), "Second argument must be an int or float"
    return a + b
