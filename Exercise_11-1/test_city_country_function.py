# Pass the test with the optional parameter
import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country_location(self):
        """Do names like 'Lagos, Nigeria - Population 5000000.' work?"""
        formatted_name = city_country('lagos', 'nigeria', '20,000,000')
        self.assertEqual(formatted_name, 'Lagos, Nigeria - Population 20,000,000.')

if __name__ == '__main__':
    unittest.main()
