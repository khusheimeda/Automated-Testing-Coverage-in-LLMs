"""
HumanEval/20
Configuration: DeepSeek-6.7B + Self-Planning
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
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each other 
        and return them in order (smaller number, larger number).
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
        (2.0, 2.2)
        >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
        (2.0, 2.0)
    """
    
    # Sort the list of numbers and then iterate through it to find the two closest elements
    sorted_numbers = sorted(numbers)
    min_difference = float('inf')
    result = ()
    
    for i in range(1, len(sorted_numbers)):
        difference = sorted_numbers[i] - sorted_numbers[i-1]
        
        if 0 < difference < min_difference:
            min_difference = difference
            result = (sorted_numbers[i-1], sorted_numbers[i])
            
    return result