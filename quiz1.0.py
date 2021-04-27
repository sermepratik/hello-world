# fill in the blanks simple
# write a program to check answer is correct or not

given_string = "Game of Thrones premieres every Sunday on __blank__."
print(given_string)

user_answer = input("Enter your answer for the blank space: ")

given_string_answer = "HBO"

if user_answer == given_string_answer:
    given_string_updated = given_string.replace('__blank__', user_answer)
    print("Hey! that's pretty good.\n",given_string_updated)
else:
    given_string_updated = "..."
    print("OH COME ON THIS IS EASY STUFF\n",given_string_updated)

