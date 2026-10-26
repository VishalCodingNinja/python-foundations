movie = {
    "title": "Inception",
    "year": 2010,
    "rating": 8.8,
}

print(movie["title"])               # Inception
movie["rating"] = 9.0               # change a value
movie["genre"] = "sci-fi"           # add a new key
print(movie.get("director", "?"))   # ? when the key is missing
print("year" in movie)              # True: in checks keys

for key, value in movie.items():
    print(key, "->", value)
