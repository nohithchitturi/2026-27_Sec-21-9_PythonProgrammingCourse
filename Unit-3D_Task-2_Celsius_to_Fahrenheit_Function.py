def celsius_to_fahrenheit(celsius):
    fahrenheit=(celsius*9/5)+32
    return fahrenheit
celsius=int(input("Enter the celsius:"))
f = celsius_to_fahrenheit(celsius)
print(f"Fahrenheit={f}")
