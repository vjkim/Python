### 8/24/2020
### Modifying an attribute's value thru a method

class Ereader():
 	"""A class to represent an ereader"""

 	def __init__(self, make, model, backlight, battery, screen_type):
 		"""Initialize the attributes to describe an ereader."""
 		self.make = make
 		self.model = model
 		self.backlight = backlight
 		self.battery = battery
 		self.screen_type = screen_type
 		self.library_count = 0

#Function to define the class
 	def get_ereader_name(self):
 		"""Return a formatted descriptive name for our ereader."""
 		long_name = self.make + " - " + self.model + ' - ' + self.backlight + ' - ' + self.battery + ' - ' + self.screen_type
 		return long_name.title()

#read library count
def read_library_count(self):
		"""Show the amount of ebooks in our kindle library."""
		print("You have " + str(self.library_count) + "books in your kindle library.")


def update_library_count(self, ebook_count):
		""" Set the library count.""" 
		self.library_count = ebook_count

# Calls the class
my_new_ereader = Ereader("Amazon Kindle", "Paperwhite", "Adjustable Backlight" , "Several months of battery life" , "700 DPI")
print(my_new_ereader.get_ereader_name())

my_new_ereader.update_library_count(48)
my_new_ereader.read_library_count()

