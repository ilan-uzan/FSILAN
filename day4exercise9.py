<<<<<<< HEAD
#Exercise 9 : Tall enough to ride a roller coaster
#Instructions
#Write code that will ask the user for their height in centimeters.
#If they are over 145cm print a message that states they are tall enough to ride.
#If they are not tall enough print a message that says they need to grow some more to ride.

height = int(input("Enter your height in centimeters: "))
if height > 145:
    print("You are tall enough to ride.")
else:
    print("You need to grow some more to ride.") 
=======
#Exercise 9: Cinemax
#Instructions
#A movie theater charges different ticket prices depending on a person’s age.
#if a person is under the age of 3, the ticket is free.
#if they are between 3 and 12, the ticket is $10.
#if they are over the age of 12, the ticket is $15.

#Ask a family the age of each person who wants a ticket.

#Store the total cost of all the family’s tickets and print it out.

num_people = int(input("How many people are in your family? "))
total_cost = 0
for i in range(num_people):
    age = int(input("Enter the age of the person: "))
    if age < 3:
        total_cost += 0
    elif 3 <= age <= 12:
        total_cost += 10
    else:
        total_cost += 15
print(f"The total cost of all the family's tickets is ${total_cost}")

#A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
#Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
#At the end, print the final list.

teenagers = ["John", "Luke", "Sarah", "Alice", "Emily"]
allowed_teens = []
for teen in teenagers:
    age = int(input(f"Enter the age of {teen}: "))
    if 16 <= age <= 21:
        print(f" Sorry {teen}, you are not allowed to watch the movie.")
    else:
        allowed_teens.append(teen)
print("\nThe final list of teenagers allowed to watch the movie:", allowed_teens)
>>>>>>> 41668fe (Added all Day4 exercises)
