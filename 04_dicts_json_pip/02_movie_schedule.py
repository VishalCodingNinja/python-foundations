schedule = {
    "Dune": ["13:00", "16:30", "20:00"],
    "Wicked": ["12:15", "18:45"],
    "Up": ["10:00"],
}

movie = input("Which movie? ")
if movie in schedule:
    times = schedule[movie]
    print(f"{movie} plays at {', '.join(times)}")
else:
    print("Not showing today.")
