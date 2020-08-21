### 8/11/2020
### Using if statements with lists

# Creating our shopping cart
shopping_cart = ['pens','paper','stapler','post-its']

# Adding each item to an order
for item in shopping_cart:
    if item == 'pens':
        print("Sorry, that item is out of stock.")
    else:
        print("Adding " + item + " to your order.")

print("Your order is complete.")
