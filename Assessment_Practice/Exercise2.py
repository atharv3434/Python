"""
STUDENT GRADE & ASSESSMENT MODULE
"""

import json


# Initial student records
students = [
    {
        "id": 1,
        "name": "Aarav Sharma",
        "course": "Python Core",
        "marks": 88.5,
        "grade": "A"
    },
    {
        "id": 2,
        "name": "Diya Patel",
        "course": "Data Science",
        "marks": 74.0,
        "grade": "B"
    }
]

# Start ID counter from highest existing ID
id_counter = max([s["id"] for s in students], default=0)


# ********************************************************************
# MENU
# ********************************************************************

def menu():

    print("\n" + "*" * 55)
    print("       STUDENT GRADE & ASSESSMENT MODULE")
    print("*" * 55)

    print("""
1. Enroll Student
2. Cohort Directory
3. Query Records
4. Revise Evaluation
5. Purge Record
6. Save to JSON
7. Load from JSON
8. Terminate
""")

    try:
        choice = int(input("Enter an Option: ").strip())
        return choice

    except ValueError:
        print("Error: Please enter a valid numerical choice.")
        return -1


# ********************************************************************
# CALCULATE GRADE
# ********************************************************************

def calculate_grade(marks):

    if marks >= 85:
        return "A"

    elif marks >= 70:
        return "B"

    elif marks >= 50:
        return "C"

    else:
        return "F"


# ********************************************************************
# ENROLL STUDENT
# ********************************************************************

def enroll_student():

    global id_counter

    print("\n******** STUDENT ENROLLMENT ********")

    # Get name
    name = input("Enter Student Name: ").strip()

    if name == "":
        print("Error: Name cannot be empty.")
        return

    # Get course
    course = input("Enter Course/Module: ").strip()

    if course == "":
        print("Error: Course cannot be empty.")
        return

    # Get marks
    try:
        marks = float(input("Enter Marks (0-100): ").strip())

    except ValueError:
        print("Error: Marks must be a number.")
        return

    # Validate marks
    if marks < 0 or marks > 100:
        print("Error: Marks must be between 0 and 100.")
        return

    # Calculate grade automatically
    grade = calculate_grade(marks)

    # Generate ID
    id_counter += 1

    # Create student dictionary
    student = {
        "id": id_counter,
        "name": name,
        "course": course,
        "marks": round(marks, 2),
        "grade": grade
    }

    # Add to list
    students.append(student)

    print("\nStudent enrolled successfully!")
    print(f"Assigned Student ID: {id_counter}")
    print(f"Grade: {grade}")


# ********************************************************************
# VIEW ONE STUDENT
# ********************************************************************

def view_one_student(student):

    print("\n******** STUDENT DETAILS ********")
    print("-" * 40)

    print(f"ID            : {student['id']}")
    print(f"Name          : {student['name']}")
    print(f"Course/Module : {student['course']}")
    print(f"Marks         : {student['marks']:.2f}")
    print(f"Awarded Grade : {student['grade']}")

    print("-" * 40)


# ********************************************************************
# VIEW ALL STUDENTS
# ********************************************************************

def view_all_students(student_list):

    if not student_list:
        print("\nNo student records found.")
        return

    print("\n******** COHORT DIRECTORY ********")

    print("-" * 75)

    print(
        f"{'ID':^5} "
        f"{'NAME':<20} "
        f"{'COURSE':<20} "
        f"{'MARKS':>10} "
        f"{'GRADE':^10}"
    )

    print("-" * 75)

    for student in student_list:

        print(
            f"{student['id']:^5} "
            f"{student['name']:<20} "
            f"{student['course']:<20} "
            f"{student['marks']:>10.2f} "
            f"{student['grade']:^10}"
        )

    print("-" * 75)


# ********************************************************************
# COHORT DIRECTORY
# ********************************************************************

def cohort_directory():

    if not students:
        print("\n[Alert] Cohort directory is empty.")
        return

    view_all_students(students)


# ********************************************************************
# SEARCH BY ID
# ********************************************************************

def search_by_id(student_id):

    for student in students:

        if student["id"] == student_id:
            return student

    return None


# ********************************************************************
# SEARCH BY NAME
# ********************************************************************

def search_by_name():

    name = input("Enter Student Name to Search: ").strip()

    if name == "":
        print("Error: Search name cannot be empty.")
        return

    results = []

    for student in students:

        if name.lower() in student["name"].lower():
            results.append(student)

    if not results:
        print(f"No records found for name: {name}")
        return

    view_all_students(results)


# ********************************************************************
# SEARCH BY COURSE
# ********************************************************************

def search_by_course():

    course = input("Enter Course Name to Search: ").strip()

    if course == "":
        print("Error: Course search term cannot be empty.")
        return

    results = []

    for student in students:

        if course.lower() in student["course"].lower():
            results.append(student)

    if not results:
        print(f"No records found for course: {course}")
        return

    view_all_students(results)


# ********************************************************************
# QUERY RECORDS
# ********************************************************************

def query_records():

    print("\n******** QUERY RECORDS ********")

    print("""
1. Search by Student ID
2. Search by Student Name
3. Search by Course
4. Return to Main Menu
""")

    try:
        choice = int(input("Enter your choice: ").strip())

    except ValueError:
        print("Error: Invalid numerical input.")
        return

    if choice == 1:

        try:
            student_id = int(input("Enter Student ID: ").strip())

        except ValueError:
            print("Error: Student ID must be an integer.")
            return

        result = search_by_id(student_id)

        if result is None:
            print(f"No student found with ID: {student_id}")
        else:
            view_one_student(result)

    elif choice == 2:

        search_by_name()

    elif choice == 3:

        search_by_course()

    elif choice == 4:

        return

    else:

        print("Invalid option.")


# ********************************************************************
# REVISE / UPDATE STUDENT
# ********************************************************************

def revise_evaluation():

    print("\n******** REVISE EVALUATION ********")

    try:
        student_id = int(input("Enter Student ID to Update: ").strip())

    except ValueError:
        print("Error: Student ID must be an integer.")
        return

    # Search student
    student = search_by_id(student_id)

    if student is None:
        print(f"No student found with ID: {student_id}")
        return

    # Display existing record
    print("\nCurrent Student Information:")
    view_one_student(student)

    # Update name
    new_name = input(
        "Enter New Name (press Enter to keep current): "
    ).strip()

    if new_name != "":
        student["name"] = new_name

    # Update course
    new_course = input(
        "Enter New Course (press Enter to keep current): "
    ).strip()

    if new_course != "":
        student["course"] = new_course

    # Update marks
    marks_input = input(
        "Enter New Marks (press Enter to keep current): "
    ).strip()

    if marks_input != "":

        try:
            new_marks = float(marks_input)

        except ValueError:
            print("Error: Marks must be numeric.")
            return

        if new_marks < 0 or new_marks > 100:
            print("Error: Marks must be between 0 and 100.")
            return

        # Update marks
        student["marks"] = round(new_marks, 2)

        # Automatically recalculate grade
        student["grade"] = calculate_grade(new_marks)

    print("\nStudent record updated successfully!")

    view_one_student(student)


# ********************************************************************
# DELETE / PURGE STUDENT
# ********************************************************************

def purge_record():

    print("\n******** PURGE RECORD ********")

    try:
        student_id = int(input("Enter Student ID to Delete: ").strip())

    except ValueError:
        print("Error: Student ID must be an integer.")
        return

    # Find student
    student = search_by_id(student_id)

    if student is None:
        print(f"No student found with ID: {student_id}")
        return

    # Display student before deleting
    print("\nStudent record found:")
    view_one_student(student)

    # Confirmation
    confirmation = input(
        "Are you sure you want to delete this record? (y/n): "
    ).strip().lower()

    if confirmation == "y":

        students.remove(student)

        print("Student record deleted successfully.")

    elif confirmation == "n":

        print("Delete operation cancelled.")

    else:

        print("Invalid confirmation. Delete operation cancelled.")


# ********************************************************************
# SAVE TO JSON
# ********************************************************************

def save_to_json():

    try:

        with open("students.json", "w") as file:

            json.dump(students, file, indent=4)

        print("\nStudent records saved successfully to students.json")

    except OSError as e:

        print(f"Error while saving file: {e}")


# ********************************************************************
# LOAD FROM JSON
# ********************************************************************

def load_from_json():

    global students, id_counter

    try:

        with open("students.json", "r") as file:

            loaded_students = json.load(file)

        # Basic validation
        if not isinstance(loaded_students, list):
            print("Error: JSON data must contain a list of students.")
            return

        students = loaded_students

        # Recalculate ID counter
        id_counter = max(
            [student["id"] for student in students],
            default=0
        )

        print("\nStudent records loaded successfully.")

    except FileNotFoundError:

        print("Error: students.json file was not found.")

    except json.JSONDecodeError:

        print("Error: students.json contains invalid JSON data.")

    except OSError as e:

        print(f"Error while reading file: {e}")


# ********************************************************************
# MAIN
# ********************************************************************

def main():

    while True:

        choice = menu()

        if choice == 1:

            enroll_student()

        elif choice == 2:

            cohort_directory()

        elif choice == 3:

            query_records()

        elif choice == 4:

            revise_evaluation()

        elif choice == 5:

            purge_record()

        elif choice == 6:

            save_to_json()

        elif choice == 7:

            load_from_json()

        elif choice == 8:

            print("\nTerminating application. Goodbye!")

            break

        else:

            print("Invalid Input! Please select an option from 1 to 8.")


# ********************************************************************
# PROGRAM START
# ********************************************************************

if __name__ == "__main__":
    main()