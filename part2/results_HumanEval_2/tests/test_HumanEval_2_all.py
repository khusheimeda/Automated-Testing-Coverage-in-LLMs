# Combined Tests - HumanEval/2
# Model: CodeLlama-7B+CoT

from solutions.codellama_7b_cot.humaneval_2 import truncate_number


######################################################################
# ITERATION 1
######################################################################

def test_truncate_number_basic():
    # Test cases from HumanEval benchmark
    assert truncate_number(3.5) == 0.5
    assert abs(truncate_number(1.33) - 0.33) < 1e-6
    assert abs(truncate_number(123.456) - 0.456) < 1e-6

######################################################################
# ITERATION 2
######################################################################

import pytest

def test_truncate_negative_number():
    '''Test that negative numbers raise ValueError'''
    with pytest.raises(ValueError):
        truncate_number(-3.5)

def test_truncate_invalid_input():
    '''Test that invalid input types raise ValueError'''
    with pytest.raises(ValueError):
        truncate_number("not a number")
    
    with pytest.raises(ValueError):
        truncate_number(None)

def test_truncate_zero():
    '''Test with zero'''
    assert truncate_number(0.0) == 0.0

def test_truncate_integer():
    '''Test with integer (no decimal part)'''
    assert truncate_number(5.0) == 0.0
    assert truncate_number(10) == 0.0

######################################################################
# ITERATION 3
######################################################################

def test_truncate_very_small_decimal():
    '''Test with very small decimal values'''
    assert abs(truncate_number(1.000000001) - 0.000000001) < 1e-8

def test_truncate_large_integer_with_decimal():
    '''Test with large number that has decimal part'''
    assert abs(truncate_number(1000000.123456) - 0.123456) < 1e-6

def test_truncate_precision_edge_cases():
    '''Test precision edge cases'''
    # Test with numbers that might have floating point representation issues
    result = truncate_number(0.1 + 0.2)
    assert result >= 0.0 and result < 1.0

######################################################################
# ITERATION 4
######################################################################

def test_truncate_additional_precision():
    '''Additional precision tests'''
    # Test with numbers that have many decimal places
    assert abs(truncate_number(42.123456789) - 0.123456789) < 1e-8
