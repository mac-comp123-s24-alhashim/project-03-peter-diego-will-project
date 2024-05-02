import turtle

game_board = { # DO NOT CHANGE
    "1" : "1",
    "2" : "O",
    "3" : "3",
    "4" : "4",
    "5" : "X",
    "6" : "O",
    "7" : "7",
    "8" : "X",
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

    #third line
    turtle.goto(75,75)
    turtle.left(90)
    turtle.forward(225-75)
    turtle.pendown()
    turtle.backward(450)
    turtle.penup()

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


turt.speed(5)
wn.tracer(0)
make_board(turt)


check_board(game_board, turt)

wn.update()

wn.exitonclick()


