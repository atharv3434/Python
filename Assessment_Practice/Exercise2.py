"""

STUDENT GRADE & ASSESSMENT MODULE

"""

students = [
{"id": 1, "name": "Aarav Sharma", "course": "Python Core", "marks": 88.5, "grade": "A"},
{"id": 2, "name": "Diya Patel", "course": "Data Science", "marks": 74.0, "grade": "B"}
]

id_counter = len(students)
#********************************************************************************************************************
def menu():
    options = '''
                1: Enroll Student
                2: Cohort Directory
                3: Query Record
                4: Revise Evaluation
                5: Purge Record
                6: Save To JSON
                7:Load from JSON
                8:Terminate
'''
    print("********  STUDENT GRADE & ASSESSMENT MODULE  ********")
    print(options)
    try:
        return int(input("Enter an Option : "))
    except ValueError:
        return -1
    

def calculate_grade(marks):
    
    if marks >= 85.0 and marks < 100.0:
        return 'A'
    elif marks >= 70.0 and marks < 85.0:
        return 'B'
    elif marks >= 50.0 and marks < 70.0:
        return 'C'
    elif marks < 50.0 and marks > 0.0:
        return 'F'
    else:
        print("Invalid Marks, enter Marks <100 and > 0")
        return None
       


#********************************************************************************************************************
def enroll_student():
    global id_counter
    print("********  STUDENT GRADE & ASSESSMENT MODULE  ********")
    name = input("Enter Your Name : ").strip()
    if name == "":
        print("Name cannot be empty")
        return
    
    course = input("Enter Your Course/Module Name: ").strip()
    if course == "":
        print("Course cannot be empty")
        return
    
    try:
        marks = float(input("Enter the Marks you have obtained : "))
        grade = calculate_grade(marks)

    except ValueError:
            print("Invalid Marks")
            return

    id_counter += 1
    students.append(dict(id = id_counter,name = name,course=course,marks=marks, grade=grade))
    print("Regestration Successfully")




#********************************************************************************************************************    
    
def cohort_directory():
    print("********  STUDENT GRADE & ASSESSMENT MODULE  ********")
    print("-" * 70)
    print(f"{'ID':^5} {'NAME':<15} {'Course/Module':<20} {'Marks':<10} {'Awarded Grade':<15}")
    print("-" * 70)

    for s in students:
        print(f"{s['id']:^5} {s['name']:<15} {s['course']:<20} {s['marks']:<10} {s['grade']:<15}")
    print("-" * 70)    

    print("Do You Want To Perform any Operation")
    print("1:Search by Student ID ")
    print("2:Search by Course Name ")
    print("3:Search by Student Name ")
    choice = int(input("Enter your Choice : "))

    try:
        if choice == 1:
            s_id = int(input("Enter the student id : "))
            search_by_id(s_id)
        elif choice == 2:
            search_by_course()
        elif choice == 3:
            ...
        else:
            print("Invalid Option Selected")
    except ValueError:
        return -1                    

#********************************************************************************************************************
    
def search_by_id(s_id):

    result = [s for s in students if s['id'] == s_id]
    if not result:
        print(f"No Student Found with ID: {s_id}")
        return None
    
    view_one_student(result[0])
    return result[0]


#******************************************************************************************************************** 
def search_by_course():
    c_name = input("Enter the Course Name : ")
    result = [s for s in students if s['course']== c_name ]

    if c_name == "":
        print("Name should not be empty!!")
        return

    if not result:
        print(f"No Student enrolled for {c_name} Course")
        return None
    
    if len(students) == 1:
        view_one_student(result[0])
    else:
        view_all_students(result)



#******************************************************************************************************************** 

def view_one_student(s_id):

    print("********  STUDENT DETAILS  ********")

    print("-" * 20)
    print(f"ID : {s_id['id']}")
    print(f"Name : {s_id['name']}")
    print(f"Course/Module : {s_id['course']}")
    print(f"Marks : {s_id['marks']}")
    print(f"Grade : {s_id['grade']}")   
    print("-" * 20)

#******************************************************************************************************************** 
def view_all_students(result):
    print("********  STUDENT GRADE & ASSESSMENT MODULE  ********")
    print("-" * 70)
    print(f"{'ID':^5} {'NAME':<15} {'Course/Module':<20} {'Marks':<10} {'Awarded Grade':<15}")
    print("-" * 70)

    for s in result:
        print(f"{s['id']:^5} {s['name']:<15} {s['course']:<20} {s['marks']:<10} {s['grade']:<15}")
    print("-" * 70)






#******************************************************************************************************************** 

    

def main():

    while True:
        result = menu()

        if result == 1:
            enroll_student()
        elif result == 2:
            cohort_directory()
        elif result == 3:
            ...
        elif result == 4:
            ...
        elif result == 5:
            ...
        elif result == 6:
            ...
        elif result == 7:
            ...
        elif result == 8:
            break
        else:
            print("Invalid Input!!!")
            

main()            
                                        
#********************************************************************************************************************