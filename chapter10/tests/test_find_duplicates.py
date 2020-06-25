"""Tests for chapter10.find_duplicates."""

import contextlib
import io
import unittest

from chapter10 import find_duplicates


class TestPrintDuplicates(unittest.TestCase):

    def test_3_2_1_1_2_4_3(self) -> None:
        mock_stdout = io.StringIO()
        with contextlib.redirect_stdout(mock_stdout):
            find_duplicates.print_duplicates([3, 2, 1, 1, 2, 4, 3])

        printed = mock_stdout.getvalue()[:-1].split('\n')
        self.assertCountEqual(['1', '2', '3'], printed)


if __name__ == '__main__':
    unittest.main()
