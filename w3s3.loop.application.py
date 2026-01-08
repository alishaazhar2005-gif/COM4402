# Nested Loops and Real World Patterns Problems
# 1. Right-Angled Triangle of Stars
for i in range(1, 6):
    print("*" * i)


# 2. Number Triangle (Row Number)
for i in range(1, 6):
    print(str(i) * i)


# 3. Increasing Number Triangle
num = 1
for i in range(1, 5):
    for j in range(i):
        print(num, end="")
        num += 1
    print()


# 4. Square Multiplication Grid
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:2}", end=" ")
    print()


# 5. Coordinate Grid
for row in range(3):
    for col in range(4):
        print(f"({row},{col})", end=" ")
    print()


# 6. Hollow Square of Stars
size = 5
for i in range(size):
    for j in range(size):
        if i == 0 or i == size - 1 or j == 0 or j == size - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# 7. Centered Pyramid of Stars
rows = 4
for i in range(rows):
    print(" " * (rows - i - 1) + "*" * (2 * i + 1))


# 8. Times Table Block (2–4 by 1–5)
for i in range(1, 6):
    for j in range(2, 5):
        print(f"{j} x {i} = {j * i:<2}", end="  ")
    print()


# 9. Checkerboard Pattern
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("#", end="")
        else:
            print(".", end="")
    print()


# 10. Pascal-like Triangle (Simple Sums)
rows = 5
triangle = []

for i in range(rows):
    row = [1] * (i + 1)
    for j in range(1, i):
        row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    triangle.append(row)

for row in triangle:
    print(" ".join(map(str, row)))

