### 8/25/2020
### The else block

print("Please enter two number to be divided. ")
print("Enter 'q' to quit")


while True:
	first_number = input("\nFirst Number: ")
	if first_number == 'q':
		break

	second_number = input("Second number: ")
	try:
                answer = int(first_number / int(second_number))
	except ZeroDivisionError:
		print("You can not divide by 0!")
	else:
		print(answer)
