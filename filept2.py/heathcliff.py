### 8/25/2020
### Analyzing text

filename = 'heathcliff.txt'

try:
	with open(filename) as file_object:
		contents = file_object.read()

except FileNotFoundError:
		message = "Sorry, the file " + filename + " cannot be found. "
		print(message)

else:
		words = contents.split()
		number_of_words = len(words)
		print("The file " + filename + "has approximately " + str(number_of_words) + "words.")


