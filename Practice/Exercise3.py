"""
Employee Management System

"""
import json

file_name = 'employee.json'

employees = []

id_counter = max([e['id'] for e in employees], default=0)

def menu():
    options = '''
                 1:Add Employee
                 2:View Employee
                 3:Search Employee
                 4:Update Employee
                 5:Delete Employee
                 6:Save To Json
                 7:Load from JSON
                 8:Exit   
    '''
    print("-" * 50)
    print("*****  Employee Management System  *****")
    print(options)
    print("-" * 50)

    try:
        choice = int(input("Enter Your Choice : ").strip())
        return choice

    except ValueError:
        print("Invalid!! Enter an Integer")
        return -1    
    

def add_employee():
    global id_counter

    print("-" * 50)
    print("    Employee Enrollment   ")
    print("-" * 50)

    name = input("Enter Employee Name : ").strip()
    if name == "":
        print("Name cannot be empty!!")
        return
    
    department = input("Enter the Name of the Department : ").strip()
    if department == "":
        print("Department Name cannot be empty!!")
        return
    
    try:
        salary = float(input("Enter the Salary : ").strip())

    except ValueError:
        print("Enter a Numeric Value!!")
        return

    if salary <= 0:
        print("Salary should be > 0")
        return


    employees.append(dict(id = id_counter + 1, name = name, department = department, salary = salary))
    print(f"Employee Data has been added Successfully with employee id {id_counter}")

    id_counter += 1    

def view_employee():

    if not employees:
        print("No Employee Found in the System, Please Add It")
        return

    view_many_employees(employees)   

def view_one_employee(employee):
    print("-" * 50)
    print("    Employee Details   ")
    print("-" * 50)

    print(f"ID:         {employee['id']}")
    print(f"Name:       {employee['name']}")
    print(f"Department: {employee['department']}")
    print(f"Salary:     {employee['salary']}")

    print("-" * 50)


def view_many_employees(employees):
    print("*" * 60)
    print("*****  Employee Management System  *****")
    print("*" * 60)

    print(f"{'id':^5}{'name':<20}{'department':>15}{'salary':^10}")

    for employee in employees:
        print(f"{employee['id']:^5}{employee['name']:<20}{employee['department']:>15}{employee['salary']:^10}")

    print("*" * 60)    


def search_by_id(e_id):
    for employee in employees:
        if employee["id"] == e_id:
            view_one_employee(employee)
            return employee

    return None       

def search_by_name():
    name = input("Enter the Employee Name To Search").strip()
    if name == "":
        print("Search Name cannot be Empty!!")
        return

    result = [e for e in employees if e['name'].lower() == name.lower()]

    if not result:
        print(f"No Employee Found with Name {name}")
        return
    
    view_many_employees(result)


def search_by_dept():
    dept = input("Enter the Department Name To Search").strip()
    if dept == "":
        print("Search Name cannot be Empty!!")
        return

    result = [e for e in employees if e['department'].lower() == dept.lower()]

    if not result:
        print(f"No Employee Found with Name {dept}")
        return
    
    view_many_employees(result)    





def search_employee():
    print("  Student Management System  ")
    print("How Would you like to Search Employee ")
    print(" 1: Search By Employee ID")
    print(" 2: Search by Name ")
    print(" 3: Search by Department ")

    try:
        choice = int(input("Enter your Choice : ").strip())

    except ValueError:
        print("Enter a Numeric Value!!")
        return

    if choice == 1:
        e_id = int(input("Enter the Employee ID To Search ").strip())
        search_by_id(e_id)
    elif choice == 2:
        search_by_name()
    elif choice == 3:
        search_by_dept()
    else:
        print("Invalid Option ")
        return                

def update_employee():
    try:
        e_id = int(input("Enter the id To Update the employee : ").strip())
        
    except ValueError:
        print("Enter a Numeric Value!!")
        return    

    employee = search_by_id(e_id)

    if employee == None:
        print(f"No employee Found with {e_id} ")
        return
    
    print("\nCurrent Employee Information:")
    view_one_employee(employee)

    name = input("Enter the Name To be Updated [Press Enter To Keep Same Name] : ").strip()

    if name != "":
        employee['name'] = name    

    dept = input("Enter the Department Name To be Updated [Press Enter To Keep Same Name] :").strip() 

    if dept != "":
        employee['department'] = dept

    
    sal = float(input("Enter the Salary to be Updated [Press Enter To Keep Same Salary : ]").strip())
    if sal != "":
        try:
            sal = float(sal)
        except ValueError:
            print("Salary should be Numeric")
            return

        if sal <= 0:
            print("Salary should be > 0")
            return

        employee["salary"] = sal          
    
    


    print("Employee Data has been Update Successfully")
    view_one_employee(employee)    

def delete_employee():
    try:
        e_id = int(input("Enter the id To Delete the employee : ").strip())
        
    except ValueError:
        print("Enter a Numeric Value!!")
        return    

    employee = search_by_id(e_id)

    if employee == None:
        print(f"No employee Found with {e_id} ")
        return
    
    print("\nCurrent Employee Information:")
    view_one_employee(employee)

    print("Are You Sure You want To Delet this Employee")
    choice = input("Enter y/n :").strip().lower()

    if choice == 'y':
        employees.remove(employee)
    elif choice == 'n':
        print("Employee Deletion Aborted...")
        return
    else:
        print("Employee Deletion Aborted...")
        return    

def save_to_json():
    
    try:
        with open(file_name, "w") as file:
            json.dump(employees, file, indent=4)

        print("Employee data saved successfully.")

    except OSError:
        print("Error while saving the file.")

def load_from_json():
    global employees

    try:
        with open(file_name, "r") as file:
            employees = json.load(file)

        print("Employee data loaded successfully.")

    except FileNotFoundError:
        print("File not found.")          

def main():
    while True:
        choice = menu()
        if choice == 1:
            add_employee()
        elif choice == 2:
            view_employee()
        elif choice == 3:
            search_employee()
        elif choice == 4:
            update_employee()
        elif choice == 5:
            delete_employee()
        elif choice == 6:
            save_to_json()
        elif choice == 7:
            load_from_json()
        elif choice == 8:
            print("Application Termination Successful. Good Bye!!")
            break
        else:
            print("Invalid Input !!")
            



if __name__ == "__main__":
    main()        
    

