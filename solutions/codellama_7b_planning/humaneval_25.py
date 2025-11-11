"""
HumanEval/25
Configuration: CodeLlama-7B + Self-Planning
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
    """Return list of prime factors of given integer in the order from smallest to largest.
     Each of the factors should be listed number of times corresponding to how many times it appears in the factorization.
     Input number should be equal to the product of all factors."""

    # Edge case: if n is 1, return empty list
    if n == 1:
        return []

    # Initialize an empty list to store the prime factors
    factors = []

    # Iterate from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # While i divides n, add it to the list of factors and divide n by i
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is not equal to 1, it means it has a prime factor that is not in the list of factors
    if n != 1:
        factors.append(n)

    return factors