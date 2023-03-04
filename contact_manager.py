import contact
import pickle

LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

FILENAME = "contacts.dat"

def main():
    mycontacts = load_contacts()
    
    choice = 0
    
    while choice != QUIT:
        choice = get_menu_choice()
        
        if choice == LOOK_UP:
            look_up(mycontacts)
        elif choice == ADD:
            add(mycontacts)
        elif choice == CHANGE:
            change(mycontacts)
        elif choice == DELETE:
            delete(mycontacts)
    
    save_contacts(mycontacts)

def load_contacts():
    try:
        input_file = open(FILENAME,"rb")
        
        contact_dct = pickle.load(input_file)
        
    except IOError:
        contact_dct = {}
    
    return contact_dct

def get_menu_choice():
    print()
    print("Menu")
    print("-----------")
    print("1.Look up a contact ")
    print("2.Add a new contact")
    print("3.Change an existing contact")
    print("4.Delete a contact")
    print("5.Quit the program")
    print()
    
    choice = int(input("Enter your choice: "))
    
    while choice < LOOK_UP or choice > QUIT:
        choice = int(input("Enter avalid choice: "))
        
    return choice

def look_up(mycontacts):
    name = input("Enter a name : ")
    print(mycontacts.get(name, "That name is not found."))
    
def add(mycontacts):
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    
    entry = contact.Contact(name,phone,email)
    
    if name not in mycontacts:
        mycontacts[name] = entry
        print("The entry has been added.")
    else:
        print("That name already exists.")

def change(mycontacts):
    name = input("Enter a name: ")
    
    if name in mycontacts:
        phone = input("Enter the new phone number: ")
        email = input("Enter the new email address: ")
        entry = contact.Contact(name,phone,email)
        mycontacts[name] = entry
        print("Information updated.")
        
    else:
        print("That name is not found.")

def  delete(mycontacts):
    name = input("Enter a name: ")
    
    if name in mycontacts:
        del mycontacts[name]
        print("Entry deleted.")
    else:
        print("That name is not found")
def save_contacts(mycontacts):
    output_file = open(FILENAME, "wb")
    pickle.dump(mycontacts,output_file)
    output_file.close()
    
if __name__ == "__main__" :
    main()
        
        
    
    
    

    
        
    