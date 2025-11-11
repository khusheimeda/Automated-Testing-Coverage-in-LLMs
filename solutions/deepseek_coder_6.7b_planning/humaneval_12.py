"""
HumanEval/12
Configuration: DeepSeek-6.7B + Self-Planning
Status: FAILED
"""

from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
def longest(strings: List[str]) -> Optional[str]:
    if not strings: # empty list
        return None