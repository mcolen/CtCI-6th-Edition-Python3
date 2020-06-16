"""Tests for chapter16.english_int."""

import unittest

from chapter16 import english_int


class TestToEnglish(unittest.TestCase):

    def test_21(self) -> None:
        self.assertEqual("Twenty One", english_int.to_english(21))

    def test_156(self) -> None:
        self.assertEqual("One Hundred Fifty Six", english_int.to_english(156))

    def test_83_999(self) -> None:
        self.assertEqual("Eighty Three Thousand Nine Hundred Ninety Nine",
                         english_int.to_english(83_999))

    def test_400_019(self) -> None:
        self.assertEqual("Four Hundred Thousand Nineteen",
                         english_int.to_english(400_019))

    def test_101_000_321(self) -> None:
        self.assertEqual("One Hundred One Million Three Hundred Twenty One",
                         english_int.to_english(101_000_321))

    def test_2_050_009_070(self) -> None:
        self.assertEqual("Two Billion Fifty Million Nine Thousand Seventy",
                         english_int.to_english(2_050_009_070))


if __name__ == '__main__':
    unittest.main()
