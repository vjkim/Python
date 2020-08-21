terms = {'variable': 'represents or refers to a value','string': 'a sequence of characters'}

if 'float' in terms:
	print("I know what a float is.")
else:
	print("I have no idea what a float is.")

print("Variable: " + [terms['variable']])
print([terms['string']])