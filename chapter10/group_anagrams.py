"""Solution to 10.2 Group Anagrams.

Write a method to sort an array of strings so that all the anagrams are
next to each other.
"""

import collections
from typing import DefaultDict, List, MutableSequence


def sort(strings: MutableSequence[str]) -> None:
    """Sorts strings so that all the anagrams are next to each other."""
    groupings: DefaultDict[int, List[str]] = collections.defaultdict(list)
    for string in strings:
        key = hash(frozenset(collections.Counter(string).items()))
        groupings[key].append(string)
    grouped_strings = (string for anagrams in groupings.values()
                       for string in anagrams)
    for i, string in zip(range(len(strings)), grouped_strings):
        strings[i] = string
