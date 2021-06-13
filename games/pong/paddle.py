from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,user_color,xcor):
        Turtle.__init__(self)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color(user_color)
        self.penup()
        self.speed("fast")
        self.goto(xcor,0)

    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(),new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(),new_y)

