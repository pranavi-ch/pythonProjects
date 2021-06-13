import time
from turtle import Turtle

FONT = ("courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.show_score(3)

    def level_up(self, lives):
        self.clear()
        self.score += 1
        self.goto(0, 0)
        self.write("Level Up !", font=FONT, align="center")
        time.sleep(0.7)
        self.show_score(lives)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write("Game Over!", font=FONT, align="center")

    def show_score(self, lives):
        self.clear()
        self.goto(-290, 270)
        self.write(f"Score : {self.score}", font=FONT)
        self.goto(120, 270)
        self.write(f"Lives : {lives}", font=FONT)

    def lost_a_life(self):
        self.clear()
        self.goto(0, 0)
        self.write("You hit a car !", font=FONT, align="center")
        time.sleep(0.7)
