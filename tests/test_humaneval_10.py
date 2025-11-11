"""
Test suite for HumanEval/10 - make_palindrome
This test suite is used to test all 4 solution variants
"""
import pytest
import sys
from pathlib import Path

def test_make_palindrome(solution_module):
    """
    Test make_palindrome from HumanEval benchmark
    solution_module: The module containing the solution to test
    """
    # Import the function from the solution module
    make_palindrome = getattr(solution_module, "make_palindrome")

    # Test cases from HumanEval benchmark
    assert make_palindrome('') == ''
    assert make_palindrome('x') == 'x'
    assert make_palindrome('xyz') == 'xyzyx'
    assert make_palindrome('xyx') == 'xyx'
    assert make_palindrome('jerry') == 'jerryrrej'
