
import math

def circle_calc(r):
    area = round((math.pi * r ** 2), 2)
    circumference = round((2 * math.pi * r), 2)
    diameter = round((2 * r), 2)
    return area, circumference, diameter


r = float(input("Enter the radius if the circle: "))
print(circle_calc(r))
