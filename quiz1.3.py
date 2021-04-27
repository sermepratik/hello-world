# okay the 4 levels seem to be working in 1.2
# now lets add number of guesses to this file
# the user gets 3 guesses to play the game, if they do not answer correct they lose the game

print("Now there are 4 levels, you can choose 1 out of 4.")
user_levels = ['noob', 'easy', 'medium', 'hard']
print("Select your level: ", *user_levels)
# let user decide his level with the input statement
user_chooses = input("PATKAN CHOOSE KAR: ")

noob_level = "__1__ for apple."
easy_level = "iPod was developed by __2__ in California, USA."
medium_level = "The Taiwan supplier of Apple is __3__."
hard_level = "Apple products are __4__ overpriced."
answer_list = ['A', 'Apple', 'Foxconn', 'usually']

if user_chooses in user_levels:
    if user_chooses == 'noob':
        print(noob_level)
    elif user_chooses == 'easy':
        print(easy_level)
    elif user_chooses == 'medium':
        print(medium_level)
    elif user_chooses == 'hard':
        print(hard_level)
else:
    print("are bhauu dile ahet tyacha madhun choose kar re bindok")

user_number_of_guess = 0
number_of_guess_allowed = 3

#while user_number_of_guess <= number_of_guess_allowed:
#    print("this is while loop to add kay")
#    user_number_of_guess += 1
# so this while loop is working

while user_number_of_guess < number_of_guess_allowed:
    if user_chooses == 'noob':
        #print('1', noob_level)
        answerx = input("2 Your answer here: ")
        if answerx == answer_list[0]:
            print("2 Hey you are not a noob anymore!")
            noob_level = noob_level.replace('__1__', answerx)
            print(noob_level)
            break
        else:
            print("2 wrong!")
            user_number_of_guess += 1
    elif user_chooses == 'easy':
        answerx = input(" Your answer here: ")
        if answerx == answer_list[1]:
            print("Hey this is still easy tier.")
            easy_level = easy_level.replace('__2__', answerx)
            print(easy_level)
            break
        else:
            print("WRONG ANSWER!")
            user_number_of_guess += 1
    elif user_chooses == 'medium':
        answerx = input(" Your answer here: ")
        if answerx == answer_list[2]:
            print("Not bad, kid.")
            medium_level = medium_level.replace('__3__', answerx)
            print(medium_level)
            break
        else:
            print("WRONG ANSWER!")
            user_number_of_guess += 1
    elif user_chooses == 'hard':
        answerx = input(" Your answer here: ")
        if answerx == answer_list[3]:
            print("EXCELLENT!")
            hard_level = hard_level.replace('__4__', answerx)
            print(hard_level)
            break
        else:
            print("WRONG ANSWER!")
            user_number_of_guess += 1
# so above while loop is also working

