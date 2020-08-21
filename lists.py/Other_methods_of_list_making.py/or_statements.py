### 8/11/2020
### Age Checker

your_age = input("How old are you? ")
friends_age = input("How old is your friend? ")

if int(your_age) >= 18 or int(friends_age) >= 18:
    print("Congrats, one of you is old enough to vote!")
else:
    print("Sorry, one of you is too young to vote!")
    
