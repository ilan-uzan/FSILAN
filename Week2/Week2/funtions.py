# def say_hello(username):
#     print(f"Hello, {username}!")

# say_hello("Alice")
# say_hello("Bob")
# say_hello("Charlie")
# say_hello("David")

# def say_hello(username,language):
#     if language == "en":
#         print(f"Hello, {username}!")
#     elif language == "es":
#         print(f"Hola, {username}!")
#     elif language == "fr":
#         print(f"Bonjour, {username}!")
#     else:
#         print("This language is not supported" + language)

# say_hello("Alice","en")
# say_hello("Bob","es")
# say_hello("Charlie","fr")
# say_hello("David","de")
# say_hello("David","fr")
# say_hello("David","es")

# favorite_number = 12
# def my_func():
#     print("I put the func in function")
#     my_name = "David"
#     print(my_name)
#     print(favorite_number)

# my_func()

# def number_multiplier(a):
#     return a * 17
# new_number = number_multiplier(9)-3
# print(new_number)

# def format_name(first_name,last_name):
#     return (first_name.title(), last_name.title())
# first, last = format_name("david","smith")
# print(first)
# print(last)

# Write a function calculation() such that it can accept two variables and calculate the addition and subtraction of it. And also it must return both addition and subtraction in a single return call

# For example:


# def calculation(a,b):
#     return a+b, a-b
# res = calculation(50,20)
# print(res)

# def greet_users(users):             # users should be a list
#     for user in users:              # Because it's a list, we can loop through it
#         print("Hello " + user.title() + " !")       # For each user, print "hello" and then his name

# # usernames = ["steve", "stan", "debbie"]
# # greet_users(usernames)

# print(greet_users)

# def args_processor(*baseball):
#     for i in baseball:
#         print(i**2)

# args_processor(20,30,40,50,60,70,80,90,100)

# def kwargs_processor(**kwargs):
#     print(kwargs)

# kwargs_processor(teacher="aaron", student="markus")

# def sample(name, age, *args, **kwargs):
#     print(f"{name} went to the park. He is {age} years old.")
#     print(args)
#     print(kwargs)

# sample("David", 25, "charlie", "cuthburt", location= "Ramat Gan", writing_utensil = "pencil")

# from functools import reduce

# def sum_numbers(first, second):
#     return first+second

# my_list = [1, 3, 5, 11]
# reduced_list = reduce(sum_numbers, my_list)

# print(reduced_list)

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
#Using map and filter, try to say hello to everyone who's name is less than or equal to 4 letters
short_names = filter(lambda name: len(name) <= 4, people)
greetings = map(lambda name: f"Hello {name}!", short_names)
print(list(greetings))

