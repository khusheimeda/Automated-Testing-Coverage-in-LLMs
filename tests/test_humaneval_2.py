"""
Test suite for HumanEval/2 - truncate_number
This test suite is used to test all 4 solution variants
"""
import pytest
import sys
from pathlib import Path

def test_truncate_number(solution_module):
    """
    Test truncate_number from HumanEval benchmark
    solution_module: The module containing the solution to test
    """
    # Import the function from the solution module
    truncate_number = getattr(solution_module, "truncate_number")

    # Test cases from HumanEval benchmark
    assert truncate_number(3.5) == 0.5
    assert abs(truncate_number(1.33) - 0.33) < 1e-6
    assert abs(truncate_number(123.456) - 0.456) < 1e-6
