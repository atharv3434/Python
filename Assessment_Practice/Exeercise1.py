"""

Product Inventory Management System

"""

products = [
{"id": 1,"name": "Laptop","category": "Electronics","price": 55000,"quantity": 10},
{"id": 2,"name": "Chair","category": "Furniture","price": 1500,"quantity": 50}
]

def Menu():
    print("*"*50)
    print("Inventory Management Menu")
    print("1 : Add Product")
    print("2 : View all Product")
    print("3 : Search Products")
    print("4 : Update Products")
    print("5 : Delete Products")
    print("6 : Exit")


    try:
        option = input(print("Select an Option : "))
    except:
        option = -1
        
    return    
        
    
    
    





def main():

    global option

    while(True):
        option = Menu()

    if option == 1:
        ...
    elif option == 2:
        ...
    elif option == 3:
        ...
    elif option == 4:
        ...
    elif option == 5:
        ...
    elif option == 6:
        return    
    else:
        print("Invalid Option")    




main()        


