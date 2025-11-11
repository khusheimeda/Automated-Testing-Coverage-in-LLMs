"""
HumanEval/2
Configuration: CodeLlama-7B + CoT
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
    """Given a positive floating point number, return its decimal part."""
    if not isinstance(number, (int, float)) or number < 0:
        raise ValueError("Invalid input. The number must be a positive real number.")
    integer_part = int(number)
    decimals = abs(number) - abs(integer_part)
    return decimals if number > 0 else -decimals