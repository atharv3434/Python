# """

# DELIMITED FLAT-FILE CATALOG MANAGEMENT SYSTEM

# """

# books = [
#     {'id': 1, 'title': 'Python Programming', 'author': 'John Zelle', 'genre': 'Technical', 'price': 650.00, 'copies': 15},
#     {'id': 2, 'title': 'Clean Code', 'author': 'Robert Martin', 'genre': 'Technical', 'price': 950.00, 'copies': 8},
#     {'id': 3, 'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'genre': 'Fiction', 'price': 350.00, 'copies': 20},
#     {'id': 4, 'title': 'Sapiens', 'author': 'Yuval Noah Harari', 'genre': 'History', 'price': 550.00, 'copies': 12},
#     {'id': 5, 'title': 'Cosmos', 'author': 'Carl Sagan', 'genre': 'Science', 'price': 480.00, 'copies': 6}
# ]

# id_counter = len(books)

# # ***********************************************************************************************************
# def menu():

#     options = '''
#                   1:Add Book
#                   2:View Catlog
#                   3:Search Books
#                   4:Update Details
#                   5:Delete Book
#                   6:Save To File
#                   7:Load from File
#                   8:Exit
# '''

#     print(" *****  DELIMITED FLAT-FILE CATALOG MANAGEMENT SYSTEM  ***** ")
#     print(options)

#     try:
#         choice = int(input("Enter Your Choice : ").strip())
#         return choice
#     except ValueError:
#         print("Invalid Input!!")
#         return -1


# # ***********************************************************************************************************
# def add_book():
#     print(" Add Book Details ")    

#     global id_counter

#     title = input("Enter the Name of the Book : ").strip()
#     if title == "":
#         print("Error! Book Name cannot be empty ")
#         return
    
#     author = input("Enter Author Name : ").strip()
#     if author == "":
#         print("Error! Author Name cannot be empty ")
#         return
    
#     genre = input("Enter Genre Name : ").strip()
#     if genre == "":
#         print("Error! Genre Name cannot be empty ")
#         return
    
#     try:
#         price = float(input("Enter the Price of the Book : ").strip())
#         if price <= 0.0:
#             print("Price must be greater than 0.0!!")
#             return
        
#         copies = int(input("Enter the Number of Copies : ").strip())
#         if copies < 0:
#             print("Number of Copies should be >= 0")
#             return
        
#     except ValueError:
#         print("Enter a Valid Numeric Value!!")
#         return

#     books.append(dict(id = id_counter + 1, title = title, author = author, genre = genre, price = price, copies = copies)) 
#     print("Book Details has been Added Successfully....")  

#     id_counter += 1 
# # ***********************************************************************************************************    
# def view_books():
    
#     if len(books) == 0:
#         print("No Books in the System, Add it!!")
#         return
#     elif len(books) == 1:
#         view_one_book(books[0])
#     else:
#         view_all_books(books)     

# # ***********************************************************************************************************    
# def view_one_book(b):
#     print(" *****  DELIMITED FLAT-FILE CATALOG MANAGEMENT SYSTEM  ***** ")
#     print("Books Available Currently")
#     print(f"ID                 :{b['id']}")
#     print(f"Book Title         :{b['title']}")
#     print(f"Author Name        :{b['author']}")
#     print(f"Genre              :{b['genre']}")
#     print(f"Price              :{b['price']:.2f}")
#     print(f"Copies             :{b['copies']}")

# # ***********************************************************************************************************    
    
# def view_all_books(books):
#     print(" *****  DELIMITED FLAT-FILE CATALOG MANAGEMENT SYSTEM  ***** ")
#     print("-" * 80)
#     print(f"{'ID':^5} {'Book Title':<25} {'Author Name':<20} {'Genre':>10} {'Price':>10} {'Copies':>8}")
#     print("-" * 80)

#     for b in books:
#         print(f"{b['id']:^5} {b['title']:<25} {b['author']:<20} {b['genre']:>10} {b['price']:>10.2f} {b['copies']:>8}")

# # ***********************************************************************************************************    
# def search_books():
#     print(" How would you like To Search Books ")   
#     print("1 : Search Book By Book id ")
#     print("2 : Search Book By Book Name ")
#     print("3 : Search Book By Book Author ")       

#     try:
#         choice = int(input("Enter your Choice : ").strip())
#         if choice == 1:
#             id = int(input("Enter the Book id : ").strip())
#             search_by_id(id)
#         elif choice == 2:
#             search_by_name()
#         elif choice == 3:
#             search_by_author()
#         else:
#             print("Invalid Option Entered")    

#     except ValueError:
#         print("Invalid Choice Entered!!! ")
#         return    


# # ***********************************************************************************************************    
# def search_by_id(id):
#     result = [b for b in books if b['id'] == id]

#     if not result:
#         print(f"No Books found with {id}")
#         return None
#     else:
#         view_one_book(result[0])
#         return result[0]

               
# # ***********************************************************************************************************   
# def search_by_name():
#     name = input("Enter the Name of the Book : ").strip()
#     if name == "":
#         print("Error! Name cannot be Empty...")
#         return
    
#     result = [b for b in books if name.lower() in b['title'].lower()]

#     if not result:
#         print(f"No Books found with Author Name {name}")
#         return None
#     else:
#         if len(result) == 1:
#             view_one_book(result[0])
#         else:
#             view_all_books(result)


# # ***********************************************************************************************************               
# def search_by_author():
#     author = input("Enter the Name of the Author : ").strip()
#     if author == "":
#         print("Error! Author Name cannot be Empty...")
#         return
    

#     result = [b for b in books if author.lower() in b['author'].lower()]

#     if not result:
#         print(f"No Books found with Name {author}")
#         return None
#     else:
#         if len(result) == 1:
#             view_one_book(result[0])
#         else:
#             view_all_books(result)


# # ***********************************************************************************************************                 
            
# def update_book():
#     try:
#         id = int(input("Enter the Book ID To Update : ").strip())  
#     except ValueError:
#         print("Enter Numeric Value!!")
#         return

#     book = search_by_id(id)        

#     if book is None:
#         return

#     title = input("Enter the Updated Name of Book : ").strip()   
#     if title != "":
#         book['title'] = title

#     name = input("Enter the Updated Author of Book : ").strip()   
#     if name != "":
#         book['author'] = name

#     genre = input("Enter the Updated Genre of Book : ").strip()   
#     if genre != "":
#         book['genre'] = genre

#     raw_price = input("Enter the Updated Price of Book : ").strip()
#     if raw_price != "":
#         try:
#             price = float(raw_price)
#             if price > 0.0:
#                 book['price'] = price
#             else:
#                 print("Enter a Valid Price (> 0.0)!!")
#                 return
#         except ValueError:
#             print("Price Should be a Numeric Value!!")
#             return

#     raw_copies = input("Enter the Updated Copies of Book : ").strip()
#     if raw_copies != "":
#         try:
#             copies = int(raw_copies)
#             if copies >= 0:
#                 book['copies'] = copies
#             else:
#                 print("Enter a Valid Copies count (>= 0)!!")
#                 return
#         except ValueError:
#             print("Copies Should be a Numeric Value!!")
#             return

#     print("\nBooks record updated successfully!")
#     view_one_book(book)


# # ***********************************************************************************************************    
# def delete_book():
#     try:
#         id = int(input("Enter the Book ID To Delete : ").strip())  
#     except ValueError:
#         print("Enter Numeric Value!!")
#         return
    
#     book = search_by_id(id)        

#     if book is None:
#         return
    
#     choice = input("Are you sure you want to delete this book permanently? (y/n): ").strip().lower()

#     if choice == 'y':
#         books.remove(book)
#         print("Book has been Deleted Successfully.")
#     elif choice == 'n':
#         print("Book Deletion Aborted.") 
#     else:
#         print("Invalid choice! Deletion cancelled.")


# # ***********************************************************************************************************
# def save_to_file():
#     """
#     Saves all book records into a pipe-delimited text file (books.txt).
#     Format per line: id|title|author|genre|price|copies
#     """
#     try:
#         with open("books.txt", "w", encoding="utf-8") as file:
#             for b in books:
#                 line = f"{b['id']}|{b['title']}|{b['author']}|{b['genre']}|{b['price']:.2f}|{b['copies']}\n"
#                 file.write(line)
#         print("Catalog saved to 'books.txt' successfully!")
#     except Exception as e:
#         print(f"Error saving to file: {e}")      


# # ***********************************************************************************************************
# def load_from_file():
#     """
#     Reads records from 'books.txt', parses pipe-delimited values,
#     casts data types appropriately, and repopulates the global catalog.
#     """
#     global books, id_counter
#     try:
#         with open("books.txt", "r", encoding="utf-8") as file:
#             loaded_books = []
#             for line in file:
#                 cleaned_line = line.strip()
#                 # Skip empty lines if any exist
#                 if not cleaned_line:
#                     continue

#                 parts = cleaned_line.split("|")
#                 # Ensure the line has all 6 required fields
#                 if len(parts) == 6:
#                     book_dict = {
#                         "id": int(parts[0]),
#                         "title": parts[1],
#                         "author": parts[2],
#                         "genre": parts[3],
#                         "price": float(parts[4]),
#                         "copies": int(parts[5])
#                     }
#                     loaded_books.append(book_dict)

#             if loaded_books:
#                 books = loaded_books
#                 # Update counter to the highest existing ID to avoid collisions
#                 id_counter = max([b["id"] for b in books], default=0)
#                 print(f"Loaded {len(books)} books from 'books.txt' successfully!")
#             else:
#                 print("File 'books.txt' is empty. No records loaded.")

#     except FileNotFoundError:
#         print("Error: 'books.txt' not found. Save some data to create the file first.")
#     except Exception as e:
#         print(f"Error reading from file: {e}")          

# # ***********************************************************************************************************              
# def main():

#     while True:
#         choice = menu()

#         if choice == 1:
#             add_book()
#         elif choice == 2:
#             view_books()
#         elif choice == 3:
#             search_books()
#         elif choice == 4:
#             update_book()
#         elif choice == 5:
#             delete_book()
#         elif choice == 6:
#             save_to_file()
#         elif choice == 7:
#             ...
#         elif choice == 8:
#             print("Successfully Exited the Program. Bye!!")
#             break
#         else:
#             print("Invalid Choice !!! ")


# main()




# Chat-GPT Solution


"""
DELIMITED FLAT-FILE CATALOG MANAGEMENT SYSTEM
"""

# books = [
#     {
#         "id": 1,
#         "title": "Python Programming",
#         "author": "John Zelle",
#         "genre": "Technical",
#         "price": 650.00,
#         "copies": 15
#     },
#     {
#         "id": 2,
#         "title": "Clean Code",
#         "author": "Robert Martin",
#         "genre": "Technical",
#         "price": 950.00,
#         "copies": 8
#     },
#     {
#         "id": 3,
#         "title": "The Great Gatsby",
#         "author": "F. Scott Fitzgerald",
#         "genre": "Fiction",
#         "price": 350.00,
#         "copies": 20
#     },
#     {
#         "id": 4,
#         "title": "Sapiens",
#         "author": "Yuval Noah Harari",
#         "genre": "History",
#         "price": 550.00,
#         "copies": 12
#     },
#     {
#         "id": 5,
#         "title": "Cosmos",
#         "author": "Carl Sagan",
#         "genre": "Science",
#         "price": 480.00,
#         "copies": 6
#     }
# ]


# Start counter from highest existing ID
# id_counter = max([book["id"] for book in books], default=0)


# ********************************************************************
# MENU
# ********************************************************************

def menu():

    print("\n" + "*" * 60)
    print("     DELIMITED FLAT-FILE CATALOG MANAGEMENT SYSTEM")
    print("*" * 60)

    print("""
1. Add Book
2. View Catalog
3. Search Books
4. Update Details
5. Delete Book
6. Save to File
7. Load from File
8. Exit
""")

    try:
        choice = int(input("Enter Your Choice: ").strip())
        return choice

    except ValueError:
        print("Invalid Input! Please enter a number.")
        return -1


# ********************************************************************
# ADD BOOK
# ********************************************************************

def add_book():

    global id_counter

    print("\n******** ADD BOOK ********")

    # Title
    title = input("Enter the Name of the Book: ").strip()

    if title == "":
        print("Error! Book Name cannot be empty.")
        return

    # Author
    author = input("Enter Author Name: ").strip()

    if author == "":
        print("Error! Author Name cannot be empty.")
        return

    # Genre
    genre = input("Enter Genre Name: ").strip()

    if genre == "":
        print("Error! Genre Name cannot be empty.")
        return

    # Price and copies
    try:

        price = float(input("Enter the Price of the Book: ").strip())

        if price <= 0:
            print("Price must be greater than 0.")
            return

        copies = int(input("Enter the Number of Copies: ").strip())

        if copies < 0:
            print("Number of Copies must be 0 or greater.")
            return

    except ValueError:
        print("Enter a valid numeric value.")
        return

    # Generate new ID
    id_counter += 1

    # Create dictionary
    book = {
        "id": id_counter,
        "title": title,
        "author": author,
        "genre": genre,
        "price": price,
        "copies": copies
    }

    # Add dictionary to list
    books.append(book)

    print("\nBook added successfully!")
    print(f"Assigned Book ID: {id_counter}")


# ********************************************************************
# VIEW ONE BOOK
# ********************************************************************

def view_one_book(book):

    print("\n******** BOOK DETAILS ********")
    print("-" * 40)

    print(f"ID          : {book['id']}")
    print(f"Book Title  : {book['title']}")
    print(f"Author      : {book['author']}")
    print(f"Genre       : {book['genre']}")
    print(f"Price       : {book['price']:.2f}")
    print(f"Copies      : {book['copies']}")

    print("-" * 40)


# ********************************************************************
# VIEW ALL BOOKS
# ********************************************************************

def view_all_books(book_list):

    if not book_list:
        print("\nNo books found.")
        return

    print("\n******** BOOK CATALOG ********")

    print("-" * 85)

    print(
        f"{'ID':^5} "
        f"{'Book Title':<25} "
        f"{'Author Name':<20} "
        f"{'Genre':<12} "
        f"{'Price':>10} "
        f"{'Copies':>8}"
    )

    print("-" * 85)

    for book in book_list:

        print(
            f"{book['id']:^5} "
            f"{book['title']:<25} "
            f"{book['author']:<20} "
            f"{book['genre']:<12} "
            f"{book['price']:>10.2f} "
            f"{book['copies']:>8}"
        )

    print("-" * 85)


# ********************************************************************
# VIEW CATALOG
# ********************************************************************

def view_books():

    if not books:
        print("\nNo Books in the System.")
        return

    view_all_books(books)


# ********************************************************************
# SEARCH BY ID
# ********************************************************************

def search_by_id(book_id):

    for book in books:

        if book["id"] == book_id:
            return book

    return None


# ********************************************************************
# SEARCH BY TITLE
# ********************************************************************

def search_by_name():

    title = input("Enter the Book Title to Search: ").strip()

    if title == "":
        print("Error! Search term cannot be empty.")
        return

    result = []

    for book in books:

        if title.lower() in book["title"].lower():
            result.append(book)

    if not result:
        print(f"No books found matching '{title}'.")
        return

    view_all_books(result)


# ********************************************************************
# SEARCH BY AUTHOR
# ********************************************************************

def search_by_author():

    author = input("Enter the Author Name to Search: ").strip()

    if author == "":
        print("Error! Search term cannot be empty.")
        return

    result = []

    for book in books:

        if author.lower() in book["author"].lower():
            result.append(book)

    if not result:
        print(f"No books found matching author '{author}'.")
        return

    view_all_books(result)


# ********************************************************************
# SEARCH BOOKS
# ********************************************************************

def search_books():

    print("\n******** SEARCH BOOKS ********")

    print("""
1. Search Book by ID
2. Search Book by Title
3. Search Book by Author
4. Return
""")

    try:

        choice = int(input("Enter your Choice: ").strip())

    except ValueError:

        print("Invalid Choice! Please enter a number.")
        return

    if choice == 1:

        try:

            book_id = int(input("Enter the Book ID: ").strip())

        except ValueError:

            print("Book ID must be an integer.")
            return

        book = search_by_id(book_id)

        if book is None:
            print(f"No Book found with ID: {book_id}")
        else:
            view_one_book(book)

    elif choice == 2:

        search_by_name()

    elif choice == 3:

        search_by_author()

    elif choice == 4:

        return

    else:

        print("Invalid Option Entered.")


# ********************************************************************
# UPDATE BOOK
# ********************************************************************

def update_book():

    print("\n******** UPDATE BOOK ********")

    # Get ID
    try:

        book_id = int(
            input("Enter the Book ID to Update: ").strip()
        )

    except ValueError:

        print("Book ID must be an integer.")
        return

    # Search book
    book = search_by_id(book_id)

    if book is None:

        print(f"No Book found with ID: {book_id}")
        return

    # Show current information
    print("\nCurrent Book Information:")
    view_one_book(book)

    # Update title
    title = input(
        "Enter Updated Book Title "
        "(press Enter to keep current): "
    ).strip()

    if title != "":
        book["title"] = title

    # Update author
    author = input(
        "Enter Updated Author "
        "(press Enter to keep current): "
    ).strip()

    if author != "":
        book["author"] = author

    # Update genre
    genre = input(
        "Enter Updated Genre "
        "(press Enter to keep current): "
    ).strip()

    if genre != "":
        book["genre"] = genre

    # Update price
    raw_price = input(
        "Enter Updated Price "
        "(press Enter to keep current): "
    ).strip()

    if raw_price != "":

        try:

            price = float(raw_price)

        except ValueError:

            print("Price must be numeric.")
            return

        if price <= 0:

            print("Price must be greater than 0.")
            return

        book["price"] = price

    # Update copies
    raw_copies = input(
        "Enter Updated Copies "
        "(press Enter to keep current): "
    ).strip()

    if raw_copies != "":

        try:

            copies = int(raw_copies)

        except ValueError:

            print("Copies must be an integer.")
            return

        if copies < 0:

            print("Copies cannot be negative.")
            return

        book["copies"] = copies

    print("\nBook record updated successfully!")

    view_one_book(book)


# ********************************************************************
# DELETE BOOK
# ********************************************************************

def delete_book():

    print("\n******** DELETE BOOK ********")

    try:

        book_id = int(
            input("Enter the Book ID to Delete: ").strip()
        )

    except ValueError:

        print("Book ID must be an integer.")
        return

    # Search book
    book = search_by_id(book_id)

    if book is None:

        print(f"No Book found with ID: {book_id}")
        return

    # Display book
    print("\nBook found:")
    view_one_book(book)

    # Confirmation
    choice = input(
        "Are you sure you want to delete this book? (y/n): "
    ).strip().lower()

    if choice == "y":

        books.remove(book)

        print("Book deleted successfully.")

    elif choice == "n":

        print("Book deletion cancelled.")

    else:

        print("Invalid choice. Deletion cancelled.")


# ********************************************************************
# SAVE TO FILE
# ********************************************************************

def save_to_file():

    try:

        with open("books.txt", "w", encoding="utf-8") as file:

            for book in books:

                line = (
                    f"{book['id']}|"
                    f"{book['title']}|"
                    f"{book['author']}|"
                    f"{book['genre']}|"
                    f"{book['price']:.2f}|"
                    f"{book['copies']}\n"
                )

                file.write(line)

        print("\nCatalog saved successfully to books.txt.")

    except OSError as e:

        print(f"Error while saving file: {e}")


# ********************************************************************
# LOAD FROM FILE
# ********************************************************************

def load_from_file():

    global books, id_counter

    loaded_books = []

    try:

        with open("books.txt", "r", encoding="utf-8") as file:

            for line in file:

                line = line.strip()

                # Skip empty lines
                if line == "":
                    continue

                # Split pipe-delimited data
                parts = line.split("|")

                # Every record must contain 6 fields
                if len(parts) != 6:

                    print("Warning: Invalid record skipped.")
                    continue

                try:

                    book = {
                        "id": int(parts[0]),
                        "title": parts[1],
                        "author": parts[2],
                        "genre": parts[3],
                        "price": float(parts[4]),
                        "copies": int(parts[5])
                    }

                    # Validate loaded data
                    if book["title"].strip() == "":
                        print("Warning: Empty title skipped.")
                        continue

                    if book["author"].strip() == "":
                        print("Warning: Empty author skipped.")
                        continue

                    if book["genre"].strip() == "":
                        print("Warning: Empty genre skipped.")
                        continue

                    if book["price"] <= 0:
                        print("Warning: Invalid price skipped.")
                        continue

                    if book["copies"] < 0:
                        print("Warning: Invalid copies skipped.")
                        continue

                    loaded_books.append(book)

                except ValueError:

                    print("Warning: Invalid numeric data skipped.")

        # Replace current books with loaded books
        books = loaded_books

        # Update ID counter
        id_counter = max(
            [book["id"] for book in books],
            default=0
        )

        print(
            f"\n{len(books)} book(s) loaded successfully "
            f"from books.txt."
        )

    except FileNotFoundError:

        print("Error: books.txt file was not found.")

    except OSError as e:

        print(f"Error while reading file: {e}")


# ********************************************************************
# MAIN
# ********************************************************************

def main():

    while True:

        choice = menu()

        if choice == 1:

            add_book()

        elif choice == 2:

            view_books()

        elif choice == 3:

            search_books()

        elif choice == 4:

            update_book()

        elif choice == 5:

            delete_book()

        elif choice == 6:

            save_to_file()

        elif choice == 7:

            load_from_file()

        elif choice == 8:

            print("\nSuccessfully Exited the Program. Bye!")
            break

        else:

            print("Invalid Choice! Please select 1 to 8.")


# ********************************************************************
# PROGRAM START
# ********************************************************************

if __name__ == "__main__":
    main()