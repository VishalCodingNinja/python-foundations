"""Module 4 · Demo: parse a nested contacts dictionary

Each contact name maps to another dictionary, which holds a phone number
and a list of tags. The program digs values out of the nested structure.

Run it:  python 04_dicts_json_pip/04_nested_contacts.py
"""

# Dictionary -> dictionary -> list: three levels of nesting
contacts = {
    "Ana": {"phone": "555-0101",
            "tags": ["work", "gym"]},
    "Raj": {"phone": "555-0199",
            "tags": ["family"]},
}

# name is the outer key ("Ana"), info is the inner dictionary
for name, info in contacts.items():
    # Turn the list of tags into one string such as "work, gym"
    tags = ", ".join(info["tags"])
    # Inside a double-quoted f-string, use single quotes for keys: info['phone']
    print(f"{name}: {info['phone']} ({tags})")

# One step at a time: contacts["Ana"] is Ana's dictionary,
# ["tags"] is the list ["work", "gym"], and [1] is its second item
print(contacts["Ana"]["tags"][1])  # gym
