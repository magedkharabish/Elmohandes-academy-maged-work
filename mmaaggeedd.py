class Person:
    def talk(self):
        print("I am speaking Arabic")

class AmericanPerson(Person):
    def talk(self):
        print("I am speaking English")

mohamed = Person()
mohamed.talk()

michael = AmericanPerson()
michael.talk()

class A:
    def do_something(self):
        print("I am A")

class B(A):
    def do_something(self):
        print("I am B")
        print("My parent is A")



a1 = A()
a1.do_something()

b1 = B()
b1.do_something()



       

       
       
