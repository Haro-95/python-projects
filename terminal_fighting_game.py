available_fighters = {
"Charles Oliveira":"fighter_1",
"Khabib Nurmagomedov":"fighter_2",
"Alexander Volkanovski":"fighter_3",
"Dustin Poirier":"fighter_4",
"Bobby Green":"fighter_5"
}

fighter_options = [1, 2, 3, 4, 5]  # Shows initial number of fighters
opponent_options = [1, 2, 3, 4]  # Shows initial number of opponents

print('\n ***** Welcome to the fighting game **** \n')
print('What is your name? \n')
name = input('Please enter your name: ')

print(f'Hello {name}, choose one of the following fighters! \n')

for number, fighter in enumerate(available_fighters, start=1):  # Enumerate all available fighters
    print(f'{number}. {fighter}')
print()


def charles():
    strength = 5
    grappling = 5
    defence = 3   
    return strength * grappling * defence


def khabib():
    strength = 5
    grappling = 5
    defence = 4
    return strength * grappling * defence


def alexander():
    strength = 5
    grappling = 3
    defence = 4
    return strength * grappling * defence


def dustin():
    strength = 4
    grappling = 3
    defence = 3
    return strength * grappling * defence


def bobby():
    strength = 3
    grappling = 4
    defence = 2
    return strength * grappling * defence


while True:
    user_input = input('Enter your choice: ')
    print()
    try:
        user_input = int(user_input)
        if user_input in fighter_options:
            break
        else:
            print('Please enter a valid number!')
    except ValueError:
        print('Please enter a valid number!')

if user_input == 1:
    user_choice = 'Charles Oliveira'
    print(f'Your fighter is {user_choice} with power of {charles()}!')
    print()
elif user_input == 2:
    user_choice = 'Khabib Nurmagomedov'
    print(f'Your fighter is {user_choice} with power of {khabib()}!')
    print()
elif user_input == 3:
    user_choice = 'Alexander Volkanovski'
    print(f'Your fighter is {user_choice} with power of {alexander()}!')
    print()
elif user_input == 4:
    user_choice = 'Dustin Poirier'
    print(f'Your fighter is {user_choice} with power of {dustin()}!')
    print()
elif user_input == 5:
    user_choice = 'Bobby Green'
    print(f'Your fighter is {user_choice} with power of {bobby()}!')
    print()

print(f'Choose who will be the opponent of {user_choice}:')
print()


if user_choice in available_fighters:  # Enumerate all available fighters without the chosen one from the user
    available_fighters.pop(user_choice)
    for number, fighter in enumerate(available_fighters, start=1):  
        print(f'{number}. {fighter}')
    print()
else:
    print('Invalid choice!')


while True:
    opponent_input = input('Enter your choice: ')
    print()
    try:
        opponent_input = int(opponent_input)
        if opponent_input in opponent_options:
            break
        else:
            print('Please enter a valid number!')
    except ValueError:
        print('Please enter a valid number!')

if user_input == 1:
    fighter_power = charles()
    if opponent_input == 1:
        opponent_power = khabib()
    elif opponent_input == 2:
        opponent_power = alexander()
    elif opponent_input == 3:
        opponent_power = dustin()
    elif opponent_input == 4:
        opponent_power = bobby()

if user_input == 2:
    fighter_power = khabib()
    if opponent_input == 1:
        opponent_power = charles()
    elif opponent_input == 2:
        opponent_power = alexander()
    elif opponent_input == 3:
        opponent_power = dustin()
    elif opponent_input == 4:
        opponent_power = bobby()

if user_input == 3:
    fighter_power = alexander()
    if opponent_input == 1:
        opponent_power = charles()
    elif opponent_input == 2:
        opponent_power = khabib()
    elif opponent_input == 3:
        opponent_power = dustin()
    elif opponent_input == 4:
        opponent_power = bobby()

if user_input == 4:
    fighter_power = dustin()
    if opponent_input == 1:
        opponent_power = charles()
    elif opponent_input == 2:
        opponent_power = khabib()
    elif opponent_input == 3:
        opponent_power = alexander()
    elif opponent_input == 4:
        opponent_power = bobby()

if user_input == 5:
    fighter_power = bobby()
    if opponent_input == 1:
        opponent_power = charles()
    elif opponent_input == 2:
        opponent_power = khabib()
    elif opponent_input == 3:
        opponent_power = alexander()
    elif opponent_input == 4:
        opponent_power = dustin()

print(f'Your fighter has power of {fighter_power} and your opponent has power of {opponent_power}!')

if fighter_power > opponent_power:
    print('Congratulations, you won!')
else:
    print('Sorry, you lost.')
