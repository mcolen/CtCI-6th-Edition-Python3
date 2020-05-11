"""Tests for solution to 1.5 One Away."""

import unittest

from chapter1.one_away import are_one_away


class TestOneAway(unittest.TestCase):
    """Simple tests of whether two given strings are one edit away."""

    def test_empty_string_and_d_are_one_away(self):
        self.assertTrue(are_one_away('', 'd'))

    def test_d_and_de_are_one_away(self):
        self.assertTrue(are_one_away('d', 'de'))

    def test_pale_and_pse_are_not_one_away(self):
        self.assertFalse(are_one_away('pale', 'pse'))

    def test_acdsfdsfadsf_and_acdsgdsfadsf_are_one_away(self):
        self.assertTrue(are_one_away('acdsfdsfadsf', 'acdsgdsfadsf'))

    def test_acdsfdsfadsf_and_acdsfdfadsf_are_one_away(self):
        self.assertTrue(are_one_away('acdsfdsfadsf', 'acdsfdfadsf'))

    def test_acdsfdsfadsf_and_acdsfdsfads_are_one_away(self):
        self.assertTrue(are_one_away('acdsfdsfadsf', 'acdsfdsfads'))

    def test_acdsfdsfadsf_and_cdsfdsfadsf_are_one_away(self):
        self.assertTrue(are_one_away('acdsfdsfadsf', 'cdsfdsfadsf'))

    def test_adfdsfadsf_and_acdfdsfdsf_are_not_one_away(self):
        self.assertFalse(are_one_away('adfdsfadsf', 'acdfdsfdsf'))

    def test_adfdsfadsf_and_bdfdsfadsg_are_not_one_away(self):
        self.assertFalse(are_one_away('adfdsfadsf', 'bdfdsfadsg'))

    def test_adfdsfadsf_and_affdsfads_are_not_one_away(self):
        self.assertFalse(are_one_away('adfdsfadsf', 'affdsfads'))

    def test_pale_and_pkle_are_one_away(self):
        self.assertTrue(are_one_away('pale', 'pkle'))

    def test_pkle_and_pable_are_not_one_away(self):
        self.assertFalse(are_one_away('pkle', 'pable'))

    def test_a_and_abc_are_not_one_away(self):
        self.assertFalse(are_one_away('a', 'abc'))


if __name__ == '__main__':
    unittest.main()
