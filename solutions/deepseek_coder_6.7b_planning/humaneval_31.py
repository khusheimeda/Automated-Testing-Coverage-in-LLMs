"""
HumanEval/31
Configuration: DeepSeek-6.7B + Self-Planning
Status: FAILED
"""



def is_prime(n):
    """Return true if a given number is prime, and false otherwise.
    >>> is_prime(6)
    False
    >>> is_prime(101)
    True
    >>> is_prime(11)
    True
    >>> is_prime(13441)
    True
    >>> is_prime(61)
    True
    >>> is_prime(4)
    False
    >>> is_prime(1)
    False
    """
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # We only need to check numbers up to the square root of n.
        if n % i == 0:                    # If there is a number that divides evenly into n with remainder 0, it's not prime.
            return False                   # So we return false in this case.
    return True                             # Otherwise, n must be prime so we return true at the end.