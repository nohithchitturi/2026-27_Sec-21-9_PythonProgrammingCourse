def simple_interest(principal,time,rate=8):
    simple_interest=(principal*time*rate)/100
    return simple_interest
principal=int(input("Enter the principal:"))
time=int(input("Enter the time:"))
rate=int(input("Enter the rate:"))
simple_interest=simple_interest(principal,time,rate)
print(f"Simple_interest={simple_interest}")