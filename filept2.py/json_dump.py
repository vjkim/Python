### 8/25/2020 
### Json.dump function

import json

phone_numbers = [1234567890]

filename = 'phone_number.json'
with open(filename, 'w') as file_object:
	json.dump(phone_numbers, file_object)
