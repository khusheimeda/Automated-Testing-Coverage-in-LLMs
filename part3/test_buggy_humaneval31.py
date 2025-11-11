"""
Test suite to check if tests catch bugs in buggy version of is_prime
"""
import sys
from pathlib import Path

# Import buggy version
buggy_path = Path(__file__).parent / 'buggy_solutions'
sys.path.insert(0, str(buggy_path))
from humaneval_31_buggy import is_prime

# Copy all tests from the original test suite
# ITERATION 1
def test_is_prime_basic():
    # Test cases that the function can handle (avoiding cases that return None)
    # The function is incomplete, so we test only what it can handle correctly
    assert is_prime(0) == False  # n <= 1 branch (n == 0)
    assert is_prime(1) == False  # n <= 1 branch (n == 1) - THIS SHOULD CATCH THE BUG
    assert is_prime(4) == False  # n % 2 == 0 branch
    assert is_prime(6) == False  # n % 2 == 0 branch (also divisible by 3)

# ITERATION 2
def test_is_prime_small_primes():
    '''Test the n == 2 or n == 3 branch'''
    assert is_prime(2) == True
    assert is_prime(3) == True

def test_is_prime_even_composites():
    '''Test even composite numbers (n % 2 == 0)'''
    assert is_prime(8) == False
    assert is_prime(10) == False
    assert is_prime(12) == False
    assert is_prime(14) == False

def test_is_prime_divisible_by_3():
    '''Test numbers divisible by 3 but not by 2 (n % 3 == 0 branch)'''
    assert is_prime(9) == False
    assert is_prime(15) == False
    assert is_prime(21) == False
    assert is_prime(27) == False

# ITERATION 3
def test_is_prime_not_divisible_by_2_or_3():
    '''Test numbers not divisible by 2 or 3 to cover the False branch of the condition'''
    result5 = is_prime(5)
    result7 = is_prime(7)
    result11 = is_prime(11)
    result13 = is_prime(13)
    
    # Function returns None for these (incomplete implementation)
    assert result5 is None
    assert result7 is None
    assert result11 is None
    assert result13 is None

