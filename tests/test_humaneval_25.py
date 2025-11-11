"""
Test suite for HumanEval/25 - factorize
This test suite is used to test all 4 solution variants
"""
import pytest
import sys
from pathlib import Path

def test_factorize(solution_module):
    """
    Test factorize from HumanEval benchmark
    solution_module: The module containing the solution to test
    """
    # Import the function from the solution module
    factorize = getattr(solution_module, "factorize")

    # Test cases from HumanEval benchmark
    assert factorize(2) == [2]
    assert factorize(4) == [2, 2]
    assert factorize(8) == [2, 2, 2]
    assert factorize(3 * 19) == [3, 19]
    assert factorize(3 * 19 * 3 * 19) == [3, 3, 19, 19]
    assert factorize(3 * 19 * 3 * 19 * 3 * 19) == [3, 3, 3, 19, 19, 19]
    assert factorize(3 * 19 * 19 * 19) == [3, 19, 19, 19]
    assert factorize(3 * 2 * 3) == [2, 3, 3]
