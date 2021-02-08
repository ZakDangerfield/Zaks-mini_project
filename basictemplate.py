import sys
import os
#Windows

# this is just defining background systems.. leave thsese
def clear():
    os.system( 'cls' )
def myfunc():
    global products
    products = ["coke", "fanta", "7up"]
myfunc()

def menu():
    print ("""welcome to the app!
option 0: close app
option 1 shows products:
option 2 create new product
option 3 edit product
option 4 remove product""")

    choice = int(input())
# choice 0 will terminate the app
    if choice == 0:
        sys.exit(0)
    
# this shows the products.. 
# see if you can make it so that if you press any key it will return you to menu
# see if you can clear the main menue from showing when entering this list
    elif choice == 1:
        print(products)
        print ("press 0 for main menu")
        type = input()
        if type == "0":
            clear()
            menu()
    elif choice == 2:
        clear()
        print (products)
        add = input("add to products? ")
        products.append(add) # study this line and what its doing
        print (f'The list: {products}')
        print ("Press 0 for main menu")
        result1 = (input())
        if result1 == "0":
            clear()
            menu()


    elif choice == 3:
        clear()
        print (products)
        print ("starting from 0 what product would you like to edit? ")
        change = int(input())
        print ("Please enter a new name for this product: ")
        changeto = input()
        products[change] = changeto
        print (f"Products updated {products}")
        print ("Press 0 for main menu")
        result1 = (input())
        if result1 == "0":
            clear()
            menu()


    elif choice == 4:
        clear()
        print (products)
        print ("What product to remove? (first_entry[0])")
        removing = int(input())
        products.pop(removing)
        print (f"Selected object has been removed: {products}")
        print("press 0 for menu")
        resulttt = input()
        if resulttt == "0":
            clear()
            menu()


menu()