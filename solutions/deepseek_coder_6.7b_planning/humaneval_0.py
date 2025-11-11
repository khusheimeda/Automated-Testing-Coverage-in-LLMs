"""
HumanEval/0
Configuration: DeepSeek-6.7B + Self-Planning
Status: FAILED
"""

from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """

    # Firstly sort the list of numbers. This will help us to find two elements in a row that are close together
    sorted_numbers = sorted(numbers)
    
    for i in range(len(sorted_numbers) - 1):   # iterate through each element and its successor
        if abs(sorted_numbers[i] - sorted_numbers[i + 1]) < threshold:   # if the difference is less than the threshold, we have a match. Return True immediately
            return True
    
    return False  # no close elements were found. Return False.