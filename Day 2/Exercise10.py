"""
Exercise 10: Run-Length String Compression
Write a program that prompts the user to enter a text string and 
compresses it using run-length encoding 
(listing character counts next to each repeated character). 
If the compressed string is not smaller in size than the original string, 
print the original string.

Sample Input: "aabcccccaaa"
Sample Output: "a2b1c5a3"
Sample Input: "abcd"
Sample Output: "abcd" (since "a1b1c1d1" is longer than "abcd")
"""

def main():
    text = input("Enter the Text Please : ").strip()

    # Edge case: Empty input
    if not text:
        print("")
        return

    compressed_parts = []
    current_char = text[0]
    count = 1

    # Traverse from index 1 to the end
    for i in range(1, len(text)):
        if text[i] == current_char:
            count += 1
        else:
            compressed_parts.append(f"{current_char}{count}")
            current_char = text[i]
            count = 1

    # Append the final sequence
    compressed_parts.append(f"{current_char}{count}")
    compressed_text = "".join(compressed_parts)

    # Output compressed only if strictly smaller in size
    if len(compressed_text) < len(text):
        print(compressed_text)
    else:
        print(text)


if __name__ == "__main__":
    main()