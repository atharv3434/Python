# import os

# FILEPATH = "catalog.txt"

# # ----------------- DEFENSIVE INPUT HELPERS -----------------
# def get_non_empty_string(prompt: str) -> str:
#     while True:
#         value = input(prompt).strip()
#         if value:
#             return value
#         print("Error: Input cannot be blank. Please re-enter.")

# def get_valid_float(prompt: str, min_val: float = 0.01) -> float:
#     while True:
#         try:
#             val = float(input(prompt).strip())
#             if val >= min_val:
#                 return val
#             print(f"Error: Value must be at least {min_val}.")
#         except ValueError:
#             print("Error: Invalid input. Please enter a valid numerical value.")

# def get_valid_int(prompt: str, min_val: int = 0) -> int:
#     while True:
#         try:
#             val = int(input(prompt).strip())
#             if val >= min_val:
#                 return val
#             print(f"Error: Number must be at least {min_val}.")
#         except ValueError:
#             print("Error: Invalid input. Please enter a whole number.")

# # ----------------- CORE CRUD OPERATIONS -----------------
# def add_entry(catalog: list[dict], next_id: int) -> int:
#     print("\n--- Add New Record ---")
#     title = get_non_empty_string("Enter Title/Name: ")
#     category = get_non_empty_string("Enter Category/Author: ")
#     price = get_valid_float("Enter Price (> 0): ", min_val=0.01)
#     quantity = get_valid_int("Enter Quantity (>= 0): ", min_val=0)

#     record = {
#         "id": next_id,
#         "title": title,
#         "category": category,
#         "price": price,
#         "quantity": quantity
#     }
#     catalog.append(record)
#     print(f"Success: Record created with ID #{next_id}")
#     return next_id + 1

# def render_catalog(catalog: list[dict]) -> None:
#     if not catalog:
#         print("\n[Alert] The catalog is currently empty.")
#         return

#     # Edge-case requirement: Key-value card for 1 record, table for > 1
#     if len(catalog) == 1:
#         item = catalog[0]
#         print("\n" + "="*40)
#         print("         SINGLE RECORD INSPECTION CARD    ")
#         print("="*40)
#         print(f"  ID        : {item['id']}")
#         print(f"  Title     : {item['title']}")
#         print(f"  Category  : {item['category']}")
#         print(f"  Price     : {item['price']:.2f}")
#         print(f"  Quantity  : {item['quantity']}")
#         print("="*40)
#         return

#     print("\n" + "="*75)
#     print(f"{'ID':<6}{'Title':<30}{'Category':<20}{'Price':<10}{'Quantity':<8}")
#     print("-" * 75)
#     for r in catalog:
#         print(f"{r['id']:<6}{r['title']:<30}{r['category']:<20}{r['price']:<10.2f}{r['quantity']:<8}")
#     print("=" * 75)

# def query_records(catalog: list[dict], search_term: str) -> list[dict]:
#     search_term = search_term.strip().lower()
#     matches = []
#     for r in catalog:
#         # Match numeric ID or substring match on string fields
#         if str(r['id']) == search_term or search_term in r['title'].lower() or search_term in r['category'].lower():
#             matches.append(r)
#     return matches

# def modify_entry(catalog: list[dict], record_id: int) -> bool:
#     for r in catalog:
#         if r['id'] == record_id:
#             print(f"Modifying Record: {r['title']}")
#             r['price'] = get_valid_float("Enter New Price: ", min_val=0.01)
#             r['quantity'] = get_valid_int("Enter New Quantity: ", min_val=0)
#             return True
#     return False

# def delete_entry(catalog: list[dict], record_id: int) -> bool:
#     for i, r in enumerate(catalog):
#         if r['id'] == record_id:
#             confirm = input(f"Are you sure you want to delete '{r['title']}'? (y/n): ").strip().lower()
#             if confirm == 'y':
#                 catalog.pop(i)
#                 return True
#             else:
#                 print("Deletion aborted.")
#                 return False
#     return False

# # ----------------- FLAT-FILE PERSISTENCE -----------------
# def sync_catalog_to_file(filepath: str, catalog: list[dict]) -> None:
#     try:
#         with open(filepath, "w", encoding="utf-8") as f:
#             for r in catalog:
#                 line = f"{r['id']}|{r['title']}|{r['category']}|{r['price']:.2f}|{r['quantity']}\n"
#                 f.write(line)
#         print(f"Catalog successfully saved to {filepath}.")
#     except Exception as e:
#         print(f"Error saving to file: {e}")

# def load_catalog_from_file(filepath: str) -> tuple[list[dict], int]:
#     records = []
#     max_id = 0
#     if not os.path.exists(filepath):
#         print(f"Info: {filepath} not found. Starting with empty catalog.")
#         return records, 1

#     try:
#         with open(filepath, "r", encoding="utf-8") as f:
#             for line_no, line in enumerate(f, 1):
#                 clean_line = line.strip()
#                 if not clean_line:
#                     continue
#                 parts = clean_line.split("|")
#                 if len(parts) != 5:
#                     print(f"Warning: Skipping corrupted line {line_no}")
#                     continue
                
#                 rec_id = int(parts[0])
#                 records.append({
#                     "id": rec_id,
#                     "title": parts[1],
#                     "category": parts[2],
#                     "price": float(parts[3]),
#                     "quantity": int(parts[4])
#                 })
#                 if rec_id > max_id:
#                     max_id = rec_id

#         print(f"Loaded {len(records)} records from {filepath}.")
#         return records, max_id + 1
#     except (ValueError, FileNotFoundError) as e:
#         print(f"Error reading {filepath}: {e}")
#         return [], 1

# # ----------------- CONTROLLER LOOP -----------------
# def main():
#     catalog, next_id = load_catalog_from_file(FILEPATH)

#     while True:
#         print("\n=== FLAT-FILE MANAGEMENT SYSTEM ===")
#         print("1. Add Record")
#         print("2. View Catalog")
#         print("3. Search Records")
#         print("4. Update Record")
#         print("5. Delete Record")
#         print("6. Save to File")
#         print("7. Load from File")
#         print("8. Exit")

#         choice = input("Select an option (1-8): ").strip()

#         if choice == "1":
#             next_id = add_entry(catalog, next_id)
#         elif choice == "2":
#             render_catalog(catalog)
#         elif choice == "3":
#             term = get_non_empty_string("Enter ID or keyword to search: ")
#             results = query_records(catalog, term)
#             render_catalog(results)
#         elif choice == "4":
#             target_id = get_valid_int("Enter Record ID to update: ")
#             if modify_entry(catalog, target_id):
#                 print("Record updated successfully.")
#             else:
#                 print("Error: Record ID not found.")
#         elif choice == "5":
#             target_id = get_valid_int("Enter Record ID to delete: ")
#             if delete_entry(catalog, target_id):
#                 print("Record deleted successfully.")
#             else:
#                 print("Error: Record ID not found.")
#         elif choice == "6":
#             sync_catalog_to_file(FILEPATH, catalog)
#         elif choice == "7":
#             catalog, next_id = load_catalog_from_file(FILEPATH)
#         elif choice == "8":
#             print("Exiting application. Goodbye!")
#             break
#         else:
#             print("Invalid selection! Please enter a number between 1 and 8.")

# if __name__ == "__main__":
#     main()



products = [ 
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 55000, "quantity": 10}, 
    {"id": 3, "name": "Smartphone", "category": "Electronics", "price": 20000, "quantity": 25} ,
    {"id": 4, "name": "Smartphone", "category": "Electronics", "price": 17800, "quantity": 12} ,
    {"id": 5, "name": "Smartphone", "category": "Electronics", "price": 31000, "quantity": 3} ,
    {"id": 2, "name": "Chair", "category": "Furniture", "price": 1500, "quantity": 50} ,
    {"id": 6, "name": "Smartphone", "category": "Electronics", "price": 200000, "quantity": 2} ,
] 

id_counter = len(products)

#-------------------------------------------------------------------------------------

def menu():
    menu_text = '''1. Add Product 
2. View All Products 
3. Search Product 
4. Update Product 
5. Delete Product 
6. Exit '''

    print('**** Product Inventory Management System ****')
    print(menu_text)
    try:
        choice = int(input('Enter your choice: '))
    except:
        choice = -1

    return choice

#-------------------------------------------------------------------------------------


def add_product():
    global id_counter
    try:
        print('**** Add new product details ****')
        name = input('Name: ').strip()
        if name == '':
            print('Name cannot be empty!')
            return
        
        category = input('Category: ').strip()
        if category == '':
            print('Category cannot be empty!')
            return
        
        price = float(input('Price: '))
        if price <= 0:
            print('Price must be > 0')
            return

        quantity = int(input('Quantity: '))
        if quantity < 0:
            print('Quantity must be >= 0')
            return

        products.append(dict(id=id_counter+1, name=name, category=category, price=price, quantity=quantity))
        id_counter += 1

    except ValueError:
        print('Please retry with a numerical value')

#-------------------------------------------------------------------------------------

def print_one_product(p):
    pid, name, category, price, quantity = p.values()
    print('---- Product Details ----')
    print(f'ID          : {pid}')
    print(f'Name        : {name}')
    print(f'Category    : {category}')
    print(f'Price       : {price}')
    print(f'Quantity    : {quantity}')
    print('-'*50)    

#-------------------------------------------------------------------------------------

def print_many_products(product_list):
    print('-'*60)
    print(f'{'ID':^5}{'Name':<20}{'Category':<20}{'Price':>10}{'Qty':>5}')
    print('-'*60)
    for p in product_list:
        pid, name, category, price, quantity = p.values()
        print(f'{pid:^5}{name:<20}{category:<20}{price:>10.2f}{quantity:>5}')
    print('-'*60)

#-------------------------------------------------------------------------------------

def view_products():
    if len(products) == 0:
        print("No products in the inventory. Please add first.")
    elif len(products) == 1:
        print_one_product(products[0])
    else:
        print_many_products(products)

#-------------------------------------------------------------------------------------

def search_product():
    try:
        print('1. Search by id')
        print('2. Search by name')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            pid = int(input('Enter the id of the product to search: '))
            search_product_by_id(pid)
        elif choice == 2:
            search_product_by_name()
        else:
            print('Invalid choice. Please try again.')
    except:
        print('Please try again with an integer input.')

#-------------------------------------------------------------------------------------
def search_product_by_id(pid):
    result = [p for p in products if p['id']==pid]
    if not result:
        print(f'No product found for id {pid}')
        return None

    print_one_product(result[0])
    return result[0]
#-------------------------------------------------------------------------------------
def search_product_by_name():
    name = input('Enter the name of the product to search: ')
    result = [p for p in products if p['name']==name]
    if not result:
        print(f'No product found for name "{name}"')
        return

    if len(result) == 1:
        print_one_product(result[0])
    else:
        print_many_products(result)
#-------------------------------------------------------------------------------------
def delete_product():
    try:
        pid = int(input('Enter id of the product to delete: '))
        p = search_product_by_id(pid)
        if p is None:
            return

        ans = input('Are you sure to delete this product? (y/n): ').lower()

        if ans == 'y':
            products.remove(p)
            print('Product deleted successfully!')
        
    except:
        print('Invalid type of value for product id. Try again with an integer.')
#-------------------------------------------------------------------------------------
def main():
    while True:
        choice = menu()

        match choice:
            case 1:
                add_product()
            case 2:
                view_products()
            case 3:
                search_product()
            case 4:
                ...
            case 5:
                delete_product()
            case 6:
                break
            case _:
                print('Invalid choice. Please retry.')


if __name__ == '__main__':
    main()