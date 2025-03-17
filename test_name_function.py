"""
A unit test verifies that one specific aspect of a function's behavior is correct.
A test case is a collection of unit tests that together prove that a function behaves as it's supposed to,
within the full range of situations you expect it to handle.
"""

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Michael Scofield' work?"""
        formatted_name = get_formatted_name('Michael', 'Scofield')
        self.assertEqual(formatted_name, 'Michael Scofield')

if __name__ == '__main__':
    unittest.main()