#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.

# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.

# Use a loop to print the name of each river included in the dictionary.

# Use a loop to print the name of each country included in the dictionary.

# Creating a dictionary of rivers and the countries they run through
rivers = {
    "Nile": "Egypt",
    "Amazon": "Brazil",
    "Yangtze": "China"}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")

print("\nRivers in the dictionary:")
for river in rivers.keys():
    print(river)


print("\nCountries in the dictionary:")
for country in rivers.values():
    print(country)
