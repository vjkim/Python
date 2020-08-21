### 8/11/2020
### Working with empty list

# Empty shopping cart
shopping_cart = ['pens']

if shopping_cart:
    for item in shopping_cart:
        print("Adding " + item + " to your cart.")
    print("Your order is complete.")
else:
    print("You must select an item before proceeding.")
