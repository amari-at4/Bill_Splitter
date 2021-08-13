# the list "walks" is already defined
# your code here
mean = 0
days = 0
for walk in walks:
    days += 1
    mean += walk['distance']

print(mean // days)
