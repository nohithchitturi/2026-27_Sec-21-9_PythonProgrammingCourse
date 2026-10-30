
num1 = int(input("Enter the number: "))
num2 = int(input("Enter the number: "))
num3 = int(input("Enter the number: "))

if num1 <= num2:
    if num1 <= num3:
        smallest = num1
    else:
        smallest = num3
else:
    if num2 <= num3:
        smallest = num2
    else:
        smallest = num3

print(f"Smallest = {smallest} (among {num1}, {num2}, {num3})")
