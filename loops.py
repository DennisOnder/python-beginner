# For loop
people = ['Dennis', 'John', 'Paul', 'Brad', 'Sarah']

for person in people:
    print(f'Current person: {person}')

print('Break')

# Break
for person in people:
    if person == 'Brad':
        break
    else:
        print(f'Current Person: {person}')

print('Break')

# Range
for i in range(len(people)):
    print(people[i])

print('Break')

for i in range(0, 10):
    print(f'Number: {i}')

print('Break')

# While loop
count = 0

while count <= 10:
    print(f'Count: {count}')
    count += 1