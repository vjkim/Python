### 8/25/2020
### Storing and reading user data

import json

username = input("What is your username? ")

filename = 'username.json'
with open(filename, 'w') as file_object:
	json.dump(username, file_object)
	print("Thank you, ill remember you when you come back!")