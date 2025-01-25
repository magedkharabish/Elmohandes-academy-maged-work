class RegistrationForm:
    def __init__(self, name, age, country, parent_no):
        self.name = name
        self.age = age
        self.country = country
        self.parent_no = parent_no

    def info(self):
        print(f"Hello, {self.name}!")  
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Country: {self.country}")
        print(f"Parent Number: {self.parent_no}")




while True:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    country = input("Enter your country: ")
    parent_no = input("Enter your parent number: ")

    if len(parent_no) > 10 or len(parent_no) < 10:
        print("Error: Parent number must have more than 10 digits.")
    student1 = RegistrationForm(name, age, country, parent_no)
    student1.info()
