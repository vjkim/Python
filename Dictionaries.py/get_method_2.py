### 8/13/2020
### Editing & deleting values in a dictionary

terms = {'integer': 'It is a number that contains a decimal place.','string':'a sequence of characters.'}

terms['integer'] = 'A whole number.'

print(terms.get('integer'))

print(terms)

del terms['integer']

print(terms)

