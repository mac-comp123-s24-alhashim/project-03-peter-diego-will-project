game_board = {
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

def check_is_xo(stringin):
    stringin = stringin.lower()
    if stringin == "x" or stringin == "o":
        pass
    else:
        while stringin != "x" and stringin != "o":
            stringin = input("Please enter an X or an O")
    return stringin

def check_is_x(stringin):
    stringin = stringin.lower()
    if stringin == "x":
        pass
    else:
        while stringin != "x":
            stringin = input("It is X's turn")
    return stringin

def check_is_o(stringin):
    stringin = stringin.lower()
    if stringin == "o":
        pass
    else:
        while stringin != "o":
            stringin = input("It is O's turn")
    return stringin

def check_whoturn(stringin, turncount):
    if turncount % 2 == 0:
        check_is_x(stringin)
    else:
        check_is_o(stringin)

def gameplay(dict):
    print(dict["1"])
    ask1 = input("Which space do you want to input for? (1-9)")
    ask2 = input("What would you like to make that space?")
    ask2 = check_is_xo(ask2)
    dict[ask1] = ask2
    print(gameboard(dict))
    pass

def gameboard(game_board):
    print (" ", game_board["1"], " ", "|", " ", game_board["2"], " ", "|", " ", game_board["3"], " ",)
    print (" ", game_board["4"], " ", "|", " ", game_board["5"], " ", "|", " ", game_board["6"], " ",)
    print (" ", game_board["7"], " ", "|", " ", game_board["8"], " ", "|", " ", game_board["9"], " ",)
    pass

while game_board["1"] == "1" and game_board["2"] == "2" and game_board["3"] == "3":
    gameplay(game_board)