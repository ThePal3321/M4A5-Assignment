import math

radius_str = input("What is the radius of your circle?: ")
radius = float(radius_str)
area = math.pi * (radius ** 2)
print(f"Your circle with the radius {radius} is: {area}")
