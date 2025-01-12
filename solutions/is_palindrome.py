#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""is_palindrome: Check if a string is a palindrome.

This module provides functionality to determine whether a given string
is a palindrome - a sequence that reads the same forwards and backwards.
The implementation ignores case and non-alphanumeric characters.

Created: 31/12/2024
Team Name: MIT Alpha
@Author: Nada Hamza
"""


def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome.

    A palindrome is a string that reads the same forwards and backwards,
    ignoring case and non-alphanumeric characters. The function first
    validates the input, then cleans the string by removing all
    non-alphanumeric characters and converting to lowercase before
    performing the palindrome check.

    Args:
        s (str): Input string to check.
            - Must be a string.
            - May include spaces, punctuation, or special characters (which will be ignored)
            - May be mixed case (which will be ignored)

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("racecar")
        True
        >>> is_palindrome("12321")
        True
        >>> is_palindrome("hello")
        False
        >>> is_palindrome(12345)
        Traceback (most recent call last):
        ...
        TypeError: Input must be a string.
    """
    # Defensive assertion for type check
    if not isinstance(s, str):
        raise TypeError(f"Input must be a string, got {type(s).__name__}")

    # Normalize the string: Remove non-alphanumeric characters and convert to lowercase.
    cleaned = "".join(char.lower() for char in s if char.isalnum())

    # Check if the cleaned string is the same backward and forward.
    return cleaned == cleaned[::-1]
