# Responding to a Failed Test

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

