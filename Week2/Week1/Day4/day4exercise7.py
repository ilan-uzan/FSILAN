<<<<<<< HEAD
#Exercise 7 : Odd or Even
#Instructions
#Write code that asks the user for a number and determines whether this number is odd or even.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")
=======
#🌟 Exercise 7: Favorite fruits
#Instructions
#Ask the user to input their favorite fruit(s) (one or several fruits).
#Hint : Use the built in input method. Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
#Store the favorite fruit(s) in a list (convert the string of words into a list of words).
#Now that we have a list of fruits, ask the user to input a name of any fruit.
#If the user’s input is in the favorite fruits list, print “You chose one of your favorite fruits! Enjoy!”.
#If the user’s input is NOT in the list, print, “You chose a new fruit. I hope you enjoy”


favorite_fruits = input("Enter your favorite fruit(s) separated by a space: ").split()
fruit = input("Enter a fruit: ")
if fruit in favorite_fruits:
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy!")
>>>>>>> 41668fe (Added all Day4 exercises)
