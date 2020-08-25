### 8/22/2020
### Read an entire file

file_path = 'Files.py/txt.py/copy_of_movies.txt'
with open(file_path) as file_objects:
	contents = file_objects.read()
	print(contents.strip())

