"""
Exercise 8: Name Anonymizer
Write a program that prompts the user to enter a full name 
(first name, middle name, last name) and anonymizes it. 
The output should print the initials of the first and middle names followed by the full last name. 
If the name consists of only a single word, print it as-is.

Sample Input: "Vinod Kumar Kayartaya"
Sample Output: "V. K. Kayartaya"
Sample Input: "Bangalore"
Sample Output: "Bangalore"

"""

def main():
    name = input("Enter Your Full Name : ").strip()

    if not name:
        print("Enter Correct Name")
        return

    parts = name.split()

    if len(parts) == 1:
        print(parts[0])
        return

    initials = [f"{word[0].upper()}." for word in parts[:-1]]
    last_name = parts[-1].capitalize()


    result = " ".join(initials) + " " + last_name
    print(result)
                
                

main()    

