"""
Assignment1: Inventory Tracker for CDAC Bookstore
Scenario
The CDAC Bookstore needs a backend helper module to manage books and their quantities. 
The inventory is stored in a Python dictionary where keys are book titles(strings) and
values are quantities in stock(non-negativeintegers).

Problem Description

Write a function manage_bookstore_inventory(inventory, action, book_title,quantity=0) that handles inventory operations safely.

1.The action parameter can be one of three options:
"add", "sell", or "lookup" 

.2.Add Action("add"):
Add the specified quantity to the existing stock of book_title. If the book is not in the inventory dictionary,
add it as a new key with quantity as the value.

3.Sell Action("sell"):
Decrease the stock of book_title by the specified quantity. If the book is not found in the inventory,
print a message: Error : Book '<book_title>'not found in inventory. and make no changes.
(Do not let th program crash with a KeyError). If the requested quantity to sell exceed the stock available ,
print: Error : Insufficient stock for '<book_title>'. Available : <current_stock>. and make no changes.
If the stock reaches exactly 0 after a successful sale ,remove the book key from the inventory entirely.

4.Lookup Action("lookup"):
Lookup the stock quantity of book_title and return it. Use safe dictionary retrieval; if the book does not exist, 
return 0 without throwing a KeyError. The function must return the updated/current inventory dictionary.

Example Walkthrough 
# Initial Inventory
# inventory = {"Python Basics": 10, "Learning AI": 5}

# 1. Add Stock inventory = manage_bookstore_inventory(inventory, "add", "Python Basics", 5)
# Result: {"Python Basics": 15, "Learning AI": 5}

# 2. Sell Stock Safely (Missing Book)inventory = manage_bookstore_inventory(inventory, "sell", "Data Science101", 1)
# Console output: Error: Book 'Data Science 101' not found in inventory.

# 3. Sell Stock (Insufficient)inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 10)
# Console output: Error: Insufficient stock for 'Learning AI'. Available:5.

# 4. Sell Stock (Exactly Zero Stock)inventory = manage_bookstore_inventory(inventory, "sell", "Learning AI", 5)
# Result: {"Python Basics": 15}
"""


def manage_bookstore_inventory(inventory, action, book_title, quantity=0):

    if action == "add":

        if book_title in inventory:
            inventory[book_title] += quantity
        else:
            inventory[book_title] = quantity

    elif action == "sell":

        if book_title not in inventory:
            print(f"Error: Book '{book_title}' not found in inventory.")
            return inventory

        current_stock = inventory[book_title]

        if quantity > current_stock:
            print(f"Error: Insufficient stock for '{book_title}'. Available: {current_stock}.")
            return inventory

        inventory[book_title] -= quantity

        if inventory[book_title] == 0:
            del inventory[book_title]

    elif action == "lookup":

        stock = inventory.get(book_title, 0)
        print(f"Stock for '{book_title}': {stock}")

    else:
        print(f"Error: Invalid action '{action}'.")

    return inventory


def main():

    inventory = {
        "Python Basics": 10,
        "Learning AI": 5
    }

    inventory = manage_bookstore_inventory(
        inventory, "add", "Python Basics", 5
    )
    print(inventory)

    inventory = manage_bookstore_inventory(
        inventory, "sell", "Data Science 101", 1
    )
    print(inventory)

    inventory = manage_bookstore_inventory(
        inventory, "sell", "Learning AI", 10
    )
    print(inventory)

    inventory = manage_bookstore_inventory(
        inventory, "sell", "Learning AI", 5
    )
    print(inventory)

    inventory = manage_bookstore_inventory(
        inventory, "lookup", "Python Basics"
    )



main()