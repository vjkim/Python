### 8/18/2020
### Removing values from a list

books = ['big data', 'checklists', 'the firm', 'tesla', 'the firm', 'the firm']

print(books)

while 'the firm' in books:
	books.remove('the firm')

print(books)