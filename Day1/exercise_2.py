"""
### Exercise 2: Fibonacci Sequence Generator
Write a Python script to print the first N terms of the Fibonacci sequence, where N is provided by the user.
* **Fibonacci sequence**: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
* **Sample Input**: N = 6
* **Sample Output**: 0, 1, 1, 2, 3, 5
"""

def main():
    n = int(input("Enter a Number : "))

    a = 0
    b = 1

    for i in range(n):
        if i == n - 1:
            print(a)
        else:
            print(a, end=", ")
        
        c = a + b
        a = b
        b = c

main()