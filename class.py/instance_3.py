### 8/24/2020
### Creating our first class/ calling methods 

# __init__ helps python's method to distiguish our names/python's name

# define class ==> capitalized names are classes. 
# it is empty because we need to put stuff in it. 


class Book():
	"""A class to create a book"""

	# A function within a class is called a method. 
	# __init__ is a method.
	# Creates an instance.

	def __init__(self, name, price, publisher):
		"""Initialize the name, price, and publisher attributes"""

		# passes self which means itself. only defines name, price, and publisher
		self.name = name
		self.price = price
		self.publisher = publisher
		# any of these variables are available with the instances below.
		# called attributes

	def hardback(self):
		""" Simulate a hardback book."""
		print(self.name.title() + " is a hardback book.")
		# only one parameter 
	def softback(self):
		""" Simulate a book being a softback book."""
		print(self.name.title() + " is a softback book.")

	def ebook(self):
		"""Simulate an ebook."""
		print(self.name.title() + " is an ebook.")


	def ebook_reader(self):
		"""Simulate an ebook reader."""
		print("Library: " + self.name.title() + ", " + str(self.price) + ", " + self.publisher.title() + ".")

#functions define the attributes within a piece of code 

# Creating an instance of our book class.
my_book = Book('elon musk', 14.99, 'virgin books')
# creates an instance of a function 

# print("I'm currently reading " + my_book.name.title() + ".")
# used to print the name of the book

# print("This book costs " + str(my_book.price) + ".")
# used to print the cost


# my_book.softback()
# my_book.hardback()

# Calling our ebook_reader method

my_book.ebook_reader()