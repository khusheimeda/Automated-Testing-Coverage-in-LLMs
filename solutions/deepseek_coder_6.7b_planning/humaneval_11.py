"""
HumanEval/11
Configuration: DeepSeek-6.7B + Self-Planning
Status: FAILED
"""

from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Strings must be of the same length")
        
    result = ""
    
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
            
    return result