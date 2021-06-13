from turtle import Turtle, Screen

screen = Screen()
t= Turtle()


def move_forwards():
    # since t is global
    t.forward(10)


def move_backwards():
    t.back(10)

def rotate_clockwise():
    t.right(20)

def rotate_anticlockwise():
    t.left(20)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

screen.listen()
#  if you add brackets in the fun name, it executes then and there, but that's not what we want
# placeholder arguments

screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=rotate_anticlockwise)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="c", fun = clear)
screen.exitonclick()