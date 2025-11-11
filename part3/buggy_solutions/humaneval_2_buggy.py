"""
HumanEval/2 - BUGGY VERSION
Configuration: CodeLlama-7B + CoT
Status: FAILED

BUG INJECTED: Off-by-one error in boundary check
- Changed: number < 0  ->  number <= 0
- This causes zero to be incorrectly rejected, even though zero should be valid (0.0 has decimal part 0.0)
- This is a realistic bug that could occur when someone misinterprets "positive" as "strictly positive"
"""

def truncate_number(number: float) -> float:
    """Given a positive floating point number, return its decimal part."""
    # BUG: Changed < 0 to <= 0, which incorrectly rejects zero
    if not isinstance(number, (int, float)) or number <= 0:  # BUG: should be < 0
        raise ValueError("Invalid input. The number must be a positive real number.")
    integer_part = int(number)
    decimals = abs(number) - abs(integer_part)
    return decimals if number > 0 else -decimals

