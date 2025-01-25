from  matplotlib import pyplot as plt
import numpy as np 

salary_list=[]
counter=0

while counter<10:
  salary=int(input("enter your salary "))
  salary_list.append(salary)
  counter+=1

xpoint = np.array(['mohamed','ahmad','adam','omar','amr','nour','ali','hana','mohab','aliaa'])
ypoint= np.array(salary_list)

plt.plot(xpoint,ypoint)

plt.show()




  
  
  
