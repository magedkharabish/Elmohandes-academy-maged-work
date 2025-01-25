user_name = "Eman222"
passward = 2122011

balance = 20970

counter = 0

while True:
    user_name_input = input("Enter Your User Name")
    pass_input = int(input("Enter Your Password"))

    if  user_name_input == user_name and pass_input == passward:
     print("Hi",user_name)
    
    
        
    money =int(input("How much money do you need ? "))
    
     if money <= balance and money !=0:

          print ("Prossing")
          print ("Get your money cash")
          balance-=money
          print (f"Your balance ={balance}$")
          print ("Thank you for using El-Talib Bank")
          break
    
     else:
         print("Prossing")
         print("You Don't Have Enough Money")

     else:
         print("Erorr in your username or your password")
         counter+=1
    if counter ==3

    print("We stoped your aconut")
