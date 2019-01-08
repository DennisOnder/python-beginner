# Open file
my_file = open('myFile.txt', 'w')

# Get file info
print('Name: ', my_file.name)
print('Is closed: ', my_file.closed)
print('Mode: ', my_file.mode)

# Write to file
my_file.write('I love JavaScript.')
my_file.write(' And Python.')
my_file.close()

# Append to file
my_file = open('myFile.txt', 'a')
my_file.write(' I hate PHP.')
my_file.close()

# Read file
my_file = open('myFile.txt', 'r')
text = my_file.read(100)
print(text)