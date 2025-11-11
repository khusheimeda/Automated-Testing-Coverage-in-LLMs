"""
HumanEval/25
Configuration: DeepSeek-6.7B + CoT
Status: FAILED
"""

from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
def factorize(n: int) -> List[int]:
    factors = []
    
    # Factor out all 2s first
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
        
    # Check for odd divisors from now on
    i = 3
    while i * i <= n:
        while (n % i == 0):
            factors.append(i)
            n = n // i
        i += 2
    
    if n != 1:  # If the remaining number is greater than 2, add it to the list of factors
       factors.append(n)
        
    return factors