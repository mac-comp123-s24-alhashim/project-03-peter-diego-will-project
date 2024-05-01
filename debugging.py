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

def check_is_xo(stringin): # CHECKS IF X OR O
    stringin = stringin.upper()
    if stringin == "X" or stringin == "O":
        pass
    else:
        while stringin != "X" and stringin != "O":
            stringin = input("Please enter an X or an O")
            stringin = stringin.upper()
    return stringin

def check_is_x(stringin): #CHECKS IF X ON X'S TURN
    stringin = stringin.upper()
    if stringin == "X":
        pass
    else:
        while stringin != "X":
            stringin = input("It is X's turn")
            stringin = stringin.upper()
    return stringin

def check_is_o(stringin): #CHECKS IF O ON O'S TURN
    stringin = stringin.upper()
    if stringin == "O":
        pass
    else:
        while stringin != "O":
            stringin = input("It is O's turn")
            stringin = stringin.upper()
    return stringin

def check_whoturn(stringin, turncount): #CHECK IF IT'S O'S OR X'S TURN
    if turncount % 2 == 0:
        check_is_x(stringin)
    else:
        check_is_o(stringin)

def is_space_taken(dict, ask1): # CHECKS IF THE SPACE IS ALREADY TAKEN
    while dict[ask1] == "X" or dict[ask1] == "O":
        ask1 = input("Please select a different space: ")
    return ask1





def gameplay(dict, turncount): #HOW THE GAME FUNCTIONS
    if turncount % 2 == 0:
        ask1 = input("Which space do you want to input for? (1-9)")
        ask1 = is_space_taken(game_board, ask1)
        dict[ask1] = "X"
        print("turncount is", (turncount + 1))
        turncount = turncount + 1
    elif turncount % 2 == 1:
        turncount = bot_hard_code(dict, turncount)
    #print(gameboard(dict))
    #turncount = turncount + 1
    print(turncount, " GAMEPLAY VERSION")
    return turncount





def gameboard(game_board): #DO NOT CHANGE
    print (" ", game_board["1"], " ", "|", " ", game_board["2"], " ", "|", " ", game_board["3"], " ",)
    print("------|-------|------")
    print (" ", game_board["4"], " ", "|", " ", game_board["5"], " ", "|", " ", game_board["6"], " ",)
    print("------|-------|------")
    print (" ", game_board["7"], " ", "|", " ", game_board["8"], " ", "|", " ", game_board["9"], " ",)
    pass



def bot_hard_code(dict, turncount):
    if game_board["5"] == "X":
        turncount = middle_start(dict, turncount)
    elif game_board["4"] == "X":
        turncount = middle_left_start(dict, turncount)
    elif game_board["6"] == "X":
        turncount = middle_right_start(dict, turncount)
    elif game_board["1"] == "X":
        turncount = top_left_start(dict, turncount)
    elif game_board["3"] == "X":
        turncount = top_right_start(dict, turncount)
    elif game_board["7"] == "X":
        turncount = bottom_left_start(dict, turncount)
    elif game_board["8"] == "X":
        turncount = bottom_middle_start(dict, turncount)
    elif game_board["9"] == "X":
        turncount = bottom_right_start(dict, turncount)
    elif game_board["2"] == "X":
        turncount = top_middle_start(dict, turncount)
    return turncount


def is_space_taken(dict, ask1):  # CHECKS IF THE SPACE IS ALREADY TAKEN
    while dict[ask1] == "X" or dict[ask1] == "O":
        ask1 = input("Please select a different space: ")
    return ask1


def middle_start(dict, turncount):
    dict["1"] = "O"
    print(gameboard(dict))
    turncount = turncount + 1
    print("turncount is", turncount)
    ask1 = input("Which space do you want to input for? (1-9)")
    ask1 = is_space_taken(game_board, ask1)
    dict[ask1] = "X"
    if game_board["4"] == "X":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif game_board["7"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif game_board["8"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif game_board["9"] == "X":
        # changed
        pmoves = ["3", "7"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif game_board["2"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif game_board["3"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif game_board["5"] == "X":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    else:
        print("You got an error in middle_startr")


def top_left_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = 2
    print("turncount is", turncount)
    ask1 = input("Which space do you want to input for? (1-9)")
    ask1 = is_space_taken(game_board, ask1)
    dict[ask1] = "X"
    if dict["4"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["8"] == "X":
        # changed
        pmoves = ["9", "7", "6"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["9"] == "X":
        # changed
        pmoves = ["8", "2", "6", "4"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["2"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["3"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["6"] == "X":
        # changed
        pmoves = ["9", "8", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    else:
        print("you got an error in top_left_startr")


def top_right_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = 2
    print("turncount is", turncount)
    ask1 = input("Which space do you want to input for? (1-9)")
    ask1 = is_space_taken(game_board, ask1)
    dict[ask1] = "X"
    if dict["4"] == "X":
        #changed
        pmoves = ["1", "7", "8"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["9"] == "X":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["8"] == "X":
        #changed
        pmoves = ["9", "4", "7"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["7"] == "X":
        # changed
        pmoves = ["8", "4", "6", "2"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["6"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["2"] == "X":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["1"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["4"] == "X":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    else:
        print("You got an error in top_right_startr")

def bottom_left_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = 2
    print("turncount is", turncount)
    ask1 = input("Which space do you want to input for? (1-9)")
    ask1 = is_space_taken(game_board, ask1)
    dict[ask1] = "X"
    if dict["1"] == "X":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["2"] == "X":
        # changed
        pmoves = ["6", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["3"] == "X":
        # changed
        pmoves = ["6", "4", "2", "8"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["4"] == "X":
        # changed
        pmoves = ["1"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["6"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["8"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["9"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount


def bottom_right_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = 2
    print("turncount is", turncount)
    ask1 = input("Which space do you want to input for? (1-9)")
    ask1 = is_space_taken(game_board, ask1)
    dict[ask1] = "X"
    if dict["1"] == "X":
        # changed
        pmoves = ["6", "2", "4", "8"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["2"] == "X":
        # changed
        pmoves = ["4", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        print("turncount is", turncount)
        return turncount
    elif dict["3"] == "X":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        print("turncount is", turncount)
        return turncount
    elif dict["4"] == "X":
        # changed
        pmoves = ["7", "2", "1"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        print("turncount is", turncount)
        return turncount
    elif dict["6"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        print("turncount is", turncount)
        return turncount
    elif dict["7"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        print("turncount is", turncount)
        return turncount
    elif dict["8"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        print("turncount is", turncount)
        return turncount


def top_middle_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = 2
    print("turncount is", turncount)
    ask1 = input("Which space do you want to input for? (1-9)")
    ask1 = is_space_taken(game_board, ask1)
    dict[ask1] = "X"
    if dict["1"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["3"] == "X":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["4"] == "X":
        # changed
        pmoves = ["7", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["6"] == "X":
        # changed
        pmoves = ["9", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["7"] == "X":
        # changed
        pmoves = ["6", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["8"] == "X":
        # changed
        pmoves = ["1", "3", "4", "6", "7", "9"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["9"] == "X":
        # changed
        pmoves = ["4", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    else:
        print("you got an error in top_middle_start")


def middle_left_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = 2
    print("turncount is", turncount)
    ask1 = input("Which space do you want to input for? (1-9)")
    ask1 = is_space_taken(game_board, ask1)
    dict[ask1] = "X"
    if dict["1"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["2"] == "X":
        # changed
        pmoves = ["7", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["3"] == "X":
        # changed
        pmoves = ["1", "7", "8"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["6"] == "X":
        # changed
        pmoves = ["1", "2", "3", "7", "8", "9"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["7"] == "X":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["8"] == "X":
        # changed
        pmoves = ["1", "7", "9"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["9"] == "X":
        # changed
        pmoves = ["7", "2", "1"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount


def middle_right_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = 4
    print("turncount is", turncount)
    ask1 = input("Which space do you want to input for? (1-9)")
    ask1 = is_space_taken(game_board, ask1)
    dict[ask1] = "X"
    if dict["1"] == "X":
        # changed
        pmoves = ["9", "8", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["2"] == "X":
        # changed
        pmoves = ["9", "1", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["3"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["4"] == "X":
        # changed
        pmoves = ["1", "2", "3", "7", "8", "9"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["7"] == "X":
        # changed
        pmoves = ["9", "2", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["8"] == "X":
        # changed
        pmoves = ["9", "7", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["9"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    else:
        print("you got an error in middle_right_start")


def bottom_middle_start(dict, turncount):
    dict["5"] = "O"
    print(gameboard(dict))
    turncount = 2
    print("turncount is", turncount)
    ask1 = input("Which space do you want to input for? (1-9)")
    ask1 = is_space_taken(game_board, ask1)
    dict[ask1] = "X"
    if dict["1"] == "X":
        # changed
        pmoves = ["9", "7", "6"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["2"] == "X":
        # changed
        pmoves = ["1", "3", "4", "6", "7", "9"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["3"] == "X":
        # changed
        pmoves = ["9", "4", "7"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["4"] == "X":
        # changed
        pmoves = ["1", "7", "9"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["6"] == "X":
        # changed
        pmoves = ["9", "7", "3"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["7"] == "X":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["9"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    else:
        "You got an error in bottom_middle_start"







def post_t4_bot_code(dict, turncount):
    #This is the code for what the bot should do after the hard-coding section based on logical statements.
    if turncount % 2 == 0:
        ask1 = input("Which space do you want to input for? (1-9)")
        ask1 = is_space_taken(game_board, ask1)
        dict[ask1] = "X"
        print("turncount is", (turncount + 1))
        turncount = turncount + 1
    elif turncount % 2 == 1:
        search_for_win(game_board, turncount)
        search_for_loss(game_board, turncount)
        if_no_win_loss(game_board, turncount)
    #turncount = turncount + 1
    print("turncount is", turncount)
    return turncount


def search_for_win(dict, turncount):
    print("search_for_win")
#This is the bot looking for a win---goes down sequentially from different starting points
    if dict["1"] == "O" and dict["2"] == "O" and dict["3"] == "3":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["5"] == "O" and dict["9"] == "9":
        dict["9"] = "O"

        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["3"] == "O" and dict["2"] == "2":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["9"] == "O" and dict["5"] == "5":
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["4"] == "O" and dict["7"] == "7":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["7"] == "O" and dict["4"] == "4":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "O" and dict["3"] == "O" and dict["1"] == "1":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "O" and dict["5"] == "O" and dict["8"] == "8":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "O" and dict["8"] == "O" and dict["5"] == "5":
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "O" and dict["5"] == "O" and dict["7"] == "7":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "O" and dict["7"] == "O" and dict["5"] == "5":
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "O" and dict["6"] == "O" and dict["9"] == "7":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "O" and dict["9"] == "O" and dict["6"] == "6":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "O" and dict["5"] == "O" and dict["6"] == "6":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "O" and dict["6"] == "O" and dict["5"] == "5":
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "O" and dict["7"] == "O" and dict["1"] == "1":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "O" and dict["5"] == "O" and dict["4"] == "4":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "O" and dict["9"] == "O" and dict["1"] == "1":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "O" and dict["5"] == "O" and dict["3"] == "3":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "O" and dict["4"] == "O" and dict["1"] == "1":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "O" and dict["8"] == "O" and dict["9"] == "9":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "O" and dict["9"] == "O" and dict["8"] == "8":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "O" and dict["5"] == "O" and dict["2"] == "2":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "O" and dict["9"] == "O" and dict["7"] == "7":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "O" and dict["5"] == "O" and dict["1"] == "1":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "O" and dict["6"] == "O" and dict["3"] == "3":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "O" and dict["1"] == "O" and dict["5"] == "5":
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("you passed search_for_win")
        pass


def search_for_loss(dict, turncount):
    print("search_for_loss")
# This is the bot looking for a potential loss---goes down sequentially from different starting points
    if dict["1"] == "X" and dict["2"] == "X" and dict["3"] == "3":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["5"] == "X" and dict["9"] == "9":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["3"] == "X" and dict["2"] == "2":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["9"] == "X" and dict["5"] == "5":
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["4"] == "X" and dict["7"] == "7":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["7"] == "X" and dict["4"] == "4":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X" and dict["3"] == "X" and dict["1"] == "1":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X" and dict["5"] == "X" and dict["8"] == "8":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X" and dict["8"] == "X" and dict["5"] == "5":
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X" and dict["5"] == "X" and dict["7"] == "7":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X" and dict["7"] == "X" and dict["5"] == "5":
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X" and dict["6"] == "X" and dict["9"] == "7":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X" and dict["9"] == "X" and dict["6"] == "6":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X" and dict["5"] == "X" and dict["6"] == "6":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X" and dict["6"] == "X" and dict["5"] == "5":
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X" and dict["7"] == "X" and dict["1"] == "1":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X" and dict["5"] == "X" and dict["4"] == "4":
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X" and dict["9"] == "X" and dict["1"] == "1":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X" and dict["5"] == "X" and dict["3"] == "3":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X" and dict["4"] == "X" and dict["1"] == "1":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X" and dict["8"] == "X" and dict["9"] == "9":
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X" and dict["9"] == "X" and dict["8"] == "8":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X" and dict["5"] == "X" and dict["2"] == "2":
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X" and dict["9"] == "X" and dict["7"] == "7":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X" and dict["5"] == "X" and dict["1"] == "1":
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X" and dict["6"] == "X" and dict["3"] == "3":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X" and dict["1"] == "X" and dict["5"] == "5":
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("you passed search_for_loss")
        pass
def if_no_win_loss(dict, turncount):
    print("search_for_no_win_loss")
    #the bot runs this code if there is no winning or losing move
    possible_moves = []
    for i in dict:
        if dict[str(i)] == str(i):
            possible_moves.append(str(i))
    if possible_moves == []:
        print("error in if_no_win_loss")
    else:
        move_choice = random.choice(possible_moves)
        move_choice = str(move_choice)
        dict[move_choice] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
    return turncount


















turncount = 0
print(gameboard(game_board))
print("turncount is", turncount)
win = ""
for i in range(9):
    if type(turncount) != int:
        print("we got a problem chief")
    if turncount < 3:
        turncount = gameplay(game_board, turncount)
        print("you're still in hell", turncount)
    elif turncount >= 3:
        print("YOU MADE IT TO POSTT4 BOT CODE", turncount)
        turncount = post_t4_bot_code(game_board, turncount)
    if game_board["1"] == "X" and game_board["2"] == "X" and game_board["3"] == "X":
        print("X wins!")
        win = "yes"
        break
    elif game_board["4"] == "X" and game_board["5"] == "X" and game_board["6"] == "X":
        print("X wins!")
        win = "yes"
        break
    elif game_board["7"] == "X" and game_board["8"] == "X" and game_board["9"] == "X":
        print("X wins!")
        win = "yes"
        break
    elif game_board["1"] == "X" and game_board["4"] == "X" and game_board["7"] == "X":
        print("X wins!")
        win = "yes"
        break
    elif game_board["2"] == "X" and game_board["5"] == "X" and game_board["8"] == "X":
        print("X wins!")
        win = "yes"
        break
    elif game_board["3"] == "X" and game_board["6"] == "X" and game_board["9"] == "X":
        print("X wins!")
        win = "yes"
        break
    elif game_board["1"] == "X" and game_board["5"] == "X" and game_board["9"] == "X":
        print("X wins!")
        win = "yes"
        break
    elif game_board["7"] == "X" and game_board["5"] == "X" and game_board["3"] == "X":
        print("X wins!")
        break
    elif game_board["1"] == "O" and game_board["2"] == "O" and game_board["3"] == "O":
        print("O wins!")
        win = "yes"
        break
    elif game_board["4"] == "O" and game_board["5"] == "O" and game_board["6"] == "O":
        print("O wins!")
        win = "yes"
        break
    elif game_board["7"] == "O" and game_board["8"] == "O" and game_board["9"] == "O":
        print("O wins!")
        win = "yes"
        break
    elif game_board["1"] == "O" and game_board["4"] == "O" and game_board["7"] == "O":
        print("O wins!")
        win = "yes"
        break
    elif game_board["2"] == "O" and game_board["5"] == "O" and game_board["8"] == "O":
        print("O wins!")
        win = "yes"
        break
    elif game_board["3"] == "O" and game_board["6"] == "O" and game_board["9"] == "O":
        print("O wins!")
        win = "yes"
        break
    elif game_board["1"] == "O" and game_board["5"] == "O" and game_board["9"] == "O":
        print("O wins!")
        win = "yes"
        break
    elif game_board["7"] == "O" and game_board["5"] == "O" and game_board["3"] == "O":
        print("O wins!")
        win = "yes"
        break
if win != "yes":
    print("It's a tie!")
