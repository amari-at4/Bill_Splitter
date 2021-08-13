# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
new_groups = dict.fromkeys(groups)

number_of_groups = int(input())
asked = 0

for key in groups:
    if asked < number_of_groups:
        new_groups[key] = int(input())
        asked += 1
    else:
        break

print(new_groups)
