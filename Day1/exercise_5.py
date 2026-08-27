"""

### Exercise 5: Basic Operator Calculator
Create a program that takes two numbers and a math operator (`+`, `-`, `*`, `/`) from the user, performs the corresponding calculation, and prints the result.
* **Sample Input**: `num1=15`, `num2=3`, `operator='/'`
* **Sample Output**: `Result: 5.0`

"""

def main():
    n = int(input("Enter the First Number : "))
    m = int(input("Enter the Second Number : "))

    operator = input("What Operation you would like to have on these Operands.... ")

    if operator == '+':
        print(f"{n} + {m} = {n + m} ")
    elif operator == '-':
        print(f"{n} - {m} = {n - m} ")  
    elif operator == '*':
        print(f"{n} x {m} = {n * m} ")
    elif operator == '/':
        print(f"{n} / {m} = {n / m} ")
    else:
        print("Invalid Operator!! Try again")              


main()    