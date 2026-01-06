# Practice Problem 1
word = input("Enter a word: ")
n = int(input("Enter a number: "))

for i in range(1, n + 1):
    print(f"{i}: {word}")


# practise Problem 2
n = int(input("Enter a number: "))
total = 0

for i in range(1, n + 1):
    total += i

print("The sum from 1 to", n, "is:", total)


# Practise Problem 3
x = int(input("Enter a number: "))

for i in range(1, 11):
    print(i, "x", x, "=", i * x)


# Practise Problem 4
sentence = input("Enter a sentence: ")
count = 0

for char in sentence:
    if char != " ":
        count += 1

print("Number of non-space characters:", count)


# Practise Problem 5
n = int(input("How many marks will you enter? "))

highest = None

for i in range(n):
    mark = int(input(f"Enter mark {i + 1}: "))

    if highest is None or mark > highest:
        highest = mark

print("The highest mark is:", highest)


# Practise Problem 6
n = int(input("How many marks will you enter? "))
passed_count = 0

for i in range(n):
    mark = int(input(f"Enter mark {i + 1}: "))
    if mark >= 40:
        print(mark)
        passed_count += 1

print("Number of students who passed:", passed_count)


# Practise Problem 7
word = input("Enter a word: ")
reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

print("Reversed word:", reversed_word)


# Practise Problem 8
n = int(input("How many names will you enter? "))
names = []

for i in range(n):
    name = input(f"Enter name {i + 1}: ")
    names.append(name)

letter = input("Enter a letter to search for: ").lower()
count = 0

for name in names:
    if letter in name.lower():
        count += 1

print("Number of names containing the letter:", count)


# Practise Problem 9
n = int(input("Enter number of students: "))
total = 0
distinctions = 0

for i in range(n):
    mark = int(input(f"Enter mark {i + 1}: "))
    total += mark
    if mark >= 70:
        distinctions += 1

average = total / n

print("Total marks:", total)
print("Average mark:", average)
print("Number of distinctions:", distinctions)


# Practise problem 10
n = int(input("How many numbers will you enter? "))
numbers = []

for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    numbers.append(num)

for num in numbers:
    print("*" * num)
