# suppose there are two levels to the quiz
# you have to give two options to the user. for option 1 give 1st question, option 2 give 2nd question
# check the answer and if correct, then update the string with the correct answer.

print("we are going step by step\nSO now there are two levels: noob and easy\nyou have to choose one")
user_level_list = ['noob','easy']
level_noob = "The Witcher series is on __1__."
level_easy = "Kangaroo animal is found in __2__."
noob_answer = "Netflix"
easy_answer = "Australia"

user_level = input("Which level will you choose? ")

if user_level == 'noob':
    print("haha noobad , okay answer this: ", level_noob)
elif user_level == 'easy':
    print("this is still easy level: ", level_easy)

user_answer = input("Put your answer here: ")

if user_answer == noob_answer:
    level_noob_updated = level_noob.replace('__1__',user_answer)
    print("Well done I guess", level_noob_updated)
elif user_answer == easy_answer:
    level_easy_updated = level_easy.replace('__2__',user_answer)
    print("Hmmm.", level_easy_updated)


