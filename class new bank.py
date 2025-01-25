class BankAccount:
    def __init__(self, account_name, password, balance=0):
        self.account_name = account_name
        self.password = password
        self.balance = balance

    def authenticate(self, password):
        if self.password == password:
            print("Authentication successful.")
            return True
        else:
            print("Incorrect password.")
            return False

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawal successful.")
            print(f"Please take your cash: {amount}")
        else:
            print("Insufficient funds for this withdrawal.")
        
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} successful.")

    def check_balance(self):
        print(f"Your balance is: {self.balance} SR")

    def transfer(self, to_account, amount):
        if amount <= self.balance:
            self.balance -= amount
            to_account.balance += amount
            print(f"Transferred {amount} SR to {to_account.account_name}.")
        else:
            print("Not enough balance for transfer.")

class ATM:
    def __init__(self):
        self.accounts = {}
        
    def create_account(self, account_name, password):
        if account_name not in self.accounts:
            self.accounts[account_name] = BankAccount(account_name, password)
            print(f"New account for {account_name} created successfully.")
        else:
            print("Account already exists.")
            
    def get_account(self, account_name):
        return self.accounts.get(account_name)

def main():
    atm = ATM()
    
    while True:
        print("""Hello in ATM
        If you need a new account, enter 'new_account'
        If you already have an account, press '0'
        """)

        user_input = input("Which user would you like to perform? (new_account/0): ")

        if user_input == 'new_account':
            new_account_name = input('Enter a new account name: ')
            new_account_password = input('Enter a password for the new account: ')
            atm.create_account(new_account_name, new_account_password)

        elif user_input == '0':
            account_name = input('Enter your account name: ')
            account = atm.get_account(account_name)

            if account:
                password = input(f"Enter password for {account_name}: ")
                if account.authenticate(password):
                    print(f'Hello, {account_name}')

                    while True:
                        process = input("""Which process would you like to perform?
                        withdraw, deposit, balance_information, transformation, exit: """)

                        if process == 'withdraw':
                            amount = int(input('How much money do you need to withdraw? '))
                            account.withdraw(amount)

                        elif process == 'deposit':
                            amount = int(input("Enter your deposit amount: "))
                            account.deposit(amount)

                        elif process == 'balance_information':
                            account.check_balance()

                        elif process == 'transformation':
                            to_account_name = input("Which person do you want to transfer money to? ")
                            to_account = atm.get_account(to_account_name)
                            if to_account:
                                amount = int(input("How much money do you need to transfer? "))
                                account.transfer(to_account, amount)
                            else:
                                print("Invalid recipient account.")

                        elif process == 'exit':
                            print("Exiting... Goodbye!")
                            break

                        else:
                            print("Invalid process, please try again.")
                else:
                    print("Failed to authenticate. Returning to main menu.")
            else:
                print("Account not found. Please try again.")
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
