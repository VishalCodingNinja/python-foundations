"""Module 4 · Dictionaries

A dictionary stores key: value pairs. Instead of looking things up by
position, as in a list, you look them up by key.

Run it:  python 04_dicts_json_pip/01_dictionaries.py
"""

# Curly braces make a dictionary; each entry is key: value
movie = {
    "title": "Inception",
    "year": 2010,
    "rating": 8.8,
}

# Square brackets with a key read its value
print(movie["title"])               # Inception
# Assigning to an existing key replaces its value
movie["rating"] = 9.0               # change a value
# Assigning to a new key adds it
movie["genre"] = "sci-fi"           # add a new key
# movie["director"] would crash with a KeyError, because that key doesn't
# exist; .get() returns a default value ("?") instead
print(movie.get("director", "?"))   # ? when the key is missing
print("year" in movie)              # True: in checks the keys

# .items() gives each key and value together, so the loop gets both
for key, value in movie.items():
    print(key, "->", value)
