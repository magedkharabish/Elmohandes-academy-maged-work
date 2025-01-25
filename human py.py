class Human:

    def __init__(self, name, age, hair_color, eye_color):
        self.name = name
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color

    def eat(self, food):
        print(f'I can eat {food}')
    
    def drink(self, drank):
        print(f'{self.name} can drink {drank}')


class Doctor(Human):
    def check(self, patient_name):
        print(f"{self.name} is checking {patient_name}")


human1 = Human('mohamed', '23', 'black', 'brown')
human1.eat("koshary")
human1.drink('coffee')

print(human1.name)
print("==============================")

human2 = Human('kareem', '30', 'yellow', 'yellow')
human2.eat("mango")
human2.drink('tea')

doctor1 = Doctor('ahmed', '30', 'brown', 'brown')
doctor1.eat("meal")
doctor1.drink('juice')
doctor1.check('ali')
