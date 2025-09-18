import random

print('Welcome to the Guessing Game!\n')

play = True

while play:

    print('I picked a number from 1 to 50. Try to guess it.\n')
    sec_num = random.randint(1, 50)
    attempts = 0

    while True:

        user_input = input('Enter your guess (or type q to quit.): ').strip().lower()
        
        if user_input in ('quit', 'q'):
            print('Exiting the game... Goodbye!')
            exit()

        if user_input == '':
            print('You did not type anything.\n')
            continue
        
        try:
            guess = int(user_input)
        except ValueError:
            print('Please only enter a number, e.g. 18.\n')
            continue

        if guess < 1 or guess > 50:
            print('Please enter a number between 1 and 50.\n')
            continue
        
        attempts += 1

        if guess < sec_num:
            print('Try higher\n')
        elif guess > sec_num:
            print('Try lower\n')
        else:
            print(f'Well Done! You guessed it in {attempts} attempts\n')
            break
    
    while True:

        next_round = input('Do you wish to play again? (yes/no): ').strip().lower()

        if next_round in ('yes', 'y'):
            play = True
            break
        elif next_round in ('no', 'n'):
            play = False
            print('Goodbye!')
            break
        else:
            print('Invalid input. Enter YES or NO.\n')