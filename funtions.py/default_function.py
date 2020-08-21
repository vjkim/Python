### 8/19/2020
### Default values


def book_description(author_name, book_type='nonfiction'):
	"""Display book information"""

	print("\nThis is a " + book_type + " book.")
	print("The author of this book is " + author_name.title())

book_description('ashlee vance', book_type='fiction')
