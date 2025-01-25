numbers = []

for i in range(5):
    num = float(input(f" Enter num {i+1}: "))
    numbers.append(num)

num1 = numbers[0]
for num in numbers:
    if num > num1:
        num1 = num

print("the greater num is :", num)
