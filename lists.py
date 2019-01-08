numbers = [1, 2, 3, 4, 5]
fruits = ['Apples', 'Oranges', 'Pears']

# Constructor
numbers2 = list((1, 3, 5, 7, 9))

# Get single value
print(fruits[1])

# Get length
print(len(fruits))

# Append to list
fruits.append('Mangos')

# Remove from list
fruits.remove('Apples')

# Insert
fruits.insert(0, 'Strawberries')

# Remove from position
fruits.pop(1)

# Reverse list
fruits.reverse()

# Sort list
fruits.sort()

# Change value
fruits[1] = 'Blueberries'
print(fruits)
