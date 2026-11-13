def area_perimeter(length,breadth):
    area=length*breadth
    perimeter=2*(length*breadth)
    return area,perimeter
length=int(input("Enter the length:"))
breadth=int(input("Enter the breadth:"))
area,perimeter=area_perimeter(length,breadth)
print(f"Area={area}")
print(f"Perimeter={perimeter}")
