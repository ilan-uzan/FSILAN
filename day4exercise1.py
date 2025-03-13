<<<<<<< HEAD
#Exercise 1 : Hello World
#Instructions
#Print the following output in one line of code:

#Hello world
#Hello world
#Hello world
#Hello world

print("Hello world\n"*4)
=======
#🌟 Exercise 1 : Favorite Numbers
#Instructions
#Create a set called my_fav_numbers with all your favorites numbers.
#Add two new numbers to the set.
#Remove the last number.
#Create a set called friend_fav_numbers with your friend’s favorites numbers.
#Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.

my_fav_numbers = {1, 2, 3, 4, 5}
my_fav_numbers.add(6)
my_fav_numbers.add(7)
my_fav_numbers.remove(7)
friend_fav_numbers = {8, 9, 10}
our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(our_fav_numbers)
>>>>>>> 41668fe (Added all Day4 exercises)
