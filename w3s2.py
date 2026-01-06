# 1. Countdown to Launch

start = int(input("Enter a starting number: "))

while start >= 1:
    print(start)
    start -= 1

print("Lift off!")


# 2. Sum Until Zero (Sentinel)

total = 0

while True:
    num = int(input("Enter an integer (0 to stop): "))
    if num == 0:
        break
    total += num

print("Total:", total)


# 3. Password Checker (Do-While Style)

correct_password = "python123"

while True:
    password = input("Enter password: ")
    if password == correct_password:
        print("Access granted")
        break
    else:
        print("Try again")


# 4. Guess the Secret Number

secret = 17

guess = int(input("Guess the number: "))

while guess != secret:
    if guess > secret:
        print("Too high")
    else:
        print("Too low")
    guess = int(input("Guess again: "))

print("Well done")


# 5. Menu Loop – Simple Calculator

while True:
    print("1. Add")
    print("2. Subtract")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "0":
        break
    elif choice == "1":
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Result:", a + b)
    elif choice == "2":
        a = int(input("First number: "))
        b = int(input("Second number: "))
        print("Result:", a - b)
    else:
        print("Invalid choice")

# 6. Input Validation (Positive Integer)

while True:
    num = int(input("Enter a positive integer: "))
    if num <= 0:
        print("Error: Must be positive")
    else:
        break

print("You entered:", num)


# 7. Average of Marks Until -1

total = 0
count = 0

while True:
    mark = int(input("Enter a mark (0–100) or -1 to stop: "))
    if mark == -1:
        break
    total += mark
    count += 1

if count > 0:
    print("Marks entered:", count)
    print("Average:", total / count)
else:
    print("No marks entered")


# 8. Limited Login Attempts

correct_username = "admin"
correct_password = "1234"
attempts = 0

while attempts < 3:
    username = input("Username: ")
    password = input("Password: ")

    if username == correct_username and password == correct_password:
        print("Login successful")
        break
    else:
        print("Incorrect login")
        attempts += 1

if attempts == 3:
    print("Account locked")


# 9. Bank Balance Simulator
balance = 100

while balance > 0:
    print("Current balance:", balance)
    withdraw = int(input("Enter withdrawal amount (0 to stop): "))

    if withdraw == 0:
        break
    elif withdraw > balance:
        print("Insufficient funds")
    else:
        balance -= withdraw

print("Final balance:", balance)


# 10. Text Menu with Do-While Style

name = None

while True:
    print("1. Enter name")
    print("2. Show last name entered")
    print("0. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter name: ")
    elif choice == "2":
        if name is None:
            print("No name entered yet")
        else:
            print("Last name entered:", name)
    elif choice == "0":
        break
    else:
        print("Invalid choice")
