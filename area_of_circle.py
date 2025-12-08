"""
Calculating circle area from radius
Report a typo

Write a program that calculates the area of a circle given its radius. The program should use the math module to get the value of pi. The input will be a single float representing the radius, and the output should be the calculated area rounded to 2 decimal places.

Sample Input 1:

5.0

Sample Output 1:

78.54

Sample Input 2:

2.5

Sample Output 2:

19.63
"""
"""
import math

r = float(input())

area = math.pi * pow(r, 2)
area = round(area, 2)

print(area)



"""

# Import the math module to use the value of pi
import math
# Define a function to calculate the area of a circle
def calculate_circle_area(radius):
    # Your code here
    area = math.pi * pow(radius, 2)
    return round(area, 2)
    # Return the calculated area rounded to 2 decimal places


# Read the radius as a float from input
radius = float(input())

# Call the function with the radius and print the result

result = calculate_circle_area(radius)
print(result)