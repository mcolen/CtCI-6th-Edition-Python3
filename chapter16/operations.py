"""Solution to 16.9 Operations.

Write methods to implement the multiply, subtract, and divide operations for
integers. The results of all of these are integers. You can use the add
operator, but not minus, times, or divide.
"""


def _negate(num: int) -> int:
    starting_increment = 1 if num < 0 else -1
    res, increment = 0, starting_increment
    while num != 0:
        res, num = res + increment, num + increment
        increment += increment
        if (num + increment > 0) != (num > 0):
            increment = starting_increment
    return res


def subtract(num1: int, num2: int) -> int:
    """Returns the difference num1 - num2.

    Does not use the minus, times, or divide operators.
    """
    return num1 + _negate(num2)



def multiply(num1: int, num2: int) -> int:
    """Returns product of num1 and num2.

    Does not use the minus, times, or divide operators.
    """
    if num1 < 0 and num2 < 0:
        return multiply(_negate(num1), _negate(num2))
    if num1 > num2:
        return multiply(num1=num2, num2=num1)
    if num1 < 0 < num2:
        return sum(num1 for _ in range(num2))
    return sum(num2 for _ in range(num1))


def divide(num1: int, num2: int) -> int:
    """Returns the quotient num1 - num2.

    Does not use the minus, times, or divide operators.
    """
    if num2 == 0:
        raise ZeroDivisionError
    abs1, abs2 = _abs(num1), _abs(num2)
    num = product = 0
    while product + abs2 <= abs1:
        num, product = num + 1, product + abs2
    return num if (num1 > 0) == (num2 > 0) else _negate(num)


def _abs(num: int) -> int:
    return num if num > 0 else _negate(num)
