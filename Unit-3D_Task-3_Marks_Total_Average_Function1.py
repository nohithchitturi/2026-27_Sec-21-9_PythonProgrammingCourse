def total_and_average(mark1,mark2,mark3):
    total=mark1+mark2+mark3
    average=(mark1+mark2+mark3)/3
    return total,average
mark1=int(input("Enter the marks"))
mark2=int(input("Enter the marks"))
mark3=int(input("Enter the marks"))
total,average=total_and_average(mark1,mark2,mark3)
print(f"Total={total}")
print(f"Average={average}")
