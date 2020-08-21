### 8/11/2020
### Using the or keyword to check values in a list

#names registered

registered_names = ['tony', 'mary', 'peter']

username = input("Please enter the username you would like to use.")

# check to see if username is already taken

if username in registered_names:
    print("Sorry, username already taken.")
else:
    print("This username is available.")
    

