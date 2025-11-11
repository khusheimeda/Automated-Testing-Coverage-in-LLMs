# Iteration 1
# 2025-11-10T16:41:24.619402

from solutions.codellama_7b_cot.humaneval_2 import truncate_number


def test_truncate_number_basic():
    # Test cases from HumanEval benchmark
    assert truncate_number(3.5) == 0.5
    assert abs(truncate_number(1.33) - 0.33) < 1e-6
    assert abs(truncate_number(123.456) - 0.456) < 1e-6
        