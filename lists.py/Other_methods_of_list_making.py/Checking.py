### 8/11/2020
### Checking if a value is not in a list


# Admin Users
admin_users = ['tony','frank']

# Ask for username
username = input("Please enter your username.")

#check if user is an admin user
if username not in admin_users:
    print("You do not have access.")
else:
    print("Access granted.")
