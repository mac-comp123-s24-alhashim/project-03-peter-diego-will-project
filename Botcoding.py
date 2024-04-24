import random


game_board = { # DO NOT CHANGE
    "1" : "1",
    "2" : "2",
    "3" : "3",
    "4" : "4",
    "5" : "5",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "9"
}



#Will's thoughts---right now this is just what the bot should do and does not include player input.
#I think after each if/else statement we will need to add a way to it to go to the next section
#of code, but I'm not sure how to do that. Right now with just this, I think it will look back to
#other states which would completely destroy the game. Right now, if there isn't a legal move somehow,
#it breaks (to add the else to the elif statements), which shouldn't ever happen. If there is something
#format wise that needs to change that I messed up, tell me and I'll go back.

#Idea for making it more complex: could use random number generation to choose between equally optimal
#moves which wouldn't be much effort, but lets get the baqse game working first.

def bot_hard_code(dict, turncount):
    if game_board["5"] == "X":
        middle_start(dict, turncount)
    elif game_board["1"] == "X":
        top_left_start(dict, turncount)
    elif game_board["3"] == "X":
        top_right_start(dict, turncount)
    elif game_board["7"] == "X":
        bottom_left_start(dict, turncount)
    elif game_board["9"] == "X":
        bottom_right_start(dict, turncount)
    elif game_board["2"] == "X":
        top_middle_start(dict, turncount)

def is_space_taken(dict, ask1): # CHECKS IF THE SPACE IS ALREADY TAKEN
    while dict[ask1] == "X" or dict[ask1] == "O":
        ask1 = input("Please select a different space: ")
    return ask1



def middle_start(dict, turncount):
    dict[1] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    ask1 = input("Which space do you want to input for? (1-9)")
    ask1 = is_space_taken(game_board, ask1)
    dict[ask1] = ask2
    if game_board["4"] == "X":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif game_board["7"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif game_board["8"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif game_board["9"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif game_board["2"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif game_board["3"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif game_board["5"] == "X":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("You got an error in middle_start")
def top_left_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    # PLAYER MOVE HERE
    if dict["4"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("you got an error in top_right_start")


def top_right_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    # PLAYER MOVE HERE
    if dict["4"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("You got an error in top_right_start")

def bottom_left_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    #PLAYER MOVE HERE
    if dict["1"] == "X":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount

def bottom_right_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    #PLAYER MOVE HERE
    if dict["1"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount


def top_middle_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    # PLAYER MOVE HERE
    if dict["1"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("you got an error in top_middle_start")

def middle_left_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    # PLAYER MOVE HERE
    if dict["1"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount

def middle_right_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    # PLAYER MOVE HERE
    if dict["1"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("you got an error in middle_right_start")



def bottom_middle_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    # PLAYER MOVE HERE
    if dict["1"] == "X":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        "You got an error in bottom_middle_start"


def gameboard(game_board): #DO NOT CHANGE
    print (" ", game_board["1"], " ", "|", " ", game_board["2"], " ", "|", " ", game_board["3"], " ",)
    print("------|-------|------")
    print (" ", game_board["4"], " ", "|", " ", game_board["5"], " ", "|", " ", game_board["6"], " ",)
    print("------|-------|------")
    print (" ", game_board["7"], " ", "|", " ", game_board["8"], " ", "|", " ", game_board["9"], " ",)
    pass



#___________________________________________________________________________________________________________
#NEW CODE---POST T4
def post_t4_bot_code(dict, turncount):
    #This is the code for what the bot should do after the hard-coding section based on logical statements.
    while turncount % 2 == 1 and turncount > 4:
        search_for_win(game_board, turncount)
        search_for_loss(dict, turncount)
        if_no_win_loss(dict, turncount)





def search_for_win(dict, turncount):
#This is the bot looking for a win---goes down sequentially from different starting points
    if dict["1"] == "O" and dict["2"] == "O" and dict["3"] == "3":
        dict["3"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["5"] == "O" and dict["9"] == "9":
        dict["9"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["3"] == "O" and dict["2"] == "2":
        dict["2"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["9"] == "O" and dict["5"] == "5":
        dict["5"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["4"] == "O" and dict["7"] == "7":
        dict["7"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["7"] == "O" and dict["4"] == "4":
        dict["4"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "O" and dict["3"] == "O" and dict["1"] == "1":
        dict["1"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "O" and dict["5"] == "O" and dict["8"] == "8":
        dict["8"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "O" and dict["8"] == "O" and dict["5"] == "5":
        dict["5"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "O" and dict["5"] == "O" and dict["7"] == "7":
        dict["7"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "O" and dict["7"] == "O" and dict["5"] == "5":
        dict["5"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "O" and dict["6"] == "O" and dict["9"] == "7":
        dict["9"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "O" and dict["9"] == "O" and dict["6"] == "6":
        dict["6"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "O" and dict["5"] == "O" and dict["6"] == "6":
        dict["6"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "O" and dict["6"] == "O" and dict["5"] == "5":
        dict["5"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "O" and dict["7"] == "O" and dict["1"] == "1":
        dict["1"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "O" and dict["5"] == "O" and dict["4"] == "4":
        dict["4"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "O" and dict["9"] == "O" and dict["1"] == "1":
        dict["1"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "O" and dict["5"] == "O" and dict["3"] == "3":
        dict["3"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "O" and dict["4"] == "O" and dict["1"] == "1":
        dict["1"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "O" and dict["8"] == "O" and dict["9"] == "9":
        dict["9"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "O" and dict["9"] == "O" and dict["8"] == "8":
        dict["8"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "O" and dict["5"] == "O" and dict["2"] == "2":
        dict["2"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "O" and dict["9"] == "O" and dict["7"] == "7":
        dict["7"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "O" and dict["5"] == "O" and dict["1"] == "1":
        dict["1"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "O" and dict["6"] == "O" and dict["3"] == "3":
        dict["3"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "O" and dict["1"] == "O" and dict["5"] == "5":
        dict["5"] = "O"
        turncount = turncount + 1
        return turncount
    else:
        pass


def search_for_loss(dict, turncount):
# This is the bot looking for a potential loss---goes down sequentially from different starting points
    if dict["1"] == "X" and dict["2"] == "X" and dict["3"] == "3":
        dict["3"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["5"] == "X" and dict["9"] == "9":
        dict["9"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["3"] == "X" and dict["2"] == "2":
        dict["2"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["9"] == "X" and dict["5"] == "5":
        dict["5"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["4"] == "X" and dict["7"] == "7":
        dict["7"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["7"] == "X" and dict["4"] == "4":
        dict["4"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X" and dict["3"] == "X" and dict["1"] == "1":
        dict["1"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X" and dict["5"] == "X" and dict["8"] == "8":
        dict["8"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X" and dict["8"] == "X" and dict["5"] == "5":
        dict["5"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X" and dict["5"] == "X" and dict["7"] == "7":
        dict["7"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X" and dict["7"] == "X" and dict["5"] == "5":
        dict["5"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X" and dict["6"] == "X" and dict["9"] == "7":
        dict["9"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X" and dict["9"] == "X" and dict["6"] == "6":
        dict["6"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X" and dict["5"] == "X" and dict["6"] == "6":
        dict["6"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X" and dict["6"] == "X" and dict["5"] == "5":
        dict["5"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X" and dict["7"] == "X" and dict["1"] == "1":
        dict["1"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X" and dict["5"] == "X" and dict["4"] == "4":
        dict["4"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X" and dict["9"] == "X" and dict["1"] == "1":
        dict["1"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X" and dict["5"] == "X" and dict["3"] == "3":
        dict["3"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X" and dict["4"] == "X" and dict["1"] == "1":
        dict["1"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X" and dict["8"] == "X" and dict["9"] == "9":
        dict["9"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X" and dict["9"] == "X" and dict["8"] == "8":
        dict["8"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X" and dict["5"] == "X" and dict["2"] == "2":
        dict["2"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X" and dict["9"] == "X" and dict["7"] == "7":
        dict["7"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X" and dict["5"] == "X" and dict["1"] == "1":
        dict["1"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X" and dict["6"] == "X" and dict["3"] == "3":
        dict["3"] = "O"
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X" and dict["1"] == "X" and dict["5"] == "5":
        dict["5"] = "O"
        turncount = turncount + 1
        return turncount
    else:
        pass
def if_no_win_loss(dict, turncount):
    #the bot runs this code if there is no winning or losing move
    possible_moves = []
    for i in dict:
        if dict[str(i)] == str(i):
            possible_moves.append(str(i))
        elif:
            pass
    move_choice = random.choice(possible_moves)
    move_choice = str(move_choice)
    dict[move_choice] = "O"
    turncount = turncount + 1
    return turncount





#___________________________________________________________________________________________________________
# This is for implementing randomness into the bot for equally valid moves. Definitions with this are
# Denotated by adding r to the end. Every one changed has #changed or # changed next to it so it'll be a bit
# easier to debug. Not sure how hard this will be to integrate with the old code, lmk if there is any
# tedious work to do, happy to do it (its what im best at lol). This code will have to be integrated,
# I fixed errors that could have led to the bot losing. Praying to god i didn't mess up any code.
# -- Will


def middle_startr(dict, turncount):
    dict[1] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    ask1 = input("Which space do you want to input for? (1-9)")
    ask1 = is_space_taken(game_board, ask1)
    dict[ask1] = "X"
    if game_board["4"] == "X":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif game_board["7"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif game_board["8"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif game_board["9"] == "X":
        # changed
        pmoves = ["3", "7"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif game_board["2"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif game_board["3"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif game_board["5"] == "X":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("You got an error in middle_startr")
def top_left_startr(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    # PLAYER MOVE HERE
    if dict["4"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        #changed
        pmoves = ["9", "7", "6"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        #changed
        pmoves = ["8", "2", "6", "4"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X":
        #changed
        pmoves = ["9", "8", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("you got an error in top_right_startr")


def top_right_startr(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    # PLAYER MOVE HERE
    if dict["4"] == "X":
        #changed
        pmoves = ["1", "7", "8"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        #changed
        pmoves = ["9", "4", "7"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        # changed
        pmoves = ["8", "4", "6", "2"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("You got an error in top_right_startr")

def bottom_left_startr(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    #PLAYER MOVE HERE
    if dict["1"] == "X":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        # changed
        pmoves = ["6", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        # changed
        pmoves = ["6", "4", "2", "8"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X":
        # changed
        pmoves = ["9", "2", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount

def bottom_right_startr(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    #PLAYER MOVE HERE
    if dict["1"] == "X":
        # changed
        pmoves = ["6", "2", "4", "8"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        # changed
        pmoves = ["4", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X":
        # changed
        pmoves = ["7", "2", "1"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount


def top_middle_startr(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    # PLAYER MOVE HERE
    if dict["1"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X":
        # changed
        pmoves = ["7", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X":
        # changed
        pmoves = ["9", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        # changed
        pmoves = ["6", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        # changed
        pmoves = ["1", "3", "4", "6", "7", "9"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        # changed
        pmoves = ["4", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("you got an error in top_middle_startr")

def middle_left_startr(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    # PLAYER MOVE HERE
    if dict["1"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        # changed
        pmoves = ["7", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        # changed
        pmoves = ["1", "7", "8"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X":
        # changed
        pmoves = ["1", "2", "3", "7", "8", "9"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        # changed
        pmoves = ["1", "7", "9"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        # changed
        pmoves = ["7", "2", "1"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("Error in middle_left_startr")

def middle_right_startr(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    # PLAYER MOVE HERE
    if dict["1"] == "X":
        # changed
        pmoves = ["9", "8", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        # changed
        pmoves = ["9", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X":
        # changed
        pmoves = ["1", "2", "3", "7", "8", "9"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        # changed
        pmoves = ["9", "2", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X":
        # changed
        pmoves = ["9", "7", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("you got an error in middle_right_startr")



def bottom_middle_startr(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    # PLAYER MOVE HERE
    if dict["1"] == "X":
        # changed
        pmoves = ["9", "7", "6"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X":
        # changed
        pmoves = ["1", "3", "4", "6", "7", "9"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X":
        # changed
        pmoves = ["9", "4", "7"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X":
        # changed
        pmoves = ["1", "7", "9"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X":
        # changed
        pmoves = ["9", "7", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("You got an error in bottom_middle_startr")


def gameboard(game_board): #DO NOT CHANGE
    print (" ", game_board["1"], " ", "|", " ", game_board["2"], " ", "|", " ", game_board["3"], " ",)
    print("------|-------|------")
    print (" ", game_board["4"], " ", "|", " ", game_board["5"], " ", "|", " ", game_board["6"], " ",)
    print("------|-------|------")
    print (" ", game_board["7"], " ", "|", " ", game_board["8"], " ", "|", " ", game_board["9"], " ",)
    pass
