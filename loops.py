
for i in range(10):
    for j in range(i + 1):
        print("X", end="")
    for j in range(9 - i, 0, -1):
        print("-", end="")
    print()

for i in range(10):
    for j in range(i):
        print("-", end="")
    print("X", end="")
    for j in range(9 - i, 0, -1):
        print("-", end="")
    print()


for i in range(10):
    for j in range(10):
        if i == j or i == (9 - j):
            print("X", end="")
        else:
            print("-", end="")
    print()


for i in range(10):
    print("X" * i, end="")
    print("-" * (9 - i))