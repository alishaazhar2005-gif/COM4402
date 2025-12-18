# Problem 1 Cinema Ticket Category
age = int(input("Enter your age: "))

if age < 5:
    print("Free entry")
elif age <= 17:
    print("Child ticket")
elif age <= 64:
    print("Adult ticket")
else:
    print("Senior ticket")


# Problem 2 library Fine Calculater
days_late = int(input("Enter number of days late: "))

if days_late == 0:
    print("No fine")
elif days_late <= 5:
    print("Fine = £1")
elif days_late <= 10:
    print("Fine = £5")
else:
    print("Fine = £10 and membership review")


# Problem 3 Exam Borderline checks (Nested)
score = int(input("Enter exam score (0–100): "))

if score >= 40:
    if 38 <= score <= 42:
        print("Borderline pass, consider review.")
    else:
        print("Clear pass.")
else:
    print("Fail.")


# Problem 4 Discount Eligibility
is_student = input("Are you a student? (yes/no): ").lower()
age = int(input("Enter your age: "))

if is_student == "yes" or age < 18:
    print("Discount applied")
else:
    print("No discount")


# Problem 5 Traffic Light Action
colour = input("Enter a traffic light colour (red, amber, green): ").lower()

if colour == "red":
    print("Stop")
elif colour == "amber":
    print("Get ready")
elif colour == "green":
    print("Go")
else:
    print("Invalid colour")


# Problem 6 Multiple of 3,5,or both
number = int(input("Enter a number: "))

if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print("No match")


# Problem 7 Meal Recommendation (Nested)
time_of_day = input("Enter time of day (morning, afternoon, evening): ").lower()
is_hungry = input("Are you hungry? (yes/no): ").lower()

if is_hungry == "no":
    print("Have some water and rest.")
elif is_hungry == "yes":
    if time_of_day == "morning":
        print("Have breakfast.")
    elif time_of_day == "afternoon":
        print("Have lunch.")
    elif time_of_day == "evening":
        print("Have dinner.")
    else:
        print("Snack time.")
else:
    print("Invalid input.")


# Problem 8 Module Mark Satus
coursework = int(input("Enter coursework mark (0–100): "))
exam = int(input("Enter exam mark (0–100): "))

if coursework < 35 or exam < 35:
    print("Automatic fail (component below 35).")
elif (coursework + exam) / 2 >= 40:
    print("Module passed.")
else:
    print("Module failed (average below 40).")


# Problem 9 Simple Two-Side Verification
pin = input("Enter your 4-digit PIN: ")

if pin == "1234":
    colour = input("What is your favourite colour? ").lower()
    if colour == "blue":
        print("Access granted.")
    else:
        print("Security answer incorrect.")
else:
    print("Wrong PIN.")


# Problem 10 Sport Suggestion By Weather & Mood
weather = input("Enter the weather (sunny, rainy, cold): ").lower()
mood = input("Enter your mood (active, tired): ").lower()

if weather == "sunny" and mood == "active":
    print("Go for a run.")
elif weather == "sunny" and mood == "tired":
    print("Relax in the park.")
elif weather == "rainy":
    print("Indoor workout.")
elif weather == "cold":
    print("Go to the gym.")
else:
    print("No suggestion available.")
