import json

# Sample JSON
userJSON = '{"firstName": "John","lastName": "Doe","age": 30}'

# Parse
user = json.loads(userJSON)

# JSONify
car = {
    'make': 'Ford',
    'model': 'Mustang',
    'year': 1968
}

carJSON = json.dumps(car)

print(f'Parsed JSON: {user}\nStringified JSON: {carJSON}')
