"""Module 4 · Demo: movie schedule dictionary

Each movie name maps to a list of showtimes. The user types a movie and the
program looks up when it plays.

Run it:  python 04_dicts_json_pip/02_movie_schedule.py
"""

# Values can be any type; here each value is a list of times
schedule = {
    "Dune": ["13:00", "16:30", "20:00"],
    "Wicked": ["12:15", "18:45"],
    "Up": ["10:00"],
}

movie = input("Which movie? ")
# Check the key exists first, so a typo can't crash the program.
# Keys must match exactly, capital letters included: "dune" is not "Dune".
if movie in schedule:
    times = schedule[movie]
    # ", ".join(times) glues the list into one string: "13:00, 16:30, 20:00"
    print(f"{movie} plays at {', '.join(times)}")
else:
    print("Not showing today.")
