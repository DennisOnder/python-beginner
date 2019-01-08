# Similar to JS objects

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30
}

# Constructor
person2 = dict(first_name='Sarah', last_name='Williams', age=22)

# Get value
print(person['first_name'])
print(person.get('last_name'))

# Add key/value
person['phone'] = '555-555-5555'
print(person)

# Get all keys
print(person.keys())

# Get all items
print(person.items())

# Copy dictionary
person2 = person.copy()
print(person2)
