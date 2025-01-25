products = {
    "Apple": 3.5,
    "Orange": 4.0,
    "Banana": 2.5,
    "Grapes": 5.0,
    "Pomegranate": 6.0
}

print("Welcome! Here's the list of products and their prices per kilogram:\n")
for product, price in products.items():
    print(f"{product}: {price} USD/kg")

cart = {}
print("\nAdd items to your cart. Type 'exit' when you are done.\n")

while True:
    item = input("Enter the product name: ")
    if item.lower() == "exit":
        break
    if item in products:
        quantity = float(input("Enter the quantity in kilograms: "))
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
    else:
        print("Product not found. Please try again.")

total = 0
print("\nCart Details:\n")
for item, quantity in cart.items():
    price = products[item] * quantity
    total += price
    print(f"{item}: {quantity} kg × {products[item]} USD = {price:.2f} USD")

print(f"\nTotal Price: {total:.2f} USD")



