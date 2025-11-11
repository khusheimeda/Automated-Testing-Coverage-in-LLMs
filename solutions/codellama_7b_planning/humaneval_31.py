"""
HumanEval/31
Configuration: CodeLlama-7B + Self-Planning
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
    """Return true if a given number is prime, and false otherwise.
    
    Args:
        n (int): The number to check for primality.
        
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    
    # Check if the number is negative or zero
    if n <= 1:
        return False
    
    # Check if the number is divisible by 2 to 61
    for i in range(2, 61 + 1):
        if n % i == 0:
            return False
    
    # If none of the above conditions are met, then the number is prime
    return True