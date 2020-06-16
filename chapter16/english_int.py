"""Solution to 16.8 English Int.

Given any integer, print an English phrase that describes the integer
(e.g. "One Thousand, Two Hundred Thirty Four").
"""


def to_english(num: int) -> str:
    """Returns an English phrase that describes num.

    Args:
        num: Integer in range [-999_999_999_999, 999_999_999_999].

    Returns:
        An English phrase that describes argument num (e.g. 'One
        Thousand, Two Hundred Thirty Four').
    """
    if num < 0:
        return 'Negative ' + to_english(-num)
    if num == 0:
        return "Zero"

    suffixes, groups = ['', ' Thousand', ' Million', ' Billion'], []
    for suffix in suffixes:
        if num % 1000 > 0:
            groups.append(_1_through_999_to_english(num % 1000) + suffix)
        num //= 1000
    return ' '.join(reversed(groups))


def _1_through_999_to_english(num: int) -> str:
    primatives = {
        1: 'One',
        2: 'Two',
        3: 'Three',
        4: 'Four',
        5: 'Five',
        6: 'Six',
        7: 'Seven',
        8: 'Eight',
        9: 'Nine',
        10: 'Ten',
        11: 'Eleven',
        12: 'Twelve',
        13: 'Thirteen',
        14: 'Fourteen',
        15: 'Fifteen',
        16: 'Sixteen',
        17: 'Seventeen',
        18: 'Eighteen',
        19: 'Nineteen',
        20: 'Twenty',
        30: 'Thirty',
        40: 'Forty',
        50: 'Fifty',
        60: 'Sixty',
        70: 'Seventy',
        80: 'Eighty',
        90: 'Ninety',
    }
    if num >= 100:
        hundreds = primatives[num // 100] + ' Hundred'
        return (hundreds if num % 100 == 0 else
                hundreds + ' ' + _1_through_999_to_english(num % 100))
    if num > 20 and num % 10 != 0:
        return primatives[num - num % 10] + ' ' + primatives[num % 10]
    return primatives[num]
