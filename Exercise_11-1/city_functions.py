# Add a third parameter(population).
# Modify the function so that the unit test fails.
def city_country(city, country, population):
    """Display a city and the country it is located."""
    location = f"{city}, {country} - population {population}."
    return location.title()

