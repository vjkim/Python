### 8/26/2020
### A function to test

from test_funtion_1 import get_formatted_name

print("Enter 'q' to quit this program. ")

while True:
	first = input("\nPlease enter your first name: ")
	if first == 'q':
		break

	last = input("\nPlease enter your last name: ")
	if last == 'q':
		break

	formatted_name = get_formatted_name(first, last)
	print("Your name is " + formatted_name + '.')

	