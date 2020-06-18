"""Tests for chapter16.xml_encoding."""

import unittest

from chapter16 import xml_encoding


class TestEncode(unittest.TestCase):

    def test_family(self) -> None:
        family = xml_encoding.Element(
            tag=0,
            attributes=[
                xml_encoding.Attribute(tag=1, value='mcdowell'),
                xml_encoding.Attribute(tag=2, value='CA'),
            ],
            children=[
                xml_encoding.Element(
                    tag=4,
                    attributes=[
                        xml_encoding.Attribute(5, value='Gayle')
                    ],
                    value='Some Message',
                )
            ])

        self.assertEqual('0 1 mcdowell 2 CA 0 4 5 Gayle 0 Some Message 0 0',
                         xml_encoding.encode(family))


if __name__ == '__main__':
    unittest.main()
