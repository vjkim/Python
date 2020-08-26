### 8/24/2020
### Read an entire file

with open('movies.txt') as file_object:
	contents = file_object.read()
	print(contents.strip())

# Open function needs one argument
# All programs mUST be in the same directory
# With ==> closes file once access is no longer needed
# We use Open because it is the best way to prevent bugs
# We could use close, but improperly closed files will become corrupted or data will be lost
# Read method ==> reads the contents and stores it in one long string, we get the entire string back 
