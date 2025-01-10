"""
find_smallest: Return the smallest number in a list.
This module provides functionality to determine the smallest number in a given list of numbers.

Created: 31/12/2024
Team Name: MIT Alpha
@Author: Hassan Suliman
"""


def find_smallest(lst: list[float]) -> float:
    """Find the smallest number in a list.
    This function identifies and returns the smallest number in a given list of numeric values.

    Args:
        lst (List[float]): List of numeric values.
            - Must contain at least one number.
            - All elements must be integers or floats.

    Returns:
        float: The smallest number in the list.

    Raises:
        ValueError: If the list is empty.
        TypeError: If the input is not a list or contains non-numeric elements.

    Examples:
        >>> find_smallest([3, 1, 4, 1, 5, 9])
        1
        >>> find_smallest([-10, -20, -30, -1])
        -30
        >>> find_smallest([7.5, 3.3, 5.2, 3.1])
        3.1
        >>> find_smallest([42])
        42
        >>> find_smallest([1, -2.5, 0, 3])
        -2.5
        >>> find_smallest([0, 0, 0])
        0

    """
    # Defensive assertions
    if not isinstance(lst, list):
        raise TypeError(f"Input must be a list, got {type(lst).__name__}")
    if not lst:
        raise ValueError("List must not be empty.")
    if not all(isinstance(x, (int, float)) and not isinstance(x, bool) for x in lst):
        raise TypeError("All elements in the list must be numeric and not boolean.")

    # Return the smallest number
    return min(lst)
