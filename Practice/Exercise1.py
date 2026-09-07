"""

Question 1 — Student Records

Create a program that stores students using a list of dictionaries.

Each student should contain:

{
    "id": 1,
    "name": "Rahul",
    "course": "Python",
    "marks": 85
}

Implement:

Add a student
Display all students
Search student by ID
Search student by name
Exit
Requirements
ID should be automatically generated.
Name cannot be empty.
Marks must be between 0 and 100.
Handle invalid numeric input using try-except.
Edge cases

Test:

Name = ""
Marks = -10
Marks = 101
Marks = abc
ID = 999

"""

students = [
    {
    "id": 1,
    "name": "Rahul",
    "course": "Python",
    "marks": 85
}
]

id_counter = max([s["id"] for s in students], default=0)

def menu():
    options = '''
                1: Add Student
                2: Display All Students
                3: Search Student
                4: Exit
'''
    print("*****  Student Management System  *****")
    print(options)
    try:
        choice =int(input("Enter Your Choice : ").strip())
        return choice
    except ValueError:
        print("Enetr a Numeric Value!!")
        return -1

def add_student():
    global id_counter

    print("*****  Student Management System  *****")

    name = input("Enter the Name of the Student : ").strip()
    if name == "":
        print("Name cannot be Empty!!!")
        return
    
    course = input("Enter the Name of the Course : ").strip()
    if course == "":
        print("Name cannot be Empty!!!")
        return
    
    try:
        marks = float(input("Enter the Marks : ").strip())
        if marks < 0 or marks > 100:
            print("Enter Marks Between 0 to 100!!")
            return

    except ValueError:
        print("Marks should be Numeric!!")  
        return

    students.append(dict(id = id_counter + 1, name = name, course = course, marks = marks))
    print("Student Data has been added Successfully") 

    id_counter += 1    

def display_one_student(s):
    print("******  Student Deatils  ******")
    print(f"ID            :{s['id']} ")
    print(f"Name          :{s['name']}  ")
    print(f"Course        :{s['course']}   ")
    print(f"Marks         :{s['marks']}  ")



def display_all_students(students):

    if not students:
        print("No Data in the Student Management System")
        return

    print("-" * 80)
    print("*****  Student Management System  *****")
    print("-" * 80)

    print(f"{'ID':^5} {'Name':<20}{'Course':<15}{'Marks':>10}")

    for s in students:
        print(f"{s['id']:^5}{s['name']:<20}{s['course']:<15}{s['marks']:10}")


def search_student():
    print("How would you like To Search Student ")
    print("1 : Search Student By ID ")
    print("2 : Search Student By Name ")


    try:
        choice = int(input("Enter Your Choice : ").strip())
        if choice == 1:
            try:
                id = int(input(" Enter the id, which needs to be Searched ").strip())
                search_by_id(id)
            except ValueError:
                print("Enter a Numeric Value!!")
                return

        elif choice == 2:
            search_by_name()

        else:
            print("Invalid Option Selected!!")
            return            

    except ValueError:
        print("Enter a Valid Value")
        return


def search_by_id(id):
    result = [s for s in students if s['id'] == id]

    if not result:
        print(f"No Student Found with {id}")
        return
    else:
        display_one_student(result[0])
        return result[0]
    
def search_by_name():
    name = input("Enter the Name of the Student To Search : ").strip()
    if name == "":
        print("Name cannot be empty!!")
        return
    
    result = [s for s in students if s['name'].lower() == name.lower()]

    if not result:
        print(f"No Student with Name {name}")
        return
    else:
        if len(result) == 1:
            display_one_student(result[0])
        else:
            display_all_students(result)    

    



def main():
    
    while True:
        choice = menu()

        if choice == 1:
            add_student()
        elif choice == 2:
            display_all_students(students)
        elif choice == 3:
            search_student()
        elif choice == 4:
            print("You have Successfully Exited the Program")
            break
        else:
            print("Invalid Input!!")

main()                            