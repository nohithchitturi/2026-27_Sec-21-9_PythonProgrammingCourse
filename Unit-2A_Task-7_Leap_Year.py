year = int(input("Enter a year: "))

if year % 4 == 0: 
    print(f"{year} is a leap year")
else:
    if year % 100 == 0:  # nested check
        print(f"{year} is not a leap year")
    else:
        if year % 400 == 0:  # innermost check
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")