list_data=[10,20,30]
try:
    index=int(input("Enter index:"))
    value=list_data[index]
    print("Value:", value)
except ValueError:
    print("Please enter a valid integer index.")
except IndexError:
    print("Index is out of range.")