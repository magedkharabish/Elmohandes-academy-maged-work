class RegistrationForm:
    def __init__(self, name, age, country, parent_no):
        self.name = name
        self.age = age
        self.country = country
        self.parent_no = parent_no

    def info(self):
    

student1 = RegistrationForm('Maged', 17, 'Jeddah', '0571301417')
student1.info()
