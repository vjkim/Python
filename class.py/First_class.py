### 8/20/2020
### Creating our first class

#define a class ==>
class Book():
	""" A Class to create a book"""
	
	def __init__(self, name, price, publisher):
		"""Initialize the name, price, and publisher attributes"""

		self.name = name
		self.price = price
		self.publisher = publisher

	def hardback(self):
		""" Simulate a hardback book."""
		print(self.name.title() + " is a hardback book.")

	def softback(self):
		"""Simulate a book being a softback book"""
		print(self.name.title() + " is a softback book.")

	def ebook(self):
		"""simulate an ebook"""
		print(self.name.title() + " is a ebook.")