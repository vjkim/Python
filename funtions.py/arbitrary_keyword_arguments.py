### 8/20/2020
### Using arbitrary keyword arguments

def seat_profile(first_name, last_name, **passenger_info):
	"""Build a dictionary containing all passenger information"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key, value in passenger_info.items():
		profile[key] = value
	return profile

passenger_profile = seat_profile('v', 'kim', 'breakfast_ordered:' == "yes", seat_number = 35)
print(passenger_profile)
