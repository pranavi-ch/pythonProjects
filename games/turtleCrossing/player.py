from turtle import Turtle

STARTING_POSITION = (0, -280)
FINISH_LINE_Y = (0, 280)
MOVE_DIST = 10
FONT = ("courier", 20, "normal")


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.lives = 3

    def go_up(self):
        self.forward(MOVE_DIST)

    def go_down(self):
        self.backward(MOVE_DIST)

    def reduce_lives(self):
        self.lives -= 1
