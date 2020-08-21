### 8/13/2020
### Looping thru a dictionary

birthday_months = {
	'tony' : 'November',
	'pat'  : 'June', 
	'mary' : 'may',
}


print(birthday_months)

# looping thru key-value pairs

book_1 = {
	'name' : 'elon musk',
	'author' : 'ashlee vance',
	'price' : 14.99,
	'publisher' : 'virgin books',
}

print(book_1)


for key, value in book_1.items():
	print("\nKey: " + key)
	print("Value: " + value)