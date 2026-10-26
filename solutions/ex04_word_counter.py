import json

sentence = input("Type a sentence: ")

counts = {}
for word in sentence.lower().split():
    word = word.strip(".,!?")
    if not word:
        continue
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1

print(json.dumps(counts, indent=2))

top_word = ""
top_count = 0
for word, count in counts.items():
    if count > top_count:
        top_word = word
        top_count = count

if top_count:
    print(f"Most common: {top_word} ({top_count}x)")
else:
    print("No words to count.")
