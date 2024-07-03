side1 = int(input("Enter the a side1:"))
side2 = int(input("Enter the a side2:"))
side3 = int(input("Enter the a side3:"))

if side1 == side2 and side2 == side3:
    print("Equilateral Triangle")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print(" Isoceles triangle")
else:
    print("Scalene triangle")
