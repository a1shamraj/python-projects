from array import array

def search(list, n):
    i = 0
    
    while i < len(list):
        if list[i] == n:
            return True
        i = i + 1
    
    return False

# def sort():
    

# def insert():
    

# def update():
    

# def delete():


while quit != True: 
    list = [3, 6, 4, 1, 9, 5]
    print(list)
    
    menu = input(
    "\nWhat operation would you like to perform?"
    "\na = Search \nb = Sort \nc = Insert \nd = Update \ne = Delete \nf = Exit \nAnswer: ").lower()
    
    if menu == "a":
        x = int(input("Input the number to search for! Answer: "))
        if search(list, x):
            print("\nElement Found!")
        else:
            print("\nElement NOT Found!")
        
    elif menu == "b":
        sort()
    elif menu == "c":
        insert()
    elif menu == "d":
        update()
    elif menu == "e":
        delete()
    elif menu == "f":
        quit()
    else:
        print("\nInvalid Operation Selected!\n")