#Challenge 2
#Write a program that asks a string to the user, and display a new string with any duplicate consecutive letters removed.
#Examples

#user's word : "ppoeemm" ➞ "poem"

#user's word : "wiiiinnnnd" ➞ "wind"

#user's word : "ttiiitllleeee" ➞ "title"

#user's word : "cccccaaarrrbbonnnnn" ➞ "carbon"
#Notes
#Final strings won’t include words with double letters (e.g. “passing”, “lottery”).

user_word = input("Enter a word: ")
new_word = "".join([user_word[i] for i in range(len(user_word)) if i == 0 or user_word[i] != user_word[i - 1]])
print("New word without consecutive duplicates:", new_word)
