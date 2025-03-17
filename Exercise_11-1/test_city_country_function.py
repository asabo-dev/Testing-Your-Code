# Fail the test
import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country_location(self):
        """Do names like 'Lagos Nigeria' work?"""
        formatted_name = city_country('lagos', 'nigeria')
        self.assertEqual(formatted_name, 'Lagos, Nigeria.')

if __name__ == '__main__':
    unittest.main()

"""
OUTPUT:
TypeError: city_country() missing 1 required positional argument: 'population'
"""