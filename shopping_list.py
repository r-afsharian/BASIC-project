shopping_list = []

def title_menu():
    title = 'Shopping List'
    width = 30
    border = '+' + '-' * (width - 2) + '+'
    print(border)
    print('|' + title.center(width - 2) + '|')
    print(border)

def check_empty():
    if not shopping_list:
        print('List is empty!\n')
        return True
    return False

def delete_by_index(idx):
    removed = shopping_list.pop(idx - 1)
    print(f'{removed} has been removed successfully!\n')

def delete_by_name(name):
    matches = [item for item in shopping_list if item.lower() == name.lower()]
    if matches:
        shopping_list.remove(matches[0])
        print(f'{matches[0]} has been removed successfully!\n')
    else:
        print('No item matched!\n')

def show_list():
    if check_empty():
        return
    
    print('\nShopping List:')
    for i, item in enumerate(shopping_list, start=1):
        print(f'{i}. {item}')
    print()

while True:
    title_menu()
    print('1. Add an item')
    print('2. Delete an item')
    print('3. Show all item')
    print('4. Search an item')
    print('5. Exit\n')

    choice = input('Choose an option (1-5): ').strip()

    if choice == '1':
        add_item = input('\nEnter an item to add: ').strip()

        if add_item == '':
            print('You entered nothing!\n')
            continue

        if add_item.lower() in [item.lower() for item in shopping_list]:
            print('Item already exists!\n')
        else:
            shopping_list.append(add_item)
            print('Item added successfully!\n')
    
    elif choice == '2':
        if check_empty():
            continue
        
        delete_item = input('\nEnter an item to delete: ').strip()

        if delete_item == '':
            print('You entered nothing! Deletion cancelled.\n')
            continue
        
        if delete_item.isdigit():
            idx = int(delete_item)
            if 1 <= idx <= len(shopping_list):
                delete_by_index(idx)
            else:
                print('Index out of range!\n')
        else:
            delete_by_name(delete_item)
    
    elif choice == '3':
        show_list()
    
    elif choice == '4':
        if check_empty():
            continue

        search_item = input('\nEnter an item to search: ').strip()

        if search_item == '':
            print('Nothing entered to search!\n')
            continue

        found = [item for item in shopping_list if search_item.lower() in item.lower()]

        if found:
            print('Found Item:')
            for i, item in enumerate(found, start=1):
                print(f'{i}. {item}')
            print()
        else:
            print('Nothing matched!\n')
    
    elif choice == '5':
        print('Program ended. Goodbye!')
        break

    else:
        print('Invalid option! Please enter a number between 1 and 5.\n')