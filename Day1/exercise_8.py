"""

Exercise 8: Score to Grade Converter
Write a script that takes a numeric test score from the user (0 to 100) and displays a corresponding letter grade based on the following scale:

90-100: A
80-89: B
70-79: C
60-69: D
Below 60: F

"""

def main():
    marks = int(input("Please Enter the Marks you have Scored : "))

    if marks < 0 or marks > 100:
        print("Invalid Score. Please enter a score between 0 and 100.")
    elif marks >= 90:
        print("Congratulations! You have scored a Grade A.")
    elif marks >= 80:
        print("Congratulations! You have scored a Grade B.")
    elif marks >= 70:
        print("You have scored a Grade C.")
    elif marks >= 60:
        print("You have scored a Grade D.")
    else:
        print("Better Luck Next Time, you have got a Grade F.")       




main()    