"""Tests for chapter05.next_number."""

import io
import unittest
import unittest.mock

from chapter05 import next_number


class TestNextNumber(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_0b10110(self, mock_stdout: io.StringIO) -> None:
        next_number.print_smaller_and_larger(0b10110)
        self.assertEqual(f'{0b10101} {0b11001}\n', mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
