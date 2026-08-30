"""
Exercise 6: Shift Cipher Encrypter
Write a program that prompts the user for a text string and a shift integer,
and encrypts the text using a Caesar cipher. 
It should shift each alphabetical character in the string by the specified shift number down the alphabet.
Maintain uppercase and lowercase characters, and leave spaces or punctuation marks completely unchanged.

Sample Input: (User inputs string "Vinod" and shift 3)
Sample Output: "Ylqrg"

"""

def main():
    text = input("Enter your message: ")
    shift = int(input("Enter shift value (e.g., 3): "))

    # 1. ENCRYPTION
    encrypted_chars = []
    for char in text:
        if char.isupper():
            # Shift uppercase letter within 'A' - 'Z'
            shifted = (ord(char) - ord('A') + shift) % 26 + ord('A')
            encrypted_chars.append(chr(shifted))
        elif char.islower():
            # Shift lowercase letter within 'a' - 'z'
            shifted = (ord(char) - ord('a') + shift) % 26 + ord('a')
            encrypted_chars.append(chr(shifted))
        else:
            # Keep spaces, numbers, and punctuation unchanged
            encrypted_chars.append(char)

    encrypted_text = "".join(encrypted_chars)

    # 3. OUTPUT
    print("\n--- RESULT ---")
    print(f"Original Text  : {text}")
    print(f"Encrypted Text : {encrypted_text}")

if __name__ == "__main__":
    main()