"""

Exercise 3: Email Domain Extractor
Write a program that prompts the user to enter an email address string. Extract the domain name (the part after the @) and print it. If the string is not a valid email (does not contain exactly one @), print "Invalid Email".

Sample Input: "vinod@vinod.co"
Sample Output: "vinod.co"
Sample Input: "vinod.co"
Sample Output: "Invalid Email"

"""


def main():
    email = input("Enter you email id : ")

    if email.count('@') != 1:
        print("Invalid Email")
        return

    # Split into username and domain parts
    parts = email.split('@')
    domain_name = parts[1]

    # Ensure there is actually a domain name after '@'
    if not domain_name:
        print("Invalid Email")
        return

    print(domain_name)


main()    