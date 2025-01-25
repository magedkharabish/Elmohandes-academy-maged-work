import time

user_name ="fatma"
password ="12345"
balance = 1500

counter = 0
while True:
    user_input=input("Enter user name ")
    password_entered=input("enter The Password ")

    if password_entered == password and user_input == user_name :
        
        print(f"Welcome {user_name}")
        withdraw = int(input("Enter The Amount you want to withdraw "))

        if balance >= withdraw:
            balance -= withdraw
            print("processing...")
            time.sleep(3)
            print("take your cash")
            print(f"your balance become {balance}")
            
        else:
            print("invalid amount")
        break
    
    else :
        print("Wrong information try again")
        counter=counter+1
        
    if counter == 3:
        print("من فضلك راجع حسابك البنكي")
        break
        
