print("Welcome to the Digital Quiz Application")

# INITIALISATION
score = 0

quiz_questions = [
    (
        "What is the capital of France?",
        ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "C"
    ),
    (
        "Which subject focuses on computer programming?",
        ["A. History", "B. Geography", "C. Computer Science", "D. Art"],
        "C"
    ),
    (
        "What does CPU stand for?",
        [
            "A. Central Processing Unit",
            "B. Computer Power Unit",
            "C. Central Program Utility",
            "D. Control Process Unit"
        ],
        "A"
    ),
    (
        "Which number is even?",
        ["A. 3", "B. 7", "C. 9", "D. 8"],
        "D"
    ),
    (
        "Which device is used to type text?",
        ["A. Monitor", "B. Mouse", "C. Keyboard", "D. Speaker"],
        "C"
    ),
    (
        "What is 5 + 7?",
        ["A. 10", "B. 11", "C. 12", "D. 13"],
        "C"
    ),
    (
        "Which data type stores true or false values?",
        ["A. Integer", "B. String", "C. Boolean", "D. Character"],
        "C"
    ),
    (
        "Which one is an output device?",
        ["A. Keyboard", "B. Mouse", "C. Scanner", "D. Printer"],
        "D"
    ),
    (
        "Which symbol is used for comments in Python?",
        ["A. //", "B. ##", "C. #", "D. <!-- -->"],
        "C"
    ),
    (
        "Which loop repeats a fixed number of times?",
        ["A. While loop", "B. For loop", "C. If statement", "D. Switch"],
        "B"
    )
]

# MAIN PROGRAM LOOP
for question_number in range(len(quiz_questions)):
    question, options, correct_answer = quiz_questions[question_number]

    print("\nQuestion", question_number + 1)
    print(question)

    # QUESTION PRESENTATION
    for option in options:
        print(option)

    # USER INPUT
    user_answer = input("Enter your answer (A, B, C, or D): ").upper()

    while user_answer not in ["A", "B", "C", "D"]:
        user_answer = input("Invalid choice. Please enter A, B, C, or D: ").upper()

    # ANSWER VALIDATION AND SCORING
    if user_answer == correct_answer:
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer was", correct_answer)

# PROGRAM TERMINATION
percentage = (score / len(quiz_questions)) * 100

print("\nQuiz Completed")
print("Final Score:", score, "out of", len(quiz_questions))
print("Percentage Score:", percentage, "%")
