# Iteration 4
# 2025-11-10T16:47:40.733122

from solutions.codellama_7b_cot.humaneval_2 import truncate_number


def test_truncate_additional_precision():
    '''Additional precision tests'''
    # Test with numbers that have many decimal places
    assert abs(truncate_number(42.123456789) - 0.123456789) < 1e-8
        