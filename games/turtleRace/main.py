import turtle
from turtle import Turtle, Screen
import random

# set width and height of the screen
screen = Screen()
screen.setup(height=400, width=500)
colors = ["red","orange","purple","blue","green","yellow"]
screen.bgcolor("black")
turtle.pencolor("white")
turtles = []
x = -220
y = 120
for i in range (0,6):
    turtles.append(Turtle("turtle"))
    turtles[i].penup()
    turtles[i].color(colors[i])
    turtles[i].goto(x,y)
    y -= 40

user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Pick the color-> ")

is_race_on = False
if user_bet:
    is_race_on = True
winner = ""

while is_race_on:
    for i in range(0,6):
        dist = random.randint(0,10)
        t = turtles[i]
        t.forward(dist)
        if t.xcor() >= 220:
            winner += colors[i]
            is_race_on = False
            break


turtle.penup()
turtle.hideturtle()

if user_bet.lower() == winner:
    turtle.write(f"You won! the winning turtle was : {winner.upper()}, Congrats! 🎉🎊 ", True, align="center")
else:
    turtle.write(f"You lost, the winning turtle was : {winner.upper()}, Sorry 😪", True, align="center")

screen.exitonclick()
