<<<<<<< HEAD
#Exercise 8 : What’s your name ?
#Instructions
#Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

name = input("Enter your name: ")
if name == "Ilan":
    print("We have the same name!")
else:
    print("My name is better.")
    
=======
#Exercise 8: Who ordered a pizza ?
#Instructions
#Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
#As they enter each topping, print a message saying you’ll add that topping to their pizza.
#Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).

topping = input("Enter a topping for your pizza: ")
pizza = []
while topping != "quit":
    pizza.append(topping)
    print(f"Adding {topping} to your pizza.")
    topping = input("Enter a topping for your pizza: ")
print("Your pizza has the following toppings:")
for topping in pizza:
    print(topping)
    print(f"The total price of your pizza is {10 + 2.5 * len(pizza)}")
>>>>>>> 41668fe (Added all Day4 exercises)
