# Make the third parameter optional.
# Ensure that the unit test passes again.
def city_country(city, country, population=''):
    """Display a city and the country it is located."""
    location = f"{city}, {country} - population {population}."
    return location.title()
