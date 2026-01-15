# 1 create a list called nums with a value 3,6,9 ,12
# Then print the first amd last element
nums = [3, 6, 9, 12]

# Print the first and last element
print(nums[0])
print(nums[-1])

# 2 make a colour list with three colour name. add a new colour to the end.
colours = ["red", "blue", "green"]

# Add a new colour to the end
colours.append("yellow")

print(colours)

# 3 give fruits= [apple ,banana ,cherry].change banana to orange
fruits = ["apple", "banana", "cherry"]

# Change banana to orange
fruits[1] = "orange"

print(fruits)

# 4 you are giving two lists :

# Given lists
list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
list3 = []

# Create list3 by combining list1 and list2
list3 = list1 + list2

# Replace middle elements in list1 (indexes 1 to 3)
list1[1:4] = [99, 100]

# Remove last two elements from list3
list3 = list3[:-2]

# Double each element in list3
for i in range(len(list3)):
    list3[i] = list3[i] * 2

# Print results
print("Updated list1:", list1)
print("Updated list3:", list3)


# given person or city
person = {
    "name": "Sam",
    "city": "london"
}

# add "age" key
person["age"] = 30  # you can choose any age

# change city to "Bolton"
person["city"] = "Bolton"

# ask for age and update
age = input("Enter your age: ")
person["age"] = int(age)

# print the dictionary
print(person)

# print each key-value pair
for key, value in person.items():
    print(f"{key}: {value}")



courses = {
    "python": {
        "students": ["Ali", "Sara", "Tom", "Ali"],
        "max_size": 3
    },
    "datasci": {
        "students": ["Sara", "Imran"],
        "max_size": 2
    }
}

# 1 & 2. Unique students per course and check FULL / OK
for course, info in courses.items():
    unique_students = set(info["students"])
    print(f"{course} unique students:", unique_students)

    if len(unique_students) > info["max_size"]:
        print("Status: FULL")
    else:
        print("Status: OK")

    print()  # blank line for readability


# 3. Build student_counts dictionary
student_counts = {}

for course, info in courses.items():
    unique_students = set(info["students"])
    for student in unique_students:
        student_counts[student] = student_counts.get(student, 0) + 1

print("Student counts:", student_counts)
