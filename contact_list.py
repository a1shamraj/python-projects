# Amy Shamraj
# INF 308

# This program essentially acts as a contact book. You can add a contact with a name and phone number. 
# Each contact is stored on a new line. You are able to add, search, view, remove and edit contacts.

menu = True # boolean for menu to function
# contact_book = []
# contact_list = []

def add():
    with open('contact_book.txt', 'a') as f: # makes contact file, appendable
            name = input("Name: ") # name input
            phone = input("Phone Number: ") # phone input
            f.writelines((name, ' : ', phone, '\n')) # appends tuple to file
            f.close()

def search():
    with open('contact_book.txt', 'r') as f: # reads from file
            search = input("Search: ") # input searchable contact
            for searchable in f: # item in file
                if search in searchable: # if input is = to item
                    print("\n" + searchable) # print contact info
                else:
                    print("Contact does not exist!") # exception case
            f.close()

def view():
    f = open('contact_book.txt', 'r') # reads from file
    full_list = f.read() # variable for reading file
    print(full_list) # print list
    f.close()

def remove():
    undesiredContact = input("Enter Contact to Remove: ")
    
    original_file = open('contact_book.txt', 'r')
    lines = original_file.readlines() # read from original file
    original_file.close()
    
    new_file = open('contact_book.txt', 'w')
    for line in lines: 
        if undesiredContact not in line.strip("\n"): # delete contact from new file
            new_file.write(line) 
    new_file.close()

while menu != False:
    contactmenu = input("\n1 = Add Contact \n2 = Search Contact \n3 = View Contacts \n4 = Remove Contact \n5 = Edit Contact Information \n6 = Exit \nAnswer: ")
    
    if contactmenu == "1":
        add() # add function
        
    elif contactmenu == "2":
        search() # search function
        
    elif contactmenu == "3":
        view() # view function
        
    elif contactmenu == "4":
        remove() # remove function
        
    elif contactmenu == "5":
        remove() # remove function
        add() # add function
        
    elif contactmenu == "6":
        quit() # quits to console
        
    else:
        print("\nInvalid Selection!") # error exception message