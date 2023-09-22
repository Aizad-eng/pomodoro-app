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

#RESETTING TIMER MECHANISM

def reset_timer():
    global reps
    global is_timer_running
    if is_timer_running:
        window.after_cancel(timer)
        canvas.itemconfig(timer_text, text= "00:00")
        title_label.config(text = "Timer")
        check_marks.config(text = "")
        reps = 0
        is_timer_running = False
        start_button.config(state=NORMAL)
        reset_button.config(state=DISABLED)

#STARTING TIMER MECHANIZM

def start_timer():
    global reps
    global is_timer_running
    is_timer_running = False
    if not is_timer_running:
        reps+=1
        work_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60

        if reps % 8 == 0:
            count_down(long_break_sec)
            title_label.config(text="LONG-BREAK")
        elif reps % 2 == 0:
            count_down(short_break_sec)
            title_label.config(text="SHORT-BREAK")
        else:
            count_down(work_sec)
            title_label.config(text="WORK-SESSION")
        is_timer_running = True
        start_button.config(state=DISABLED)
        reset_button.config(state=NORMAL)

#COUNT DOWN MECHANISM
def count_down(count):

    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec<10:
        count_sec =f"0{count_sec}"
    if count>=0:
        global timer
        canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark =""
        for _ in range(math.floor(reps/2)):
            mark+="✔️"
            check_marks.config(text = mark)

#UI SETUP
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady=50, bg=YELLOW)
canvas = Canvas(width=200, height=224, background=YELLOW, highlightthickness=0)


title_label = Label(text="IDLE TIMER",font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)


start_button = Button(text= "Start", command =start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset",command=reset_timer)
reset_button.grid(column=2, row=2)

tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(103,130, text="00:00", fill="white", font=(FONT_NAME,35, "bold"))
canvas.grid(column=1, row=1)

check_marks = Label(fg = GREEN, bg = YELLOW)
check_marks.grid(column=1, row=2)

window.mainloop()