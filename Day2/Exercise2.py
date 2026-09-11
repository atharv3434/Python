"""

Exercise 2: Reversed Uppercased String
Write a program that takes a string input from the user, reverses the string, converts the entire reversed string to uppercase, and prints the result.

Sample Input: "Bangalore"
Sample Output: "EROLAGNAB"

"""

def main():
    string = input("Enter a Word : ").upper()
    reversed_upper = string[::-1].upper()
    print(reversed_upper)


main()