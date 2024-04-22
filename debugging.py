import random
# this is a work doc. feel free to delete or edit, its just to check if things are working before implementing
# it in the full game.
game_board = { # DO NOT CHANGE
    "1" : "O",
    "2" : "X",
    "3" : "X",
    "4" : "4",
    "5" : "O",
    "6" : "6",
    "7" : "7",
    "8" : "8",
    "9" : "X"
}

def if_no_win_loss(dict, turncount):
    #the bot runs this code if there is no winning or losing move
    possible_moves = []
    for i in dict:
        if dict[str(i)] == str(i):
            possible_moves.append(str(i))
        else:
            pass
    move_choice = random.choice(possible_moves)
    move_choice = str(move_choice)
    dict[move_choice] = "O"
    turncount = turncount + 1
    return turncount

def gameboard(game_board): #DO NOT CHANGE
    print (" ", game_board["1"], " ", "|", " ", game_board["2"], " ", "|", " ", game_board["3"], " ",)
    print("------|-------|------")
    print (" ", game_board["4"], " ", "|", " ", game_board["5"], " ", "|", " ", game_board["6"], " ",)
    print("------|-------|------")
    print (" ", game_board["7"], " ", "|", " ", game_board["8"], " ", "|", " ", game_board["9"], " ",)
    pass



turncount = 5


if_no_win_loss(game_board, turncount)
gameboard(game_board)



