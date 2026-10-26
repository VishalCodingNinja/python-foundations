"""Solution · Exercise 4: word counter (Module 4)

Task: exercises/ex04_word_counter.py
Run it:  python solutions/ex04_word_counter.py
"""

import json

sentence = input("Type a sentence: ")

# The dictionary maps each word to how many times it appears
counts = {}
# .lower() makes "The" and "the" the same word; .split() breaks the
# sentence into a list of words wherever there are spaces
for word in sentence.lower().split():
    word = word.strip(".,!?")  # remove punctuation from both ends
    if not word:
        continue  # skip anything that was only punctuation, like "!"
    if word in counts:
        counts[word] += 1   # seen before: add one
    else:
        counts[word] = 1    # first time: start the count at one

# indent=2 spreads the JSON over several lines, which is easier to read
print(json.dumps(counts, indent=2))

# Find the biggest count: check every word and remember the best so far
top_word = ""
top_count = 0
for word, count in counts.items():
    if count > top_count:
        top_word = word
        top_count = count

# top_count is still 0 if the sentence had no words at all
if top_count:
    print(f"Most common: {top_word} ({top_count}x)")
else:
    print("No words to count.")
