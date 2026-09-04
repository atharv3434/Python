"""
Product Inventory Management System
"""

products = [ 
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000.0, "quantity": 10}, 
    {"id": 3, "name": "Smartphone", "category": "Electronics", "price": 20000.0, "quantity": 25},
    {"id": 4, "name": "Smartphone", "category": "Electronics", "price": 17800.0, "quantity": 12},
    {"id": 5, "name": "Smartphone", "category": "Electronics", "price": 31000.0, "quantity": 3},
    {"id": 2, "name": "Chair", "category": "Furniture", "price": 1500.0, "quantity": 50},
    {"id": 6, "name": "Smartphone", "category": "Electronics", "price": 200000.0, "quantity": 2},
] 

# Set counter safely to the highest existing ID
i_counter = max([p["id"] for p in products], default=0)

#********************************************************************************************************************

def Menu():
    print("\n***** Product Inventory Management System *****")
    options = '''
                  1 : Add Product
                  2 : View all Product
                  3 : Search Product
                  4 : Update Product
                  5 : Delete Product
                  6 : Exit
'''
    print(options)
    try:
        choice = int(input("Enter your Choice : ").strip())
        return choice
    except ValueError:
        return -1


#********************************************************************************************************************

def add_product():
    global i_counter
    print("\n***** Add Product *****")

    try:
        name = input("Enter a Product Name : ").strip()
        if name == "":
            print("Name cannot be empty.")
            return
    
        category = input("Enter the Category : ").strip()
        if category == "":
            print("Category cannot be empty.")
            return
    
        price = float(input("Enter the Price : ").strip())
        if price <= 0:
            print("Price should be greater than zero.")
            return
    
        quantity = int(input("Enter the Quantity : ").strip())
        if quantity < 0:
            print("Enter Valid Quantity (>= 0).")
            return
        
    except ValueError:
        print("Please Retry with a Valid Numeric Value!!")
        return

    # Keep standard keys: "id" and "quantity" (lowercase)
    i_counter += 1
    new_product = {
        "id": i_counter,
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity
    }
    products.append(new_product)
    print(f"Product added successfully with ID #{i_counter}!")


#******************************************************************************************************************************************

def view_all_products(product_list):
    print("\n***** Product Inventory Management System *****")
    print("-" * 75)
    print(f"{'ID' :^5} {'Name' :<20} {'Category':<20} {'Price':>12} {'Quantity':>8}")
    print("-" * 75)
    # Loop over product_list argument, not the global products list
    for p in product_list:
        print(f"{p['id'] :^5} {p['name'] :<20} {p['category'] :<20} {p['price']:>12.2f} {p['quantity']:>8}")
    print("-" * 75)


#******************************************************************************************************************************************

def view_one_product(p):
    print("\n***** Product Details *****")
    print(f"ID       : {p['id']}")
    print(f"Name     : {p['name']}")
    print(f"Category : {p['category']}")
    print(f"Price    : {p['price']:.2f}")
    print(f"Quantity : {p['quantity']}")


#******************************************************************************************************************************************

def view_product():
    if len(products) > 1:
        view_all_products(products)
    elif len(products) == 1:
        view_one_product(products[0])
    else:
        print("No Products in the Inventory. Add it First To View.")


#******************************************************************************************************************************************

def search_by_id(p_id):
    result = [p for p in products if p['id'] == p_id]
    if not result:
        print(f"No Product Found with ID: {p_id}")
        return None
    
    view_one_product(result[0])
    return result[0]


#******************************************************************************************************************************************

def search_by_name():
    name = input("Enter the Name of the Product : ").strip()
    if name == "":
        print("Name should not be empty.")
        return

    # Case-insensitive substring match
    results = [p for p in products if name.lower() in p['name'].lower()]
    if not results:
        print(f"No Product Found with Name: '{name}'")
        return None
    
    if len(results) == 1:
        view_one_product(results[0])
    else:
        view_all_products(results)


#******************************************************************************************************************************************

def search_product():
    print("\nHow would you like to search the product:")
    print("1 : Search By ID")
    print("2 : Search by Name")

    try:
        option = int(input("Enter your Choice : ").strip())
        if option == 1:
            s_id = int(input("Enter the ID of the Product : ").strip())
            search_by_id(s_id)
        elif option == 2:
            search_by_name()
        else:
            print("This is an Invalid Choice!!")
    except ValueError:
        print("Invalid Option! Please enter a valid number.")


#******************************************************************************************************************************************
        
def update_data():
    try:
        product_id = int(input("Enter the Product ID To Update: "))

        result = search_by_id(product_id)

        if result is None:
            print(f"No Product found for ID: {product_id}")
            return

        # Update Name
        u_name = input("Enter the Name: ").strip()

        if u_name == "":
            pass
        else:
            result["name"] = u_name

        # Update Category
        u_category = input("Enter the Category: ").strip()

        if u_category == "":
            pass
        else:
            result["category"] = u_category

        # Update Price
        u_price = float(input("Enter the Price: "))

        if u_price <= 0:
            print("Invalid Price. Price must be greater than 0.")
            return
        else:
            result["price"] = u_price

        # Update Quantity
        u_quantity = int(input("Enter the Quantity: "))

        if u_quantity < 0:
            print("Invalid Quantity. Quantity cannot be negative.")
            return
        else:
            result["quantity"] = u_quantity

        print("Product updated successfully!")

    except ValueError:
        print("Wrong Input! Please enter a valid number.")


#******************************************************************************************************************************************
        
def del_product():
    try:
        del_id = int(input("Enter the product ID, which you want to Delete : "))
        result = search_by_id(del_id)

        if result is None:
                return
        
        print(result)
        final_res = input("Enter y to delete it permanently : ").strip().lower()

        if final_res == 'y':
            products.remove(result)
            print(f"Product #{del_id} deleted successfully.")
        else:
            print("Deletion has been Cancelled")  
        
    except ValueError:
        print("Invalid Input")    



    


#******************************************************************************************************************************************
def main():
    while True:
        result = Menu()
        
        if result == 1:
            add_product()
        elif result == 2:
            view_product()
        elif result == 3:
            search_product()
        elif result == 4:
            update_data()
        elif result == 5:
            del_product()
        elif result == 6:
            print("Exiting Product Inventory System. Goodbye!")
            break
        else:
            print("Invalid Selection! Enter a number between 1 and 6.")


main()