import time
from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highscore.txt") as hs:
            self.high_score = int(hs.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        # clear the previous score
        self.clear()
        self.goto(0, 270)
        self.write(f"Score : {self.score}  HighScore: {self.high_score}", align="center",
                   font=("courier", 22, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=("courier", 22, "normal"))
        time.sleep(0.5)
        self.clear()
        if self.score > self.high_score:
            self.goto(0, 0)
            self.write("New High Score!", align="center", font=("courier", 22, "normal"))
            time.sleep(0.5)
        self.clear()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt",mode="w") as hs:
                hs.write(f"{self.high_score}")
        # reset score to 0
        self.score = 0
        self.update_scoreboard()
