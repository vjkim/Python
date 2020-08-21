### 8/13/2020
### Other ways to loop thru a dictionary

birthday_months = {
	'tony' : 'November',
	'pat'  : 'June', 
	'mary' : 'may',
}

for name in birthday_months.keys():
	print(name.title())


for months in birthday_months.values():
	print(months.title())

for months in set(birthday_months.values()):
	print(months.title())
