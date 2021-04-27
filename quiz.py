print("How well do you know Game of Thrones?")
print("\nYou can choose between 4 levels: noob, easy, medium, hard.\n")

# list of all the levels available for now
user_level_list = ["noob", "easy", "medium", "hard"]
user_level = input("Which level you choose?")
if user_level == "noob":
    print("haha noobad")
else:
    print("baghun tak na bindok input")

# list of blanks that appear in the questions
blanks = ["__1__", "__2__", "__3__", "__4__"]

level_noob = 'Game of Thrones premiers every __1__ night on HBO.'

level_easy = 'The Starks have their age-old castle at __2__ in the North.'

level_medium = 'Joffrey Baratheon is the son of __3__.'

level_hard = '__4__ wins the game in the end.'

# all level answers here
ans_list_noob = ["Sunday"]
ans_list_easy = ["Winterfell"]
ans_list_medium = ["Jamie Lannister"]
ans_list_hard = ["Bran"]


# define a function which takes user input and gives corresponding list as output
def first_function(user_level):
    if user_level not in user_level_list:
        print("are baba neat tak input")
    elif user_level == "easy":
        print("good job, you can read")
        print(level_easy)
        return level_easy

#first_function('easy')
first_function(user_level)