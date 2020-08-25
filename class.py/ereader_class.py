 ### 8/21/2020
 ### Creating a new Ereader class

class Ereader():
 	"""A class to represent an ereader"""

 	def __init__(self, make, model, backlight, battery, screen_type):
 		""" Initialize the attributes to describe an ereader"""
 		self.make = make
 		self.model = model
 		self.backlight = backlight
 		self.battery = battery
 		self.screen_type = screen_type

 	def get_ereader_name(self):
 		""" Return a formatted descriptive name for our ereader"""
 		long_name = self.make + " - " + self.model + ' - ' + self.backlight + ' - ' + self.battery + ' - ' + self.screen_type
 		return long_name.title()


my_new_ereader = Ereader("Amazon Kindle", "Paperwhite", "Adjustable Backlight" , "Several months of battery life" , "700 DPI")
print(my_new_ereader.get_ereader_name())