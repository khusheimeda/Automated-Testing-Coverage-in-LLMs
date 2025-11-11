"""
Test suite for HumanEval/20 - find_closest_elements
This test suite is used to test all 4 solution variants
"""
import pytest
import sys
from pathlib import Path

def test_find_closest_elements(solution_module):
    """
    Test find_closest_elements from HumanEval benchmark
    solution_module: The module containing the solution to test
    """
    # Import the function from the solution module
    find_closest_elements = getattr(solution_module, "find_closest_elements")

    # Test cases from HumanEval benchmark
    assert find_closest_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2]) == (3.9, 4.0)
    assert find_closest_elements([1.0, 2.0, 5.9, 4.0, 5.0]) == (5.0, 5.9)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2]) == (2.0, 2.2)
    assert find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0]) == (2.0, 2.0)
    assert find_closest_elements([1.1, 2.2, 3.1, 4.1, 5.1]) == (2.2, 3.1)
