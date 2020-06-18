"""Tests for chapter10.find_duplicates."""

import io
import unittest
import unittest.mock

from chapter10 import find_duplicates


class TestPrintDuplicates(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_3_2_1_1_2_4_3(self, mock_stdout: io.StringIO) -> None:
        find_duplicates.print_duplicates([3, 2, 1, 1, 2, 4, 3])

        printed = mock_stdout.getvalue()[:-1].split('\n')
        self.assertCountEqual(['1', '2', '3'], printed)


if __name__ == '__main__':
    unittest.main()
