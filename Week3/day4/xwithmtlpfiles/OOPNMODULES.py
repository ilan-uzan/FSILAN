# 🌟 Exercise 1: Currencies
# Instructions
# class Currency:
#      def __init__(self, currency, amount):
#          self.currency = currency
#          self.amount = amount

     #Your code starts HERE


# Using the code above, implement the relevant methods and dunder methods which will output the results below.
# Hint : When adding 2 currencies which don’t share the same label you should raise an error.
# >>> c1 = Currency('dollar', 5)
# >>> c2 = Currency('dollar', 10)
# >>> c3 = Currency('shekel', 1)
# >>> c4 = Currency('shekel', 10)

# >>> str(c1)
# '5 dollars'

# >>> int(c1)
# 5

# >>> repr(c1)
# '5 dollars'

# >>> c1 + 5
# 10

# >>> c1 + c2
# 15

# >>> c1 
# 5 dollars

# >>> c1 += 5
# >>> c1
# 10 dollars

# >>> c1 += c2
# >>> c1
# 20 dollars

# >>> c1 + c3
# TypeError: Cannot add between Currency type <dollar> and <shekel>

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount
    
    def __str__(self):
        return f"{self.amount} {self.currency}{'s' if self.amount > 1 else ''}"
    
    def __repr__(self):
        return self.__str__()
    
    def __int__(self):
        return self.amount
    
    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other
        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            return self.amount + other.amount
        return NotImplemented
    
    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
        elif isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(f"Cannot add between Currency type <{self.currency}> and <{other.currency}>")
            self.amount += other.amount
        else:
            return NotImplemented
        return self
    
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)

print(str(c1))   
print(int(c1))   
print(repr(c1))  
print(c1 + 5)    
print(c1 + c2)   
c1 += 5
print(c1) 
c1 += c2
print(c1)       
print(c1 + c3)   



# 🌟 Exercise 2: Import
# Instructions
# In a file named func.py create a function that sum 2 numbers, and prints the result
# In a file named exercise_one.py import the function and call it to print the result
# Hint: You can use the the following syntaxes:

# import module_name 

# OR 

# from module_name import function_name 

# OR 

# from module_name import function_name as fn 

# OR

# import module_name as mn



# 🌟 Exercise 3: String module
# Instructions
# Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
# Hint: use the string module

import string
import random

def generate_random_string(length=5):
    characters = string.ascii_letters  
    return ''.join(random.choices(characters, k=length))

random_string = generate_random_string()
print(random_string)  


# 🌟 Exercise 4 : Current Date
# Instructions
# Create a function that displays the current date.
# Hint : Use the datetime module.

from datetime import datetime

def display_current_date():
    current_date = datetime.today().date()  
    print("Current Date:", current_date)

display_current_date()


# Exercise 5 : Amount of time left until January 1st
# Instructions
# Create a function that displays the amount of time left from now until January 1st.
# (Example: the 1st of January is in 10 days and 10:34:01hours).

from datetime import datetime

def time_until_new_year():
    now = datetime.now()  # Get the current date and time
    next_new_year = datetime(now.year + 1, 1, 1)  # January 1st of next year
    time_left = next_new_year - now  # Calculate the time difference

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"The 1st of January is in {days} days and {hours}:{minutes}:{seconds} hours.")

time_until_new_year()


# Exercise 6 : Birthday and minutes
# Instructions
# Create a function that accepts a birthdate as an argument (in the format of your choice), then displays a message stating how many minutes the user lived in his life.

from datetime import datetime

def minutes_lived():
    """
    Asks the user for their birthdate and calculates the number of minutes they have lived.
    """
    birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")  
    
    try:
        
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")
        
    
        now = datetime.now()
        
        
        time_lived = now - birthdate
        minutes_lived = int(time_lived.total_seconds() // 60)  
        
        print(f"You have lived approximately {minutes_lived:,} minutes.")
    
    except ValueError:
        print("Invalid date format! Please enter your birthdate in YYYY-MM-DD format.")

minutes_lived()

# Exercise 7 : Faker Module
# Instructions
# Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
# Create an empty list called users. Tip: It should be a list of dictionaries.
# Create a function that adds new dictionaries to the users list. Each user has the following keys: name, adress, langage_code. Use faker to populate them with fake data.

from faker import Faker

fake = Faker()

users = []

def add_fake_user():
    """
    Generates a fake user with name, address, and language code,
    and adds them to the users list.
    """
    user = {
        "name": fake.name(),
        "address": fake.address(),
        "language_code": fake.language_code()
    }
    users.append(user)


for _ in range(5):
    add_fake_user()


for user in users:
    print(user)
    print("-" * 40)