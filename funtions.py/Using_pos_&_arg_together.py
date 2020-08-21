### 8/20/2020
### Using positional and arbitrary arguments together

def assign_seat(seat,*requests):
	"""Assign a seat and requests to a passenger"""
	print("\nAssign seat " + str(seat) + "following passenger requests.")
	for request in requests:
		print("- " + request)

assign_seat(36, 'window seat')