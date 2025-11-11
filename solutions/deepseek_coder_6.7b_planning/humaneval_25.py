"""
HumanEval/25
Configuration: DeepSeek-6.7B + Self-Planning
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
from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    
    # Divide n by 2 until it can no longer be divided evenly.
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        
    # The remaining number is odd, so we try dividing it by all odd numbers starting from 3.
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
            
        if n == 1: # If the remaining number is a prime number, break loop.
            break
    
    return factors