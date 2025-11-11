"""
Test suite for HumanEval/1 - separate_paren_groups
This test suite is used to test all 4 solution variants
"""
import pytest
import sys
from pathlib import Path

def test_separate_paren_groups(solution_module):
    """
    Test separate_paren_groups from HumanEval benchmark
    solution_module: The module containing the solution to test
    """
    # Import the function from the solution module
    separate_paren_groups = getattr(solution_module, "separate_paren_groups")

    # Test cases from HumanEval benchmark
    assert separate_paren_groups('(()()) ((())) () ((())()())') == [
    assert separate_paren_groups('() (()) ((())) (((())))') == [
    assert separate_paren_groups('(()(())((())))') == [
    assert separate_paren_groups('( ) (( )) (( )( ))') == ['()', '(())', '(()())']
