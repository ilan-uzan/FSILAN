#Exercise 7 : Odd or Even
#Instructions
#Write code that asks the user for a number and determines whether this number is odd or even.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("The number is even.")
else:
    print("The number is odd.")