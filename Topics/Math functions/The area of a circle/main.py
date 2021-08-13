import math


def circle_area(radius):
    return round(math.pi * pow(radius, 2), 2)


print(circle_area(int(input())))
