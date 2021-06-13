import turtle
from turtle import Screen
import time
from car import CarManager
from player import Player
from scoreboard import Scoreboard

turtle.hideturtle()
screen = Screen()
screen.bgcolor("white")
screen.setup(width=600, height=600)
screen.tracer(0)

# player is a turtle
player = Player()
car_manager = CarManager()
score_board = Scoreboard()
game_is_on = True
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # detect car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 25:
            player.reduce_lives()
            if player.lives == 0:
                game_is_on = False
                score_board.game_over()
            else:
                score_board.lost_a_life()
                score_board.show_score(player.lives)
                time.sleep(0.7)
                player.goto(0, -280)
                car_manager.reset_cars()

    # detect when turtle reached the other side
    if player.ycor() > 280:
        score_board.level_up(player.lives)
        player.goto(0, -280)
        car_manager.reset_cars()

screen.exitonclick()
