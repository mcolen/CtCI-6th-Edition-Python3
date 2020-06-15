"""Solution to 16.7 Number Max.

Write a method that finds the maximum of two numbers. You should not use
if-else or any other comparison operator.
"""


def number_max(num1: int, num2: int) -> int:
    """Returns the maximum of num1 and num2.

    Does not use if-else or any other comparison operator.
    """
    num1_coeff = _is_negative(num2 - num1)
    num2_coeff = num1_coeff ^ 1
    return num1_coeff * num1 + num2_coeff * num2


def _is_negative(num: int) -> int:
    return (1 << num.bit_length() & num) >> num.bit_length()
