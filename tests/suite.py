from unittest import TestSuite, TestLoader
from test_parser import ParserTestCase

def suite():
    suite = TestSuite()
    suite = TestLoader().loadTestsFromTestCase(ParserTestCase)
    return suite