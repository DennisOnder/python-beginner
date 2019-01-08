x = 5
y = 5

if x > y:
    print(f'{x} is greater than {y}')
elif x == y:
    print(f'{x} is equal to {y}')    
else:
    print(f'{y} is greater than {x}')

# Nested statements
if x > 2:
    if x <= 10:
        print(f'{x} is qreater than 10, but less than or equal to 10.')

# Logical operators (and, or, not)
if x > 2 and x <= 10:
    print(f'{x} is qreater than 10, but less than or equal to 10.')

# Membership operators

numbers = [1,2,3,4,5]

if x in numbers:
    print(x in numbers)
elif x not in numbers:
    print(x not in numbers)

# Identity operators (is, is not)
if x is y:
    print(x is y)