"""

Exercise 7: Multiplication Table Generator
Write a program that takes an integer from the user and prints its multiplication table from 1 to 10.

Sample Input: 5
Sample Output:
5 x 1 = 5
5 x 2 = 10
...
5 x 10 = 50

"""

def main():
    n = int(input("Enter the Number for Generating Table : "))
    if(n < 1):
        print("Enter a Positiv Number")
        return
    
    for i in range(1,10):
        print(f"{n} x {i} = {n * i}")




main()    