"""
Test suite for HumanEval/12 - longest
This test suite is used to test all 4 solution variants
"""
import pytest
import sys
from pathlib import Path

def test_longest(solution_module):
    """
    Test longest from HumanEval benchmark
    solution_module: The module containing the solution to test
    """
    # Import the function from the solution module
    longest = getattr(solution_module, "longest")

    # Test cases from HumanEval benchmark
    assert longest([]) == None
    assert longest(['x', 'y', 'z']) == 'x'
    assert longest(['x', 'yyy', 'zzzz', 'www', 'kkkk', 'abc']) == 'zzzz'
