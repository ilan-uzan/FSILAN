# Instructions
# The computer choose a random word and mark stars for each letter of each word.
# Then the player will guess a letter.
# If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
# If the letter isn’t in the word(s) then add a body part to the gallows (head, body, left arm, right arm, left leg, right leg).
# The player will continue guessing letters until they can either solve the word(s) (or phrase) or all six body parts are on the gallows.
# The player can’t guess the same letter twice.


# Starter code
# Here is a piece of code that will give you a random word.
print("Welcome to Hangman!")
import random
wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist) 
masked = "*" * len(word)
tries = 0
print(masked)
while tries < 6 and masked != word:
    letter = input("Enter a letter: ")
    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                masked = masked[:i] + letter + masked[i+1:]
    else:
        tries += 1
    print(masked)
if masked == word:
    print("You won!")
else:
    print("You lost!")





