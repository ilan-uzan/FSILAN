# 🌟 Exercise 1 : What are you learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

def display_message():
    print("I am learning Python in this course")
display_message()

# 🌟 Exercise 2: What’s your favorite book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

def favorite_book(title):
    print(f"One of my favorite books is {title}")
favorite_book("Alice in Wonderland")
favorite_book("The Great Gatsby")
favorite_book("The Catcher in the Rye") 


# 🌟 Exercise 3 : Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.

def describe_city(city, country):
    print(f"{city} is in {country}")
describe_city("Reykjavik", "Iceland")
describe_city("Paris", "France")
describe_city("New York", "USA")

# Exercise 4 : Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success message, otherwise show a fail message and display both numbers.

def random_number(num):
    import random
    random_num = random.randint(1,100)
    if num == random_num:
        print("Success")
    else:
        print("Fail")
    print(f"Your number: {num}, Random number: {random_num}")
random_number(50)

# 🌟 Exercise 5 : Let’s create some personalized shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
def make_shirts(size, text):
    print(f"The size of the shirt is {size} and the text is {text}")
make_shirts("Large", "I hate python")
# Call the function make_shirt().
# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.

def make_shirts(size="Large", text="I hate python"):
    print(f"The size of the shirt is {size} and the text is {text}")
make_shirts()    
make_shirts("Medium")

# 🌟 Exercise 6 : Magicians …
# Instructions
# Using this list of magician’s names

# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
def show_magicians():
    for name in magician_names:
        print(name)
show_magicians()
def make_great():
    for i in range(len(magician_names)):
        magician_names[i] = magician_names[i] + " the Great"
make_great()
show_magicians()

# 🌟 Exercise 7 : Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.
# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”
# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40
# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

def get_random_temp(season):
    import random
    if season == "summer":
        return random.randint(16,40)
    elif season == "autumn" or season == "fall":
        return random.randint(-10,23)
    elif season == "winter":
        return random.randint(-10,16)
    elif season == "spring":
        return random.randint(16,32)
    else:
        return random.randint(-10,40)
def main():
    season = input("Enter a season: ")
    temp = get_random_temp(season)
    print(f"The temperature right now is {temp} degrees Celsius.")
    if temp < 0:
        print("Brrr, that’s freezing! Wear some extra layers today")
    elif 0 <= temp < 16:
        print("Quite chilly! Don’t forget your coat")
    elif 16 <= temp < 24:
        print("It's a nice day")
    elif 24 <= temp < 32:
        print("It's getting hot")
    elif 32 <= temp <= 40:
        print("It's hot")
main()
# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.


# 🌟 Exercise 8 : Star Wars Quiz
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers

# data = [
#     {
#         "question": "What is Baby Yoda's real name?",
#         "answer": "Grogu"
#     },
#     {
#         "question": "Where did Obi-Wan take Luke after his birth?",
#         "answer": "Tatooine"
#     },
#     {
#         "question": "What year did the first Star Wars movie come out?",
#         "answer": "1977"
#     },
#     {
#         "question": "Who built C-3PO?",
#         "answer": "Anakin Skywalker"
#     },
#     {
#         "question": "Anakin Skywalker grew up to be who?",
#         "answer": "Darth Vader"
#     },
#     {
#         "question": "What species is Chewbacca?",
#         "answer": "Wookiee"
#     }
# ]


# Create a function that asks the questions to the user, and check his answers. Track the number of correct, incorrect answers. Create a list of wrong_answers
# Create a function that informs the user of his number of correct/incorrect answers.
# Bonus : display to the user the questions he answered wrong, his answer, and the correct answer.
# If he had more then 3 wrong answers, ask him to play again.

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]
def quiz():
    correct = 0
    incorrect = 0
    wrong_answers = []
    for question in data:
        user_answer = input(question["question"] + " ")
        if user_answer.lower() == question["answer"].lower():
            correct += 1
        else:
            incorrect += 1
            wrong_answers.append(question)
    print(f"Correct answers: {correct}")
    print(f"Incorrect answers: {incorrect}")
    if incorrect > 3:
        print("You had more than 3 wrong answers. Please play again.")
        quiz()
    else:
        print("Good job!")
quiz()