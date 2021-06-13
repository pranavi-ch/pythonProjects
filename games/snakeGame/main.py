from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Classic Snake Game")

# controls the frame updating
screen.tracer(0)

# we make 3 turtles with 3 squares and consider it as a snake- in snake.py file
snake_color = screen.textinput(prompt="What color snake would you like?(blue/green/white/red/magenta/purple)",
                               title="Snake color").lower()
snake = Snake(snake_color)

# initializes food shape , speed ,size,
food = Food()

# scoreboard
score_board = Scoreboard()

# animating the snake movement (moving the snake)
screen.listen()
screen.onkey(key="Up",fun=snake.up)
screen.onkey(key="Down",fun=snake.down)
screen.onkey(key="Left",fun=snake.left)
screen.onkey(key="Right",fun=snake.right)
game_is_on = True


while game_is_on:
    screen.update()  # related to the tracer()
    time.sleep(0.1)  # changes the frame speed
    snake.move()
    # create food and detect collision with the food, relocate after every collision
    if snake.head.distance(food) < 15:
        score_board.increase_score()
        snake.extend()
        food.refresh()

    if(snake.head.xcor() > 300 or snake.head.xcor() < -300
            or snake.head.ycor() > 300 or snake.head.ycor() < -300):
        score_board.game_over()
        score_board.reset()
        snake.reset()
        time.sleep(0.9)

    # detect collision with tail, slicing list
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score_board.game_over()
            score_board.reset()
            snake.reset()
            time.sleep(0.9)

    # increase speed
    if score_board.score == 6:
        snake.inc_speed("fast")
    if score_board.score == 11:
        snake.inc_speed("fastest")

screen.exitonclick()
