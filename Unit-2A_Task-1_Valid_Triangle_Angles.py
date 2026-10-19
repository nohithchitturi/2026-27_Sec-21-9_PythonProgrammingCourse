#check weather the angles are form valid triangle
angle1=float(input("Enter the angle1 in degrees:"))
angle2=float(input("Enter the angle2 in degrees:"))
angle3=float(input("Enter the angle3 in degrees:"))
if angle1 > 0 and angle2 > 0 and angle3 > 0 and angle1 +  angle2 + angle3 == 180:
    print(f"valid triangle(angles={angle1},{angle2},{angle3})")
else:
    print(f"not a valid triangle(angles={angle1},{angle2},{angle3})")
