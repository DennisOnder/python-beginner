name = 'Dennis'
age = 18

print('Concatenation', 'Hello! My name is ' + name + ', and I am ' + str(age) + ' years old.')
print('Formatting', 'My name is {name}, and I am {age}.'.format(name=name, age=age))

# F-Strings
print('F-String/Template Literal', f'Hello, my name is {name}, and I am {age}.')

# String methods
s = 'hello world'

# Capitalize
print(s.capitalize())

# Uppercase
print(s.upper())

# Lowercase
print(s.lower())

# Length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Split into array/list
print(s.split())