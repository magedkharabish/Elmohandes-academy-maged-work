accounts = {
    'maged': 1000,
    'ahmed': 1999999,
    'somaya': 3000000,
    'roquaya': 3000000000000000000000000000000000000000000
}

passwords = {
    'maged': '1234',
    'ahmed': '12345',
    'somaya': '123456',
    'roquaya': '1234567'
}

def new_account(account_name, password):
    if account_name not in accounts:
        accounts[account_name] = 0
        passwords[account_name] = password
        print(f"New account for {account_name} created successfully.")
    else:
        print("Account already exists.")

def authenticate(account_name):
    password = input(f"Enter password for {account_name}: ")
    if passwords.get(account_name) == password:
        print("Authentication successful.")
        return True
    else:
        print("Incorrect password.")
        return False

def withdraw(balance, withdraw_amount):
    if withdraw_amount <= balance:
        print("Processing withdrawal...")
        print("Please take your cash.")
        balance -= withdraw_amount
        print("Withdrawal successful.")
        return balance
    else:
        print("Your balance is not enough for this withdrawal.")
        return balance

def deposit(balance):
    deposit_amount = int(input("Enter your deposit amount: "))
    balance += deposit_amount
    print(f"Deposit of {deposit_amount} successful.")
    return balance

def balance_information(balance):
    print(f'Your balance is: {balance} SR')

def transformation(from_account, balance):
    to_account = input("Which person do you want to transfer money to? ")
    if to_account in accounts:
        transfer_amount = int(input("How much money do you need to transfer? "))
        if transfer_amount <= balance:
            print('Processing transfer...')
            balance -= transfer_amount
            accounts[to_account] += transfer_amount
            print(f"Successful transfer of {transfer_amount} to {to_account}.")
        else:
            print("Not enough balance for transfer.")
    else:
        print("Invalid recipient account.")

while True:
    print("""Hello in ATM
    If you need a new account, enter 'new_account'
    If you already have an account, press '0'
    """)

    user = input("Which user would you like to perform? (new_account/0): ")

    if user == 'new_account':
        new_account_name = input('Enter a new account name: ')
        new_account_password = input('Enter a password for the new account: ')
        new_account(new_account_name, new_account_password)
        
    else:
        account = input('Enter your account name: ')

        if account in accounts:
            if authenticate(account):
                print(f'Hello, {account}')
                balance = accounts[account]

                process = input("""Which process would you like to perform?
                withdraw, deposit, balance_information, transformation: """)
                
                if process == 'withdraw':
                    withdraw_amount = int(input('How much money do you need to withdraw? '))
                    new_balance = withdraw(balance, withdraw_amount)
                    accounts[account] = new_balance

                elif process == 'deposit':
                    new_balance = deposit(balance)
                    accounts[account] = new_balance

                elif process == 'balance_information':
                    balance_information(balance)

                elif process == 'transformation':
                    transformation(account, balance)
                    new_balance = accounts[account]
                    accounts[account] = new_balance

                else:
                    print("Invalid process, please try again.")
            else:
                print("Failed to authenticate. Returning to main menu.")
        else:
            print("Account not found. Please try again.")
