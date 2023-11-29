import random
from cryptography.fernet import Fernet

# Setting variables
capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
small_letters = 'abcdefghijklmnopqrstuvwxyz'
special_characters = '!@#$%^&*_+=-":?/'
numbers = '0123456789'

password_combination_1 = capital_letters + small_letters
password_combination_2 = capital_letters + small_letters + special_characters
password_combination_3 = capital_letters + small_letters + numbers
password_combination_4 = capital_letters + small_letters + special_characters + numbers

# Requesting input

while True:
    try:
        user_input_length = int(input("Please enter your password length: "))
        if 1 <= user_input_length <= 20:
            break
        else:
            print('Please enter number between 1 and 20!')
    except ValueError:
        print('Please enter number between 1 and 20! \n')

user_input_characters = input("Do you want to include special characters? ").lower()
user_input_numbers = input("Do you want to include numbers? ").lower()


# Logic
password_version_1 = "".join(random.sample(password_combination_1, user_input_length))
password_version_2 = "".join(random.sample(password_combination_2, user_input_length))
password_version_3 = "".join(random.sample(password_combination_3, user_input_length))
password_version_4 = "".join(random.sample(password_combination_4, user_input_length))

# Check for equality

if user_input_characters == 'yes' and user_input_numbers == 'yes':
    print(f'Your password is: {password_version_4}')
elif user_input_characters == 'no' and user_input_numbers == 'no':
    print(f'Your password is: {password_version_1}')
elif user_input_characters == 'yes' and user_input_numbers == 'no':
    print(f'Your password is: {password_version_2}')
elif user_input_characters == 'no' and user_input_numbers == 'yes':
    print(f'Your password is: {password_version_3}')

else:
    print('Something went wrong. Please, try again. ')

encryption_question = input('\nDo you want to encrypt your password? ').lower()

if encryption_question == 'yes':
    key = Fernet.generate_key()
    f = Fernet(key)
    token = f.encrypt(b"password_version_4")
    file = open('encrypted_password.txt', 'x')
    file.writelines(f'Here is your encrypted password: \n {token}')
    file.close()



else:
    print('\nGoodbye!')

