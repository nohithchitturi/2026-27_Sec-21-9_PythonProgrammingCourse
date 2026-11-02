number=int(input("Enter a number: "))
original_number=number
reversed_number=0
while number>0:
    digit=number%10
    reversed_number=reversed_number * 10 + digit
    number=number // 10
print(f"Reverse of {original_number} is {reversed_number}")