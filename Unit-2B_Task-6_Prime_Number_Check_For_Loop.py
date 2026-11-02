number = int(input("Enter a number between 1 and 100: "))
count = 0

for i in range(1, number + 1):
    if number % i == 0:
        count = count + 1

if count == 2:
    print(f"{number} is a prime number (divisor count = {count})")
else:
    print(f"{number} is not a prime number (divisor count = {count})")