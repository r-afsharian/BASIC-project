def get_notes():
    try:
        with open('notes.txt', 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        return []


def add_note():
    note = input('\n📝 Enter the note to save: ').strip()

    if note == '':
        print('\n❌ You enetered nothing!\n')
        return
    
    with open('notes.txt', 'a') as file:
        file.write(note + '\n')
    
    print(f'\n✅ Note "{note}" added successfully!\n')


def view_notes():
    notes = get_notes()
    if not notes:
        print('\n❌ No note found! Please add a note first.\n')
        return
    
    print('📃 Notes List:')
    for i, note in enumerate(notes, start=1):
        print(f'{i}. {note.strip()}')
    print('-----------------')
    print(f'📊 Total Notes: {len(notes)}')
    print('-----------------\n')


def search_note():
    notes = get_notes()
    if not notes:
        print('\n❌ No note found! Please add a note first.\n')
        return
    
    search_word = input('\n🔍 Enter the word to search: ').strip()

    if search_word == '':
        print('\n⚠️ You must enter a word to search!\n')
        return
    
    found = False
    print('\n--- 🔎 Search Results ---')
    for i, note in enumerate(notes, start=1):
        if search_word.lower() in note.lower():
            print(f'{i}. {note.strip()}')
            found = True

    if not found:
        print(f'❌ No match found for "{search_word}"\n')
    print('-------------------------\n')

def delete_note():
    notes = get_notes()
    if not notes:
        print('\n❌ No note found! Please add a note first.\n')
        return
    
    print('\n--- 🗑 Current Notes ---')
    for i, note in enumerate(notes, start=1):
        print(f'{i}. {note.strip()}')
    print('---------------------\n')
    
    delete_index = input('Enter the number of the note to delete: ').strip()
    
    if not delete_index.isdigit():
        print('\n⚠️ Please enter a valid number.\n')
        return
    
    delete_index = int(delete_index)

    if 1 <= delete_index <= len(notes):
        deleted_note = notes.pop(delete_index - 1)
        with open('notes.txt', 'w') as file:
            file.writelines(notes)
        print(f'\n✅ Note "{deleted_note.strip()}" deleted successfully!\n')
    else:
        print('\n❌ Invalid note number!\n')


def show_menu():
    print('=' * 35)
    print('📓          NOTES MENU          📓 ')
    print('=' * 35)
    print('1️⃣  Add Note')
    print('2️⃣  View Notes')
    print('3️⃣  Search Note')
    print('4️⃣  Delete Note')
    print('5️⃣  Exit')
    print('=' * 35)


while True:
    show_menu()
    choice = input('\nChoose an option (1-5): ').strip()

    if choice == '1':
        add_note()
    elif choice == '2':
        view_notes()
    elif choice == '3':
        search_note()
    elif choice == '4':
        delete_note()
    elif choice == '5':
        print('\n👋 Program ended. Goodbye!\n')
        break
    else:
        print('\n⚠️  Invalid input! Please enter a number between 1 and 5.')