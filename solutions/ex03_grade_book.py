"""Solution · Exercise 3: grade book (Module 3)

Task: exercises/ex03_grade_book.py
Run it:  python solutions/ex03_grade_book.py
"""

# Start with an empty list and add one score per pass of the loop
scores = []
for i in range(1, 6):  # i is 1, 2, 3, 4, 5, used to number the prompts
    score = float(input(f"Score {i}: "))
    scores.append(score)

# The average is the sum of the scores divided by how many there are
average = sum(scores) / len(scores)

# Accumulator pattern: start a counter at 0 and add 1 for every pass
passed = 0
for score in scores:
    if score >= 50:
        passed += 1

print(f"Average: {average:.1f}")  # :.1f shows 1 decimal place
print("Highest:", max(scores))
print("Lowest:", min(scores))
print(f"Passed: {passed} of {len(scores)}")
