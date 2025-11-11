"""
HumanEval/11
Configuration: CodeLlama-7B + CoT
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
    Perform binary XOR on two strings a and b consisting only of 1s and 0s.

    Args:
        a (str): The first input string.
        b (str): The second input string.

    Returns:
        str: The result of the binary XOR operation.

    Raises:
        ValueError: If either input string is not composed only of 1s and 0s.
    """
    if not a.isdigit() or not b.isdigit():
        raise ValueError("Input strings must consist only of 1s and 0s.")

    result = ""
    for i, j in zip(a, b):
        result += str(int(i) ^ int(j))

    return result