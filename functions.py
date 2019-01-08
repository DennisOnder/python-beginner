def sayHello(name = 'User'):
    print(f'Hello, {name}')

sayHello('Dennis')

# Return values
def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(2, 2))

# Lambda Functions
getAnotherSum = lambda num1, num2 : num1 + num2
print(getAnotherSum(3, 5))