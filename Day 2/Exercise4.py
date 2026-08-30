"""

Exercise 4: Vowel & Consonant Frequency
Write a program that prompts the user to enter a string and counts:

The individual frequency of each vowel (a, e, i, o, u), case-insensitively.
The total count of all consonants.
Sample Input: "Vinod Kumar Kayartaya"
Sample Output:
Vowel Frequencies:
a: 4
e: 0
i: 1
o: 1
u: 1
Total Consonants: 12

"""

def main():
    text = input("Enter a String Please : ").lower()
    vowels = {'a' : 0, 'e' : 0, 'i' : 0, 'o' : 0, 'u': 0}
    consonants = 0

    for char in text:
        if char in vowels:
            vowels[char] += 1
        elif char.isalpha():
            consonants += 1    

    print("Vowel Frequencies:")
    for v, count in vowels.items():
        print(f"{v}: {count}")

    print(f"Total Consonants: {consonants}")
    

main()    