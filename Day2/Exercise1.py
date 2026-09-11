"""

Exercise 1: Sentence Analysis (Character & Word Count)
Write a Python program that prompts the user to enter a sentence. The program must count and display:

The total number of characters (including spaces and punctuation).
The total number of words.
Sample Input: "Learning Python is fun!"
Sample Output:
Total Characters: 23
Total Words: 4

"""

def main():
    sent = input("Enter a Sentence: ")
    
    total_characters = len(sent)
    total_words = len(sent.split())
    
    print(f"Total Characters: {total_characters}")
    print(f"Total Words: {total_words}")


main()    