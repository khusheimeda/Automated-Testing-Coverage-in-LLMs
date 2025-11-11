"""
HumanEval/31 - BUGGY VERSION
Configuration: DeepSeek-6.7B + CoT
Status: FAILED

BUG INJECTED: Wrong boundary condition for edge case
- Changed: n <= 1  ->  n < 1
- This causes n=1 to not be caught by the first condition, potentially falling through to other conditions
- Since the function is incomplete, n=1 would return None instead of False
- This is a realistic off-by-one error that could occur when someone forgets the equality check
"""

def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
    # BUG: Changed <= 1 to < 1, which misses the n=1 case
    if n < 1:  # BUG: should be <= 1
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    # Function is incomplete, so n=1 would return None (fall through)

