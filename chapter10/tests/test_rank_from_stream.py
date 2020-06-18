"""Tests for chapter10.rank_from_stream."""

import unittest

from chapter10 import rank_from_stream


class TestStreamRanker(unittest.TestCase):

    def test_track_5_1_4_4_5_9_7_13_3_rank_4(self) -> None:
        stream_ranker = rank_from_stream.StreamRanker()
        for x in [5, 1, 4, 4, 5, 9, 7, 13, 3]:
            stream_ranker.track(x)

        self.assertEqual(3, stream_ranker.get_rank_of_number(4))


if __name__ == '__main__':
    unittest.main()
