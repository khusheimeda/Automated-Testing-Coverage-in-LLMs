"""
HumanEval/20
Configuration: DeepSeek-6.7B + CoT
Status: FAILED
"""

from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    if len(numbers) < 2:
        raise ValueError("Input list must contain at least two numbers")
    
    numbers.sort()  # Sort the input array in ascending order
    closest_diff = float('inf')  # Initialize closest difference as infinity
    result = (0, 0)  # Initialize result pair with zeros

    for i in range(1, len(numbers)):
        diff = numbers[i] - numbers[i-1]
        if diff < closest_diff:
            closest_diff = diff
            result = (numbers[i-1], numbers[i])
    
    return result