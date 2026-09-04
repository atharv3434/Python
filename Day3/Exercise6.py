"""
Exercise 6: Grading on a Curve
Scenario: A professor wants to adjust exam grades. 
Prompt the user to enter a list of space-separated test scores. 
Convert them to a list of integers. Using a single list comprehension with conditionals,
apply the following curve rules:

If a score is below 50, add 10 points.
If a score is 50 or higher, add 5 points.
The maximum possible score is capped at 100 (e.g., a score of 98 becomes 100, not 103).
Print the original and the curved grades.
Sample Input: "45 88 30 98 50"
Sample Output:
Original: [45, 88, 30, 98, 50]
Curved: [55, 93, 40, 100, 55]
"""

def main():
    # 1. Read input and convert each space-separated value into an integer
    original = [int(x) for x in input("Enter the Numbers: ").strip().split()]

    # 2. Single list comprehension applying conditions and capping at 100
    curved = [
        min(100, score + 10) if score < 50 else min(100, score + 5)
        for score in original
    ]

    # 3. Print the results
    print(f"Original: {original}")
    print(f"Curved: {curved}")


if __name__ == "__main__":
    main()