### 8/10/2020
### Using a key to get a value


# Create a dictionary of terms
terms = {'variable': 'represents or refers to a value stored in memory', 'string': 'a sequence of characters'}

if 'float' in terms:
	print("i know what a float is.")
else:
	print("i have no idea what a float is.")
print(terms['variable'])

#creat an empty dictionary
terms = {}

terms['variable'] = 'represents or refers to a value stored in memory'
terms['integer'] = 'a whole number'

print(terms['variable'])
print(terms['integer'])