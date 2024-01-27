class BankAccount:

    deposits_counter = 0
    withdrawal_counter = 0

    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
        print(f'Account {self.name} created!')

    def show_balance(self):
        return f'\nYour balance is ${self.balance:.2f}\n'

    def deposit(self, amount):
        self.balance += amount
        self.deposits_counter += 1

        return '\nSuccessful deposit!\n'

    def withdraw(self, amount):
        if amount > self.balance:
            return '\nInsufficient funds!\n'
        else:
            self.balance -= amount
            self.withdrawal_counter += 1
            return '\nSuccessful withdrawal\n'

    def password_verification(self):
        try:
            code = int(input('\nPlease enter your PIN code: '))
            if user_code == code:
                return True
            else:
                return False
        except ValueError:
            print('Incorrect PIN, please try again.')


while True:
    user_name = input('Please, enter your name: ')
    if not user_name.isdigit():
        break
    else:
        print('Please enter a valid name!')

while True:
    try:
        user_balance = int(input('Please, enter your initial balance: '))
        break
    except ValueError:
        print('Please enter a valid number!')
        continue

while True:
    user_code = (input(f'Hello {user_name}, please choose a 4-digit PIN code: '))
    if user_code.isdigit() and len(user_code) == 4:
        user_code = int(user_code)
        break
    else:
        print('Please enter a valid 4 digit code!')

print()
app = BankAccount(user_name, user_balance)
print()

while True:
    print('1. Balance \n2. Deposit \n3. Withdrawal \n4. Deposit Statistic \n5. Withdrawal Statistic \n6. Exit')

    try:
        operation = int(input('Choose operation (1-6): '))
    
        if operation == 1:
            print()
            attempts = 3
            while attempts != 0:
                if app.password_verification():

                    print(app.show_balance())
                    break
                else:
                    print(f'Wrong code! Please try again! {attempts - 1} attempts left.')
                    attempts -= 1

        elif operation == 2:
            print()
            deposit_amount = int(input('Please enter the amount you want to deposit: '))
            deposit_result = app.deposit(deposit_amount)
            print(deposit_result)

        elif operation == 3:
            print()
            attempts = 3
            while attempts != 0:
                if app.password_verification():
                    withdrawal_amount = int(input('Please enter the amount you want to withdrawal: '))
                    withdrawal_result = app.withdraw(withdrawal_amount)
                    print(withdrawal_result)
                    break
                else:
                    print(f'Wrong code! Please try again! {attempts - 1} attempts left.')
                    attempts -= 1

        elif operation == 4:
            print(f'You have made {app.deposits_counter} deposits in total!\n')
        elif operation == 5:
            print(f'You have made {app.withdrawal_counter} withdrawals in total!\n')
        elif operation == 6:
            break

    except ValueError:
        print('\nPlease enter a valid number!\n')
