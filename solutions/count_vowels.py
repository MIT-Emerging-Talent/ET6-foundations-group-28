#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for counting vowels in strings.

This module provides functionality to count vowels in a given string,
considering both lowercase and uppercase vowels (a, e, i, o, u).

Created: 29/12/2024
Team Number: 28
Team Name: MIT Alpha
Author: Ghyath Ibrahim
"""


def count_vowels(s: str) -> int:
    """Count the number of vowels in a string.

    Args:
        s (str): The input string to count vowels from.
            Can be any string including empty string.

    Returns:
        int: The number of vowels (a, e, i, o, u) in the string,
            case-insensitive.

    Raises:
        AssertionError: If input is not a string.

    Examples:
        >>> count_vowels("hello")
        2
        >>> count_vowels("HELLO")
        2
        >>> count_vowels("")
        0
        >>> count_vowels("aEiOu")
        5
    """
    assert isinstance(s, str), f"Input must be string, got {type(s).__name__}"

    vowels = {"a", "e", "i", "o", "u"}
    count = 0

    for (
        char
    ) in s.lower().strip():  # make the string lowercase and remove the whitespaces
        if char in vowels:
            count += 1

    return count
