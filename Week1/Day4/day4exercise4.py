<<<<<<< HEAD
#Exercise 4 : Your computer brand
#Instructions
#Create a variable called computer_brand which value is the brand name of your computer.
#Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".

computer_brand = "Apple"
print(f"I have a {computer_brand} computer")
#Output: I have a Apple computer
=======
#🌟 Exercise 4: Floats
#Instructions
#Recap – What is a float? What is the difference between an integer and a float?
#Create a list containing the following sequence of floats and integers (it should be a list with mixed types): 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don’t hard-code the sequence).
#Can you think of another way to generate a sequence of floats?

#A float is a type of number that contains a decimal point. An integer is whole number whitout a decimal point.

list = [1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]
print(list)

#Another way to generate a sequence of floats is by using the range() function. For example, to generate a sequence of floats from 1.5 to 5 with a step of 0.5:
list = [float(i) for i in range(15, 51, 5)]
print(list)
>>>>>>> 41668fe (Added all Day4 exercises)
