### 8/25/2020
### Writing to an empty file

filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("Hello, my name is V")
	