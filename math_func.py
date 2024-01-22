import math
import sys


# Return the value of base ^ exponent
def perform_pow(base: float, exponent: float) -> float:
    if not exponent == int(exponent) and exponent < 0:
        raise ValueError("Negative exponent must be an integer")
    try:
        result = math.pow(base, exponent)
    except OverflowError as e:
        raise OverflowError(f'{base} ^ {exponent} is too large of a number')
    # Errr that happened when base and exponent is too small
    if 0 < base < 1 and 0 < exponent < 1 and result == 1:
        raise ValueError(f'{base} or {exponent} is small')
    return result


# Return the sum of the digits
def perform_digit_addition(val: float) -> int:
    val = str(val)
    val = val.replace('.', '')
    res = 0
    for digit in val:
        res += int(digit)

    return res


# return the factorial of val
def factorial(val: float) -> float:
    val = int(val)
    result = 1
    for i in range(2, val + 1):
        result *= i
        if result > sys.float_info.max:
            raise ValueError(f'The number {val} is too large for factorial argument')
    return result
