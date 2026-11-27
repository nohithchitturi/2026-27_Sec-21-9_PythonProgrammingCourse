try:
    a=int(input("Enter number:"))
    b=int(input("Enter number:"))
    result=a/b
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Please enter valid number.")
else:
    print("Result:",result)
finally:
    print("Program finished.")
