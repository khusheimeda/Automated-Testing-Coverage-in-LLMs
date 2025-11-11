# Iteration 3
# 2025-11-10T16:47:08.092870

from solutions.codellama_7b_cot.humaneval_2 import truncate_number


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
        