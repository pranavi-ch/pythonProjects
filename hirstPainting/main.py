import colorgram
import random as rm
from turtle import Turtle, Screen
import turtle as tr

tr.colormode(255)

colors = colorgram.extract('hirst.jpg',30)

rgb_colors = []
def gen_color_set():
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        #create rgb color tuple
        new_color = (r, g, b)
        rgb_colors.append(new_color)


def gen_random_color():
    return rm.choice(rgb_colors)


def draw_hirst(t):
    t.hideturtle()
    t.speed("fastest")
    t.setheading(220)
    t.penup()
    t.forward(250)
    t.setheading(0)
    for dot in range(1,101):
        t.dot(10, gen_random_color())
        t.forward(50)
        if dot % 10 == 0:
            t.setheading(90)
            t.forward(50)
            t.setheading(180)
            t.forward(500)
            t.setheading(0)



gen_color_set()
t = Turtle()
draw_hirst(t)


screen = Screen()
screen.exitonclick()

