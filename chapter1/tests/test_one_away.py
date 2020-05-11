"""Tests for chapter1.one_away."""

import unittest

from chapter1.one_away import are_one_away


class TestOneAway(unittest.TestCase):

    def test_empty_string_d(self):
        self.assertTrue(are_one_away('', 'd'))

    def test_d_de(self):
        self.assertTrue(are_one_away('d', 'de'))

    def test_pale_pse(self):
        self.assertFalse(are_one_away('pale', 'pse'))

    def test_acdsfdsfadsf_acdsgdsfadsf(self):
        self.assertTrue(are_one_away('acdsfdsfadsf', 'acdsgdsfadsf'))

    def test_acdsfdsfadsf_acdsfdfadsf(self):
        self.assertTrue(are_one_away('acdsfdsfadsf', 'acdsfdfadsf'))

    def test_acdsfdsfadsf_acdsfdsfads(self):
        self.assertTrue(are_one_away('acdsfdsfadsf', 'acdsfdsfads'))

    def test_acdsfdsfadsf_cdsfdsfadsf(self):
        self.assertTrue(are_one_away('acdsfdsfadsf', 'cdsfdsfadsf'))

    def test_adfdsfadsf_acdfdsfdsf(self):
        self.assertFalse(are_one_away('adfdsfadsf', 'acdfdsfdsf'))

    def test_adfdsfadsf_bdfdsfadsg(self):
        self.assertFalse(are_one_away('adfdsfadsf', 'bdfdsfadsg'))

    def test_adfdsfadsf_affdsfads(self):
        self.assertFalse(are_one_away('adfdsfadsf', 'affdsfads'))

    def test_pale_pkle(self):
        self.assertTrue(are_one_away('pale', 'pkle'))

    def test_pkle_pable(self):
        self.assertFalse(are_one_away('pkle', 'pable'))

    def test_a_abc(self):
        self.assertFalse(are_one_away('a', 'abc'))


if __name__ == '__main__':
    unittest.main()
