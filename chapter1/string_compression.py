"""Solution to 1.6 String Compression.

Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string `aabcccccaaa` would
become `a2b1c5a3`. If the "compressed" string would not become smaller
than the original string, your method should return the original string.
You can assume the string has only uppercase and lowercase letters
(a-z).
"""

import itertools


def compressed(s: str) -> str:
    """Performs basic string compression of repeated characters.

    Args:
        s: Any string.

    Returns:
        A compression of the argument s using the counts of repeated
        characters. For example, the string 'aabcccccaaa' would become
        'a2b1c5a3'.

        If the "compressed" string would not become smaller than the
        original string, returns the original string.
    """
    if sum(s[i] == s[i + 1] for i in range(len(s) - 1)) <= len(s) // 2:
        return s
    counts, prev_char, count = [], s[0], 1
    for c in itertools.islice(s, 1, None):
        if c == prev_char:
            count += 1
        else:
            counts.append(prev_char + str(count))
            prev_char, count = c, 1
    return ''.join(counts) + prev_char + str(count)
