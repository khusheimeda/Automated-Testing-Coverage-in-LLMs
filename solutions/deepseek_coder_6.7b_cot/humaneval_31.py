"""
HumanEval/31
Configuration: DeepSeek-6.7B + CoT
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
    if n <= 1: # The smallest prime number is 2, so anything less than that is not a prime number
        return False
    elif n == 2 or n == 3: # 2 and 3 are prime numbers
        return True
    elif n % 2 == 0 or n % 3 == 0: # If the number is divisible by 2 or 3, it's not a prime number
        return False