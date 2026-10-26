contacts = {
    "Ana": {"phone": "555-0101",
            "tags": ["work", "gym"]},
    "Raj": {"phone": "555-0199",
            "tags": ["family"]},
}

for name, info in contacts.items():
    tags = ", ".join(info["tags"])
    print(f"{name}: {info['phone']} ({tags})")

print(contacts["Ana"]["tags"][1])  # gym
