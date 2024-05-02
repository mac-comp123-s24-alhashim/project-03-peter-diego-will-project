import turtle

# Initialize the turtle
pen = turtle.Turtle()

# Draw a red square
pen.color("black")
pen.pensize(10)
for _ in range(4):
    pen.forward(100)
    pen.right(90)

# Move the turtle to a new position
pen.penup()

pen.pendown()

# Draw a blue circle overlapping part of the square
pen.color("blue")
pen.circle(50)

turtle.done()