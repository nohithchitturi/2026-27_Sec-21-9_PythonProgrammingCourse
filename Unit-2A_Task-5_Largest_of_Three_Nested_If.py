
Number1 = int(input("Enter a number1: "))
Number2 = int(input("Enter a number2: "))
Number3 = int(input("Enter a number3: "))

if Number1 >= Number2:
    if Number1 >= Number3:
        largest = Number1
    else:
        largest = Number3
else:
    if Number2 >= Number3:
        largest = Number2
    else:
        largest = Number3

print(f"Largest = {largest} among {Number1}, {Number2}, {Number3}")
