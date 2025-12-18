import math

# Problem 6: Shape Area Calculator
shape = input("Enter shape (circle, square, triangle, rectangle): ").lower()

match shape:
    case "circle":
        radius = float(input("Enter radius: "))
        area = math.pi * radius**2
        print(f"Area = {area:.2f}")
    case "square":
        side = float(input("Enter side length: "))
        area = side**2
        print(f"Area = {area:.2f}")
    case "triangle":
        base = float(input("Enter base: "))
        height = float(input("Enter height: "))
        area = 0.5 * base * height
        print(f"Area = {area:.2f}")
    case "rectangle":
        length = float(input("Enter length: "))
        width = float(input("Enter width: "))
        area = length * width
        print(f"Area = {area:.2f}")
    case _:
        print("Invalid shape")


# Problem 7: Day of Week Message
day = int(input("Enter day number (1–7): "))

match day:
    case 1:
        print("Monday - Start of work week")
    case 6 | 7:
        print("Weekend - Relax!")
    case 2 | 3 | 4 | 5:
        print("Weekday")
    case _:
        print("Invalid day")


# Problem 8: Drink Order System
drink = input("Enter drink choice (coffee, tea, water, juice): ").lower()

match drink:
    case "coffee":
        price = 2.50
    case "tea":
        price = 1.80
    case "water":
        price = 1.00
    case "juice":
        price = 2.00
    case _:
        price = 0.0

print(f"Drink: {drink.capitalize()}, Price: £{price:.2f}")


# Problem 9: Grade Letter to Number
grade = input("Enter grade letter (A-F): ").upper()

match grade:
    case "A":
        print("80-100")
    case "B":
        print("70-79")
    case "C":
        print("60-69")
    case "D":
        print("50-59")
    case "F":
        print("0-49")
    case _:
        print("Invalid grade")


# Problem 10: Command Line Tool
command = input("Enter command (create, read, update, delete, list): ").strip().lower()

match command:
    case "create":
        print("Creating new file...")
    case "read":
        print("Reading file contents...")
    case "update":
        print("Updating file...")
    case "delete":
        print("Deleting file...")
    case "list":
        print("Files: file1.txt, file2.py")
    case _ if command.startswith("help"):
        print("Available commands: create, read, update, delete, list")
    case _:
        print("Unknown command. Type 'help'")
