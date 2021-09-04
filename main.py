from tkinter import *
import math

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
# reset timer
def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    canvas.itemconfig(timer_text, text=f"00:00")
    # title_label "Timer"
    title_label.config(text="Timer")
    # reset check_marks
    check_marks.config(text="")
    # reset reps
    global  reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
# button start
def start_timer():
    global reps

    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        # If it's the 8th rep:
        count_down(long_break_sec)
        title_label.config(text="Long break", fg=RED)
    elif reps % 2 == 0:
        # If it's the 2nd/4th/6th
        count_down(short_break_sec)
        title_label.config(text="Short break", fg=PINK)
    else:
        # If it's the 1st/3rd/5th/7th rep:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"  # Dynamic typing

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Timer title label
title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 36, "bold"))
title_label.grid(column=1, row=0)

# Tomato
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column=1, row=1)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

# Check mark

check_marks = Label(font=(FONT_NAME, 11, "bold"), fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

window.mainloop()
