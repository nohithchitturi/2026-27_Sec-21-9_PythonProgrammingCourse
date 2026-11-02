total_input_numbers = int(input("Enter how many numbers: "))
largest = float(input("Enter a number: "))  
for i in range(total_input_numbers - 1): 
    number = float(input("Enter a number: "))  
    if number > largest:  
        largest = number  
print(f"Largest among {total_input_numbers} numbers is {largest}")