import random
import turtle
from imageTools import *

wn = turtle.Screen()
turt = turtle.Turtle()

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
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
    if turncount % 2 == 0:
        ask1 = input("Which space do you want to input for? (1-9)")
        ask1 = is_space_taken(game_board, ask1)
        dict[ask1] = "X"
        print("turncount is", (turncount + 1))
        turncount = turncount + 1
        wn.tracer(0)
        check_board(game_board, turt)
        wn.update()
    elif turncount % 2 == 1:
        turncount = bot_hard_code(dict, turncount)
        wn.tracer(0)
        check_board(game_board, turt)
        wn.update()
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
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
    return turncount


def is_space_taken(dict, ask1):  # CHECKS IF THE SPACE IS ALREADY TAKEN
    while dict[ask1] == "X" or dict[ask1] == "O":
        ask1 = input("Please select a different space: ")
    return ask1


def middle_start(dict, turncount):
    dict["1"] = "O"
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
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
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
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
    elif dict["7"] == "X":
        dict["4"] = "O"
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
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
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
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
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
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
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
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["3"] == "X":
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["4"] == "X":
        # changed
        pmoves = ["7", "2", "1"]
        rc = random.choice(pmoves)
        rc = str(rc)
        dict[rc] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["6"] == "X":
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["7"] == "X":
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount
    elif dict["8"] == "X":
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = 4
        print("turncount is", turncount)
        return turncount


def top_middle_start(dict, turncount):
    dict["5"] = "O"
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
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
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
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
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
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
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
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
    while turncount % 2 == 0 and turncount < 9:
        ask1 = input("Which space do you want to input for? (1-9)")
        ask1 = is_space_taken(game_board, ask1)
        dict[ask1] = "X"
        print("turncount is", (turncount + 1))
        turncount = turncount + 1
    if turncount % 2 == 1 and turncount < 9:
        turncount = search_for_win(game_board, turncount)
        print(turncount)
        turncount = search_for_loss(game_board, turncount)
        print(turncount)
    if turncount % 2 == 1 and turncount < 9:
        turncount = if_no_win_loss(game_board, turncount)
        print(turncount)
    print("turncount is", turncount)
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
    return turncount


def search_for_win(dict, turncount):
    print("search_for_win ", turncount)
#This is the bot looking for a win---goes down sequentially from different starting points
    if dict["1"] == "O" and dict["2"] == "O" and dict["3"] == "3" and turncount % 2 == 1:
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["5"] == "O" and dict["9"] == "9" and turncount % 2 == 1:
        dict["9"] = "O"

        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["3"] == "O" and dict["2"] == "2" and turncount % 2 == 1:
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["9"] == "O" and dict["5"] == "5" and turncount % 2 == 1:
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["4"] == "O" and dict["7"] == "7" and turncount % 2 == 1:
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "O" and dict["7"] == "O" and dict["4"] == "4" and turncount % 2 == 1:
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "O" and dict["3"] == "O" and dict["1"] == "1" and turncount % 2 == 1:
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "O" and dict["5"] == "O" and dict["8"] == "8" and turncount % 2 == 1:
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "O" and dict["8"] == "O" and dict["5"] == "5" and turncount % 2 == 1:
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "O" and dict["5"] == "O" and dict["7"] == "7" and turncount % 2 == 1:
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "O" and dict["7"] == "O" and dict["5"] == "5" and turncount % 2 == 1:
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "O" and dict["6"] == "O" and dict["9"] == "7" and turncount % 2 == 1:
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "O" and dict["9"] == "O" and dict["6"] == "6" and turncount % 2 == 1:
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "O" and dict["5"] == "O" and dict["6"] == "6" and turncount % 2 == 1:
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "O" and dict["6"] == "O" and dict["5"] == "5" and turncount % 2 == 1:
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "O" and dict["7"] == "O" and dict["1"] == "1" and turncount % 2 == 1:
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "O" and dict["5"] == "O" and dict["4"] == "4" and turncount % 2 == 1:
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "O" and dict["9"] == "O" and dict["1"] == "1" and turncount % 2 == 1:
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "O" and dict["5"] == "O" and dict["3"] == "3" and turncount % 2 == 1:
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "O" and dict["4"] == "O" and dict["1"] == "1" and turncount % 2 == 1:
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "O" and dict["8"] == "O" and dict["9"] == "9" and turncount % 2 == 1:
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "O" and dict["9"] == "O" and dict["8"] == "8" and turncount % 2 == 1:
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "O" and dict["5"] == "O" and dict["2"] == "2" and turncount % 2 == 1:
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "O" and dict["9"] == "O" and dict["7"] == "7" and turncount % 2 == 1:
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "O" and dict["5"] == "O" and dict["1"] == "1" and turncount % 2 == 1:
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "O" and dict["6"] == "O" and dict["3"] == "3" and turncount % 2 == 1:
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "O" and dict["1"] == "O" and dict["5"] == "5" and turncount % 2 == 1:
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("you passed search_for_win")
        return turncount


def search_for_loss(dict, turncount):
    print("search_for_loss ", turncount)
# This is the bot looking for a potential loss---goes down sequentially from different starting points
    if dict["1"] == "X" and dict["2"] == "X" and dict["3"] == "3" and turncount % 2 == 1:
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["5"] == "X" and dict["9"] == "9" and turncount % 2 == 1:
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["3"] == "X" and dict["2"] == "2" and turncount % 2 == 1:
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["9"] == "X" and dict["5"] == "5" and turncount % 2 == 1:
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["4"] == "X" and dict["7"] == "7" and turncount % 2 == 1:
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["1"] == "X" and dict["7"] == "X" and dict["4"] == "4" and turncount % 2 == 1:
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X" and dict["3"] == "X" and dict["1"] == "1" and turncount % 2 == 1:
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X" and dict["5"] == "X" and dict["8"] == "8" and turncount % 2 == 1:
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["2"] == "X" and dict["8"] == "X" and dict["5"] == "5" and turncount % 2 == 1:
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X" and dict["5"] == "X" and dict["7"] == "7" and turncount % 2 == 1:
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X" and dict["7"] == "X" and dict["5"] == "5" and turncount % 2 == 1:
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X" and dict["6"] == "X" and dict["9"] == "7" and turncount % 2 == 1:
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["3"] == "X" and dict["9"] == "X" and dict["6"] == "6" and turncount % 2 == 1:
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X" and dict["5"] == "X" and dict["6"] == "6" and turncount % 2 == 1:
        dict["6"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X" and dict["6"] == "X" and dict["5"] == "5" and turncount % 2 == 1:
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["4"] == "X" and dict["7"] == "X" and dict["1"] == "1" and turncount % 2 == 1:
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X" and dict["5"] == "X" and dict["4"] == "4" and turncount % 2 == 1:
        dict["4"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["6"] == "X" and dict["9"] == "X" and dict["1"] == "1" and turncount % 2 == 1:
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X" and dict["5"] == "X" and dict["3"] == "3" and turncount % 2 == 1:
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X" and dict["4"] == "X" and dict["1"] == "1" and turncount % 2 == 1:
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X" and dict["8"] == "X" and dict["9"] == "9" and turncount % 2 == 1:
        dict["9"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["7"] == "X" and dict["9"] == "X" and dict["8"] == "8" and turncount % 2 == 1:
        dict["8"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X" and dict["5"] == "X" and dict["2"] == "2" and turncount % 2 == 1:
        dict["2"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["8"] == "X" and dict["9"] == "X" and dict["7"] == "7" and turncount % 2 == 1:
        dict["7"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X" and dict["5"] == "X" and dict["1"] == "1" and turncount % 2 == 1:
        dict["1"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X" and dict["6"] == "X" and dict["3"] == "3" and turncount % 2 == 1:
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X" and dict["1"] == "X" and dict["5"] == "5" and turncount % 2 == 1:
        dict["5"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    elif dict["9"] == "X" and dict["6"] == "X" and dict["3"] == "3" and turncount % 2 == 1:
        dict["3"] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        return turncount
    else:
        print("you passed search_for_loss")
        return turncount
def if_no_win_loss(dict, turncount):
    print("search_for_no_win_loss ", turncount)
    #the bot runs this code if there is no winning or losing move
    possible_moves = []
    for i in dict:
        if dict[str(i)] == str(i):
            possible_moves.append(str(i))
    if possible_moves == [] and turncount < 9:
        pass
    elif turncount < 9:
        move_choice = random.choice(possible_moves)
        move_choice = str(move_choice)
        print("move_choice ", move_choice)
        dict[move_choice] = "O"
        print(gameboard(dict))
        turncount = turncount + 1
        print("if_no_win_loss ", turncount, " after choosing move?")
    else:
        turncount = turncount + 1
        pass
    return turncount

"""
def is_won(game_board):
    win = ""
    if game_board["1"] == "X" and game_board["2"] == "X" and game_board["3"] == "X":
        win = "yes"
        return win
    elif game_board["4"] == "X" and game_board["5"] == "X" and game_board["6"] == "X":
        win = "yes"
        return win
    elif game_board["7"] == "X" and game_board["8"] == "X" and game_board["9"] == "X":
        win = "yes"
        return win
    elif game_board["1"] == "X" and game_board["4"] == "X" and game_board["7"] == "X":
        win = "yes"
        return win
    elif game_board["2"] == "X" and game_board["5"] == "X" and game_board["8"] == "X":
        win = "yes"
        return win
    elif game_board["3"] == "X" and game_board["6"] == "X" and game_board["9"] == "X":
        win = "yes"
        return win
    elif game_board["1"] == "X" and game_board["5"] == "X" and game_board["9"] == "X":
        win = "yes"
        return win
    elif game_board["7"] == "X" and game_board["5"] == "X" and game_board["3"] == "X":
        win = "yes"
        return win
    elif game_board["1"] == "O" and game_board["2"] == "O" and game_board["3"] == "O":
        win = "yes"
        return win
    elif game_board["4"] == "O" and game_board["5"] == "O" and game_board["6"] == "O":
        win = "yes"
        return win
    elif game_board["7"] == "O" and game_board["8"] == "O" and game_board["9"] == "O":
        win = "yes"
        return win
    elif game_board["1"] == "O" and game_board["4"] == "O" and game_board["7"] == "O":
        win = "yes"
        return win
    elif game_board["2"] == "O" and game_board["5"] == "O" and game_board["8"] == "O":
        win = "yes"
        return win
    elif game_board["3"] == "O" and game_board["6"] == "O" and game_board["9"] == "O":
        win = "yes"
        return win
    elif game_board["1"] == "O" and game_board["5"] == "O" and game_board["9"] == "O":
        win = "yes"
        return win
    elif game_board["7"] == "O" and game_board["5"] == "O" and game_board["3"] == "O":
        return win
    else:
        return win
"""








def check_board(dict, turtle):
    top_left(dict, turtle)

    top_middle(dict, turtle)

    top_right(dict, turtle)

    middle_left(dict, turtle)

    middle(dict, turtle)

    middle_right(dict, turtle)

    bottom_left(dict, turtle)

    bottom_middle(dict, turtle)

    bottom_right(dict, turtle)
    return dict


def make_board(turtle):
    turtle.pensize(10)
    #first line
    turtle.right(90)
    turtle.penup()
    turtle.forward(75)
    turtle.left(90)
    turtle.forward(225)
    turtle.pendown()
    turtle.backward(450)
    turtle.penup()
    turtle.goto(0,0)
    #second line
    turtle.left(90)
    turtle.forward(75)
    turtle.right(90)
    turtle.forward(225)
    turtle.pendown()
    turtle.backward(450)
    turtle.penup()
    turtle.goto(0, 0)
    #third line
    turtle.goto(75,75)
    turtle.left(90)
    turtle.forward(225-75)
    turtle.pendown()
    turtle.backward(450)
    turtle.penup()
    turtle.goto(0,0)
    #fourthline
    turtle.goto(-75, 75)
    turtle.forward(225 - 75)
    turtle.pendown()
    turtle.backward(450)
    turtle.penup()
    draw_numbers(turtle)
    return turt

def draw_numbers(turtle):
    turtle.pensize(10)
    turtle.color("black")
    # Reference line 1
    #turtle.goto(-250, 115)
    #turtle.color("blue")
    #turtle.pendown()
    #turtle.setheading(0)
    #turtle.forward(550)
    #turtle.penup()
    #turtle.goto(-250, 200)
    #turtle.pendown()
    #turtle.setheading(0)
    #turtle.forward(550)
    #turtle.penup()
    #turtle.color("Black")

    # Make One

    turtle.penup()
    turt.goto(-175, 115)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(50)
    turtle.penup()
    turtle.goto(-150,115)
    turtle.pendown()
    turtle.setheading(90)
    turtle.forward(85)
    turtle.left(135)
    turtle.forward(25)

    # Make Two

    turtle.penup()
    turtle.goto(20, 115)
    turtle.setheading(180)
    turtle.pendown()
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(65)
    turtle.circle(20, 200)

    # Make Three

    turtle.penup()
    turtle.goto(130,200)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(40)
    turtle.right(120)
    turtle.forward(40)
    turtle.left(120)
    turtle.circle(-25, 200)
    turtle.pendown()

    # Make Four

    turtle.penup()
    turtle.goto(-125, -10)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(50)
    turtle.right(125)
    turtle.forward(60)
    turtle.setheading(270)
    turtle.forward(80)

    #Make Five

    turtle.penup()
    turtle.goto(20,45)
    turtle.pendown()
    turtle.setheading(180)
    turtle.forward(150-115)
    turtle.left(90)
    turtle.forward(40)
    turtle.left(110)
    turtle.circle(-25, 220)

    # Make Six

    turtle.penup()
    turtle.goto(150, -45)
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(25)
    turtle.setheading(180)
    turtle.circle(-25, 90)
    turtle.forward(40)
    turtle.circle(-25, 160)

    # Make Seven

    turtle.penup()
    turtle.goto(-175, -115)
    turtle.pendown()
    turtle.setheading(0)
    turtle.forward(50)
    turtle.right(105)
    turtle.forward(85)

    # Make Eight

    turtle.penup()
    turtle.goto(0, -160)
    turtle.setheading(0)
    turtle.pendown()
    turtle.circle(22.5)
    turtle.penup()
    turtle.goto(0, -205)
    turtle.pendown()
    turtle.circle(22.5)

    # Make Nine

    turtle.penup()
    turtle.goto(150, -160)
    turtle.pendown()
    turtle.setheading(0)
    turtle.circle(25)
    turtle.setheading(0)
    turtle.circle(25, 90)
    turtle.backward(40)
    turtle.circle(25, -160)
    turtle.hideturtle()
    turtle.penup()

def turtle_erase_mode(turtle):
    turtle.color("white")
    turtle.pensize(15)
    return turtle

def make_x(turtle):
    turtle.pensize(10)
    turtle.color("red")
    turtle.setheading(0)
    #first line
    turtle.penup()
    turtle.left(45)
    turtle.forward(50)
    turtle.pendown()
    turtle.backward(100)
    turtle.penup()
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.backward(100)
    turtle.penup()

def make_O(turtle):
    turtle.pensize(10)
    turtle.color("blue")
    #making circle
    turtle.penup()
    turtle.setheading(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.pendown()
    turtle.circle(50)
    turtle.penup()
    turtle.forward(100)


def top_left(dict, turtle):
    if dict["1"] == "X" or dict["1"] == "O":
        turtle.penup()
        turtle_erase_mode(turtle)
        turtle.goto(-175, 115)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(50)
        turtle.penup()
        turtle.goto(-150, 115)
        turtle.pendown()
        turtle.setheading(90)
        turtle.forward(85)
        turtle.left(135)
        turtle.forward(25)
        turtle.pensize(10)
        turtle.penup()
    else:
        pass
    turtle.goto(-150, 150)
    if dict["1"] == "X":
        make_x(turt)
    elif dict["1"] == "O":
        make_O(turt)
    else:
        pass
def top_middle(dict, turtle):
    if dict["2"] == "X" or dict["2"] == "O":
        turtle.penup()
        turtle_erase_mode(turtle)
        turtle.goto(20, 115)
        turtle.setheading(180)
        turtle.pendown()
        turtle.forward(40)
        turtle.right(120)
        turtle.forward(65)
        turtle.circle(20, 200)
        turtle.pensize(10)
        turtle.penup()
    else:
        pass

    turtle.goto(0, 150)
    if dict["2"] == "X":
        make_x(turt)
    elif dict["2"] == "O":
        make_O(turt)
    else:
        pass
def top_right(dict, turtle):
    if dict["3"] == "X" or dict["3"] == "O":
        turtle.penup()
        turtle_erase_mode(turtle)
        turtle.goto(130, 200)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(40)
        turtle.right(120)
        turtle.forward(40)
        turtle.left(120)
        turtle.circle(-25, 200)
        turtle.pensize(10)
        turtle.pendown()
        turtle.penup()
    else:
        pass
    turtle.goto(150, 150)
    if dict["3"] == "X":
        make_x(turt)
    elif dict["3"] == "O":
        make_O(turt)
    else:
        pass

def middle_left(dict,turtle):
    if dict["4"] == "X" or dict["4"] == "O":
        turtle.penup()
        turtle_erase_mode(turtle)
        turtle.goto(-125, -10)
        turtle.pendown()
        turtle.setheading(180)
        turtle.forward(50)
        turtle.right(125)
        turtle.forward(60)
        turtle.setheading(270)
        turtle.forward(80)
        turtle.pensize(10)
        turtle.penup()
    else:
        pass
    turtle.goto(-150, 0)
    if dict["4"] == "X":
        make_x(turt)
    elif dict["4"] == "O":
        make_O(turt)
    else:
        pass

def middle(dict, turtle):
    if dict["5"] == "X" or dict["5"] == "O":
        turtle.penup()
        turtle_erase_mode(turtle)
        turtle.goto(20, 45)
        turtle.pendown()
        turtle.setheading(180)
        turtle.forward(150 - 115)
        turtle.left(90)
        turtle.forward(40)
        turtle.left(110)
        turtle.circle(-25, 220)
        turtle.pensize(10)
        turtle.penup()
    turtle.goto(0, 0)
    if dict["5"] == "X":
        make_x(turt)
    elif dict["5"] == "O":
        make_O(turt)
    else:
        pass


def middle_right(dict, turtle):
    if dict["6"] == "X" or dict["6"] == "O":
        turtle.penup()
        turtle_erase_mode(turtle)
        turtle.goto(150, -45)
        turtle.setheading(0)
        turtle.pendown()
        turtle.circle(25)
        turtle.setheading(180)
        turtle.circle(-25, 90)
        turtle.forward(40)
        turtle.circle(-25, 160)
        turtle.penup()
    else:
        pass
    turtle.goto(150, 0)
    if dict["6"] == "X":
        make_x(turt)
    elif dict["6"] == "O":
        make_O(turt)
    else:
        pass

def bottom_left(dict, turtle):
    if dict["7"] == "X" or dict["7"] == "O":
        turtle.penup()
        turtle_erase_mode(turtle)
        turtle.goto(-175, -115)
        turtle.pendown()
        turtle.setheading(0)
        turtle.forward(50)
        turtle.right(105)
        turtle.forward(85)
        turtle.pensize(10)
        turtle.penup()
    else:
        pass
    turtle.goto(-150, -150)
    if dict["7"] == "X":
        make_x(turt)
    elif dict["7"] == "O":
        make_O(turt)
    else:
        pass

def bottom_middle(dict, turtle):
    if dict["8"] == "X" or dict["8"] == "O":
        turtle.penup()
        turtle_erase_mode(turtle)
        turtle.goto(0, -160)
        turtle.setheading(0)
        turtle.pendown()
        turtle.circle(22.5)
        turtle.penup()
        turtle.goto(0, -205)
        turtle.pendown()
        turtle.circle(22.5)
        turtle.pensize(10)
        turtle.penup()
    else:
        pass
    turtle.goto(0, -150)
    if dict["8"] == "X":
        make_x(turt)
    elif dict["8"] == "O":
        make_O(turt)
    else:
        pass

def bottom_right(dict, turtle):
    if dict["9"] == "X" or dict["9"] == "O":
        turtle.penup()
        turtle_erase_mode(turtle)
        turtle.goto(150, -160)
        turtle.pendown()
        turtle.setheading(0)
        turtle.circle(25)
        turtle.setheading(0)
        turtle.circle(25, 90)
        turtle.backward(40)
        turtle.circle(25, -160)
        turtle.pensize(10)
        turtle.penup()
    turtle.goto(150, -150)
    if dict["9"] == "X":
        make_x(turt)
    elif dict["9"] == "O":
        make_O(turt)
    else:
        pass


lossPic = Picture("Screenshot 2024-05-01 at 8.13.26 PM.png")

def loss_picture(lossPic):
    lossPic.show()







turncount = 0
print(gameboard(game_board))
print("turncount is", turncount)
wn.tracer(0)
make_board(turt)
wn.update()
win = ""
for i in range(9):
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
    if type(turncount) != int:
        print("we got a problem chief")
    if turncount < 3:
        turncount = gameplay(game_board, turncount)
        print("you're still in hell", turncount)
        wn.tracer(0)
        check_board(game_board, turt)
        wn.update()
    elif turncount >= 3:
        print("YOU MADE IT TO POSTT4 BOT CODE", turncount)
        turncount = post_t4_bot_code(game_board, turncount)
    wn.tracer(0)
    check_board(game_board, turt)
    wn.update()
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
        loss_picture(lossPic)
        win = "yes"
        break
    elif game_board["4"] == "O" and game_board["5"] == "O" and game_board["6"] == "O":
        print("O wins!")
        loss_picture(lossPic)
        win = "yes"
        break
    elif game_board["7"] == "O" and game_board["8"] == "O" and game_board["9"] == "O":
        print("O wins!")
        loss_picture(lossPic)
        win = "yes"
        break
    elif game_board["1"] == "O" and game_board["4"] == "O" and game_board["7"] == "O":
        print("O wins!")
        loss_picture(lossPic)
        win = "yes"
        break
    elif game_board["2"] == "O" and game_board["5"] == "O" and game_board["8"] == "O":
        print("O wins!")
        loss_picture(lossPic)
        win = "yes"
        break
    elif game_board["3"] == "O" and game_board["6"] == "O" and game_board["9"] == "O":
        print("O wins!")
        loss_picture(lossPic)
        win = "yes"
        break
    elif game_board["1"] == "O" and game_board["5"] == "O" and game_board["9"] == "O":
        print("O wins!")
        loss_picture(lossPic)
        win = "yes"
        break
    elif game_board["7"] == "O" and game_board["5"] == "O" and game_board["3"] == "O":
        print("O wins!")
        loss_picture(lossPic)
        win = "yes"
        break
if win != "yes":
    print("It's a tie!")


wn.exitonclick()