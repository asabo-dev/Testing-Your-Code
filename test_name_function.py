# Adding New Tests

import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""

    def test_first_last_name(self):
        """Do names like 'Michael Scofield' work?"""
        formatted_name = get_formatted_name('Michael', 'Scofield')
        self.assertEqual(formatted_name, 'Michael Scofield')

    def test_first_last_middle_name(self):
        """Do names like 'Bola Ahmed Tinubu' work?"""
        formatted_name = get_formatted_name('bola','tinubu' , 'ahmed')
        self.assertEqual(formatted_name, 'Bola Ahmed Tinubu')

if __name__ == '__main__':
    unittest.main()

