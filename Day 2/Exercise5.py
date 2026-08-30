"""
Exercise 5: Custom Title Case Formatter
Write a program that accepts a string input from the user and outputs it in Title Case 
(capitalizing the first letter of each word and lowercasing the remaining letters). 
Do not use Python's built-in .title() method.

Sample Input: "WELCOME TO BANGALORE CITY"
Sample Output: "Welcome To Bangalore City"
"""

def main():
    sentence = input("Enter a Sentence : ").strip()

    if not sentence:
        print("")
        return

    words = sentence.split()
    formatted_words = []

    for word in words:
        formatted_word = word[0].upper() + word[1:].lower()
        formatted_words.append(formatted_word)

    result = " ".join(formatted_words)
    print(result)

main()