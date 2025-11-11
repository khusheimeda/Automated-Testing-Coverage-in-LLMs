"""
Test suite for HumanEval/0 - has_close_elements
This test suite is used to test all 4 solution variants
"""
import pytest
import sys
from pathlib import Path

def test_has_close_elements(solution_module):
    """
    Test has_close_elements from HumanEval benchmark
    solution_module: The module containing the solution to test
    """
    # Import the function from the solution module
    has_close_elements = getattr(solution_module, "has_close_elements")

    # Test cases from HumanEval benchmark
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
    assert has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 1.0) == True
    assert has_close_elements([1.1, 2.2, 3.1, 4.1, 5.1], 0.5) == False
