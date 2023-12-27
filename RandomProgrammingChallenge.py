"""
The below code was a programming challenge I found in a Facebook Group. I implemented a default dictionary to complete it.

Beginning of Challenge:
You're planning a trip around world and want to keep track of countries you'll be visiting. 
Write code to create list of unique countries you will visit from list of cities you'll be traveling to.
"""

from collections import defaultdict

cities = [
{"city": "Paris", "country": "France"},
{"city": "Berlin", "country": "Germany"},
{"city": "Geneva", "country": "Switzerland"},
{"city": "Nice", "country": "France"},
{"city": "Rome", "country": "Italy"},
{"city": "Dubai", "country": "UAE"},
{"city": "Bangkok", "country": "Thailand"},
{"city": "Phuket", "country": "Thailand"},
{"city": "Tokyo", "country": "Japan"},
{"city": "Osaka", "country": "Japan"},
{"city": "Los Angeles", "country": "United States"},
{"city": "New York City", "country": "United States"}]

# Output: List of unique countries you plan to visit
countries = []

for i in cities:
    if i['country'] not in countries:
        countries.append(i['country'])

print(countries) 

# Outputs: ['France', 'Germany', 'Switzerland', 'Italy', 'UAE', 'Thailand', 'Japan', 'United States']

# Bonus Challenge: How could you count the number of cities you'll visit in each country?
citiesPerCountry = defaultdict(lambda: 0)

for i in cities:
    citiesPerCountry[i['country']] += 1

print(dict(citiesPerCountry))

# Outputs: {'France': 2, 'Germany': 1, 'Switzerland': 1, 'Italy': 1, 'UAE': 1, 'Thailand': 2, 'Japan': 2, 'United States': 2}

# How many different ways can you think of?
# You could also do something tuples and zip
# Enjoy
