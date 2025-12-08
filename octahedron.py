"""
Octahedron
Report a typo

A regular octahedron is a three-dimensional geometric shape, a polyhedron with eight equal faces and twelve equal edges. Have you ever seen 8-sided dice? That's a regular octahedron. In this task you need to calculate its area and volume.

Write a program that reads a positive integer representing the edge length of the regular octahedron and prints two values – its area and volume (in that order), both rounded to 2 decimal places and split by one space.

Formula to calculate the area of an octahedron (a is edge length):

2∗3∗a22∗3

​∗a2

Formula to calculate the volume:

13∗2∗a331​∗2

​∗a3

Sample Input 1:

54

Sample Output 1:

10101.32 74229.24

"""
import math


def area_of_octahedron(x):
    area = 2 * math.sqrt(3) * pow(x, 2)
    return round(area, 2)


def volume_of_octahedron(x):
    volume = (1/3) * math.sqrt(2) * pow(x, 3)
    return round(volume, 2)


x = abs(int(input()))


area = area_of_octahedron(x)
volume = volume_of_octahedron(x)

print(f"{area} {volume}")