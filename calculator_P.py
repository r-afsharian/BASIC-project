while True:

    num1 = int(input('\n1st number: '))
    num2 = int(input('2nd number: '))

    print('\nOperations List:')
    print('1. Addition (+)')
    print('2. Subtraction (-)')
    print('3. Multiplication (*)')
    print('4. Division (/)')
    print('5. Power (^)\n')
    
    choice = input('Choose an option (1-5): \n')

    if choice == '1':
        result = num1 + num2
        print('Result:', result)
    
    elif choice == '2':
        result = num1 - num2
        print('Result:', result)

    elif choice == '3':
        result = num1 * num2
        print('Result:', result)
    
    elif choice == '4':
        if num2 != 0:
            result = num1 / num2
            print('Result:', result)
        else:
            print('Error: Division by zero is impossible!')

    elif choice == '5':
        result = num1 ** num2
        print('Result:', result)

    else:
        print('Invalid Option! Please Choose between 1 and 5.')

    
    while True:
        again = input('\nDo you want to continue? (yes/no)').strip().lower()

        if again in ('yes', 'y'):
            should_continue = True
            break
        
        elif again in ('no', 'n'):
            should_continue = False
            break

        else:
            print('Please enter YES or NO.')

    if not should_continue:
        print('Goodbye!')
        break