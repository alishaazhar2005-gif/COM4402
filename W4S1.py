# def greet(name, age):
#     # name = input("Please enter your name:")
#     print(f"Hello, {name}!")
#     # age = int(input("Enter your age: "))
#     print(f"In ten years you will be {age + 10} years old!")
#
# greet("Alisha", 20)
# greet("Bob", 30)
# greet("Charlie", 40)



# def add(a, b):
#     return a + b
#
# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
#
# result = a + b
# result = add(a, b)

# 1- Fix the Greeting
def greet():
    message = "Hello from the function"
    return message

message = greet()
print(message)


# 2- Local vs Global Guess
def add_one (count):
    count = count +1
    print ("inside :,count" )
    return count

count=0
count=add_one(count)
print("Outside:",count)


#  3 – Complete the Function
def area_of_rectangle(width, height):
    area = width * height
    return area

w = float(input("Enter width: "))
h = float(input("Enter height: "))

result = area_of_rectangle(w, h)
print("Area is", result)


# 4 – Parameter vs Global
#Version 1 (global)
rate = 0.2

def calculate_tax(amount):
    return amount * rate

price = 100
tax = calculate_tax(price)
print("Tax:", tax)

# Version 2 (no global)
def calculate_tax(amount, rate):
    return amount * rate

price = 100
rate = 0.2
tax = calculate_tax(price, rate)
print("Tax:", tax)


# 5 – Bug Hunt: Discount Function
def apply_discount(price):
    discount = 0
    if price > 100:
        discount = 10
    return price - discount

p = float(input("Enter price: "))
result = apply_discount(p)
print("Final price:", result)


#  6 – ATM Helper Functions
def show_menu():
    print("1. Deposit")
    print("2. Withdraw")
    print("0. Exit")
    return input("Enter choice: ")

def deposit(balance):
    amount = float(input("Amount to deposit: "))
    if amount > 0:
        balance += amount
    else:
        print("Invalid amount")
    return balance

def withdraw(balance):
    amount = float(input("Amount to withdraw: "))
    if amount > 0 and amount <= balance:
        balance -= amount
    else:
        print("Invalid withdrawal")
    return balance

balance = 0

while True:
    choice = show_menu()
    if choice == "1":
        balance = deposit(balance)
    elif choice == "2":
        balance = withdraw(balance)
    elif choice == "0":
        break
    else:
        print("Invalid choice")

print("Final balance:", balance)


# 7 – Scope Explanation in Comments
def add_mark(current_total, mark):
    # current_total is passed in, so the function knows its value
    return current_total + mark

total = 0

mark1 = int(input("Enter mark 1: "))
total = add_mark(total, mark1)

mark2 = int(input("Enter mark 2: "))
total = add_mark(total, mark2)

print("Total:", total)


# 8 – Rewrite Using Functions
def get_user_details():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    return name, age

def print_message(name, age):
    if age >= 18:
        print(f"Hello {name}, you are an adult.")
    else:
        print(f"Hello {name}, you are under 18.")

name, age = get_user_details()
print_message(name, age)


#  9 (Medium) – Login + Scope
def check_password(input_password):
    correct_password = "python123"
    return input_password == correct_password

def login():
    pwd = input("Enter password: ")
    if check_password(pwd):
        print("Welcome")
    else:
        print("Access denied")

login()
login()


#  10 (Medium) – Refactor Parking Time Calculator
def convert_minutes(minutes):
    hours = minutes // 60
    remaining = minutes % 60
    return hours, remaining

def print_time(hours, remaining):
    if hours > 0 and remaining > 0:
        print(f"{hours} hour(s) and {remaining} minute(s)")
    elif hours > 0:
        print(f"{hours} hour(s)")
    else:
        print(f"{remaining} minute(s)")

minutes = int(input("Enter total parking minutes: "))
hours, remaining = convert_minutes(minutes)
print_time(hours, remaining)

