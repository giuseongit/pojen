from unittest import TestCase
from pojen import json_parser

class ParserTestCase(TestCase):
    def test_parses_json(self):
        json = """{"key":"val", "val": "key"}"""
        data = json_parser.parse(json)

        self.assertEqual(type(data), dict)
        self.assertEqual(len(data), 2)
        self.assertEqual(data["key"], "val")