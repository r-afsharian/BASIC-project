students = {}

def check_empty():
    if not students:
        print('\n ❌ The list is empty!\n')
        return True
    return False


def add_student():
    name = input("\nEnter the student's name: ").strip()
    grade_input = input("\n Enter the student's grade: ").strip()

    if name == '' or grade_input == '':
        print("\n❌ Name and grade cannot be empty!\n")
        return
    
    try:
        grade = float(grade_input)
    except ValueError:
        print('\n❌ Grade must be a number!\n')
        return
    
    students[name] = grade
    print(f"\n✅ Student {name} added successfully!\n")


def find_student():
    if check_empty():
        return

    search = input('\n🔍 Enter the name to search: ').strip()

    if search in students:
        print(f"\n🔹 {search}'s grade is {students[search]}")
    else:
        print('\n❌ Student not found!\n')


def min_max_grade():
    if check_empty():
        return
    
    highest = max(students, key=students.get)
    lowest = min(students, key=students.get)

    print("\n📊 Grade Summary:")
    print(f"Highest grade → {highest}: {students[highest]}")
    print(f"Lowest grade → {lowest}: {students[lowest]}")


def average_grade():
    if check_empty():
        return
    
    grade = students.values()
    average = sum(grade) / len(grade)
    print(f"\n📈 Average grade: {average:.2f}\n")


def view_students():
    if check_empty():
        return
    
    print("--- Student's List ---")
    for name, grade in sorted(students.items()):
        print(f"📃 {name}: {grade}")
    print('--------------\n')


def show_menu():
    print('\n' + '=' * 28)
    print('= STUDENT MANAGEMENT MENU =')
    print('=' * 28)
    print('1. Add Student')
    print('2. Find a Student')
    print('3. Minimum & Maximum Grade')
    print('4. Average Grade')
    print('5. View All Students')
    print('6. Exit')
    print('=' * 28)


while True:
    show_menu()
    choice = input('\nChoose an option (1-6): ').strip()

    if choice == '1':
        add_student()
    elif choice == '2':
        find_student()
    elif choice == '3':
        min_max_grade()
    elif choice == '4':
        average_grade()
    elif choice == '5':
        view_students()
    elif choice == '6':
        print('\nProgram ended. Goodbye! 👋')
        break
    else:
        print('\n❌ Invalid Option! Please enter a number between 1 and 6.\n')