"""
Unit tests for py_status_resource package.
"""
import os
import sys
import unittest

from py_status_resource import StatusResource


sys.path.insert(0, os.path.abspath('.'))


class TestStatusResource(unittest.TestCase):
    """
    Tests for StatusResource class
    """

    def setUp(self):
        self.sr = StatusResource()

    def test1(self):
        """
        * Exit code equals 0
        * Message is empty
        """
        self.assertEqual(0, self.sr.code)
        self.assertFalse(self.sr.message)

    def test2(self):
        """
        * Exit code equals 0
        * Message is not empty
        """
        self.sr.print_message(0, "Print info message")
        self.assertEqual(0, self.sr.code)
        self.assertEqual("Print info message", self.sr.message)

    def test3(self):
        """
        * Exit code equals 1
        * Message is not empty
        """
        self.sr.print_message(1, "Print error message")
        self.assertEqual(1, self.sr.code)
        self.assertEqual("Print error message", self.sr.message)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
