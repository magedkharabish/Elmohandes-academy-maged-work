while True: 
    name = input('Enter your name (or type "exit" to quit): ')
    age = input('Enter your age: ')
    print('Hello ' + name)
    print('Your age is ' + age)
    if name.lower() == "exit":
        print("Goodbye!")
        break
    

