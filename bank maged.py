




accounts = {'maged':1000 ,
            'ahmed': 2000 ,
            'somaya':99999999 ,
            'roquaya':5000 ,
            }

def withdraw(balance, withdraw_account):
    if withdraw_ammount <= balance:
        print("prossing")
        print("get cash")
        balance -= withdraw_ammount
        print("sussful")
        return balance
    
    else:
        print("your balance is not enough")
def deposite(balance):
   deposite_account_ammount = int (input("enter your deposite"))
   balace += deposit_ammount
   print("susscessful deposit proces")
   print(" procesing")
   return balance
        
   
def balance_information(balance):
    print(f'your balance is = {balance} SR')
def transformation(from_account,balance,all_account):
    to_account = input ("wnich person you want to transfer")
    if to_account in all_account:
        print('ok')
        transformation_ammount = int(input("how much money do you need to transfer"))
        if transformation_ammount <= balance:
                                     print('prossing')
                                     balance -= transformation_ammount
                                     all_account[to_account] += transformation_ammount
                                     
                







    
    pass

while True:
    account = input ('enter your account name :')
    if account in accounts :
        print('hello',account)
        balance = accounts[account]
        procces = input ("which procces (withdraw,deposit,balance_information,transformation")
        if procces == 'withdraw':
            withdraw_ammount = int(input('how much money do you need'))
            newbalace=0
            new_balance=withdraw (balance,withdraw_ammount)
            accounts[account]= new_balance
        elif procces == 'deposite':
           new_balance = deposit(balance)
           account[account] = new_balance
           
        elif procces == 'balance_information':
            balance_information(balance)
        elif procces == 'transformation':
            transformation(account,balance,accounts)
          
        else:
            print("repeat long in ")

            
