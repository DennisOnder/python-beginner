import camelcase
from datetime import date
from time import time as timestamp

# Custom module
from validator import validate_email as validateEmail

today = date.today()
time = timestamp()
c = camelcase.CamelCase()
is_email = validateEmail('dennisOnder@gmail.com')

print(today, time)
print(c.hump('hello there world'))
 
if is_email == True:
    print('Email is valid.')
else:
    print('Email invalid.')