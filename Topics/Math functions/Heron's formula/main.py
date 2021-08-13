import math


def get_surface(side_1, side_2, side_3):
    half_perimeter = (side_1 + side_2 + side_3) / 2
    return math.sqrt(half_perimeter * (half_perimeter - side_1) * (half_perimeter - side_2) * (half_perimeter - side_3))


a = int(input())
b = int(input())
c = int(input())

print(get_surface(a, b, c))
