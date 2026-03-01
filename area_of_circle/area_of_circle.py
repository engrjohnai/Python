

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