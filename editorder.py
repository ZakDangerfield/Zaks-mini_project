import sys
import os
import csv 
def clear():
    	os.system( 'cls' )
import pandas as pd 

def finnish():
    finnish = input("Your order has been updated. Press any key to return to the orders edit menu.")
    if finnish == "0":
        clear()
        update_order()
    else:
        clear()
        update_order()

def update_order():
    clear()
    # reading the csv file 
    full_order_list = pd.read_csv("order.csv") 
    print (full_order_list)
    print (" ")
    row_edit = int(input("Please enter the order number. \n The order number is located on the first collumn: "))
    Collumn_edit = 0
    while Collumn_edit not in range(1,6):
        try:
            Collumn_edit = int(input("""What would you like to change: 
Customer name [1]
Customer address [2]
Customer phone number [3]
Order date [4]
Exit back to the Orders menu [5]
"""))
            if Collumn_edit not in range(1,6):
                clear()
                print("Action not recognised")
            
            elif Collumn_edit == 1:
                clear()
                new_edit = input("Please update the name: ")
            # updating the column value/data 
                full_order_list.loc[row_edit, 'Customer name'] = new_edit
            # writing into the file
                full_order_list.to_csv("order.csv", index=False) 
                clear()
                finnish()

            elif Collumn_edit == 2:
                clear()
                new_edit = input("Please update the first line of address followed by the postcode:\n \n ")
                full_order_list.loc[row_edit, 'Customer address'] = new_edit
                full_order_list.to_csv("order.csv", index=False) 
                clear()
                finnish()
                
            elif Collumn_edit == 3:
                clear()
                new_edit = input("Updating phone number: ")
                full_order_list.loc[row_edit, 'Customer phone number'] = new_edit
                full_order_list.to_csv("order.csv", index=False)
                finnish()
                clear()
            elif Collumn_edit == 4:
                clear()
                new_edit = input("Update the date of the order. DD/MM/YYYY \n \n")
                full_order_list.loc[row_edit, 'Customer address'] = new_edit
                full_order_list.to_csv("order.csv", index=False)
                finnish()
                clear()
            elif Collumn_edit == 5:
                clear()
                order_menu()
        except ValueError:
                    clear()
                    print("Please enter an integer.")
                    order_menu()
    return Collumn_edit 

update_order()