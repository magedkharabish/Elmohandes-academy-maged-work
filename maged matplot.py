from matplotlib import pyplot as plt
import numpy as np
salary_list=[]
counter = 0
while counter <10:
    salary=int(input("enter your salary "))
    salary_list.append(salary)
    counter+=1
xpoint = np.array(['mohamed','ali','amr','nour','maged','ahmed','somaya','roquaya','kareem','omar'])
ypoint=np.array(salary_list)
plt.plot(xpoint,ypoint)
plt.show()
