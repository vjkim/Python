### 8/13/2020
### Using a dictionary in a list


book_0 = {'name' : 'elon musk', 'author' : 'ashlee vance', 'price' : '14.99', 'publisher' : 'virgin books'}
book_1 = {'name' : 'team of rivals', 'author' : 'doris kearn goodwin', 'price':'10', 'publisher' : 'simon & shuster'}
book_2 = {'name' : 'The everything store', 'author' : 'brad stone', 'price' : '12.99', 'publisher' : 'simon & shuster'}

books  = [book_0, book_1, book_2]

for book in books:
	print(book)


stock_items = []

# Make 50 blue pens

for blue_pen in range(0,50):
	new_blue_pen = {'color' : 'blue', 'type' : 'ballpoint', 'price' : "1.99"}
	stock_items.append(new_blue_pen)

print(stock_items)


# Changing the price of the first 5 pens

for blue_pen in stock_items[0:5]:
	if blue_pen['price'] == '1.99':
		blue_pen['price'] = '0.99'

for blue_pen in stock_items[0:5]:
	print(blue_pen)
