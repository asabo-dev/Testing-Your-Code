# Exercise 11-3 Test for Employee Class
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class Employee"""

    def setUp(self):
        """Create an employee entry with a first name, last name and salary for use in all test methods."""
        first_name = 'John'
        last_name = 'Doe'
        self.annual_salary = 5000
        self.employee = Employee(first_name, last_name, self.annual_salary)
       
    def test_give_default_raise(self):
        """Test that default raise works properly."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, self.annual_salary + 5000)

    def test_give_custom_raise(self):
        """Test that custom raise works properly."""
        custom_raise = 10000
        self.employee.give_raise(custom_raise)
        self.assertEqual(self.employee.annual_salary, self.annual_salary + custom_raise)

if __name__ == '__main__':
    unittest.main() 
