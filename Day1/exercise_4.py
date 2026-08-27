"""

### Exercise 4: Odd or Even Checker
Write a program that prompts the user for an integer and prints whether it is even or odd.
* **Sample Input**: `7`
* **Sample Output**: `7 is an Odd number.`

"""

def main():
    n = int(input("Enter a Positiv Number : "))

    if(n % 2 ==0):
        print(f"{n} is an Even Number")
    else:
        print(f"{n} is an Odd Number")

main()            