scores = []
for i in range(1, 6):
    score = float(input(f"Score {i}: "))
    scores.append(score)

average = sum(scores) / len(scores)

passed = 0
for score in scores:
    if score >= 50:
        passed += 1

print(f"Average: {average:.1f}")
print("Highest:", max(scores))
print("Lowest:", min(scores))
print(f"Passed: {passed} of {len(scores)}")
