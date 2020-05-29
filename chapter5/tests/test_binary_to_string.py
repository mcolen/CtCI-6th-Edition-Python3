"""Tests for chapter5.binary_to_string."""

import io
import unittest
import unittest.mock

from chapter5 import binary_to_string


class TestBinaryToString(unittest.TestCase):

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_0_125(self, mock_stdout: io.StringIO) -> None:
        binary_to_string.fraction_to_binary(0.125)
        self.assertEqual('.001\n', mock_stdout.getvalue())


if __name__ == "__main__":
    unittest.main()
