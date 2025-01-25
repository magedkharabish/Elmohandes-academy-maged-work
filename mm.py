import  pygame
import time
pygame.mixer.init()


pygame.mixer.music.load("Cash_Machine.wav")
user_name = 'maged'
password = '1231233'

balance = 800000000000
counter = 0
while True :
    user_input = input('enter your user name: ')
    
    password_input = input('enter your password: ')
    if user_input == user_name and password_input == password:
        print ('hello',user_name)
        withdraw = float(input('how much money do you need ? '))
        if withdraw <= balance and withdraw !=0 :
            pygame.mixer.music.play()
            print("prococeing..")
            time.sleep(7)
            print("get your cash.")
            time.sleep(3)
            balance -=withdraw
            print(f'your balnce is ={balance}SR')
            time.sleep(5)
            print("thank you for useing maged bank (; ")
            pygame.mixer.music.stop()
        else:
            print("your balane is not enough!!")
    else:
            print("error in username or password ")
            counter +=1
            if counter==3:
                print("your acc had been blocked")
                break
            
