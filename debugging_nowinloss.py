import random

game_board = { # DO NOT CHANGE
    "1" : "X",
    "2" : "O",
    "3" : "X",
    "4" : "X",
    "5" : "O",
    "6" : "X",
    "7" : "O",
    "8" : "O",
    "9" : "X"
}

def if_no_win_loss(dict, turncount):
    #the bot runs this code if there is no winning or losing move
    possible_moves = []
    for i in dict:
        if dict[str(i)] == str(i):
            possible_moves.append(str(i))
    if possible_moves == []:
        pass
    else:
        move_choice = random.choice(possible_moves)
        print(possible_moves)
        print(move_choice)
        dict[move_choice] = "O"
        print(dict)
    return turncount

turncount = 1
if_no_win_loss(game_board, turncount)