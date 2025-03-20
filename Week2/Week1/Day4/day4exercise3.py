<<<<<<< HEAD
#Exercise 3 : What is the output ?
#Instructions
#Predict the output of the following code snippets:

#>>> 5 < 3
#>>> 3 == 3
#>>> 3 == "3"
#>>> "3" > 3
#>>> "Hello" == "hello"

print(5 < 3) #False
print(3 == 3) #True
print(3 == "3") #False
print("3" > 3) #Error
print("Hello" == "hello") #False
=======
#🌟 Exercise 3: List
#Instructions
#Using this list basket = ["Banana", "Apples", "Oranges", "Blueberries"];

#Remove “Banana” from the list.
#Remove “Blueberries” from the list.
#Add “Kiwi” to the end of the list.
#Add “Apples” to the beginning of the list.
#Count how many apples are in the basket.
#Empty the basket.
#Print(basket)

basket = ["Banana", "Apples", "Oranges", "Blueberries"]
basket.remove("Banana") #Remove “Banana” from the list.
basket.remove("Blueberries") #Remove “Blueberries” from the list.
basket.append("Kiwi") #Add “Kiwi” to the end of the list.
basket.insert(0, "Apples") #Add “Apples” to the beginning of the list.
print(basket.count("Apples")) #Count how many apples are in the basket.
basket.clear() #Empty the basket.
print(basket) #Print(basket)
#Output: ['Apples', 'Oranges', 'Kiwi']
>>>>>>> 41668fe (Added all Day4 exercises)
