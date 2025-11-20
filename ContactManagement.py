

import os

'''
Choices Parameters
'''

Show_Function = 1
Search_Function = 2
Add_Function = 3
Delete_Function = 4
Modify_Function = 5
Quit_Function = 6


def main():

    Decision = 0

    while Decision != Quit_Function:

        print("\n Contacts Menu")
        print("----------------")
        print(" Choice Menu ")
        print("1 - Show the list of contacts")
        print("2 - Search for a specific contact")
        print("3 - Add a contact")
        print("4 - Delete a contact")
        print("5 - Modify a contact")
        print("6 - Quit\n")
        
        Decision = int(input("Enter your choice: "))

        if Decision == Show_Function:
            show()             
        elif Decision == Search_Function:
            search()             
        elif Decision == Add_Function:
            add()
        elif Decision == Delete_Function:
            delete()
        elif Decision == Modify_Function:
            modify()
        elif Decision == Quit_Function:
            print("Exiting the system...")
        else:
            print("Error: invalid choice. Please try again.")

        

def show():

    try:
        contact_file = open('contact.txt', 'r')

        name = contact_file.readline()
        
        print("----------------")
        print("List of contacts\n")
    
        while name != '':

            email = contact_file.readline()
            phone = contact_file.readline()

            name = name.rstrip('\n')
            
            print("Name:", name)
            print("Email:", email)
            print('Phone:', phone)

            name = contact_file.readline()

        contact_file.close()
        
    except IOError as err:
        print(err)



def search():
    
    found = False
    print("----------------")
    search = input("Enter a name to search for: ")

    contact_file = open('contact.txt', 'r')

    name = contact_file.readline()

    while name != '':
        
        email = contact_file.readline()
        phone = contact_file.readline()

        name = name.rstrip('\n')

       
        if name == search:

            print("Name:", name)
            print("Email:", email)
            print("Phone:", phone)
    
            found = True

        name = contact_file.readline()

    contact_file.close()

    # If the search value was not found in the file
    # display a message.
    if not found:
        print("Contact not found")
    

def add():

    another = 'y'
    
    contact_file = open("contact.txt", 'a')
    print("----------------")
    while another == 'y' or another == 'Y':
        print("Please enter the following contact data:")
        name = input("Name: ")
        email = input("Email: ")
        phone = input("Phone: ")

        contact_file.write(name + '\n')
        contact_file.write(email + '\n')
        contact_file.write(phone + '\n')

        print("Do you want to add another record?")
        another = input("Y = yes, anything else = no: ")

    contact_file.close()

def delete():

    found = False
    print("----------------")
    search = input("Which name do you want to delete?:  ")
    
    contact_file = open("contact.txt", 'r')
    temp_file = open("temp.txt", 'w')

    name = contact_file.readline()


    while name != '':

        email = contact_file.readline()
        phone = contact_file.readline()

        name = name.rstrip('\n')

        if name != search:
            temp_file.write(phone + '\n')
            temp_file.write(email + '\n')
            temp_file.write(phone + '\n')
        else:
            
            found = True

        name = contact_file.readline()

  
    contact_file.close()
    temp_file.close()

    os.remove("contact.txt")

    os.rename("temp.txt", "contact.txt")

    if found:
        print("The file has been updated.")
    else:
        print("That contact was not found in the file.")


def modify():

    found = False
    print("----------------")
    
    search = input("Enter a name to search for update: ")
    email = input("Enter the new email for update: ")
    phone = input("Enter the new phone for update: ")
    
    contact_file = open('contact.txt', 'r')

    temp_file = open('temp.txt', 'w')

    name = contact_file.readline()


    while name != '':
        
         email = contact.readline()
         phone = contact.readline()

         name = name.rstrip('\n')

         if descr == search:
             
             temp_file.write(email + '\n')
             temp_file.write(phone + '\n')
            
             found = True
         else:
             temp_file.write(email + '\n')
             temp_file.write(phone + '\n')

         email = contact_file.readline()

         contact_file.close()
         temp_file.close()

         os.remove("contact.txt")

   
         os.rename("temp.txt", "coffee.txt")

    if found:
        print("The file has been updated.")
    else:
        print("That contact was not found in the file.")

        





main()
