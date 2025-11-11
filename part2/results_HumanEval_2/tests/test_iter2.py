# Iteration 2
# 2025-11-10T16:46:33.751643

from solutions.codellama_7b_cot.humaneval_2 import truncate_number


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
        