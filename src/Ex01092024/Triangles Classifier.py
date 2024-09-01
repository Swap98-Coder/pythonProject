# Triangle Program

Side1 = float(input("Enter the lenght of Side1"))
Side2 = float(input("Enter the lenght of Side2"))
Side3 = float(input("Enter the lenght of Side3"))

if Side1 == Side2 == Side3:
    print("Equilateral Triangle")
elif Side1 == Side2 != Side3:
    print("Isosceles Triangle")
elif Side2 == Side3 != Side1:
    print("Isosceles Triangle")
elif Side3 == Side1 != Side2:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
