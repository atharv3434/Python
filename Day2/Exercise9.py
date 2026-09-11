"""
Exercise 9: Longest Palindromic Substring

Write a program that prompts the user to enter a text string and finds
the longest substring within it that reads the same forward and backward.

If there are multiple palindromic substrings of the same maximum length,
print any one of them.
"""

def main():
    text = input("Enter a Text : ").lower().strip()

    if not text:
        print("Enter Correct Text")
        return

    longest = ""

    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):

            sub_string = text[start:end]

            if sub_string == sub_string[::-1]:

                if len(sub_string) > len(longest):
                    longest = sub_string

    print("Longest Palindromic Substring :", longest)


main()