contacts=[]
def add_contact():
    name=input("Enter name:").title()
    contact_no=input("Enter contact number: ")
    contact={
        "name":name,
        "contact_no":contact_no
    }
    contacts.append(contact)
    print("Contact added succesfully!")

def view_contact():
    if len(contacts)==0:
        print("No contact found!")
        return
    print("-----Contact list-----")
    for contact in contacts:
        print(f"name:{contact['name']}")
        print(f"Contact number :{contact['contact_no']}")
        print("-----------------------")

def search_contact():
    search_name=input("Enter name to search: ").title()
    found=False
    for contact in contacts:
        if contact["name"]==search_name:
            print("Contact Found")
            print("Name:",contact["name"])
            print("Contact number:",contact["contact_no"])
            found=True
            break
    if not found:
        print("Contact not found")

while True:
    print("\n======== Contact Book ========")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Exit")

    choice=int(input("Enter choice: "))
    if choice==1:
        add_contact()
    elif choice==2:
        view_contact()
    elif choice==3:
        search_contact()
    elif choice==4:
        print("program ended!")
        break
    else:
        print("Invalid choice")

