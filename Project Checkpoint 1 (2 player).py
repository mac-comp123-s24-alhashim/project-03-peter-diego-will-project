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
        ask2 = input("X or O?")
        ask2 = check_is_x(ask2)
    elif turncount % 2 == 1:
        ask2 = input("X or O?")
        ask2 = check_is_o(ask2)
    ask1 = input("Which space do you want to input for? (1-9)")
    ask1 = is_space_taken(game_board, ask1)
    dict[ask1] = ask2
    print(gameboard(dict))
    turncount = turncount + 1
    print(turncount)
    return turncount

def gameboard(game_board): #DO NOT CHANGE
    print (" ", game_board["1"], " ", "|", " ", game_board["2"], " ", "|", " ", game_board["3"], " ",)
    print("------|-------|------")
    print (" ", game_board["4"], " ", "|", " ", game_board["5"], " ", "|", " ", game_board["6"], " ",)
    print("------|-------|------")
    print (" ", game_board["7"], " ", "|", " ", game_board["8"], " ", "|", " ", game_board["9"], " ",)
    pass

turncount = 0
print(gameboard(game_board))
win = ""
for i in range(9):
    turncount = gameplay(game_board, turncount)
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