"""
Library Book Management System
"""

import json

books = []

id_counter = max([b["id"] for b in books], default=0)


# --------------------------------------------------
# MENU
# --------------------------------------------------

def menu():
    options = '''
                1. Add Book
                2. View All Books
                3. Search Books
                4. Update Book
                5. Delete Book
                6. Save To JSON
                7. Load From JSON
                8. Exit
    '''

    print("****** Library Book Management System ******")
    print(options)

    try:
        choice = int(input("Enter your Choice: ").strip())
        return choice

    except ValueError:
        print("Error: Enter a Numeric Value!!")
        return -1


# --------------------------------------------------
# ADD BOOK
# --------------------------------------------------

def add_book():
    global id_counter

    print("\n***** Book Details *****")

    title = input("Enter the Book Name: ").strip()

    if title == "":
        print("Error: Name cannot be Empty")
        return

    author = input("Enter Author Name: ").strip()

    if author == "":
        print("Error: Author Name cannot be Empty")
        return

    genre = input("Enter Genre of the Book: ").strip()

    if genre == "":
        print("Error: Genre cannot be Empty")
        return

    try:
        price = float(input("Enter the Price for the Book: ").strip())

    except ValueError:
        print("Price should be Numeric!!")
        return

    if price <= 0:
        print("Price should be > 0")
        return

    try:
        quantity = int(input("Enter the No of Copies: ").strip())

    except ValueError:
        print("Quantity should be Numeric")
        return

    if quantity < 0:
        print("Quantity should be >= 0")
        return

    id_counter += 1

    book = {
        "id": id_counter,
        "title": title,
        "author": author,
        "genre": genre,
        "price": price,
        "quantity": quantity
    }

    books.append(book)

    print("Book Data has been Added Successfully")


# --------------------------------------------------
# VIEW ALL BOOKS
# --------------------------------------------------

def view_all_books(book_list):

    if not book_list:
        print("No Books in the System, Add a Book")
        return

    print("*" * 80)
    print("******** Book Management System ********")
    print("*" * 80)

    print(
        f"{'ID':^5}"
        f"{'Title':<20}"
        f"{'Author':<20}"
        f"{'Genre':<15}"
        f"{'Price':>10}"
        f"{'Quantity':^10}"
    )

    print("-" * 80)

    for book in book_list:
        print(
            f"{book['id']:^5}"
            f"{book['title']:<20}"
            f"{book['author']:<20}"
            f"{book['genre']:<15}"
            f"{book['price']:>10.2f}"
            f"{book['quantity']:^10}"
        )

    print("*" * 80)


# --------------------------------------------------
# VIEW ONE BOOK
# --------------------------------------------------

def view_one_book(book):

    print("*" * 40)
    print("******** Book Details ********")

    print(f"ID       : {book['id']}")
    print(f"Title    : {book['title']}")
    print(f"Author   : {book['author']}")
    print(f"Genre    : {book['genre']}")
    print(f"Price    : {book['price']:.2f}")
    print(f"Quantity : {book['quantity']}")

    print("*" * 40)


# --------------------------------------------------
# SEARCH BY ID
# --------------------------------------------------

def search_by_id(book_id):

    for book in books:

        if book["id"] == book_id:
            return book

    return None


# --------------------------------------------------
# SEARCH BY TITLE
# --------------------------------------------------

def search_by_name():

    title = input("Enter the Name of the Book: ").strip()

    if title == "":
        print("Book Name cannot be Empty")
        return

    result = [
        book
        for book in books
        if title.lower() in book["title"].lower()
    ]

    if not result:
        print(f"No Book Found with Name: {title}")
        return

    view_all_books(result)


# --------------------------------------------------
# SEARCH BY AUTHOR
# --------------------------------------------------

def search_by_author():

    author = input("Enter the Name of Author: ").strip()

    if author == "":
        print("Author Name cannot be Empty")
        return

    result = [
        book
        for book in books
        if author.lower() in book["author"].lower()
    ]

    if not result:
        print(f"No Book Found with Author: {author}")
        return

    view_all_books(result)


# --------------------------------------------------
# SEARCH BOOK
# --------------------------------------------------

def search_book():

    print("\nHow Would You Like To Search the Book?")
    print("1. Search By ID")
    print("2. Search By Title")
    print("3. Search By Author")
    print("4. Exit")

    try:
        choice = int(input("Enter your Choice: ").strip())

    except ValueError:
        print("Enter a Numeric Value!!")
        return

    if choice == 1:

        try:
            book_id = int(
                input("Enter the ID to Search the Book: ").strip()
            )

        except ValueError:
            print("ID should be Numeric")
            return

        book = search_by_id(book_id)

        if book is None:
            print(f"No Book Found with ID {book_id}")
            return

        view_one_book(book)

    elif choice == 2:
        search_by_name()

    elif choice == 3:
        search_by_author()

    elif choice == 4:
        return

    else:
        print("Invalid Option Selected")


# --------------------------------------------------
# UPDATE BOOK
# --------------------------------------------------

def update_book():

    try:
        book_id = int(
            input("Enter the Book ID which needs to be Updated: ").strip()
        )

    except ValueError:
        print("ID should be Numeric")
        return

    book = search_by_id(book_id)

    if book is None:
        print(f"No Book Found with ID {book_id}")
        return

    print("\nCurrent Book Details:")
    view_one_book(book)

    # -----------------------------
    # UPDATE TITLE
    # -----------------------------

    new_title = input(
        "Enter Updated Name [Press Enter To Keep Same Name]: "
    ).strip()

    if new_title != "":
        book["title"] = new_title

    # -----------------------------
    # UPDATE AUTHOR
    # -----------------------------

    new_author = input(
        "Enter Updated Author [Press Enter To Keep Same Author]: "
    ).strip()

    if new_author != "":
        book["author"] = new_author

    # -----------------------------
    # UPDATE GENRE
    # -----------------------------

    new_genre = input(
        "Enter Updated Genre [Press Enter To Keep Same Genre]: "
    ).strip()

    if new_genre != "":
        book["genre"] = new_genre

    # -----------------------------
    # UPDATE PRICE
    # -----------------------------

    new_price = input(
        "Enter Updated Price [Press Enter To Keep Same Price]: "
    ).strip()

    if new_price != "":

        try:
            new_price = float(new_price)

        except ValueError:
            print("Price should be Numeric!!")
            return

        if new_price <= 0:
            print("Price should be > 0")
            return

        book["price"] = new_price

    # -----------------------------
    # UPDATE QUANTITY
    # -----------------------------

    new_quantity = input(
        "Enter Updated Quantity [Press Enter To Keep Same Quantity]: "
    ).strip()

    if new_quantity != "":

        try:
            new_quantity = int(new_quantity)

        except ValueError:
            print("Quantity should be Numeric!!")
            return

        if new_quantity < 0:
            print("Quantity should be >= 0")
            return

        book["quantity"] = new_quantity

    print("Book Data has been Updated Successfully")

    view_one_book(book)


# --------------------------------------------------
# DELETE BOOK
# --------------------------------------------------

def delete_book():

    try:
        book_id = int(
            input("Enter the Book ID which needs to be Deleted: ").strip()
        )

    except ValueError:
        print("ID should be Numeric")
        return

    book = search_by_id(book_id)

    if book is None:
        print(f"No Book Found with ID {book_id}")
        return

    print("\nBook to be Deleted:")
    view_one_book(book)

    choice = input(
        "Are You Sure You Want To Delete Above Book? [y/n]: "
    ).strip().lower()

    if choice == "y":

        books.remove(book)

        print("Book Deleted Successfully")

    elif choice == "n":

        print("Book Deletion Aborted")

    else:

        print("Invalid Choice. Book Deletion Aborted")


# --------------------------------------------------
# SAVE TO JSON
# --------------------------------------------------

def save_to_json():

    try:

        with open("books.json", "w", encoding="utf-8") as file:

            json.dump(
                books,
                file,
                indent=4
            )

        print("Data has been Saved Successfully")

    except OSError as e:

        print(f"Error Occurred while Saving File: {e}")


# --------------------------------------------------
# LOAD FROM JSON
# --------------------------------------------------

def load_from_json():

    global books
    global id_counter

    try:

        with open("books.json", "r", encoding="utf-8") as file:

            books = json.load(file)

        # Recalculate ID counter
        id_counter = max(
            [book["id"] for book in books],
            default=0
        )

        print("Data has been Loaded Successfully")

    except FileNotFoundError:

        print("Error: books.json File Not Found")

    except json.JSONDecodeError:

        print("Error: Invalid JSON File")

    except OSError as e:

        print(f"Error Occurred while Loading File: {e}")


# --------------------------------------------------
# MAIN
# --------------------------------------------------

def main():

    while True:

        choice = menu()

        if choice == 1:

            add_book()

        elif choice == 2:

            view_all_books(books)

        elif choice == 3:

            search_book()

        elif choice == 4:

            update_book()

        elif choice == 5:

            delete_book()

        elif choice == 6:

            save_to_json()

        elif choice == 7:

            load_from_json()

        elif choice == 8:

            print("Application Termination Successful. Good Bye!!")
            break

        else:

            print("Invalid Option Selected!!")


# --------------------------------------------------
# PROGRAM START
# --------------------------------------------------

if __name__ == "__main__":
    main()