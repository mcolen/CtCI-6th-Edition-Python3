"""Tests for chapter16.living_people."""

import unittest

from chapter16 import living_people


class TestMostPopulousYear(unittest.TestCase):

    def test_4_people_3_overlapping(self) -> None:
        self.assertEqual(1950, living_people.most_populous_year([
            living_people.Person(birth_year=1900, death_year=1950),
            living_people.Person(birth_year=1900, death_year=1945),
            living_people.Person(birth_year=1950, death_year=2000),
            living_people.Person(birth_year=1947, death_year=2000),
        ]))


if __name__ == '__main__':
    unittest.main()
