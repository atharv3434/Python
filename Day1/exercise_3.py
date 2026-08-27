"""

### Exercise 3: Prime Number Checker
Write a program that checks whether a positive integer entered by the user is a prime number.
* **Logic**: A prime number is a number greater than 1 that has no positive divisors other than 1 and itself.
* **Sample Input**: `17`
* **Sample Output**: `17 is a prime number.`

"""

def main():
    n = int(input("Enter a Positiv Integer : "))

    if(n < 2):
        print(f"{n} is not a prime Number")
        return 0


    for i in range(2,n//2 +1):
        if(n % i == 0):
            print("This is not an prime Number")
            return
           
    print("This is an Prime Number")       

main()