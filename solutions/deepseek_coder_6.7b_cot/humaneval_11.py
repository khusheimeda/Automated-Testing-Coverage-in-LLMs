"""
HumanEval/11
Configuration: DeepSeek-6.7B + CoT
Status: FAILED
"""

from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
from typing import List

def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError("Input strings must be the same length")
    
    result = ""
    for i in range(len(a)):
        # XOR operation between two bits is performed by checking 
        # if both are different (1^0 or 0^1) and adding '1' to result.
        if a[i] != b[i]:
            result += "1"
        else:
            result += "0"
    return result