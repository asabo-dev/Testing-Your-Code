# Pass the test with the optional parameter
# Add another test to accomodate three parameters
import unittest
from city_functions import city_country

class CityTestCase(unittest.TestCase):
    """Tests for city_functions.py"""

    def test_city_country_location(self):
        """Do names like 'Lagos, Nigeria.' work?"""
        formatted_name = city_country('kuala lumpur', 'malaysia')
        self.assertEqual(formatted_name, 'Kuala Lumpur, Malaysia.')
    
    def test_location_population(self):
        """Can the function display the location and population?"""
        formatted_name = city_country('lagos', 'nigeria', '20,000,000')
        self.assertEqual(formatted_name, 'Lagos, Nigeria - Population 20,000,000.') 

if __name__ == '__main__':
    unittest.main()
