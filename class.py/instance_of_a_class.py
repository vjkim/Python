### 8/24/2020
### Creating our first class

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

#functions define the attributes within a piece of code 

my_book = Book('elon musk', 14.99, 'virgin books.')

# creates an instance of a function 