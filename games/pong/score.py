from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.lscore = 0
        self.rscore = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.color("white")
        self.display_scoreboard()

    def inc_rscore(self):
        self.rscore += 1

    def inc_lscore(self):
        self.lscore += 1

    def display_scoreboard(self):
        self.clear()
        self.goto(-120,200)
        self.write(f"{self.lscore}", align="center",
                   font=("courier", 50, "normal"))
        self.goto(120,200)
        self.write(f"{self.rscore}", align="center",
                   font=("courier", 50, "normal"))
