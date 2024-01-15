class Calculator:

    def __init__(self, num1, num2):     
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        if self.num2 == 0:
            raise ValueError('Cannot divide by 0!')
        else:
            return self.num1 / self.num2


all_operations = ['+', '-', '*', '/']
print()
    
operation = input("Choose operation (+, -, *, /): ")
while operation not in all_operations:
    print('Please enter valid operation!')
    operation = input("Choose operation (+, -, *, /): ")

while True:
    try:
        user_first_number = float(input('Enter your first number: '))
        user_second_number = float(input('Enter your second number: '))
        break
    except ValueError:
        print('Please enter a valid number!')

app = Calculator(user_first_number, user_second_number)

if operation == '+':
    if not user_first_number.is_integer() and not user_second_number.is_integer():
        print(f'{user_first_number} + {user_second_number} = {app.addition():.2f}')
    else:
        user_first_number = int(user_first_number)
        user_second_number = int(user_second_number)
        print(f'{user_first_number:.0f} + {user_second_number:.0f} = {app.addition():.0f}')
elif operation == '-':
    if not user_first_number.is_integer() and not user_second_number.is_integer():
        print(f'{user_first_number} - {user_second_number} = {app.subtraction():.2f}')
    else:
        user_first_number = int(user_first_number)
        user_second_number = int(user_second_number)
        print(f'{user_first_number:.0f} - {user_second_number:.0f} = {app.subtraction():.0f}')
elif operation == '*':
    if not user_first_number.is_integer() and not user_second_number.is_integer():
        print(f'{user_first_number} * {user_second_number} = {app.multiplication():.2f}')
    else:
        user_first_number = int(user_first_number)
        user_second_number = int(user_second_number)
        print(f'{user_first_number:.0f} * {user_second_number:.0f} = {app.multiplication():.0f}')
elif operation == '/':
    try:
        if not user_first_number.is_integer() and not user_second_number.is_integer():
            print(f'{user_first_number} / {user_second_number} = {app.division():.2f}')
        else:
            user_first_number = int(user_first_number)
            user_second_number = int(user_second_number)
            print(f'{user_first_number:.0f} / {user_second_number:.0f} = {app.division():.0f}')
    except ValueError as error:
        print(error)
