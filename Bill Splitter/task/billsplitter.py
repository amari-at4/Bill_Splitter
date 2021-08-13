import random

print("Enter the number of friends joining (including you):")
number_of_people = int(input())
print()
if number_of_people <= 0:
    print("No one is joining for the party")
    exit()

party = dict()

print("Enter the name of every friend (including you), each on a new line:")
for _ in range(number_of_people):
    friend = str(input())
    party[friend] = 0

print()
print("Enter the total bill value:")
bill_value = int(input())
print()
print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
is_lucky = input()
print()
if is_lucky == "Yes":
    people = list(party.keys())
    lucky_one = people[random.randint(0, len(people) - 1)]
    number_sharing_bill = number_of_people - 1
    print(f"{lucky_one} is the lucky one!")
else:
    number_sharing_bill = number_of_people
    lucky_one = None
    print("No one is going to be lucky")


bill_per_person = round(bill_value / number_sharing_bill, 2)
if (bill_per_person * 10) % 10 == 0:
    bill_per_person = int(bill_per_person)
print()
for person in party:
    if person != lucky_one:
        party[person] = bill_per_person
print(party)
