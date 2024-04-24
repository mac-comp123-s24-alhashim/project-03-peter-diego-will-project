import turtle

game_board = { # DO NOT CHANGE
    "1" : "O",
    "2" : "O",
    "3" : "X",
    "4" : "O",
    "5" : "X",
    "6" : "O",
    "7" : "X",
    "8" : "O",
    "9" : "O"
}

wn = turtle.Screen()

turt = turtle.Turtle()


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
    return turt


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
    turtle.goto(-150, 150)
    if dict["1"] == "X":
        make_x(turt)
    elif dict["1"] == "O":
        make_O(turt)
    else:
        pass
def top_middle(dict, turtle):
    turtle.goto(0, 150)
    if dict["2"] == "X":
        make_x(turt)
    elif dict["2"] == "O":
        make_O(turt)
    else:
        pass
def top_right(dict, turtle):
    turtle.goto(150, 150)
    if dict["3"] == "X":
        make_x(turt)
    elif dict["3"] == "O":
        make_O(turt)
    else:
        pass

def middle_left(dict,turtle):
    turtle.goto(-150, 0)
    if dict["4"] == "X":
        make_x(turt)
    elif dict["4"] == "O":
        make_O(turt)
    else:
        pass

def middle(dict, turtle):
    turtle.goto(0, 0)
    if dict["5"] == "X":
        make_x(turt)
    elif dict["5"] == "O":
        make_O(turt)
    else:
        pass


def middle_right(dict, turtle):
    turtle.goto(150, 0)
    if dict["6"] == "X":
        make_x(turt)
    elif dict["6"] == "O":
        make_O(turt)
    else:
        pass

def bottom_left(dict, turtle):
    turtle.goto(-150, -150)
    if dict["7"] == "X":
        make_x(turt)
    elif dict["7"] == "O":
        make_O(turt)
    else:
        pass

def bottom_middle(dict, turtle):
    turtle.goto(0, -150)
    if dict["8"] == "X":
        make_x(turt)
    elif dict["8"] == "O":
        make_O(turt)
    else:
        pass

def bottom_right(dict, turtle):
    turtle.goto(150, -150)
    if dict["9"] == "X":
        make_x(turt)
    elif dict["9"] == "O":
        make_O(turt)
    else:
        pass


turt.speed("fastest")

make_board(turt)

check_board(game_board, turt)


wn.exitonclick()


