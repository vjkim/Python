### 8/20/2020
### Arbitrary Arguments


def create_passenger(*requests):
	"""Summarize passenger requests"""
	print("\nThis passenger has requested: ")
	for request in requests:
		print("- " + request)

create_passenger('window seat', 'seat near the top of the plane', 'preorder breakfast')