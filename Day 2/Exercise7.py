"""
Exercise 7: Manual Substring Counter
Write a program that prompts the user to enter a main text string and a substring.
Count how many times the substring appears in the main string without using Python's built-in .count() method.

Sample Input: (User inputs main string "banana" and substring "an")
Sample Output: 2
"""

def main():
    text = input("Enter a Word or Sentence: ").strip().lower()
    sub_string = input("Enter a substring: ").strip().lower()

    if not text or not sub_string:
        print("Invalid Input!")
        return

    sub_len = len(sub_string)
    count = 0

    # Slide across the string up to the point where the remaining slice fits the substring length
    for i in range(len(text) - sub_len + 1):
        if text[i : i + sub_len] == sub_string:
            count += 1

    print(f"Sample Output: {count}")


main()