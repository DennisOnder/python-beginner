# Unchangeable list

# Create tuple
fruits = ('Apples', 'Mangos', 'Bananas')
fruits2 = tuple(('Apples', 'Mangos', 'Bananas'))

# Get value
print(fruits[1])

# Can't change values - example: fruits[0] = 'Whatever'

# Sets
fruits_set = {'Apples', 'Mangos', 'Bananas'}

# Check if in set
print('Apples' in fruits_set)

# Add to set
fruits_set.add('Grapes')

# Clear entire set
fruits_set.clear()
print(fruits_set)