"""
HumanEval/1
Configuration: DeepSeek-6.7B + Self-Planning
Status: FAILED
"""

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")  # Remove spaces from the string
    
    groups = []  # Initialize an empty list to hold the separated parentheses groups
    stack = []  # Use a stack to keep track of open braces
    
    start = 0   # Start index for each group
    
    for end, char in enumerate(paren_string):
        if char == '(':
            if not stack:
                start = end
            stack.append(char)  # Push open brace onto the stack
            
        elif char == ')':
            stack.pop()   # Pop from stack for every closed braces
            if not stack:  # If stack becomes empty, we found a separate group
                groups.append(paren_string[start: end+1])
    
    return groups