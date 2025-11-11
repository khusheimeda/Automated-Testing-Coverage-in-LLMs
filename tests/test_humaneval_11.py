"""
Test suite for HumanEval/11 - string_xor
This test suite is used to test all 4 solution variants
"""
import pytest
import sys
from pathlib import Path

def test_string_xor(solution_module):
    """
    Test string_xor from HumanEval benchmark
    solution_module: The module containing the solution to test
    """
    # Import the function from the solution module
    string_xor = getattr(solution_module, "string_xor")

    # Test cases from HumanEval benchmark
    assert string_xor('111000', '101010') == '010010'
    assert string_xor('1', '1') == '0'
    assert string_xor('0101', '0000') == '0101'
