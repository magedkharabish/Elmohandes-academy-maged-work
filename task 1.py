while True:
    try:
        number = float(input("Enter a number (negative to break): "))
        if number < 0:
            print("Negative number entered")
            break
        else:
            print(f"You entered: {number}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
