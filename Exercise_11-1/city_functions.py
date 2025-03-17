# Make the third parameter optional.
def city_country(city, country, population=''):
    """Display a city and the country it is located."""
    if population:
        location = f"{city}, {country} - population {population}."
    else:
        location = f"{city}, {country}."
    return location.title()

