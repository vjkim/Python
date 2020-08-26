### 8/25/2020
### Making a list from a file


#
filename = 'movies_line_by_line.txt'

with open(filename) as file_object:
	lines = file_object.readlines()
# Readline() method stores the objects in lists which we can continue to work with after the lines


for line in lines:
	print(line.strip())

# We use a simple for loop to get a line from lines

print("\n--------------------------------------------------------------------------------------------------\n")

popped_movies = lines.pop()

for line in lines:
	print(line.strip())

print("\n--------------------------------------------------------------------------------------------------\n")

sorted_list = lines.sort()

for line in lines:
	print(line.strip())