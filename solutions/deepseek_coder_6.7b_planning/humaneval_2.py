"""
HumanEval/2
Configuration: DeepSeek-6.7B + Self-Planning
Status: FAILED
"""



def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """
def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part  (largest integer smaller than given number) and decimals
     (leftover part always smaller than 1).

    Return the decimal part of the number.
    """

    # Handling edge case where negative numbers are provided as input.
    if number < 0:
        raise ValueError('Input should be a positive floating point number')
    
    # The fractional part is obtained by subtracting integer part from original number. 
    decimal_part = number - int(number)

    return decimal_part