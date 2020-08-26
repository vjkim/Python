### 8/25/2020
### Writing multiple lines to a file using append

message = input("What is your favorite film? ")
print(message.title())

filename = 'favorite_film.txt'

with open(filename, 'a') as file_object:
	file_object.write(message + "\n")