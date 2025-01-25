class Calculator:

    def _init_(self):
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
