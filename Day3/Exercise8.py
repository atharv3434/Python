"""
Exercise 8: De-duplicating Shopping Cart
Scenario: An online shopping cart has duplicate items due to double-clicks: 
["apple", "banana", "apple", "orange", "banana", "banana"]. 
Write a program that processes the list and removes all duplicate items, 
but keeps the first occurrence of each item in its original order. 
Print the cleaned cart.

Hardcoded Input: cart = ["apple", "banana", "apple", "orange", "banana", "banana"]
Sample Output: ['apple', 'banana', 'orange']


"""

def main():

    cart = ["apple", "banana", "apple", "orange", "banana", "banana"]

    new_cart = []
    # result = [c for c in cart if c not in new_cart  ]
    for c in cart:
        if c not in new_cart:
            new_cart.append(c)

    # new_cart.append(result)
    # print(new_cart)
    print(new_cart)



if __name__ == '__main__':
    main()    