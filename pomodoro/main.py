import math
from tkinter import *

# TODO include sounds

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global timer
    global reps

    # to stop the count mechanism, cancels the function
    window.after_cancel(timer)

    # display title as timer again
    title_label.config(text="Timer")

    # reset to 00:00
    canvas.itemconfig(timer_text, text="00:00")

    # reset reps to 0
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    time_in_secs = 0
    # config used to change the internals of widget
    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        time_in_secs = WORK_MIN * 60
        title_label.config(text="WORK", fg=GREEN)
    elif reps == 2 or reps == 4 or reps == 6:
        time_in_secs = SHORT_BREAK_MIN * 60
        title_label.config(text="SHORT BREAK", fg=PINK)
    elif reps == 8:
        time_in_secs = LONG_BREAK_MIN * 60
        title_label.config(text="LONG BREAK", fg=RED)
        reps = 0

    count_down(time_in_secs)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    # converting seconds to minutes and seconds
    global timer
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"
    timer_string = str(minutes) + ":" + str(seconds)
    # to change the image         // we want to change the timer dims
    canvas.itemconfig(timer_text, text=timer_string)
    if count > 0:
        # after one second, call countdown again, with count as time-1 second since one sec has passed
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        checks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            checks += "✔"
        check_marks.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #

# To create a main window, tkinter offers a method Tk
window = Tk()
window.title("Pomodoro")
# add padding TO THE CANVAS from window
window.config(padx=20, pady=20, bg=YELLOW)

# Canvas widget allows to layer widgets
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# creates object of the image
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)

# create timer/Break/Work label (Label object) widget, adds the heading of ('Timer')
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 40), bg=YELLOW)
title_label.grid(column=1, row=0)

# countdown timer
timer_text = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# buttons-> start and reset, use 'command' kwarg to enable click to start
start_button = Button(text="Start", highlightthickness=0, font=(FONT_NAME, 15), command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", highlightthickness=0, font=(FONT_NAME, 15), command=reset_timer)
reset_button.grid(column=2, row=2)

# display check mark text label widget
check_marks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15))
check_marks.grid(column=1, row=3)

# mainloop()
# is used when your application is ready to run.
# mainloop() is an infinite loop used to run the application,
# wait for an event to occur and process the event as long as the window is not closed.
window.mainloop()
