### 8/19/2020
### Returning a dictionary

def build_book(name, author, publisher):
	""" Create a dictionary of book information"""
	build_book = {'name': name, 'author' : author, 'publisher' : publisher}
	return build_book

my_book = build_book('elon musk', 'ashlee vance', 'virgin books')
print(my_book)