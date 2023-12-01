# Create a dictionary
countries = {
    "JP": "Japan",
    "KR": "Korea",
    "MX": "Mexico"
}

# Print the dictionary
print(countries)

# Access value using a key
country_name = countries.get("JP")
print(country_name)

# Checking if a key exists
has_korea = "KR" in countries
print("Has Korea:", has_korea)

# Remove a key-value pair
countries.pop("MX", None)

# Iterate over the dictionary
for key, value in countries.items():
    print(f"{key} => {value}")
