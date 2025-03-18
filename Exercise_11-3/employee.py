# Exercise 11-3
class Employee:
    """Store employee information (name, salary)."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the class attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
        
    def give_raise(self, salary_raise=5000):
        """Add at least $5,000 to annual salary"""
        self.annual_salary += salary_raise
        
