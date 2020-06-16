"""Solution to 16.10 Living People.

Given a list of people with their birth and death years, implement a
method to compute the year with the most number of people alive. You may
assume that all people were born between 1900 and 2000 (inclusive). If a
person was alive during any portion of that year, they should be
included in that year's count. For example, Person (birth = 1908,
death = 1909) is included in the counts for both 1908 and 1909.
"""

import dataclasses
from typing import Sequence

Year = int

MIN_BIRTH_YEAR = 1900
MAX_BIRTH_YEAR = 2000


@dataclasses.dataclass
class Person:
    """A person."""
    birth_year: Year
    death_year: Year


def most_populous_year(people: Sequence[Person]) -> Year:
    """Computes the year with the most people alive.

    Assumes all people were born between MIN_YEAR and MAX_YEAR (inclusive).

    Args:
        people: A sequence of people with birth years and death years.
            If a person was alive during any portion of a year, they are
            counted toward the number of people alive in that year.

    Returns:
        A year in which a maximal number of people were alive.
    """
    net_birth_counts = [0] * (MAX_BIRTH_YEAR - MIN_BIRTH_YEAR + 1)
    for person in people:
        net_birth_counts[person.birth_year - MIN_BIRTH_YEAR] += 1
        if person.death_year < MAX_BIRTH_YEAR:
            net_birth_counts[person.death_year - MIN_BIRTH_YEAR + 1] -= 1

    res, max_population, population = MIN_BIRTH_YEAR, 0, 0
    for i, net_birth_count in enumerate(net_birth_counts):
        population += net_birth_count
        if population > max_population:
            max_population = population
            res = MIN_BIRTH_YEAR + i
    return res
