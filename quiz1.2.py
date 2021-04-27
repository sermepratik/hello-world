# 4 levels quiz

print("Now there are 4 levels, you can choose 1 out of 4.")
uls = ['noob','easy','medium','hard']
print("Select your level: ", *uls)
# let user decide his level with the input statement
user_chooses = input("PATKAN CHOOSE KAR: ")

noob_level = "__1__ for apple."
easy_level = "iPod was developed by __2__ in California, USA."
medium_level = "The Taiwan supplier of Apple is __3__."
hard_level = "Apple products are __4__ overpriced."
answer_list = ['A', 'Apple', 'Foxconn', 'usually']

if user_chooses not in uls:
    print("are bhauu dile ahet tyacha madhun choose kar re bindok")
else:
    if user_chooses == 'noob':
        print(noob_level)
        answerx = input("Your answer here: ")
        if answerx == answer_list[0]:
            print("Hey you are not a noob anymore!")
            noob_level = noob_level.replace('__1__', answerx)
            print(noob_level)
    elif user_chooses == 'easy':
        print(easy_level)
        answerx = input("Your answer here: ")
        if answerx == answer_list[1]:
            print("This is still easy tier.")
            easy_level = easy_level.replace('__2__', answerx)
            print(easy_level)
    elif user_chooses == 'medium':
        print(medium_level)
        answerx = input("Your answer here: ")
        if answerx == answer_list[2]:
            print("Not bad, kid.")
            medium_level = medium_level.replace('__3__', answerx)
            print(medium_level)
    elif user_chooses == 'hard':
        print(hard_level)
        answerx = input("Let's see you get this: ")
        if answerx == answer_list[3]:
            print("well well, how the turntables, well done good sir.")
            hard_level = hard_level.replace("__4__", answerx)
            print(hard_level)



# now take user answer? i wantd to take the answer in the if statement itself.
#print("Now time for answers!")
#user_answer = input("Your answer here: ")
# let me try something here, ima put input method in the if statements
# yes! i got it to work!


