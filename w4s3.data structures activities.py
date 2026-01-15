# 2 Classroom Seating Plan
# List is used because order matters

def create_row(names):
    return names

def get_student_at(row, index):
    if index < len(row):
        return row[index]
    return None

def swap_seats(row, i1, i2):
    temp = row[i1]
    row[i1] = row[i2]
    row[i2] = temp

def remove_student(row, name):
    if name in row:
        row.remove(name)


# 3 Unique Course Code
# Set is used because duplicates are not allowed

def enrol_module(modules, code):
    modules.add(code)

def is_enrolled(modules, code):
    return code in modules

def drop_module(modules, code):
    if code in modules:
        modules.remove(code)

def count_modules(modules):
    return len(modules)


# 4 Fixed Student Record
# Tuple is used because data should not change

def create_student(id_number, name, year):
    return (id_number, name, year)

def get_name(student):
    return student[1]

def get_year(student):
    return student[2]


# 5 Product Catalogue
# Dictionary: product -> price

def add_product(catalogue, name, price):
    catalogue[name] = price

def get_price(catalogue, name):
    if name in catalogue:
        return catalogue[name]
    return None

def increase_all_prices(catalogue, percent):
    for item in catalogue:
        catalogue[item] = catalogue[item] + (catalogue[item] * percent / 100)

def remove_product(catalogue, name):
    if name in catalogue:
        del catalogue[name]


# 6  Complete or Debug Code
def average(numbers):
    if len(numbers) == 0:
        return 0

    total = 0
    for n in numbers:
        total = total + n

    return total / len(numbers)


# 7 – Complete the Dictionary Lookup
capitals = {
    "France": "Paris",
    "Spain": "Madrid",
    "Japan": "Tokyo"
}

def get_capital(country):
    if country in capitals:
        return capitals[country]
    return "Unknown country"

# 8 – Debug the Set Membership
def count_unique_emails(emails):
    unique = set()

    for email in emails:
        unique.add(email)

    return len(unique)

# 9–10: Slightly More Advanced Activities
# 9 – Word Frequency Counter (Dictionary)
def word_counts(sentence):
    words = sentence.lower().split()
    counts = {}

    for word in words:
        if word in counts:
            counts[word] = counts[word] + 1
        else:
            counts[word] = 1

    return counts


# 10 – Simple In-Memory “Database” of Students
def add_student(students, student_id, name, mark):
    students[student_id] = {"name": name, "mark": mark}

def get_student(students, student_id):
    if student_id in students:
        return students[student_id]
    return None

def update_mark(students, student_id, new_mark):
    if student_id in students:
        students[student_id]["mark"] = new_mark

def delete_student(students, student_id):
    if student_id in students:
        del students[student_id]

