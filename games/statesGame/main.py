import turtle
import pandas
import time
import threading

# setup
screen = turtle.Screen()
screen.setup(width=700, height=700)
screen.title("Indian States Game")
# insert image of blank map into screen
screen.addshape("blank-map.gif")
turtle.shape("blank-map.gif")
# retrieve data and convert to dataframe object
states_data = pandas.read_csv("states.csv")
# convert the state names into a list
states_list = states_data["state"].tolist()


# # code snipped used to calculate the coordinates of the states:
# screen.addshape("filled-map.gif")
# turtle.shape("filled-map.gif")

# get coordinates on mouse click
# def get_coord(x, y):
#     print(x, y)

# turtle.onscreenclick(get_coord)
# # keeps screen open
# turtle.mainloop()

# setup


def print_elapsed_time(elapsed_time):
    writer = turtle.Turtle()
    writer.hideturtle()
    writer.pencolor("black")
    writer.penup()
    writer.goto(-250, 0)
    writer.write(f'You took {round(elapsed_time, 2)} secs', align="left",
                 font=("courier", 30, "bold"))


def write_state(write_state):
    x_coor = float(states_data[states_data["state"] == write_state]["x"])
    y_coor = float(states_data[states_data["state"] == write_state]["y"])
    writer = turtle.Turtle()
    writer.pencolor("black")
    writer.penup()
    writer.goto(x_coor, y_coor)
    writer.write(f"{write_state}", align="left",
                 font=("courier", 10, "normal"))


def print_missed_states(missed_states):
    writer = turtle.Turtle()
    writer.pencolor("red")
    writer.penup()
    if len(missed_states) == 0:
        writer.goto(-300,0)
        writer.write("You didn't miss anything!, Good Job", align="left",
                     font=("courier", 20, "normal"))
        return

    y = 300
    writer.goto(-300, y)
    writer.write("You missed : ", align="left",
                 font=("courier", 20, "normal"))
    for i in range(0, len(missed_states)):
        y -= 20
        writer.goto(0, y)
        writer.write(f"{i+1}) {missed_states[i]}", align="left",
                     font=("courier", 14, "normal"))


def update_high_score(elapsed):
    with open("high_score.txt") as timefile:
        least_time = float(timefile.read())

    with open("high_score.txt", "w") as timefile:
        if least_time > elapsed:
            writer = turtle.Turtle()
            writer.pencolor("red")
            writer.penup()
            writer.goto(-300, 0)
            writer.write("NEW HIGH SCORE!", align="left",
                             font=("courier", 20, "normal"))
            timefile.write(f"{elapsed}")
        else:
            timefile.write(f"{least_time}")


guessed_states_count = 0
start_time = time.time()
# start game
while guessed_states_count < 28:
    # prompt user to enter state name
    answer_state = screen.textinput(title="Guess a state name",
                                    prompt=f"Enter the name of a state/exit, guessed : {guessed_states_count}/28")
    if (answer_state == "exit"):
        break
    if answer_state.title() in states_list:
        # fill name in state
        write_state(answer_state.title())
        guessed_states_count += 1
        # to avoid matching again
        states_list.remove(answer_state.title())

# print how much time taken
elapsed_time = round(time.time() - start_time, 2)
print_elapsed_time(elapsed_time)
time.sleep(0.6)
screen.clear()
print_missed_states(states_list)
if len(states_list) == 0:
    update_high_score(elapsed_time)

screen.exitonclick()
