### 8/25/2020
### File paths


file_path = 'files.py\txt.py\copy_of_movies.txt'

# Absolute file paths tell the program exactly where it is stored
with open(file_path) as file_objects:
	# Relative file path tells python to look in the location relative to the directory where the text is stored
	contents = file_objects.read()
	print(contents.strip())