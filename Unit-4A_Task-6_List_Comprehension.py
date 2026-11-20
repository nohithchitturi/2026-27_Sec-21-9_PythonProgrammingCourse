list_data = range(1, 11)  
list_squares = [x * x for x in list_data]
list_evens = [x for x in list_data if x % 2 == 0]
print("Squares:", list_squares)
print("Evens:", list_evens)