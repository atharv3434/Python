"""
Product Inventory Management System

Create a product inventory system.

Each product:

{
    "id": 1,
    "name": "Laptop",
    "category": "Electronics",
    "price": 55000,
    "quantity": 10
}

Menu:

1. Add Product
2. View Products
3. Search Product
4. Update Product
5. Delete Product
6. Exit
Add Product

Validate:

Name not empty
Category not empty
Price > 0
Quantity >= 0
Search

Allow searching by:

ID
Product name

Name search should be case-insensitive.

Example:

Search: laptop

should find:

Laptop
LAPTOP
Gaming Laptop

"""

products =[
    {
    "id": 1,
    "name": "Laptop",
    "category": "Electronics",
    "price": 55000,
    "quantity": 10
},
]

id_counter = max([p["id"]for p in products], default = 0)

def menu():
    options = '''
                1. Add Product
                2. View Products
                3. Search Product
                4. Update Product
                5. Delete Product
                6. Exit
'''

    print("******  Product Inventory Management System  ******")
    print(options)

    try:
        choice = int(input("Enter your choice : ").strip())
        return choice
    except ValueError:
        print("Enter a Numeric Value!!")
        return -1
    

def add_product():
    global id_counter
    print("Add Details of the Product : ")

    name = input("Enter the Name of the Product : ").strip()
    if name == "":
        print("Name should not be Empty!!")
        return  

    category = input("Enter the Category of the Product : ").strip()
    if category == "":
        print("Category cannot be Empty!!")
        return

    try: 
        price = float(input("Enter the Price : ").strip())
        if price <= 0:
            print("Price should be > 0")
            return
        
    except ValueError:
        print("Price should be Numeric Value")
        return

    try: 
        quantity = int(input("Enter the Quantity of the Product : ")) 
        if quantity < 0 :
            print("Quantity must be >= 0 ")
            return

    except ValueError:
        print("Quantity should be Numeric!!")
        return

    products.append(dict(id = id_counter + 1, name = name, category = category, price = price, quantity = quantity))
    print("Product has been Added Successfully")

    id_counter += 1  


def view_products():

    
    if not products:
        print("No Products in the System, Add it...")
        return

    view_many_products(product)      


def view_one_product(p_id):

    if not products:
            print("No Items in the Product Management System, Add it First")
            return

    print("*******  Product Details  *******")  
    print(f"ID:               {p_id['id']}")
    print(f"Name:             {p_id['name']}")
    print(f"Category:         {p_id['category']}")
    print(f"Price:            {p_id['price']}")
    print(f"Quantity          {p_id['quantity']}")  
                            
def view_many_products(product):
    print("-" * 80)
    print("*******  Product Details  *******")
    print("-" * 80)

    print(f"{'ID':^5}{'Name':<20}{'Category':<15}{'Price':>15}{'Quantity':>10}")

    for p in products:
        print(f"{product['id']:^5}{product['name']:<20}{product['category']:<15}{product['price']:>15}{product['quantity']:>10}")

def search_product(p_id):
      
    result = [p for p in products if p['id'] == p_id]
    if not result:
        print(f"No Product Found with ID: {p_id}")
        return None
    
    view_one_product(result[0])
    return result[0]

def update_product():

    try:
        product_id = int(input("Enter the Product ID To Update: "))

        result = search_product(product_id)

        if result is None:
            print(f"No Product found for ID: {product_id}")
            return

        # Update Name
        u_name = input("Enter the Name: ").strip()

        if u_name != "":
            result['name'] = u_name
           

        # Update Category
        u_category = input("Enter the Category: ").strip()

        if u_category != "":
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

def delete_product():
    try:
        product_id = int(input("Enter the Product ID To Delete: "))

        result = search_product(product_id)

        if result is None:
            print(f"No Product found for ID: {product_id}")
            return
        
        products.remove(result)

    except ValueError:
        print("ID should be Numeric!!")
        return    


def main():

    while True:
        choice = menu()
        if choice == 1:
            add_product()
        elif choice == 2:
            view_products()
        elif choice == 3:
            try:
                p_id = int(input("Enter the product id : "))
                search_product(p_id)

            except ValueError:
                print("Enter a Numeric Value!!")
                return
        
        elif choice == 4: 
            update_product()
        elif choice == 5:
            delete_product()
        elif choice == 6:
            print("Exited Program Successfully")
            break
        else:
            print("Invalid Input!!")


main()            
                        







