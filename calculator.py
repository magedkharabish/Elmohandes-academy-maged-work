class Calculator:

    def _init_(self):
        

        print("""
Hello welcome in your Calculator
your markers are :

+ : summition
- : subtractor
* : multiply
/ : division
= : equal
""")

        first_number = float(input("Enter the first number :"))
        while True:
            marker = input('Enter the marker ( + , - , * , / , = :)')
            if marker == '=':
                print(first_number)
                flag = self.equal()
                if flag == 0:
                    break
                else:
                    marker = input('Enter the marker ( + , - , * , / :)')
                    
                
            another_number = float(input("Enter the another number :"))

            if marker == '+':
                r = self.summition(first_number,another_number)
                first_number = r
                
            elif marker == '-':
                r = self.subtractor(first_number,another_number)
                first_number = r

            elif marker == '*':
                r = self.multiply(first_number,another_number)
                first_number = r

            elif marker == '/':
                r = self.devision(first_number,another_number)
                first_number = r

            else:
                print('incorrect marker')
    
##############################################    

    def summition(self,num1,num2):
        result = num1 + num2
        return result

    def subtractor(self,num1,num2):
        result = num1 - num2
        return result

    def multiply(self,num1,num2):
        result = num1 * num2
        return result

    def devision(self,num1,num2):
        result = num1 / num2
        return result

    def equal(self):
        check_complete = input("Do you want to continue ? (y/n) :")
        if check_complete == 'y':
            return 1
        else:
            return 0

while True:
    c =   Calculator()
