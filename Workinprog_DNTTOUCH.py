# 26/01 added a corriers sub menu and will implement a view/add/edit and remove
# 26/01 add a sub menu for Products
# 24/01 option 3 drinks list is now editable/ copy and paste and implement it for snacks.
# 24/01 options 1 and 2 successfully read and alter the desired txt files
# 24/01 successfully added index numbers to list 
#make sure every entry has menu with any key at the end! ZD
# put an else statement at the end for any invalid commands in the main menu (else: menu())
# print ("{0}: {1}".format(i+0,line)) change (i+0 to i+1 if you need to index from 1 instead of 0)
import sys
import os
#Windows

def clear():
	os.system( 'cls' )

# display_drinks = open("drinks.txt", "r")
# drink_list = display_drinks.read()

#this function is for the snacks file to be read only
# display_snacks = open("snacks.txt", "r = read , write(overwrite) , a = append")
# snacks_list = display_snacks.read()

# display_couriers = open("couriers.txt", "r")
# couriers_list = display_couriers.read()

def menu():
    print ("""
Welcome to the main menu.
Please pick from the following options.

[1]: Shows our Drinks and Snacks menu.   [2]: Creates a new drinks/snacks entry.

[3]: Edit products.                      [4]: Removes products

[0]: exits the app. 
Your option: """)

#     def Cour_menu():
#         print("""Welcome to your couriers section.
# [1] View all Couriers.    [2] Add a new Courier to the system.

# [3] Edit your Couriers.    [4] Remove Courier. 

# Your option: """)

    choice = int(input())
    
    #Leave app
    if choice == 0:
        clear()
        print ("are you sure you want to leave? press 3 for yes or 0 no")
        result3 = int(input())
        if result3 == 3:
            sys.exit(3)
        elif result3 == 0:
            clear()
            menu()
        else:
            print ("incorrect command returned to menu")
            clear()
            menu()
    
# Display drinks or snacks (WORKING)
    elif choice == 1:
        clear()
        d_or_s = input("would you like to see the Drinks menu[1] or our snacks menu[2]? ")
        if d_or_s == "1":
            print ("Here is the Drinks list: ")
            with open('drinks.txt') as f:
                for i, line in enumerate(f):
                    print ("{0}: {1}".format(i+0,line))
            print ("Press any key for main menu")
            result1 = (input())
            if result1 == "0":
                clear()
                menu()
            else:
                clear()
                menu()
            
        elif d_or_s == "2":
            print ("Here is the snacks list: ")
            with open('snacks.txt') as f:
                for i, line in enumerate(f):
                    print ("{0}: {1}".format(i+0,line))
        print ("Press any key for main menu")
        result1 = (input())
        if result1 == "0":
            clear()
            menu()
        else:
            clear()
            menu()
            
#Add a drink or snack to their respective library(WORKING)
    elif choice == 2:
        clear()
        print("What entry would you like to add to? Drinks[1] or Snacks[2]")
        d_or_s = input()
        if d_or_s == "1":
            new_drinks_entry = open("drinks.txt", "a")
            new_drink = input("Please enter the name of a new Drink? ")          
            new_drinks_entry.write("\n")
            new_drinks_entry.write(new_drink)
            new_drinks_entry.close()
            print (f"Here is the ammended list: \n")
            with open('drinks.txt') as f:
                for i, line in enumerate(f):
                    print ("{0}: {1}".format(i+0,line))
            print ("Press any key for main menu")
            result1 = (input())
            if result1 == "0":
                clear()
                menu()
            else:
                clear()
                menu()
                
        elif d_or_s == "2":
            new_snacks_entry = open("snacks.txt", "a")
            new_snack = input("Please enter the name of a new snack? ")          
            new_snacks_entry.write("\n")
            new_snacks_entry.write(new_snack)
            new_snacks_entry.close()
            print (f"Here is the ammended snacks list: \n")
            with open('snacks.txt') as f:
                for i, line in enumerate(f):
                    print ("{0}: {1}".format(i+0,line))
            print ("Press any key for main menu")
            result1 = (input())
            if result1 == "0":
                clear()
                menu()
            else:
                clear()
                menu()
        else:
            print("Incorrect command, Please press any key to return to the main menu")
            print ("Press any key for main menu")
            result1 = (input())
            if result1 == "0":
                clear()
                menu()
            else:
                clear()
                menu()

# Edit a drink or snack index (WORKING)
    elif choice == 3:
        clear()
        print ("What directory would you like to edit? drinks[1] or snacks?[2] ")
        d_or_s = input()
        if d_or_s == "1":
            with open('drinks.txt') as f:
                for i, line in enumerate(f):
                    print ("{0}: {1}".format(i+0,line))
            change = int(input("What drink number would you like to edit? "))
            change_to = input("Please give this number a new name: ")
            # Edit codes:
            drinks_edit = open("drinks.txt")
            edit_drinks_list = drinks_edit.readlines()
            edit_drinks_list[change] = (f"{change_to} \n") # this replaces the index with the edit 
            drinks_edit.close()
            drinks_edit = open("drinks.txt", "w")
            new_drinkfile_contents = "".join(edit_drinks_list)
            drinks_edit.write(new_drinkfile_contents)
            drinks_edit.close()
            #readable file code
            print ("Here is the Drinks list: ")
            with open('drinks.txt') as f:
                for i, line in enumerate(f):
                    print ("{0}: {1}".format(i+0,line))
        elif d_or_s == "2":
            with open('snacks.txt') as g:
                for i, line in enumerate(g):
                    print ("{0}: {1}".format(i+0,line))
            change_s = int(input("What Snack number would you like to edit? "))
            change_to_s = input("Please give this number a new name: ")
            # Edit codes:
            snacks_edit = open("snacks.txt")
            edit_snacks_list = snacks_edit.readlines()
            edit_snacks_list[change_s] = (f"{change_to_s} \n") # this replaces the index with the edit 
            snacks_edit.close()
            snacks_edit = open("snacks.txt", "w")
            new_snacksfile_contents = "".join(edit_snacks_list)
            snacks_edit.write(new_snacksfile_contents)
            snacks_edit.close()
            #readable file code
            print ("Here is the Snacks list: ")
            with open('snacks.txt') as f:
                for i, line in enumerate(f):
                    print ("{0}: {1}".format(i+0,line))
            print ("Press any key for main menu")
            result1 = (input())
            if result1 == "0":
                clear()
                menu()
            else:
                clear()
                menu()

    # # Remove a drinks option
    elif choice == 4:
        clear()
        print(" What products list do you want to remove from? Drink[1] Snacks[2]")
        remove_item = input()
        if remove_item == "1":
            print ("Here is the Drinks list: ")
            with open('drinks.txt') as f:
                for i, line in enumerate(f):
                    print ("{0}: {1}".format(i+0,line))
            print ("What drink number would you like to remove? ")
            removal = int(input())
            print (f"are you sure you want to remove this product? [Y/N]")
            are_you_sure = input()
            if are_you_sure == "y":
                a_file = open("drinks.txt", "r")
                lines = a_file.readlines()
                a_file.close()
                del lines[removal]
                new_drinks_file = open("drinks.txt", "w+")
                for line in lines:
                    new_drinks_file.write(line)
                new_drinks_file.close()
                print("press any key for menu")
                resulttt = input()
                if resulttt == "0":
                    clear()
                    menu()
                else:
                    clear()
                    menu()
            else:
                print("Removal was aborted")
                print("press any key for menu")
                resulttt = input()
                if resulttt == "0":
                    clear()
                    menu()
                else:
                    clear()
                    menu()
            
    
    #Couriers menu
    elif choice == 5:
        clear()
        Cour_menu()

menu()
Cour_menu()