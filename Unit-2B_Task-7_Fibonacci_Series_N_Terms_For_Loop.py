n = int(input("Enter how many terms: "))
first = 0
second = 1

for i in range(1, n + 1):
    print(f"Fibonacci series term {i} of {n} terms = {first}")
    next_term = first + second
    first = second
    second = next_term