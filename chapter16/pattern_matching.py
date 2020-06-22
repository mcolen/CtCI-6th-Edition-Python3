"""Solution to 16.18 Pattern Matching.

You are given two strings, `pattern` and `value`. The `pattern` string
consists of just the letters `a` and `b`, describing a pattern within a
string. For example, the string `catcatgocatgo` matches the pattern
`aabab` (where `cat` is a` and `go` is `b`). It also matches patterns
like `a`, `ab`, and `b`. Write a method to determine if `value` matches
`pattern`.
"""

import itertools


def matches(pattern: str, value: str) -> bool:
    """Returns True if given value matches given pattern."""
    if not pattern:
        return not value
    char1, char2 = ('a', 'b') if pattern[0] == 'a' else ('b', 'a')
    count1 = sum(char == char1 for char in pattern)
    count2 = len(pattern) - count1
    leading_char1s = pattern.index(char2) if count2 > 0 else len(pattern)
    for len1 in range(len(value) // count1 + 1):
        len_remaining = len(value) - len1 * count1
        if count2 > 0 and len_remaining % count2 != 0:
            continue
        len2 = len_remaining // count2 if count2 > 0 else 0
        idx, offset2 = len1, leading_char1s * len1
        for char in itertools.islice(pattern, 1, None):
            offset, len_ = (0, len1) if char == char1 else (offset2, len2)
            if any(value[offset + i] != value[idx + i] for i in range(len_)):
                break
            idx += len_
        else:
            return True
    return False
