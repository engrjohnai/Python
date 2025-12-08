"""
Sine and cosine
Report a typo

Write a program that reads a value representing an angle (in radians), and prints the difference between its sine and cosine.

Do not round the result.

Sample Input 1:

1.96

Sample Output 1:

1.3046632855763227
"""
import math

x = float(input())


result = math.sin(x) - math.cos(x)


print(result)