# Exercise 1
# Instructions
# Write a script that inserts an item at a defined index in a list.

list = ["ilan","lan","an","n", "o"]
list.insert(0, "I")
list.insert(1, "L")
list.insert(2, "A")
list.insert(3, "N")
print(list)



# Exercise 2
# Instructions
# Write a script that counts the number of spaces in a string.

string = "I am a string and i hate python"
count = 0
for ilan in string:
    if ilan == " ":
        count += 1
print(count)


# Exercise 3
# Instructions
# Write a script that calculates the number of upper case letters and lower case letters in a string.

string = "I am a string and i hate python"
upper = 0
lower = 0
for ilan in string:
    if ilan.isupper():
        upper += 1
    elif ilan.islower():
        lower += 1
print(f"Upper case letters: {upper}")
print(f"Lower case letters: {lower}")


# Exercise 4
# Instructions
# Write a function to find the sum of an array without using the built in function:

# >>>my_sum([1,5,4,2])
# >>>12

def my_sum(list):
    sum = 0
    for ilan in list:
        sum += ilan
    return sum
print(my_sum([1,5,4,2]))

# Exercise 5
# Instructions
# Write a function to find the max number in a list

# >>>find_max([0,1,3,50])
# >>>50

def find_max(list):
    max = list[0]
    for ilan in list:
        if ilan > max:
            max = ilan
    return max
print(find_max([0,1,3,50]))

# Exercise 6
# Instructions
# Write a function that returns factorial of a number

# >>>factorial(4)
# >>>24

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))


# Exercise 7
# Instructions
# Write a function that counts an element in a list (without using the count method):

# >>>list_count(['a','a','t','o'],'a')
# >>>2

def list_count(list, element):
    count = 0
    for ilan in list:
        if ilan == element:
            count += 1
    return count
print(list_count(['a','a','t','o'],'a'))

# Exercise 8
# Instructions
# Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

# >>>norm([1,2,2])
# >>>3
 
def norm(list):
    sum = 0
    for ilan in list:
        sum += ilan ** 2
    return sum ** 0.5
print(norm([1,2,2]))

# Exercise 9
# Instructions
# Write a function to find if an array is monotonic (sorted either ascending of descending)

# >>>is_mono([7,6,5,5,2,0])
# >>>True

# >>>is_mono([2,3,3,3])
# >>>True

# >>>is_mono([1,2,0,4])
# >>>False

def is_mono(list):
    return list == sorted(list) or list == sorted(list, reverse=True)
print(is_mono([7,6,5,5,2,0]))
print(is_mono([2,3,3,3]))
print(is_mono([1,2,0,4]))



# Exercise 10
# Instructions
# Write a function that prints the longest word in a list.

def longest_word(list):
    longest = ""
    for ilan in list:
        if len(ilan) > len(longest):
            longest = ilan
    return longest
print(longest_word(["ilan", "lan", "an", "n", "o"]))


# Exercise 11
# Instructions
# Given a list of integers and strings, put all the integers in one list, and all the strings in another one.

list = [1,2,3,"ilan","lan","an"]
integers = []
strings = []
for ilan in list:
    if type(ilan) == int:
        integers.append(ilan)
    else:
        strings.append(ilan)
print(integers)
print(strings)

# Exercise 12
# Instructions
# Write a function to check if a string is a palindrome:

# >>>is_palindrome('radar')
# >>>True

# >>>is_palindrome('John)
# >>>False

def is_palindrome(string):
    return string == string[::-1]
print(is_palindrome('radar'))
print(is_palindrome('John'))
print(is_palindrome('madam'))

# Exercise 13
# Instructions
# Write a function that returns the amount of words in a sentence with length > k:

# >>>sentence = 'Do or do not there is no try'
# >>>k=2
# >>>sum_over_k(sentence,k)
# >>>3

def sum_over_k(sentence, k):
    count = 0
    for ilan in sentence.split():
        if len(ilan) > k:
            count += 1
    return count
print(sum_over_k('Do or do not there is no try', 2))   


# Exercise 14
# Instructions
# Write a function that returns the average value in a dictionary (assume the values are numeric):

# >>>dict_avg({'a': 1,'b':2,'c':8,'d': 1})
# >>>3

def dict_avg(dict):
    return sum(dict.values()) / len(dict)
print(dict_avg({'a': 1,'b':2,'c':8,'d': 1}))


# Exercise 15
# Instructions
# Write a function that returns common divisors of 2 numbers:

# >>>common_div(10,20)
# >>>[2,5,10]

def common_div(a, b):
    return [i for i in range(1, min(a,b)+1) if a % i == 0 and b % i == 0]
print(common_div(10,20))

# Exercise 16
# Instructions
# Write a function that test if a number is prime:

# >>>is_prime(11)
# >>>True

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
print(is_prime(11))
print(is_prime(4))
print(is_prime(1))
print(is_prime(3))

# Exercise 17
# Instructions
# Write a function that prints elements of a list if the index and the value are even:

# >>>weird_print([1,2,2,3,4,5])
# >>>[2,4]

def weird_print(list):
    return [ilan for ilan in list if ilan % 2 == 0]
print(weird_print([1,2,2,3,4,5]))

# Exercise 18
# Instructions
# Write a function that accepts an undefined number of keyworded arguments and return the count of different types:

# >>>type_count(a=1,b='string',c=1.0,d=True,e=False)
# >>>int: 1, str:1 , float:1, bool:2

def type_count(**kwargs):
    types = {}
    for ilan in kwargs.values():
        if type(ilan) in types:
            types[type(ilan)] += 1
        else:
            types[type(ilan)] = 1
    return types
print(type_count(a=1,b='string',c=1.0,d=True,e=False))

# Exercise 19
# Instructions
# Write a function that mimics the builtin .split() method for strings.

# By default the function uses whitespace but it should be able to take an argument for any character and split with that argument.

def split(string, char=" "):
    return string.split(char)
print(split("I am a string and i hate python"))
print(split("I-am-a-string-and-i-hate-python", "-"))

# Exercise 20
# Instructions
# Convert a string into password format.

# Example:
# input : "mypassword"
# output: "***********"

def password(string):
    return "*" * len(string)
print(password("mypassword"))


# Exercises Part 2

# Exercise 1
# Instructions
# Draw the following pattern using for loops:
#   *
#  ***
# *****

for i in range(1, 4):
    print(" " * (3-i) + "*" * (2*i-1))

# Draw the following pattern using for loops:
#     *
#    **
#   ***
#  ****
# *****

for i in range(1, 6):
    print(" " * (5-i) + "*" * i)

# Draw the following pattern using for loops:
# *
# **
# ***
# ****
# *****
# *****
#  ****
#   ***
#    **
#     *

for i in range(1, 6):
    print("*" * i)
for i in range(5, 0, -1):
    print(" " * (5-i) + "*" * i)

# Exercise 2
# Instructions
# Analyse this code before executing it. Write some commnts next to each line. Write the value of each variable and their changes, and add the final output. Try to understand the purpose of this program.

my_list = [2, 24, 12, 354, 233] # list of integers
for i in range(len(my_list) - 1): # loop through the list
    minimum = i    # set minimum to i
    for j in range( i + 1, len(my_list)): # loop through the list starting from i+1
        if(my_list[j] < my_list[minimum]): # if the current element is less than the minimum
            minimum = j # set minimum to j
            if(minimum != i): # if minimum is not equal to i
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i] # swap the elements
print(my_list) # print the sorted list

