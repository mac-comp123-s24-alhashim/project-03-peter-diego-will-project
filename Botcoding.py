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





def middle_start(dict, turncount):
    dict[1] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    # PLAYER MOVE HERE
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
        break
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
        break


def top_left_start(dict, turncount):
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
        break

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
        break

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
        break



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
        break