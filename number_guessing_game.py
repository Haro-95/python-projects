import random

print()
print('***** Welcome to the number guessing game ***** \n')
print('I have selected a number between 1 and 100. Try to guess it in 5 attempts.')

attempts = 5
while attempts != 0:
    
    try:
        secret_number = random.randint(1, 100)
        for attempt in range(attempts):
            guess = int(input('Enter your guess: '))
            
            if guess.is_integer:
                attempts -= 1

            if guess == secret_number:
                print(f'Congratulations! You guessed the correct number in {attempt + 1} attempts')
                break

            elif guess < secret_number:
                print('Your number is too low, try again!')
            elif guess > secret_number:
                print('Your number is too high, try again!')
    
        else:
            print(f"\nSorry you've ran out of attempts. The correct number is {secret_number}. Try again.")
            print()

    except ValueError:
        print('Enter a valid number between 1 and 100!')
