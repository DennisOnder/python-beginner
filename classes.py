class User:
    # Constructor
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
    def greeting(self):
        return f'My name is {self.name}. I am {self.age} years old. My email address is {self.email}. Thanks!'

# Extend class
class Customer(User):
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email
        self.balance = 0
    def set_balance(self, balance):
        self.balance = balance
    def new_greeting(self):
        return f'My name is {self.name}. I am {self.age} years old. My email address is {self.email}. Also, my balance is {self.balance}. Thanks!'

# Initialize user object
dennis = User('Dennis', 18, 'dennisOnder@gmail.com')
janet = Customer('Janet', 22, 'janet@mail.com')

print(janet.greeting())
print(janet.new_greeting())