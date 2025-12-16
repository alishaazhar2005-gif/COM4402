# Activity 1
# Get input from user
item_name = input("Item name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

# Calculate total
total = price * quantity
# Using concatenation
print("You bought " + str(quantity) + " x " + item_name + " at £" + str(price) + " each. Total = £" + str(total))
# Using f-string
print(f"You bought {quantity} x {item_name} at £{price} each. Total = £{total}")

# Activity 2
# Ask for the user's age
age = int(input("Enter your age: "))
# Using commas in print()
print("You are", age, "years old.")
# Using f-string
print(f"You are {age} years old.")

# Activity 3
# Ask for input
full_name = input("Enter your full name: ").strip()
course_name = input("Enter your course name: ").strip()
# Format the strings
full_name = full_name.title()       # Converts to title case
course_name = course_name.upper()   # Converts to uppercase
# Print using f-string
print(f"Student: {full_name} ({course_name})")

# Activity 4
# Get user input
name = input("Enter your name: ").strip()
age = int(input("Enter your age: "))
course = input("Enter your course: ").strip()
# Print all details in one print() call using \n and f-string
print(f"Your details:\nName: {name}\nAge: {age}\nCourse: {course}")

# Activity 5
# Template message
template = "Hello NAME, welcome to COURSE."
# Get user input
name = input("Enter your name: ").strip()
course = input("Enter your course: ").strip()
# Replace placeholders with user input
message = template.replace("NAME", name).replace("COURSE", course)
# Print final message
print(message)

# Activity 6
# Ask the user to type a sentence
sentence = input("Type a sentence: ")
# Print the sentence in all uppercase
print("Uppercase:", sentence.upper())
# Print the sentence in all lowercase
print("Lowercase:", sentence.lower())
# Print the length of the sentence
print("Length of the sentence:", len(sentence))

# Activity 7
# Ask the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
# Check if the second number is zero
if num2 == 0:
    print("Error: cannot divide by zero")
else:
    # Perform division and print result using an f-string
    result = num1 / num2
    print(f"{num1} divided by {num2} is {result}")

# Activity 8
# Ask the user for a username
username = input("Enter your username: ")
# Strip spaces and convert to lowercase
processed_username = username.strip().lower()
# Print both the raw and processed username
print(f"Raw: '{username}'")
print(f"Processed: '{processed_username}'")

# Activity 9
# Ask user for input
name = input("Enter your name: ")
course = input("Enter your course: ")
year = int(input("Enter your year of study: "))
# Generate a personalised letter using a triple-quoted f-string
letter = f"""
Dear {name.title()},
Congratulations on pursuing your {course.upper()} course!
Wishing you all the best for your {year} year ahead.

Sincerely,
The Team
"""
# Print the letter
print(letter)

# Activity 10
# Given variables
name = "Sam"
age = 19
course = "COM4402"

# Using +
print("Hello " + name + ", you are " + str(age) + " and enrolled in " + course + ".")
# Advantage: Simple and straightforward for short strings
# Disadvantage: Need to convert non-strings manually and can get messy with many variables

# Using commas
print("Hello", name + ", you are", age, "and enrolled in", course + ".")
# Advantage: Automatically converts non-strings, cleaner than +
# Disadvantage: Adds spaces automatically which may not always be desired

# Using f-string
print(f"Hello {name}, you are {age} and enrolled in {course}.")
# Advantage: Very readable and concise, variables are embedded directly
# Disadvantage: Requires Python 3.6+ and knowledge of f-string syntax
