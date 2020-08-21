### 8/18/2020
### Adding user input in a dictionary

# Create an empty dictionary
rental_properties = {}

#Set a flag to indicate that we are taking applications
rental_open = True

while rental_open:
	#prompt users for username and address.
	username = input('\nWhat is your name?')
	rental_property = input("What is the address of the property that you have to rent?")

	#store the responses in a dictionary
	rental_properties[username] = rental_property

	# Ask if the user knows any one else looking to rent a property
	repeat = input("\nDo you know anyone who might like to rent a new property?")
	if repeat == 'no':
		rental_open = False

	#adding property is complete

print("\n--- Property to rent ---")
for username, rental_property in rental_properties.items():
	print(username + " has " + rental_property + "to rent.")
	