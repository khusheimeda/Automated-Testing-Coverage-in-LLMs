"""
HumanEval/11
Configuration: CodeLlama-7B + Self-Planning
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
    """
    Performs binary XOR on two strings consisting only of 1s and 0s.

    Args:
        a (str): The first input string.
        b (str): The second input string.

    Returns:
        str: The result of the binary XOR operation as a string.
    """

    # Ensure that both inputs are strings consisting only of 1s and 0s
    if not all(c in ['0', '1'] for c in a) or not all(c in ['0', '1'] for c in b):
        raise ValueError("Input strings must consist only of '0' and '1'")

    # Initialize an empty string to store the result
    result = ""

    # Iterate over the characters of both input strings simultaneously
    for ca, cb in zip(a, b):
        # Perform binary XOR on the current characters
        result += str(int(ca) ^ int(cb))

    return result