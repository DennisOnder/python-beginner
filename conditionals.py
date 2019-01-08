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