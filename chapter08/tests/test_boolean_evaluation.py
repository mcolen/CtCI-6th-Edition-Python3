"""Tests for chapter08.boolean_evaluation."""

import unittest

from chapter08 import boolean_evaluation


class TestBooleanEvaluation(unittest.TestCase):

    def test_1_xor_0_or_0_or_1_false(self) -> None:
        self.assertEqual(
            2, boolean_evaluation.count_eval('1^0|0|1', result=False))

    def test_0_and_0_and_0_and_1_xor_1_or_0_true(self) -> None:
        self.assertEqual(
            10, boolean_evaluation.count_eval('0&0&0&1^1|0', result=True))


if __name__ == '__main__':
    unittest.main()
