### using break to end a loop

prompt = "\n Please enter the name of a book you have read recently"

prompt += "\nTo quit, enter 'q' "

if book == 'q':
	break
else:
	print("You have recently read " + book.title() + ".")