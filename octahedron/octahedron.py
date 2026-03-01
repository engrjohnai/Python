
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