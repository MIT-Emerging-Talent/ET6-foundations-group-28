#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
This module contains a function that checks if a number is even or odd.

Function:
- is_even(num): Returns True if the number is even, False otherwise.
Created: [04/01/24]
Team Number: 28
Team Name: MIT Alpha
Author: Duha Mohammed
"""


def is_even(num: int) -> bool:
    """
    This function checks if a number is even.

    Args:
        num (int): The number to be checked.

    Returns:
        bool: True if the number is even, False otherwise.

    Examples:
        >>> is_even(4)
        True
        >>> is_even(5)
        False
        >>> is_even(0)
        True
    """
    assert isinstance(num, int), "Input must be an integer"
    return num % 2 == 0


# Example usage:
if __name__ == "__main__":
    print(is_even(4))  # Output: True
