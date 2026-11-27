# Example solution: ZeroDivisionError and ValueError
try:
    num = float(input("Enter numerator: "))
    den = float(input("Enter denominator: "))
    print("Quotient:", num / den)
except ZeroDivisionError:
    print("Denominator cannot be zero.")
except ValueError:
    print("Please enter valid numbers.")