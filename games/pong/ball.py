from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        self.color("white")
        self.goto(0, 0)

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        # increases move speed
        self.move_speed *= 0.9

    def reset(self, towards):
        # reset the move speed
        self.move_speed = 0.1
        self.goto(0, 0)
        if towards == "left":
            self.x_move = -10
        else:
            self.x_move = 10
        self.y_move = 10


