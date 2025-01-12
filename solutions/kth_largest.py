#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for finding the kth largest element in a list.
This module provides a function to find the kth largest element in a list of strings,
where each string represents an integer without leading zeros.

Created: 04/01/2025
Team Number: 28
Team Name: MIT Alpha
Author: Ahd Abdelrahim
"""


def kth_largest(nums: list, k: int) -> str:
    """
    Return the string that represents the kth largest integer in nums.

    Parameters:
        nums (list): A list of strings where each string represents a positive integer.
        k (int): The position (1-indexed) of the largest element to find.

    Returns:
        str: The string representation of the kth largest integer in the list.

    Raises:
        AssertionError: If the input list is empty, k is not an integer, or k is out of bounds.

    Examples:
    >>> kth_largest(["3", "2", "1", "5", "6", "4"], 2)
    '5'

    >>> kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], 4)
    '4'

    >>> kth_largest(["3", "2", "3", "1", "2", "4", "5", "5", "6"], 9)
    '1'

    """
    # Ensure correct input
    assert isinstance(nums, list), "First argument must be a list"
    assert len(nums) > 0, "List can't be empty"
    assert all(isinstance(num, str) for num in nums), "List items must be strings"
    assert all(num.lstrip("+-").isdigit() for num in nums), (
        "Strings must consists of integers only"
    )
    assert all(num[0] != "0" for num in nums), "Integers can't have leading zeros"
    assert isinstance(k, int), "Second argument must be an integer"
    assert 1 <= k <= len(nums), "k must be in the range (1 <= k <= list length)"
    # Sort numbers as integers in reverse order
    nums = sorted(nums, key=int, reverse=True)
    # Return Kth number after sorting
    return nums[k - 1]
