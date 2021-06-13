import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard

# screen setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height= 600)
screen.title("Pong")
screen.tracer(0)


# ask user paddle color preference
paddle_color = screen.textinput(prompt="What color do you want your paddles?(Red/green/blue/yellow/magenta)",
                                title="Paddle Color").lower()
total_points = int(screen.textinput(prompt = "How many points do you want to play for?", title = "How many points"))


# right and left paddle
paddle_r = Paddle(paddle_color,350)
paddle_l = Paddle(paddle_color,-350)

# create ball
ball = Ball()

# scoreboard
score_board = Scoreboard()
screen.listen()

screen.onkey(paddle_l.move_up,"w")
screen.onkey(paddle_l.move_down,"s")
screen.onkey(paddle_r.move_up,"Up")
screen.onkey(paddle_r.move_down,"Down")

# while ********************************************
game_is_on = True
winner = None
while game_is_on:
    score_board.display_scoreboard()
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

    # detect collision with wall top and bottom walls,
    # change dir, 280 because width of box is 20
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    # right paddle :
    # ball.xcor() ->
    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if ball is missed by r or l paddle
    if ball.xcor() > 380:
        # l scored
        score_board.inc_lscore()
        if(score_board.lscore == total_points):
            winner = "left"
            break

        time.sleep(0.9)
        ball.reset("right")

    if(ball.xcor()) < -380:
        # r scored
        score_board.inc_rscore()
        if(score_board.rscore == total_points):
            winner = "right"
            break
        time.sleep(0.9)
        ball.reset("left")

# end while ***********************************************
display_winner_turtle = Turtle()
display_winner_turtle.color("cyan")
display_winner_turtle.penup()
display_winner_turtle.goto(80,20)
display_winner_turtle.write(f"{winner} won! ✌🎊\nPress (esc)",align="center",
                   font=("courier", 50, "bold"))

screen.exitonclick()