### 8/13/2020
### Using a flag to stop the program

prompt = "Enter 'q' to end this program."
prompt += "\nWhat is your name?"

#set our flag to true

active = True

while active:
	message = input(prompt)

	if message == 'q':
		active = false
	else:
		print(message)

		