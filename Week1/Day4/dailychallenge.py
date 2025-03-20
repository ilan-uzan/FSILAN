#Instructions
#Using the input function, ask the user for a string. The string must be 10 characters long.
#If it’s less than 10 characters, print a message which states “string not long enough”.
#If it’s more than 10 characters, print a message which states “string too long”.
#If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

#Then, print the first and last characters of the given text.
#The user enters "HelloWorld"
#Then you have to print 
#H
#d


#3. Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:

#The user enters "HelloWorld"
#Then, you have to construct the string character by character
#H
#He
#Hel
#... etc
#HelloWorld


#4. Bonus: Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). For example:

#Hlrolelwod

user_input = input("Enter a string: ")
if len(user_input) < 10:
    print("string not long enough")
elif len(user_input) > 10:  
    print("string too long")
else:
    print("perfect string")
print(user_input[0])
print(user_input[-1])
for i in range(1,len(user_input)+1):
        print(user_input[:i])
import random
user_input = list(user_input)
random.shuffle(user_input)
print(''.join(user_input))
