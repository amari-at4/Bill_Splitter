import math


def cotangent(radius):
    return round(1 / math.tan(math.radians(radius)), 10)


print(cotangent(int(input())))
