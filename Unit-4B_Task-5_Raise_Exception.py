try:
    age=int(input("Enter age:"))
    if age < 0:
        raise ValueError("Age cannot be nagative.")
    print("Valid age:",age)
except ValueError as error:
    print("Error:",error)