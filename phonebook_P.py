contacts = {}

def check_empty():
    if not contacts:
        print('Contact list is empty!\n')
        return True
    return False

def add_contact():
    name = input('Enter the contact name: ').strip()
    phone = input('Enter the contact phone number: ').strip()

    if name == '' or phone == '':
        print('Name and phone cannat be empty!\n')
        return
    
    contacts[name] = phone
    print(f'{name} added successfully!\n')

def view_contacts():
    if check_empty():
        return
    
    print('--- Contact List ---')
    for name, phone in contacts.items():
        print(f'{name}: {phone}')
        print('------------------------')

def find_contact():
    if check_empty():
        return
    
    name = input('\nEnter the name to find: ').strip()

    if name in contacts:
        print(f"{name}'s phone number is {contacts[name]}")
    else:
        print('Contact not found!\n')

def delete_contact():
    if check_empty():
        return
    
    name = input('\nEnter the name to delete:').strip()

    if name in contacts:
        del contacts[name]
        print(f'{name} deleted successfully!\n')
    else:
        print('Contact not found!\n')

def show_menu():
    print('==== PHONEBOOK MENU ====')
    print('1. Add Contact')
    print('2. View All Contacts')
    print('3. Find a Contact')
    print('4. Delete a Contact')
    print('5. Exit')

while True:
    show_menu()

    choice = input('Choose an option (1-5): ').strip()

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        find_contact()
    elif choice == '4':
        delete_contact()
    elif choice == '5':
        print('Goodbye!')
        break
    else:
        print('Invalid Option! Please enter a number between 1 and 5.\n')