# Problem 1 – Simple ATM (Core Features)
def atm_simple():
    balance = 0.0

    while True:
        print("\n=== Simple ATM ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show balance")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print(f"Deposited ${amount:.2f}")
            else:
                print("Deposit amount must be positive.")

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"Withdrew ${amount:.2f}")

        elif choice == "3":
            print(f"Current balance: ${balance:.2f}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice, try again.")


# Problem 2 – Limited Login + Main Menu
def login_then_menu():
    correct_user = "admin"
    correct_pass = "python123"
    attempts = 0
    max_attempts = 3

    # Login phase
    while attempts < max_attempts:
        username = input("Username: ")
        password = input("Password: ")

        if username == correct_user and password == correct_pass:
            print("Login successful")
            break
        else:
            print("Incorrect username or password")
            attempts += 1

    if attempts == max_attempts:
        print("Account locked")
        return  # stop the function here

    # Main menu phase
    while True:
        print("\n=== Main Menu ===")
        print("1. Say hello")
        print("2. Show username")
        print("0. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Hello!")

        elif choice == "2":
            print(f"Logged in as: {username}")

        elif choice == "0":
            print("Logging out...")
            break

        else:
            print("Invalid choice")


# Problem 3 – Marks Entry & Classification
def marks_classification():
    n = int(input("How many marks will you enter? "))

    total = 0
    fail_count = 0
    distinction_count = 0

    # Loop to read each mark
    for i in range(1, n + 1):
        mark = int(input(f"Enter mark {i}: "))

        total += mark

        if mark < 50:
            print("Fail")
            fail_count += 1
        elif mark >= 75:
            print("Distinction")
            distinction_count += 1
        else:
            print("Pass")

    # After the loop
    if n > 0:
        average = total / n
    else:
        average = 0

    print("\n=== Summary ===")
    print(f"Total marks: {total}")
    print(f"Average: {average:.2f}")
    print(f"Number of fails: {fail_count}")
    print(f"Number of distinctions: {distinction_count}")


# Problem 4 – Enhanced ATM with Daily Limit
def atm_with_limit():
    balance = 100.0
    withdrawn_today = 0.0
    max_withdraw = 250.0

    while True:
        print("\n=== ATM with Daily Limit ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show balance")
        print("4. Show withdrawn today")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                balance += amount
                print(f"Deposited ${amount:.2f}")
            else:
                print("Deposit amount must be positive.")

        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Withdrawal amount must be positive.")
            elif amount > balance:
                print("Insufficient balance.")
            elif withdrawn_today + amount > max_withdraw:
                print("Daily withdrawal limit exceeded.")
            else:
                balance -= amount
                withdrawn_today += amount
                print(f"Withdrew ${amount:.2f}")

        elif choice == "3":
            print(f"Current balance: ${balance:.2f}")

        elif choice == "4":
            print(f"Withdrawn today: ${withdrawn_today:.2f}")
            print(f"Daily limit: ${max_withdraw:.2f}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


# Problem 5 – Parking Meter Simulator
def parking_meter():
    time_minutes = 0
    max_minutes = 120

    while True:
        print("\n=== Parking Meter ===")
        print("1. Insert £1 (30 minutes)")
        print("2. Insert £2 (60 minutes)")
        print("3. Show time remaining")
        print("0. Finish and print ticket")

        choice = input("Enter choice: ")

        if choice == "1":
            if time_minutes + 30 <= max_minutes:
                time_minutes += 30
                print("Added 30 minutes.")
            else:
                print("Maximum parking time reached.")

        elif choice == "2":
            if time_minutes + 60 <= max_minutes:
                time_minutes += 60
                print("Added 60 minutes.")
            else:
                print("Maximum parking time reached.")

        elif choice == "3":
            hours = time_minutes // 60
            minutes = time_minutes % 60
            print(f"Time remaining: {hours} hour(s) {minutes} minute(s)")

        elif choice == "0":
            hours = time_minutes // 60
            minutes = time_minutes % 60
            print("Printing ticket...")
            print(f"Final time: {hours} hour(s) {minutes} minute(s)")
            break

        else:
            print("Invalid choice")

