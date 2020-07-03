"""Solution to 16.20 T9.

On old cell phones, users typed on a numeric keypad and the phone would
provide a list of words that matched those numbers. Each digit mapped to
a set of 0-4 letters. Implement an algorithm to return a set of matching
words, given a sequence of digits. You are provided a list of valid
words (provided in whatever data structure you'd like). The mapping is
shown in the diagram below:

1:
2: abc
3: def
4: ghi
5: jkl
6: mno
7: pqrs
8: tuv
9: wxyz
0:

EXAMPLE
Input:  8733
Output: tree, used
"""

from typing import AbstractSet, MutableSequence, Set, Sequence

Digit = str

DIGIT_TO_CHARS = {
    '2': {'a', 'b', 'c'},
    '3': {'d', 'e', 'f'},
    '4': {'g', 'h', 'i'},
    '5': {'j', 'k', 'l'},
    '6': {'m', 'n', 'o'},
    '7': {'p', 'q', 'r', 's'},
    '8': {'t', 'u', 'v'},
    '9': {'w', 'x', 'y', 'z'},
}


def matching_words(digits: Sequence[Digit],
                   dictionary: AbstractSet[str]) -> Set[str]:
    """Computes the set of matching words, given a sequence of digits.

    Args:
        digits: Sequence of entries on a numeric keypad.
        dictionary: Valid words.

    Returns:
        Subset of dictionary that can match given digits in T9.
    """
    if any(digit not in DIGIT_TO_CHARS for digit in digits):
        return set()

    res = set()

    def dfs(chars: MutableSequence[str]) -> None:
        if len(chars) == len(digits):
            word = ''.join(chars)
            if word in dictionary:
                res.add(word)
            return
        for char in DIGIT_TO_CHARS[digits[len(chars)]]:
            chars.append(char)
            dfs(chars)
            chars.pop()
    dfs(chars=[])
    return res
