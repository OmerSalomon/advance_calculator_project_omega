import math


# Return the value of base ^ exponent
def perform_pow(base: float, exponent: float) -> float:
    if not exponent == int(exponent) and exponent < 0:
        raise ValueError("Negative exponent must be an integer")
    return math.pow(base, exponent)


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
    if val < 0 or not val.is_integer():
        raise ValueError("There is no factorial for non native number")
    if val > 1000:
        raise ValueError("Can not perform factorial for such a large number")
    val = int(val)
    result = 1
    for i in range(2, val + 1):
        result *= i
    return result
