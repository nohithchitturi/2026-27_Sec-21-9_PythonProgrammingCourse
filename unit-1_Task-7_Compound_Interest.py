Principal=int(input("Enter the amount:"))
Rate=int(input("Enter the rate of interest:"))
Time=int(input("Enter the time:"))
Amount=Principal * (1+Rate/100) ** Time
Compoundintrest= Amount-Principal
print(Compoundintrest)