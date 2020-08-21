### 8/18/2020
### Positional Arguments

# creating our funtion
def book_description(book_type, author_name):
	"""Display book information"""
	print("\nThis book is " + book_type + ".")
	print("The author of this book is " + author_name.title() + ".")

book_description('non-fiction','ashlee vance')
book_description('fiction','dan brown')
