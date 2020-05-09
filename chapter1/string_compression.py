"""Solution to 1.6 String Compression.

Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string `aabcccccaaa` would
become `a2b1c5a3`. If the "compressed" string would not become smaller
than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters
(a-z).
"""

from itertools import islice


def compressed(s: str) -> str:
    """Returns a compressed s using the counts of repeated characters.

    If the "compressed" string would not become smaller than s, simply
    returns s. Assumes s has only uppercase and lowercase letters.
    """
    if sum(c1 == c2 for c1, c2 in zip(s, islice(s, 1, None))) <= len(s) // 2:
        return s
    counts, prev_char, count = [], s[0], 1
    for c in islice(s, 1, None):
        if c == prev_char:
            count += 1
        else:
            counts.append(prev_char + str(count))
            prev_char, count = c, 1
    return ''.join(counts) + prev_char + str(count)
