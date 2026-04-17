import math

#volume of sphere
radius = float(input("Enter radius of the sphere: "))
volume = round(4/3*math.pi*pow(radius,3),2)
print(f"The volume of sphere is {volume}cm^3")


#Area of a circle
radius2 = float(input(f"Enter the radius of circle: "))
Area = round(math.pi*pow(radius2,2),2)
print(f"The are of the circle is {Area}cm^2")


#the hypothesis of the triangle
x = float(input("Enter the length of the triangle: "))
y = float(input("Enter the width of the triangle: "))
hypo = round(math.sqrt(pow(x,2)+pow(y,2)))
print(f"The hypothesis of the triangle is {hypo}cm")

