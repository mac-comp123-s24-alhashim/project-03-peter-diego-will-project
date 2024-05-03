from tkinter import *

game_board = {  # DO NOT CHANGE
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
}
def gameboard(game_board): #DO NOT CHANGE
    print (" ", game_board["1"], " ", "|", " ", game_board["2"], " ", "|", " ", game_board["3"], " ",)
    print("------|-------|------")
    print (" ", game_board["4"], " ", "|", " ", game_board["5"], " ", "|", " ", game_board["6"], " ",)
    print("------|-------|------")
    print (" ", game_board["7"], " ", "|", " ", game_board["8"], " ", "|", " ", game_board["9"], " ",)
    pass

pmove = None
def player_move():
    def submit():
        global pmove
        pmove = entry.get()
        pmove = pmove[-1]
        pmove = str(pmove)
        window.destroy()
        return pmove

    window = Tk()
    window.title("Select Move")
    submit = Button(window, text="Lock in Move", command=submit)
    submit.pack()
    entry = Entry(window)
    entry.config(font=("Helvetica", 20))
    entry.insert(0, "Insert Move 1-9: ")
    entry.config(width=20)
    entry.pack()
    window.mainloop()


player_move()
game_board[pmove] = "X"
print(game_board)

print("hi")

print(gameboard)
