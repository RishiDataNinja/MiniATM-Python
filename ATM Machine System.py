# 🚀 ATM Simulation Project using OOP in Python

class Atm:

    # Constructor - initializes pin and balance
    def __init__(self):
        self.pin = ''           # Stores ATM PIN
        self.balance = 0        # Stores account balance
        self.menu()              # Display menu after object creation

    # Main menu for user interaction
    def menu(self):
        while True:
            user_input = input("""
            Hi how can I help you
            1. Press 1 to create pin
            2. Press 2 to change pin
            3. Press 3 to check balance
            4. Press 4 to withdraw
            5. Anything else to exit
            """)

             # Handle user choices
            if user_input == '1':
                self.create_pin()
            elif user_input == '2':
                self.change_pin()
            elif user_input == '3':
                self.check_balance()
            elif user_input == '4':
                self.withdraw()
            elif user_input == '5':
                print("Thank you! Exiting now.")
                break
            else:
                print("Invalid choice. Please select 1 to 5 only.")

    # 🔐 Create a new PIN and set initial balance
    def create_pin(self):
        while True:
            user_pin = input('Enter a 4-digit numeric PIN: ')
            if user_pin.isdigit() and len(user_pin) == 4:
                self.pin = user_pin
                break
            else:
                print("❌ Invalid PIN format! Try again.")

        while True:
            try:
                user_balance = int(input('Enter initial balance (₹): '))
                if user_balance >= 0:
                    self.balance = user_balance
                    break
                else:
                    print("❌ Balance cannot be negative.")
            except ValueError:
                print("❌ Please enter a valid number!")

        print('✅ PIN created successfully!')

     # Change existing PIN
    def change_pin(self):
        old_pin = input('Enter your old PIN: ')
        if old_pin == self.pin:
            while True:
                new_pin = input('Enter new 4-digit PIN: ')
                if new_pin.isdigit() and len(new_pin) == 4:
                    self.pin = new_pin
                    print('✅ PIN changed successfully!')
                    break
                else:
                    print("❌ Invalid PIN format.")
        else:
            print('❌ Incorrect old PIN.')

    # Check balance after PIN verification
    def check_balance(self):
        entered_pin = input('Enter your PIN to check balance: ')
        if entered_pin == self.pin:
            print(f'💰 Your current balance is: ₹{self.balance}')
        else:
            print('❌ Incorrect PIN.')

     # Withdraw money from account
    def withdraw(self):
        entered_pin = input('Enter your PIN to withdraw: ')
        if entered_pin == self.pin:
            try:
                amount = int(input('Enter amount to withdraw (₹): '))
                if amount <= self.balance and amount > 0:
                    self.balance -= amount
                    print(f'✅ Withdrawal successful! Remaining balance: ₹{self.balance}')
                elif amount <= 0:
                    print("❌ Amount must be greater than 0.")
                else:
                    print('❌ Insufficient balance.')
            except ValueError:
                print("❌ Please enter a valid number.")
        else:
            print('❌ Incorrect PIN.')

# Create object of ATM class to start the program

obj = Atm()