class Person:
    def __init__(self, name, family_name, age, eye_color):
        self.name = name
        self.family_name = family_name
        self.age = age
        self.eye_color = eye_color

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Family Name: {self.family_name}")
        print(f"Age: {self.age}")
        print(f"Eye Color: {self.eye_color}")
person1 = Person("maged", "kharabish", 17, "black")
person1.display_info()
