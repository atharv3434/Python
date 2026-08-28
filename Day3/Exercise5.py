"""
Exercise 5: The Spy's Word Reverser

Scenario: A secret agent wants to send an encrypted message.
The encryption rule is simple: reverse every word in the sentence,
but keep the order of words unchanged.

Sample Input:  "Meet me at midnight"
Sample Output: "teeM em ta thgindim"
"""

def main():
    sentence = input("Enter the secret message: ")

    # 1. sentence.split() breaks sentence into a list of words: ['Meet', 'me', 'at', 'midnight']
    # 2. [word[::-1] for word in ...] reverses each individual word using string slicing [::-1]
    # 3. " ".join(...) joins the reversed words back into a single string with spaces
    encrypted_message = " ".join([word[::-1] for word in sentence.split()])

    print(encrypted_message)


if __name__ == "__main__":
    main()