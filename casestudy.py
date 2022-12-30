# Amy Shamraj
# INF 308

# This program reflects a portal that incorporates both administrative view and patient view. They are able to 
# record any relavent information to a text file.

mainmenu = False

class db_functions():
    def add():
        with open('patient_book.txt', 'a') as f: # makes patient file, appendable
                p_firstname = input("Patient First Name: ") # name input
                p_lastname = input("Patient Last Name: ") # name input
                p_dob = input("Date of Birth: ") # phone input
                f.writelines((p_lastname, ', ', p_firstname, ' : ', p_dob, '\n')) # appends tuple to file
                f.close()
    
    def search():
        with open('patient_book.txt', 'r') as f: # reads from file
                s_last = input("Patient Last Name: ") # input patient last name
                s_first = input("Patient First Name: ") # input patient first name
                s_dob = input("Patient Date of Birth: ") # input patient dob
                for searchable in f: # item in file
                    if s_last and s_first and s_dob in searchable: # if input is = to item
                        print("\n" + searchable) # print patient info
                f.close()

    def view():
        f = open('patient_book.txt', 'r') # reads from file
        full_list = f.read() # variable for reading file
        print(full_list) # print list
        f.close()
    
    def remove():
        p_last = input("Enter Last Name of Patient to Remove: ")
        p_first = input("Enter First Name of Patient to Remove: ")
        p_dob = input("Enter Date of Birth of Patient to Remove: ")

        original_file = open('patient_book.txt', 'r')
        lines = original_file.readlines() # read from original file
        original_file.close()

        new_file = open('patient_book.txt', 'w')
        for line in lines: 
            if p_last and p_first and p_dob not in line.strip("\n"): # delete contact from new file
                new_file.write(line) 
                print("ERROR: Patient Retrieval Failed!")
            else:
                print(p_last + ', ' + p_first + ' successfully removed!')
        new_file.close()
    
    def appointment():
        p_lastname = input("Please Enter Your Last Name. ")
        p_dob = input("Please Enter Your Date of Birth. ")
        booking_type = input("What kind of appointment would you like to schedule? \n1 = COVID Vaccine \n2 = COVID Booster \nType Here: ")
        
        if booking_type == "1":
            print("COVID Vaccine Selected... ")
            appt_type = "COVID Vaccine"
        elif booking_type == "2":
            print("COVID Booster Selected... ")
            appt_type = "COVID Booster"
        else:
            print("Invalid booking type.")
        
        booking_date = input("\nWhat date would you like to book your appointment for? \n(Format: XX/XX/XXXX) \n Date: ")
        
        original_file = open('patient_book.txt', 'r')
        lines = original_file.readlines() # read from original file
        original_file.close()
        
        new_file = open('patient_book.txt', 'w')
        for line in lines: 
            if line.startswith(p_lastname) and p_dob in line: # check for patient info on line
                line = line.strip() + ((' // ' + appt_type + ' : '+ booking_date)) # value
            new_file.write(line) # append
        new_file.close()
    
    def pnotes():
        p_lastname = input("Please Enter Patient Last Name. ")
        p_dob = input("Please Enter Patient Date of Birth. ")
        p_notes = input("Notes: ")
        
        original_file = open('patient_book.txt', 'r')
        lines = original_file.readlines() # read from original file
        original_file.close()
        
        new_file = open('patient_book.txt', 'w')
        for line in lines: 
            if line.startswith(p_lastname) and p_dob in line: # check in line
                line = line.strip() + ((' /// Notes: ' + p_notes)) # value
            new_file.write(line) # append
        new_file.close()


class Admin():
    def Portal_Login():
        username = input("Enter username! \n Username: ").lower()
        password = input("\nEnter password! \n Password: ").lower()

        if username == 'admin' and password == 'admin':
            Admin.Admin_Portal()
        else:
            print("Admin Verification Failed!")
            exit()

    def Admin_Portal():
        contactmenu = input("\n1 = Add Patient \n2 = Search Patient \n3 = View ALL Patients \n4 = Remove Patient \n5 = Edit Patient Information \n6 = Exit \nAnswer: ")
    
        if contactmenu == "1":
            db_functions.add() # add function
        
        elif contactmenu == "2":
            db_functions.search() # search function
            notes = input("Would you like to include additional notes? \nY/N: ").lower()
            if notes == "y":
                db_functions.pnotes()
            elif notes == "n":
                exit()
            else: 
                print("Invalid input")
        
        elif contactmenu == "3":
            db_functions.view() # view function
        
        elif contactmenu == "4":
            db_functions.remove() # remove function
        
        elif contactmenu == "5":
            db_functions.remove() # remove function
            db_functions.add() # add function
        
        elif contactmenu == "6":
            quit() # quits to console
        
        else:
            print("\nInvalid Selection!") # error exception message

class Patient():
    def Patient_View():
        last = input("Please Enter Your Last Name. ")
        first = input("Please Enter Your First Name. ")
        dob = input("Please Enter Your Date of Birth. ")
        
        with open('patient_book.txt', 'r') as f: # reads from file
                for searchable in f: # item in file
                    if last and first and dob in searchable: # if input is = to item
                        print("\n" + searchable) # print contact info
                f.close()
                
    def Report_Symptoms():
        p_lastname = input("Please Enter Your Last Name. ")
        p_dob = input("Please Enter Your Date of Birth. ")
        p_symptoms = input("Symptoms: ")
        
        original_file = open('patient_book.txt', 'r')
        lines = original_file.readlines() # read from original file
        original_file.close()
        
        new_file = open('patient_book.txt', 'w')
        for line in lines: 
            if line.startswith(p_lastname) and p_dob in line:
                line = line.strip() + ((' /// Symptoms: ' + p_symptoms))
            new_file.write(line)
        new_file.close()
    
    def Patient_Portal():
        contactmenu = input("\n1 = View Information \n2 = Book Appointment \n3 = View Results \n4 = Report Symptoms \n5 = Exit \nAnswer: ")
    
        if contactmenu == "1":
            Patient.Patient_View()
        
        elif contactmenu == "2":
            db_functions.appointment()
        
        elif contactmenu == "3":
            Patient.Patient_View()
        
        elif contactmenu == "4":
            Patient.Report_Symptoms()
        
        elif contactmenu == "5":
            quit() # quits to console
        else:
            print("\nInvalid Selection!") # error exception message

while mainmenu != True:
    main = input("\n1 = Admin Portal \n2 = Patient Portal \n3 = Exit\nAnswer: ")
    
    if main == "1":
        Admin.Portal_Login()
    elif main == "2":
        Patient.Patient_Portal()
    elif main == "3":
        exit()