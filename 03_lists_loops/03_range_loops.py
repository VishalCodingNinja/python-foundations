print(list(range(5)))          # [0, 1, 2, 3, 4]
print(list(range(1, 6)))       # [1, 2, 3, 4, 5]
print(list(range(0, 10, 2)))   # [0, 2, 4, 6, 8]
print(list(range(5, 0, -1)))   # [5, 4, 3, 2, 1]

for month in range(1, 13):
    print("Month", month)

names = ["Ana", "Raj", "Li"]
for i in range(len(names)):
    print(i, names[i])
