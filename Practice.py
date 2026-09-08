import json

books = []
# Tracks the next ID dynamically based on existing books
id_counter = max([b["id"] for b in books], default=0)

file_name = "data.json"


def menu():
  option = """
                1: Add Book
                2: View Books
                3: Exit
                4: Save To File
                5: Load from File
    """
  print("\n***** Book Management System *****")
  print(option)
  try:
    choice = int(input("Enter your Choice : ").strip())
    return choice
  except ValueError:
    print("Enter a Numeric Value!!")
    return -1


def add_book():
  global id_counter
  print("\n--- Add Book Details ---")

  name = input("Enter the Name of the Book : ").strip()
  if name == "":
    print("Name cannot be empty!!!")
    return

  try:
    price = float(input("Enter the Price of the Book : ").strip())
    if price <= 0:
      print("Price should be > 0 ")
      return

    quantity = int(input("Enter the Quantity : ").strip())
    if quantity < 0:
      print("Quantity cannot be below 0 ")
      return
  except ValueError:
    print("Enter a Numeric Value!!")
    return

  # Fix 1: Increment the tracker so IDs remain unique
  id_counter += 1

  books.append(
      dict(id=id_counter, name=name, price=price, quantity=quantity)
  )
  print("Book has been added Successfully .... ")


def view_book():
  if len(books) == 0:
    print("No Books in the System, Please Add the Books First ")
    return

  if len(books) == 1:
    view_one_book()
  else:
    view_many_books()


def view_one_book():
  # Fix 2: Get the single book from the index since books is a list
  book = books[0]
  print("-" * 35)
  print("***** Book Details *****")
  print("-" * 35)
  print(f"ID:         {book['id']}")
  print(f"Name:       {book['name']}")
  print(f"Price:      ${book['price']:.2f}")
  print(f"Quantity:   {book['quantity']}")
  print("-" * 35)


def view_many_books():
  print("-" * 65)
  print("***** Book Inventory *****")
  print("-" * 65)
  # Fix 3: Standardize the text header alignment
  print(f"{'ID':^5}{'Name':<25}{'Price':>15}{'Quantity':>15}")
  print("-" * 65)

  # Fix 4: Use explicit string dictionary keys
  for b in books:
    print(f"{b['id']:^5}{b['name']:<25}{b['price']:>15.2f}{b['quantity']:>15}")
  print("-" * 65)


def save_to_file():
  with open(file_name, "wt", encoding="utf-8") as file:
    json.dump(books, file, indent=4)
  print("Data successfully saved to file.")


def load_from_file():
  global books, id_counter
  try:
    with open(file_name, "r", encoding="utf-8") as file:
      # Clear existing active list elements before appending loaded ones
      books = json.load(file)
      # Fix 5: Recalculate id_counter so new additions don't duplicate old IDs
      id_counter = max([b["id"] for b in books], default=0)
    print("Data successfully loaded from file.")
  except FileNotFoundError:
    print("No saved file found.")


def main():
  while True:
    choice = menu()
    if choice == 1:
      add_book()
    elif choice == 2:
      view_book()
    elif choice == 3:
      print("Successfully Exited from the Program....")
      break
    elif choice == 4:
      save_to_file()
    elif choice == 5:
      load_from_file()
    else:
      # Fix 6: Changed from 'return' to 'continue' to preserve the runtime loop
      print("Invalid Input! Try again.")
      continue


if __name__ == "__main__":
    main()
