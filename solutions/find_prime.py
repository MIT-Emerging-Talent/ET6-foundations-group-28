#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
find_prime
A function that takes a number and returns True if the number is prime,
and False if it is not prime.

Created: 25/12/2024
Team Number: 28
Team Name: MIT Alpha
Author: Maab Mohamedkhair
"""


def find_prime(number):
    """
    Check if a number is prime or not and return True or False.

    Parameters:
    number (int): The number to check.

    Returns:
    bool: True if the number is prime, False otherwise.

    Raises:
    AssertionError: If the input is not an integer or is less than or equal to zero.

    Examples:
    >>> find_prime(4)
    False

    >>> find_prime(5)
    True

    >>> find_prime(0)
    Traceback (most recent call last):
    ...
    AssertionError: Invalid input, Enter a number greater than zero.
    """
    assert isinstance(number, int), "Input must be an integer."
    assert number > 0, "Invalid input, Enter a number greater than zero."

    if number <= 1:
        return False  # Prime numbers are greater than 1
    if number == 2:
        return True  # 2 is the only even prime number
    if number % 2 == 0:
        return False  # Exclude other even numbers

    # Check divisibility from 3 to sqrt(number)
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True
