"""

Exercise 9: The Josephus Elimination Game
Scenario: A group of N soldiers (numbered 1 to N) stand in a circle. 
Starting from the first soldier, every K-th soldier is eliminated from the circle. 
The count continues with the next remaining soldier, moving clockwise. 
This process repeats until only one soldier remains. 
Write a program that prompts the user to enter N(number of soldiers) and 
K(elimination interval). 
Simulate the game using a list and print the order of eliminations and the final survivor.

Sample Input: N = 5, K = 2
Sample Output:
Soldier circle initialized: [1, 2, 3, 4, 5]
Eliminated soldier: 2 (Remaining: [1, 3, 4, 5])
Eliminated soldier: 4 (Remaining: [1, 3, 5])
Eliminated soldier: 1 (Remaining: [3, 5])
Eliminated soldier: 5 (Remaining: [3])
The sole survivor is: 3


"""

def main():
    try:
        n = int(input("Enter the nth Number of Soldier : ").strip())
        k = int(input("Enter the kth Number of Soldier to be Eliminated : ").strip())

    except ValueError:
        print("Enter a Numeric Value")
        return

    if n <= 0 or k <= 0:
        print("N and K must be greater than 0")
        return

    circle = []

    for i in range(1, n + 1):
        circle.append(i)

    print("Soldier circle initialized:", circle)

    index = 0

    while len(circle) > 1:

        index = (index + k - 1) % len(circle)

        eliminated = circle.pop(index)

        print(f"Eliminated soldier: {eliminated} (Remaining: {circle})")

    print("The sole survivor is:", circle[0])


if __name__ == '__main__':
    main()