"""Exercise 4: Word counter  (Module 4: dictionaries and JSON)

Write a program that:
  1. asks for a sentence
  2. counts how often each word appears, in a dictionary
     (ignore upper/lower case and the punctuation . , ! ?)
  3. prints the dictionary as pretty JSON
  4. prints the most common word

Sample run:
    Type a sentence: The cat saw the dog. The dog ran!
    {
      "the": 3,
      "cat": 1,
      "saw": 1,
      "dog": 2,
      "ran": 1
    }
    Most common: the (3x)

Hint: sentence.lower().split() gives you a list of words.
Hint: word.strip(".,!?") removes punctuation from both ends.
Hint: json.dumps(counts, indent=2) makes the pretty JSON.
Solution: solutions/ex04_word_counter.py
"""

# TODO 1: import json and ask for the sentence

# TODO 2: loop over the words and add 1 to counts[word] each time

# TODO 3: print the JSON, then find the word with the biggest count
