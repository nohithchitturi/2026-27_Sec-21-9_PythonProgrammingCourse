total_input_numbers = int(input("Enter how many numbers:"))
total_sum = 0
for input_index in range(total_input_numbers):
    entered_number = float(input("Enter a number:"))
    total_sum = total_sum + entered_number
    average = total_sum / total_input_numbers
    print(f"sum = {total_sum}")
    print(f"Average = {average}")