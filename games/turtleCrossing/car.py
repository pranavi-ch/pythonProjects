import time
import turtle
from turtle import Turtle
import random

STARTING_MOVE_DIST = 5
MOVE_INCREMENT = 10
CHANCES = 10


colors = ["purple","sea green","teal","blue","light blue","red",
          "lavender","pink","yellow","orange"]


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.car_speed = STARTING_MOVE_DIST
        self.chances = CHANCES

    def create_car(self):
        random_chance = random.randint(0,self.chances)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(colors))
            new_car.penup()
            # leave safe space for turtle
            random_y = random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def reset_cars(self):
        # increase speed of cars, increase chances
        if self.chances > 2:
            self.chances -= 1
        self.car_speed = MOVE_INCREMENT




