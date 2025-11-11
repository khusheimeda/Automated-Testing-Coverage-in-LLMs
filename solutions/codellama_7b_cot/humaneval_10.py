"""
HumanEval/10
Configuration: CodeLlama-7B + CoT
Status: FAILED
"""



def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """

    # Check if the input string is already a palindrome
    if is_palindrome(string):
        return string

    # Find the longest postfix of the input string that is a palindrome
    postfix = ""
    for i in range(len(string), 0, -1):
        substr = string[-i:]
        if is_palindrome(substr):
            postfix = substr
            break

    # Find the prefix of the input string that comes before the palindromic suffix
    prefix = ""
    for i in range(len(string)):
        if string[:i+1] == postfix:
            prefix = string[:i]
            break

    # Return the concatenation of the prefix and the reverse of the suffix
    return prefix + postfix[::-1]