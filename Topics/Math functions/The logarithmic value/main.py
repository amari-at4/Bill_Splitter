import math

first_number = int(input())
second_number = int(input())

if second_number > 1:
    result = math.log(first_number, second_number)
else:
    result = math.log(first_number)

print(round(result, 2))
